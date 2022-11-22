import sqlite3
from util import log_func


class Database:
	""" This class serves as a database object, that can be used to interact with the database """

	def __init__(self):
		self.conn = sqlite3.connect("references.db")
		self.commit = self.conn.commit  # commit is more easily available

	@log_func
	def select(self, first: bool = False, **kwargs):
		""" Return first or all items meeting kwargs conditions """

		cur = self.conn.cursor()

		attr = " AND ".join(f"{k} = ?" for k in kwargs.keys())
		val = list(kwargs.values())

		if not val:
			query = "SELECT * FROM books"
		else:
			query = f"SELECT * FROM books WHERE {attr}"

		cur_exec = cur.execute(query, val)
		data = cur_exec.fetchone() if first else cur_exec.fetchall()
		cur.close()
		return data

	@log_func
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

	@log_func
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

	@log_func
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

	@log_func
	def delete_all(self):
		""" Delete all values unconditionally """

		cur = self.conn.cursor()

		query = f"DELETE FROM books"

		cur.execute(query).fetchall()
		cur.close()
