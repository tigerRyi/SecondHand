import pymysql


def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='SecondHand',
                                 password='SecondHand',
                                 db='SecondHand',
                                 )
    cur = connection.cursor()
    return connection, cur


def close_connection(connection, cur):
    connection.commit()
    connection.close()
    cur.close()


def insertPerson(person):
    connection, cur = get_connection()

    sql_InsertPerson = "INSERT INTO person (id, name ) VALUES (%s, %s);"
    cur.execute(sql_InsertPerson, (str(person.id), person.name))

    close_connection(connection, cur)
    return


def SelectAllPeople():
    connection, cur = get_connection()

    sql_getAllPeople = "SELECT id, name FROM person;"
    cur.execute(sql_getAllPeople)
    people = cur.fetchall()

    close_connection(connection, cur)
    return people


def SelectPersonById(id):
    connection, cur = get_connection()

    sql_getPersonById = "SELECT id, name FROM person WHERE id = %s;"
    cur.execute(sql_getPersonById, (id))
    person = cur.fetchone()

    close_connection(connection, cur)
    return person


def deletePersonById(id):
    connection, cur = get_connection()

    sql_deletePersonById = "DELETE FROM person WHERE id = %s;"
    cur.execute(sql_deletePersonById, (id))

    close_connection(connection, cur)


def updatePersonById(id, name):
    connection, cur = get_connection()

    sql_updatePersonById = "UPDATE person SET name = %s WHERE id = %s;"
    cur.execute(sql_updatePersonById, (name, id))

    close_connection(connection, cur)
    return