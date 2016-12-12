import psycopg2
import uuid
def populateDestinations(conn, cur):
    area_of_campus = 'Northside'
    destinations = []
    destinations.append('Ugly Statue')
    destinations.append('Leutner')
    destinations.append('Clark')
    destinations.append('Village Starbucks')
    query = 'INSERT INTO DESTINATIONS (did,dname,area_of_campus) VALUES (%s, %s, %s)'
    for dname in destinations:
        try:
            did = uuid.uuid4()
            data = (did,dname,area_of_campus)
            cur.execute(query,data)
        except psycopg2.Error as e:
            if e.pgcode == '23505':
                try:
                    did = uuid.uuid4()
                    data = (did,dname,area_of_campus)
                    cur.execute(query,data)
                except:
                    raise
            else:
                pass
    area_of_campus = 'Bottom of the hill'
    destinations = []
    destinations.append('Fribley')
    destinations.append('Staley')
    destinations.append('Parking Lot')
    for dname in destinations:
        try:
            did = uuid.uuid4()
            data = (did,dname,area_of_campus)
            cur.execute(query,data)
        except psycopg2.Error as e:
            if e.pgcode == '23505':
                try:
                    did = uuid.uuid4()
                    data = (did,dname,area_of_campus)
                    cur.execute(query,data)
                except:
                    raise
            else:
                pass
    area_of_campus = 'Top of the hill'
    destinations = []
    destinations.append('Carlton')
    destinations.append('Glasier')
    destinations.append('Parking Lot')
    for dname in destinations:
        try:
            did = uuid.uuid4()
            data = (did,dname,area_of_campus)
            cur.execute(query,data)
        except psycopg2.Error as e:
            if e.pgcode == '23505':
                try:
                    did = uuid.uuid4()
                    data = (did,dname,area_of_campus)
                    cur.execute(query,data)
                except:
                    raise
            else:
                pass
    area_of_campus = 'Quad'
    destinations = []
    destinations.append('Veale')
    destinations.append('Strosacker')
    destinations.append('Tomlinson')
    destinations.append('Nord')
    for dname in destinations:
        try:
            did = uuid.uuid4()
            data = (did,dname,area_of_campus)
            cur.execute(query,data)
        except psycopg2.Error as e:
            if e.pgcode == '23505':
                try:
                    did = uuid.uuid4()
                    data = (did,dname,area_of_campus)
                    cur.execute(query,data)
                except:
                    raise
            else:
                pass
    conn.commit()