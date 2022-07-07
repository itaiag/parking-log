import sqlite3

from definitions import database_full_path


def insert_update_delete_db(query, args=()):
    con = sqlite3.connect(database_full_path)
    cur = con.cursor()
    result = cur.execute(query, args)
    row_count = result.rowcount
    con.commit()
    con.close()
    return row_count


def select_db(query, args=(), one=False):
    con = sqlite3.connect(database_full_path)
    cur = con.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value)\
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r


def get_parking_spots():
    query = '''
    SELECT
     *
    FROM 
     tblParkSpots;
    '''
    return select_db(query)


def get_parking():
    query = '''
    SELECT
        tblCars.Name,
        tblParkSpots.City,
        tblParkSpots.Street,
        tblParkSpots.Num,
        tblParkSpots.Description,
        tblParkSpots.Geolocation,
        tblParks.Driver,
        tblParks.Date
    FROM
        tblParks
    INNER JOIN tblCars ON tblCars.PK_Cars = tblParks.FK_Parks_Cars
    INNER JOIN tblParkSpots ON tblParkSpots.PK_ParkSpots = tblParks.FK_Parks_ParkSpots;
    '''
    return select_db(query)


def get_cars():
    query = '''
    SELECT
        PK_Cars,
        Name
    FROM
        tblCars
    '''
    return select_db(query)


def get_car(car_id: int):
    query = f'''
    SELECT
        PK_Cars,
        Name
    FROM
        tblCars
    WHERE
        PK_Cars = {car_id} 
    '''
    return select_db(query)


def add_car(car_name: str):
    query = f"INSERT INTO tblCars VALUES (NULL, '{car_name}')"
    return insert_update_delete_db(query)


def delete_car(car_id: int):
    query = f'''
    DELETE FROM
        tblCars
    WHERE
        PK_Cars = {car_id};
    '''
    insert_update_delete_db(query)


def add_park(date, car_id, park_spot_id, driver):
    query = f'''INSERT INTO tblParks VALUES 
        (NULL, {car_id}, {park_spot_id}, '{date}', '{driver}');'''
    return insert_update_delete_db(query)


def get_parking_as_dict() -> dict:
    con = sqlite3.connect(database_full_path)
    cur = con.cursor()
    cur.execute('''
    SELECT
        tblCars.Name,
        tblParkSpots.City,
        tblParkSpots.Street,
        tblParkSpots.Num,
        tblParkSpots.Description,
        tblParkSpots.Geolocation,
        tblParks.Driver,
        tblParks.Date
    FROM
        tblParks
    INNER JOIN tblCars ON tblCars.PK_Cars = tblParks.FK_Parks_Cars
    INNER JOIN tblParkSpots ON tblParkSpots.PK_ParkSpots = tblParks.FK_Parks_ParkSpots;
    ''')
    desc = cur.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cur.fetchall()]
    con.close()
    return data


