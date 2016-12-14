from webapp import server as router
from webapp.wordid import integer_to_wordset, wordset_to_integer
import webapp.database as database
from datetime import datetime

from flask import render_template, request, redirect, url_for

import psycopg2


try:
    conn = psycopg2.connect(dbname='postgres', user='postgres',
        password='economicalchinchillacorndog', host='localhost')
except:
    print('No Database.')
    import sys
    sys.exit(1)

EXAMPLE_TRIP2 = ('Tahitians.deities.Aachen', 'Fribley', 'Leutner', '12:15PM', 'specialuserid',)
EXAMPLE_TRIP = ('special_trip_id', 'Leutner', 'Fribley', '3:00PM', 'specialuserid',)

@router.route('/')
def index():
    return render_template('index.html')

@router.route('/u/<caseid>')
def profile_page(caseid):
    user = database.getUser(conn, caseid)
    if user is None:
        return redirect(url_for('index'))
    first_name = user[2]
    last_name = user[3]
    trips = database.getUserTrips(conn, caseid)
    # print('trips'+str(trips ))
    friend_list = database.listFriends(conn, caseid)
    print('Friend list: %s' % (friend_list,))

    like_count = database.countLikes(conn, caseid)
    return render_template('profile.html',
                           title1='W', title2='%s %s' % (first_name, last_name,),
                           username=caseid, trips=trips,
                           first_name=first_name, last_name=last_name, 
                           friend_list=friend_list, like_count=like_count)

@router.route('/u/<caseid>/friend')
def friend_user(caseid):
    requesting_user = request.args.get('user')
    print('%s sent a friend request to %s' % (requesting_user, caseid,))
    database.makeFriends(conn, requesting_user, caseid)
    return redirect('/u/%s' % (caseid,))

@router.route('/u/<caseid>/block')
def block_user(caseid):
    requesting_user = request.args.get('user')
    database.blockUser(conn, requesting_user, caseid)
    return redirect('/u/%s' % (caseid,))

@router.route('/new_trip')
def new_trip():
    destinations = database.getAllDestinations(conn)
    from_ = request.args.get('from_')
    to_ = request.args.get('to_')
    ehour = request.args.get('ehour')
    emin = request.args.get('emin')
    caseid = request.args.get('caseid')
    if not (from_ and to_ and emin and ehour and caseid):
        return render_template('new_trip.html',
                title1='W', title2='Finalize Trip Details',
                destinations=destinations,
                trip=EXAMPLE_TRIP)
    start_time = datetime.now().replace(hour = int(ehour)).replace(minute = int(emin))
    # make a new trip here
    # TODO Write in the new create trip here.
    db_uuid = database.createNewTrip(conn,caseid, from_,to_,start_time)
    # TODO Get the db_uuid for the new trip
    nice_name = db_uuid
    return redirect('/t/%s' % (nice_name,))


def generic_trip(results_to_return):
    print('generic_trip...')
    from_ = request.args.get('from_')
    to_ = request.args.get('to_')
    caseid = request.args.get('caseid')
    try:
        ehour = int(request.args.get('ehour'))
        emin = int(request.args.get('emin'))
        lhour = int(request.args.get('lhour'))
        lmin = int(request.args.get('lmin'))
    except (TypeError, ValueError):
        ehour = None

    if from_ is None or to_ is None or ehour is None or emin is None or lhour is None or lmin is None:
        from_ = ''
        to_ = ''
        emin = ''
        ehour = ''
        lmin = ''
        lhour = ''
        friend_trips = []
        trips = database.getAllTrips(conn, results_to_return)
        trips = list(trips)
    else:
        start_time = datetime.now().replace(hour = ehour).replace(minute = emin)
        end_time = datetime.now().replace(hour = lhour).replace(minute = lmin)
        prefer_friends = bool(request.args.get('friends'))
        if prefer_friends and caseid is not None:
            friend_trips = database.getSpecificFriendsTrips(conn, results_to_return, from_,to_,start_time,end_time,caseid)
            trips = list(friend_trips)
            trips2 = database.getSpecificTrips(conn, results_to_return-len(trips),from_,to_,start_time,end_time)
        else:
            trips = database.getSpecificTrips(conn, results_to_return,from_,to_,start_time,end_time)
            trips = list(trips)
    destinations = database.getAllDestinations(conn)

    return render_template('find_trip.html',
        title1='W', title2='Find a Trip',
        destinations=destinations,
        from_=from_, to_=to_, ehour = ehour, emin = emin, lmin = lmin, lhour= lhour,
        friend_trips=[], trips=trips)


@router.route('/trip', methods=['GET'])
def tripfinder():
    return generic_trip(3)

@router.route('/trip_more', methods=['GET'])
def loadMoreTrips():
    return generic_trip(10)

@router.route('/t/<shorttripid>/join', methods=['GET'])
def joinTripPage(shorttripid):
    # TODO implement joining a trip
    # TODO GET trip to check if it exists
    # TODO Write user to trip
    print('joining trip %s' % (shorttripid,))
    long_id = shorttripid
    trip_exists = database.checkTripExists(conn, shorttripid)
    if not trip_exists:
        print('trip does not exist')
        return redirect('/trip')
    print('trip exists')

    caseid = request.args.get('caseid')
    print('request.args %s' % (request.args,))
    if caseid is not None:
        print('add user %s to trip %s' % (caseid, shorttripid,))
        database.addToTrip(conn, shorttripid, caseid)

    return redirect('/t/%s' % (shorttripid,))

@router.route('/t/<shorttripid>/like', methods=['GET'])
def rateTrip(shorttripid):
    database.rateTrip(conn, shorttripid)
    return redirect('/t/%s' % (shorttripid,))

@router.route('/t/<shorttripid>', methods=['GET'])
def tripDetailPage(shorttripid):
    # TODO add a join trip button with a case id field
    long_id = shorttripid

    trips = list(database.getOneTrip(conn, shorttripid))

    if len(trips) <= 0:
        print('I have reached a special case')
        if shorttripid == 'soon_trip':
            return render_template('trip_detail_soon.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP, user_list=[('Jane', 'jan2',), ('John', 'joh3',)])
        elif shorttripid == 'done_trip':
            return render_template('trip_detail_done.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP, user_list=[('Jane', 'jan2',), ('John', 'joh3',)])
        elif shorttripid == 'active_trip':
            return render_template('trip_detail_active.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP, user_list=[('Jane', 'jan2',), ('John', 'joh3',)])
        # no result
        print('shorttripid = %s' % (shorttripid,))
        return redirect('/trip')
    else:
        # TODO get list of users for the trip
        user_list = database.getUserByTrip(conn, shorttripid)
        # TODO check time and use a different template
        print('trip tuple: %s' % (trips,))
        trip = trips[0]
        if (datetime.now() - trip[3]).total_seconds() < 0:
            return render_template('trip_detail_soon.html', trip=trip, title1='W', title2='Trip', user_list=user_list)
        elif (datetime.now() - trip[3]).total_seconds() < 60 * 60:
            return render_template('trip_detail_active.html', trip=trip, title1='W', title2='Trip', user_list=user_list)
        else:
            return render_template('trip_detail_done.html', trip=trip, title1='W', title2='Trip', user_list=user_list)
