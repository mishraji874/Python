import sqlite3

# Connection with the DataBase
# 'library.db'
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# SQL piece of code Executed
cursor.execute("""
	
	CREATE TABLE book(
		title,
		author,
		published);""")

List = [('A', 'B', 2008), ('C', 'D', 2008),
						('E', 'F', 2010)]

connection. executemany("""
				
	INSERT INTO
	book(title, author, published)
	VALUES (?, ?, ?)""", List)

sql = """
	SELECT * FROM book;"""
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
	print(x)

# Changes saved into database
connection.commit()

# Connection closed(broken)
# with DataBase
connection.close()
