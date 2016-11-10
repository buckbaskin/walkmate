from webapp import server as router

from flask import render_template, request, redirect

import psycopg2

try:
    conn = psycopg2.connect(dbname='postgres', user='postgres',
        password='economicalchinchillacorndog', host='localhost')
except:
    print('No Database.')

EXAMPLE_TRIP = ('special_trip_id', 'Leutner', 'Fribley', '3:00PM', 'specialuserid',)

@router.route('/')
def index():
    return render_template('index.html')

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
        print('Database requets failed.')
    
    if not from_ == '' and not to_ == '' and not at_ == '':
        message = 'The database results go here. We probably want to template a list.'
    else:
        message = 'Can you provide more information?'
        trips = []

    if trips == []:
        trips = [EXAMPLE_TRIP]
    
    return render_template('find_trip.html', 
        from_=from_, to_=to_, at_=at_, message=message, 
        friend_trips=[], trips=trips)

@router.route('/trip_more', methods=['GET'])
def loadMoreTrips():
    # TODO implement this
    return redirect('/trip')

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
    long_id = expandIdentifier(shorttripid)

    try:
        cur = conn.cursor()

        cur.execute('''SELECT * FROM trips WHERE id = %s OR short_id = %s''',
            (long_id, shorttripid,))

        trip = cur.fetchmany(1)
    except:
        trip = []

    if len(trip) <= 0:
        if shorttripid == 'special_trip_id':
            return render_template('trip_detail.html', trip=EXAMPLE_TRIP)
        # no result
        return redirect('/trip')
    else:
        return render_template('trip_detail.html', trip=trip)