import sqlite3

dataFile = 'data/data.db'
defaultData = 'data/default_data.txt'

def init():
  conn = sqlite3.connect(dataFile)
  cursor = conn.cursor()
  cursor.execute('CREATE TABLE soul (id INTEGER PRIMARY KEY AUTOINCREMENT, text VARCHAR(1024))')
  try:
    with open(defaultData, 'r', encoding='UTF-8') as f:
      lines = f.readlines()
      for line in lines:
        cursor.execute('INSERT INTO soul (text) VALUES (?)',(line,))
  finally:
    if f:
      f.close()
  cursor.close()
  conn.commit()
  conn.close()

def add(text):
  conn = sqlite3.connect(dataFile)
  cursor = conn.cursor()
  cursor.execute('INSERT INTO soul (text) VALUES (?)',(text,))
  cursor.close()
  conn.commit()
  conn.close()

def list():
  conn = sqlite3.connect(dataFile)
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM soul ORDER BY id')
  values = cursor.fetchall()
  cursor.close()
  conn.close()
  return values

def get():
  conn = sqlite3.connect(dataFile)
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM soul ORDER BY RANDOM() LIMIT 1')
  value = cursor.fetchone()
  cursor.close()
  conn.close()
  return value

def delete(id):
  conn = sqlite3.connect(dataFile)
  cursor = conn.cursor()
  cursor.execute('DELETE FROM soul WHERE id=?',(id,))
  cursor.close()
  conn.commit()
  conn.close()