import sqlite3
from os import path
import logging as log
from definitions import root_dir, database_name


def init_database():
    log.info("About to init database")
    con = sqlite3.connect(path.join(root_dir, database_name))
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS car")
    cur.execute("DROP TABLE IF EXISTS park")
    # Create table
    cur.execute('''CREATE TABLE tblCars
                   (PK_Cars INTEGER PRIMARY KEY,
                   Name TEXT NOT NULL
                   )''')
    cur.execute('''CREATE TABLE tblParks
                    (PK_Parks INTEGER PRIMARY KEY,
                     FK_Parks_Cars INTEGER,
                     FK_Parks_ParkSpots INTEGER,
                     Date TEXT,
                     Driver TEXT,
                     FOREIGN KEY (FK_Parks_Cars) REFERENCES tblCars (PK_Cars),
                     FOREIGN KEY (FK_Parks_ParkSpots) REFERENCES tblParkSpots (PK_ParkSpots)
                     )''')
    cur.execute('''CREATE TABLE tblParkSpots
                    (PK_ParkSpots INTEGER PRIMARY KEY,
                     City TEXT,
                     Street TEXT,
                     Num INTEGER,
                     Geolocation TEXT,
                     Description TEXT                     
                     )''')
    con.commit()
    cur.execute("INSERT INTO tblCars VALUES (NULL, 'Peugeot 208')")
    cur.execute("INSERT INTO tblCars VALUES (NULL, 'Mazda 3')")

    for i in range(1, 90):
        cur.execute(f"INSERT INTO tblParkSpots VALUES (NULL, 'Raanana','Bar-Ilan',{i},'','')")
    con.commit()
    cur.execute(f"INSERT INTO tblParks VALUES (NULL, '1','45','07/07/2022 10:00','Itai')")
    cur.execute(f"INSERT INTO tblParks VALUES (NULL, '2','37','07/07/2022 11:00','Meital')")
    con.commit()
    con.close()
