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
    
    try:
        cur = conn.cursor()

        if not from_ == '':
            # TODO Get trips that match the from/to/at request
            pass
        else:
            # TODO Get all trips (this might be good here, but not sorted by nearest in time for example)
            cur.execute("""SELECT * FROM trips""")

        trips = cur.fetchmany(10)
    except:
        trips = []
        print('Database requests failed.')
    
    if from_ == '' or to_ == '' or at_ == '':
        message = 'Can you provide more information?'
        trips = []
    else:
        message = ''
    
    return render_template('find_trip.html', 
        title1='W', title2='Find More Trips',
        from_=from_, to_=to_, at_=at_, message=message, 
        friend_trips=[], trips=trips)

@router.route('/t/<shorttripid>/join', methods=['POST'])
def joinTripPage(shorttripid):
    # TODO implement joining a trip
    # TODO GET trip to check if it exists
    # TODO Write user to trip
    long_id = wordset_to_integer(shorttripid)
    try:
        cur = conn.cursor()
        cur.execute('''SELECT * FROM trips WHERE id = %s OR short_id = %s''',
            (long_id, shorttripid,))
        trip_exists = len(cur.fetchmany(1)) > 0
    except:
        trip_exists = False
    if not trip_exists:
        return redirect('/trip')

    caseid = request.args.get('caseid')
    if caseid is not None:
        # TODO add it to the trip
        pass

    return redirect('/t/%s' % (shorttripid,))



@router.route('/t/<shorttripid>', methods=['GET'])
def tripDetailPage(shorttripid):
    # TODO add a join trip button with a case id field
    long_id = shorttripid

    try:
        cur = conn.cursor()

        # TODO fix this. Get trips that match the trip id, and take the first one
        cur.execute('''SELECT * FROM TRIPS WHERE tripid = %s''',
            (long_id,))

        trip = cur.fetchmany(1)
    except:
        trip = []

    # TODO remove these: They are special cases for helping with creating templates
    if len(trip) <= 0:
        print('I have reached a special case')
        if shorttripid == 'Tahitians.deities.Aachen':
            return render_template('trip_detail_active.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP2)
        elif shorttripid == 'soon_trip':
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
        # TODO use this render template
        return render_template('trip_detail_active.html', trip=trip)
