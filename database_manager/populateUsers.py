import psycopg2
import hashlib
import datetime
def populateUsers(conn, cur):
    query = 'INSERT INTO USERS (caseid, hashed_password, first_name, last_name, date_joined) VALUES (%s, %s, %s, %s, %s)'
    caseid = 'wcb38'
    first_name = 'Buck'
    last_name = 'Baskin'
    password = 'buckpickapassword'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    caseid = 'pjt37'
    first_name = 'Pete'
    last_name = 'Thompson'
    password = 'petepickapassword'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    caseid = 'raw141'
    first_name = 'Bobby'
    last_name = 'Wagner'
    password = 'fakepasswordsarehard'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    caseid = 'peb30'
    first_name = 'Patrick'
    last_name = 'Bonano'
    password = 'thisisasecurepassword'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    caseid = 'prn15'
    first_name = 'Paul'
    last_name = 'Nettleton'
    password = 'butwhyeastereggs'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    caseid = 'jns83'
    first_name = 'Jadin'
    last_name = 'Stoffle'
    password = 'notasouffle'
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
    except psycopg2.Error as e:
        raise e
    conn.commit()