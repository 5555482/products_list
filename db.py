import sqlite3

def getAll():
    conn = sqlite3.connect('db.sqlite3')

    print "Opened database successfully";

    cursor = conn.execute("SELECT ID,NAME,PRICE from PRODUCT")

    rows = [x for x in cursor]
    cols = [x[0] for x in cursor.description]
    data = []
    for row in rows:
      entry = {}
      for prop, val in zip(cols, row):
        entry[prop] = val
      data.append(entry)

    print "Operation done successfully";
    conn.close()

    return data

def getOne(id):
    conn = sqlite3.connect('db.sqlite3')

    print "Opened database successfully";

    cursor = conn.execute("SELECT ID,NAME,DESCRIPTION,PRICE from PRODUCT where ID=%s" % id)

    rows = [x for x in cursor]
    cols = [x[0] for x in cursor.description]
    data = []
    for row in rows:
      entry = {}
      for prop, val in zip(cols, row):
        entry[prop] = val
      data.append(entry)

    print "Operation done successfully";
    conn.close()

    return data

def putOne(name, description, price):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute("INSERT INTO PRODUCT ('NAME', 'DESCRIPTION', 'PRICE') VALUES(?,?,?)", (name, description, price))

    conn.commit()
    print "Operation done successfully";
    c.close()
    conn.close()

    return

def updateOne(id, name, description, price):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute("UPDATE PRODUCT SET NAME=?, DESCRIPTION=?, PRICE=? WHERE ID=?", (name, description, price, id))

    conn.commit()
    print "Operation done successfully";
    c.close()
    conn.close()

    return

def delete(id):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute("DELETE FROM PRODUCT WHERE ID=%s" % id)

    conn.commit()
    print "Operation done successfully";
    c.close()
    conn.close()

    return
