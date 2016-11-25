from webapp import server as router
from webapp.wordid import integer_to_wordset, wordset_to_integer

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

@router.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if not (email and password):
        if not email:
            email = ''
        return render_template('login.html',
                               title1='W', title2='Login',
                               email=email)
    else:
        # do some login stuff
        return redirect('/trip')

@router.route('/u/<shortuserid>/edit')
def edit_profile_page(shortuserid):
    # TODO implement profile editing
    return redirect('/u/%s' % (shortuserid,))

@router.route('/u/<shortuserid>')
def profile_page(shortuserid):
    user_id = wordset_to_integer(shortuserid)
    if shortuserid == 'logged.out':
        logged_in=False
    else:
        logged_in = True
    first_name = 'Jane'
    last_name = 'Doe'
    description = 'I am a fan of Walkmate'
    list_of_up_to_five_friends = [('other_user1',), ('other_user2',)]
    return render_template('profile.html',
                           title1='W', title2='%s %s' % (first_name, last_name,),
                           logged_in=logged_in, username=shortuserid, user_id=user_id,
                           first_name=first_name, last_name=last_name,
                           description=description, friends=list_of_up_to_five_friends)

@router.route('/new_trip')
def new_trip():
    from_ = request.args.get('trip-from')
    to_ = request.args.get('trip-to')
    at_ = request.args.get('trip-at')
    if not (from_ and to_ and at_):
        return render_template('new_trip.html',
                title1='W', title2='Finalize Trip Details',
                trip=EXAMPLE_TRIP)

    # make a new trip here
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
    
    try:
        cur = conn.cursor()

        cur.execute("""SELECT * FROM trips""")

        trips = cur.fetchmany(3)
    except:
        trips = []
        print('Database requests failed.')
    
    if not from_ == '' and not to_ == '' and not at_ == '':
        message = 'The database results go here. We probably want to template a list.'
    else:
        message = 'Can you provide more information?'
        trips = []

    if trips == []:
        trips = [EXAMPLE_TRIP]
    
    return render_template('find_trip.html',
        title1='W', title2='Find a Trip',
        from_=from_, to_=to_, at_=at_, message=message, 
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

        cur.execute("""SELECT * FROM trips""")

        trips = cur.fetchmany(10)
    except:
        trips = []
        print('Database requets failed.')
    
    if not from_ == '' and not to_ == '' and not at_ == '':
        message = 'The database results go here. We probably want to template a list.'
    else:
        message = 'Can you provide more information?'
        trips = []

    if trips == []:
        trips = [EXAMPLE_TRIP]
    
    return render_template('find_trip.html', 
        title1='W', title2='Find More Trips',
        from_=from_, to_=to_, at_=at_, message=message, 
        friend_trips=[], trips=trips)

def expandIdentifier(shortIdentifier):
    # TODO maybe implement this
    # Maybe just make a short id for everything when it is inserted into db
    return shortIdentifier

def compressIdentifier(longIdentifier):
    # TODO maybe implement this
    # Maybe just make a short id for everything when it is inserted into db
    return longIdentifier

@router.route('/t/<shorttripid>/join', methods=['GET'])
def joinTripPage(shorttripid):
    # TODO implement joining a trip
    return redirect('/t/%s' % (shorttripid,))

@router.route('/t/<shorttripid>', methods=['GET'])
def tripDetailPage(shorttripid):
    long_id = wordset_to_integer(shorttripid)

    try:
        cur = conn.cursor()

        cur.execute('''SELECT * FROM trips WHERE id = %s OR short_id = %s''',
            (long_id, shorttripid,))

        trip = cur.fetchmany(1)
    except:
        trip = []

    if len(trip) <= 0:
        if shorttripid == 'Tahitians.deities.Aachen':
            return render_template('trip_detail_active.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP2)
        if shorttripid == 'soon_trip':
            return render_template('trip_detail_soon.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP)
        if shorttripid == 'done_trip':
            return render_template('trip_detail_done.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP)
        if shorttripid == 'special_trip_id':
            return render_template('trip_detail_active.html',
                title1='W', title2='Trip Details',
                trip=EXAMPLE_TRIP)
        # no result
        return redirect('/trip')
    else:
        return render_template('trip_detail_active.html', trip=trip)
