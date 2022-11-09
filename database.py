import sqlite3
from pubsub import pub
from datetime import datetime


def log(func):
	"""
	Log decorator, logs function, values and docstrings

	:param func: Function to be decorated
	:return: Wrapper-function
	"""

	def wrapper(self, *args, **kwargs):
		message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Add date and time information
		message += f" - {func.__name__}({args}, {kwargs}):{func.__doc__}"  # Log-data for function call
		pub.sendMessage("DIN MOR", message=message)  # Send the message with pubsub

		return func(self, *args, **kwargs)

	return wrapper

class Database:
	""" This class serves as a database object, that can be used to interact with the database """

	def __init__(self):
		self.conn = sqlite3.connect("references.db")
		self.commit = self.conn.commit  # commit is more easily available

	@log
	def select(self, first: bool = False, **kwargs):
		""" Return first or all items meeting kwargs conditions """

		cur = self.conn.cursor()

		attr = " AND ".join(f"{k} = ?" for k in kwargs.keys())
		val = list(kwargs.values())

		if not val:
			query = "SELECT * FROM books"
		else:
			query = f"SELECT * FROM books WHERE {attr}"
			query.format(attr)

		data = cur.execute(query, val).fetchall()
		cur.close()
		return data[0] if first else data

	@log
	def insert(self, **kwargs):
		""" Insert new item with values from kwargs """

		cur = self.conn.cursor()

		attr = list(kwargs.keys())
		val = list(kwargs.values())

		attr_str = "(" + ", ".join(attr) + ")"
		val_str = "(" + ("?, " * len(val)).rstrip(", ") + ")"
		query = f"INSERT INTO books {attr_str} VALUES {val_str}"

		cur.execute(query, val).fetchall()
		cur.close()

	@log
	def update(self, index, **kwargs):
		""" Update item with given index, using values from kwargs """

		cur = self.conn.cursor()

		attr = list(kwargs.keys())
		val = list(kwargs.values())
		val.append(index)

		attr_str = ", ".join(f"{a} = ?" for a in attr)
		query = f"UPDATE books SET {attr_str} WHERE id = ?"

		cur.execute(query, val).fetchall()
		cur.close()

	@log
	def delete(self, **kwargs):
		""" Delete values meeting kwargs conditions """

		cur = self.conn.cursor()

		attr = " AND ".join(f"{k} = ?" for k in kwargs.keys())
		val = list(kwargs.values())

		assert len(val) != 0, "Cannot delete without conditions"  # delete_all should be used

		query = f"DELETE FROM books WHERE {attr}"
		query.format(attr)

		cur.execute(query, val).fetchall()
		cur.close()

	@log
	def delete_all(self):
		""" Delete all values unconditionally """

		cur = self.conn.cursor()

		query = f"DELETE FROM books"

		cur.execute(query).fetchall()
		cur.close()
