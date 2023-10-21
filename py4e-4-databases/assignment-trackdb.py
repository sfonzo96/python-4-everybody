import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

sqlScript = '''DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);'''

cur.executescript(sqlScript)

fileName = input('Enter file name: ')
if ( len(fileName) < 1 ) : fileName = 'Library.xml'

def lookup(dict, key):
    found = False
    for child in dict:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

data = ET.parse(fileName)

all = data.findall('dict/dict/dict')

print('Dict count:', len(all))

for dict in all:
    if ( lookup(dict, 'Track ID') is None ) : continue

    name = lookup(dict, 'Name')
    genre = lookup(dict, 'Genre')
    artist = lookup(dict, 'Artist')
    album = lookup(dict, 'Album')
    count = lookup(dict, 'Play Count')
    rating = lookup(dict, 'Rating')
    length = lookup(dict, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    print(name, genre, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))

    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    
    # some tracks don't have a genre so select query might throw an exception if not handled
    if genre:
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, genre_id, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, genre_id, album_id, length, rating, count ) )

    conn.commit()





