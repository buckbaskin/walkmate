from webapp import server as router
from webapp.wordid import integer_to_wordset, wordset_to_integer
import webapp.database as database

from flask import render_template, request, redirect, url_for

import psycopg2

try:
    conn = psycopg2.connect(dbname='postgres', user='postgres',
        password='economicalchinchillacorndog', host='localhost')
except:
    print('No Database.')

EXAMPLE_TRIP2 = ('Tahitians.deities.Aachen', 'Fribley', 'Leutner', '12:15PM', 'specialuserid',)
EXAMPLE_TRIP = ('special_trip_id', 'Leutner', 'Fribley', '3:00PM', 'specialuserid',)

@router.route('/')
def index():
    return render_template('index.html')

@router.route('/u/<caseid>')
def profile_page(caseid):
    user = database.getUser(conn, caseid)
    first_name = user[2]
    last_name = user[3]
    trips = database.getUserTrips(conn, caseid)
    return render_template('profile.html',
                           title1='W', title2='%s %s' % (first_name, last_name,),
                           username=caseid, trips=trips,
                           first_name=first_name, last_name=last_name)

@router.route('/new_trip')
def new_trip():
    from_ = request.args.get('from_')
    to_ = request.args.get('to_')
    at_ = request.args.get('trip-at')
    caseid = request.args.get('caseid')
    if not (from_ and to_ and at_):
        return render_template('new_trip.html',
                title1='W', title2='Finalize Trip Details',
                trip=EXAMPLE_TRIP)

    # make a new trip here
    # TODO Write in the new create trip here.
    
    # TODO Get the db_uuid for the new trip
    db_uuid = 12345678910
    nice_name = integer_to_wordset(int(db_uuid))
    return redirect('/t/%s' % (nice_name,))


@router.route('/trip', methods=['GET'])
def tripfinder():
    from_ = request.args.get('trip-from')
    to_ = request.args.get('trip-to')
    at_ = request.args.get('trip-at')
    if from_ is None or to_ is None or at_ is None:
        from_ = ''
        to_ = ''
        at_ = ''
    prefer_friends = request.args.get('friends')
    
    trips = database.getAllTrips(conn, 3)
    destinations = database.getAllDestinations(conn)
    print(destinations)

    return render_template('find_trip.html',
        title1='W', title2='Find a Trip',
        destinations=destinations,
        from_=from_, to_=to_, at_=at_,
        friend_trips=[], trips=trips)

@router.route('/trip_more', methods=['GET'])
def loadMoreTrips():
    from_ = request.args.get('trip-from')
    to_ = request.args.get('trip-to')
    at_ = request.args.get('trip-at')
    if from_ is None or to_ is None or at_ is None:
        from_ = ''
        to_ = ''
        at_ = ''
    prefer_friends = request.args.get('friends')
    
    trips = database.getAllTrips(conn, 10)
    
    return render_template('find_trip.html', 
        title1='W', title2='Find More Trips',
        from_=from_, to_=to_, at_=at_,
        trips=trips)

@router.route('/t/<shorttripid>/join', methods=['POST'])
def joinTripPage(shorttripid):
    # TODO implement joining a trip
    # TODO GET trip to check if it exists
    # TODO Write user to trip
    long_id = shorttripid
    trip_exists = database.checkTripExists(conn, shorttripid)
    if not trip_exists:
        return redirect('/trip')

    caseid = request.args.get('caseid')
    if caseid is not None:
        database.addToTrip(conn, tripid, caseid)

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
        user_list = [('Jane', 'jan2')]
        # TODO check time and use a different template
        print('trip tuple: %s' % (trips,))
        return render_template('trip_detail_active.html', trip=trips[0], user_list=user_list)
