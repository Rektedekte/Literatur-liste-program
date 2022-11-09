import wx
import gui
from database import Database
from pubsub import pub
import sys
import os


class LogFrame(gui.LogFrame):
	""" Frame to permit logging """

	def __init__(self, parent):
		gui.LogFrame.__init__(self, parent)
		pub.subscribe(self.listener, "DIN MOR")

	def listener(self, message):
		"""
		Listener writes log-messages to the frame

		:param message: Message to log
		:return: None
		"""

		curr = self.log_label.GetLabel()

		if curr:
			curr += "\n"

		curr += message
		self.log_label.SetLabel(curr)


class MainFrame(gui.MainFrame):
	""" Main frame and entry of the program """

	def __init__(self, parent, dbg=False):
		""" Initialize dialogs to be spawned on command and other stuff """

		gui.MainFrame.__init__(self, parent)
		self.IdChange(None)
		self.search_dialog = SearchDialog(self)
		self.new_dialog = NewDialog(self)
		self.update_dialog = UpdateDialog(self)
		self.file_dialog = FileDialog(self)
		self.replace_dialog = ReplaceDialog(self)

		if dbg:
			self.log_frame = LogFrame(self)
			self.log_frame.Show()

		self.SetIcon(wx.Icon("icon.png"))

	def OnSize(self, event):
		"""
		Triggered when the size of the window changes.
		Ensures that the size of the data_view stays consistent.
		"""

		width, height = self.GetClientSize()
		self.data_view.SetSize(width - 10, height - 90)

	def IdChange(self, event):
		"""
		When the content of id_input changes, update the search to only show that id.
		Is also used to reset searches.
		"""

		index = self.id_input.GetValue()

		items = db.select(id=index) if index else db.select()
		self.SetItems(items)

	def SetItems(self, items):
		"""
		Set items in data_view loaded from database.

		:param items: List of length 5 tuples
		:return: None
		"""

		items = [", ".join(str(v) for v in item) for item in items]
		self.data_view.SetItems(items)

	def DeleteItem(self, event):
		"""
		Delete item with specific id, if no id has been written, get the selected value form data_view.
		"""

		index = self.id_input.GetValue()

		if not index:
			index = self.data_view.GetStringSelection().split(", ")[0]

		if index:
			db.delete(id=index)
			self.IdChange(event)
			db.commit()

	def Search(self, event):
		""" Start the search-dialog """

		self.search_dialog.ShowModal()

	def New(self, event):
		""" Start the new-dialog """

		self.new_dialog.ShowModal()

	def UpdateItem(self, event):
		""" Start the update-dialog """

		self.update_dialog.ShowModal()

	def ResetSearch(self, event):
		""" Reload items from the database """

		self.id_input.SetLabel("")
		self.SetItems(db.select())

	def Export(self, event):
		""" Export database-items into a csv file """

		items = db.select()
		items = "\n".join(", ".join(str(v) for v in item[1:]) for item in items)

		with open("litteratur-liste.csv", "w+", encoding="utf-8") as f:
			# f.write("navn, forfatter, år, sider\n")
			f.write(items)

	def AppendImport(self, event):
		""" Start the file-dialog, and set the callback to AppendImportFinal """

		self.file_dialog.set_callback(self.AppendImportFinal)
		self.file_dialog.ShowModal()

	def AppendImportFinal(self, file):
		""" Finalize the import of new items, and commit the changes to db """

		try:
			with open(file, "r", encoding="utf-8") as f:
				lines = f.read().splitlines()

			for line in lines:
				name, author, year, pages = line.split(", ")
				db.insert(navn=name, forfatter=author, år=year, sider=pages)

			db.commit()
			self.IdChange(None)

		except:
			pass  # Hehe

	def ReplaceImport(self, event):
		"""
		Alternate function to AppendImport.
		Substitutes values in database with values imported
		"""

		self.file_dialog.set_callback(self.ReplaceImportConfirm)
		self.file_dialog.ShowModal()

	def ReplaceImportConfirm(self, file):
		"""
		Callback for ReplaceImport.
		Initiate the replace-dialog to ensure the user understands.
		"""

		v = self.replace_dialog.ShowModal()

		if not v:
			db.delete_all()
			self.AppendImportFinal(file)

	def KnaggerMoment(self, event):
		os.popen("knagger.bat")

	def Exit(self, event):
		""" Close the main window, thus stopping the problem """

		self.Close()


class FileDialog(gui.FileDialog):
	""" Dialog for file-selection """

	def __init__(self, parent, callback=None):
		gui.FileDialog.__init__(self, parent)
		self.callback = callback

	def set_callback(self, callback):
		""" Callback can be set on initialization, but can also be set for reuse """

		self.callback = callback
		self.file_picker.SetPath("")

	def Accept(self, event):
		""" Close the dialog and return to parent """

		if self.callback is None:  # If no callback is specified
			self.EndModal(-1)

		self.callback(self.file_picker.GetPath())
		self.EndModal(0)


class SearchDialog(gui.LookupDialog):
	""" Dialog for searching items, inherits from the general lookup-dialog """

	def __init__(self, parent):
		gui.LookupDialog.__init__(self, parent)

	def Return(self, event):
		""" Return function, loads all items meeting the conditions specified """

		index = self.id_box.GetValue()
		name = self.name_box.GetValue()
		author = self.author_box.GetValue()
		year = self.year_box.GetValue()
		pages = self.pages_box.GetValue()

		kwargs = {
			k: v for k, v in zip(
				("id", "navn", "forfatter", "år", "sider"),
				(index, name, author, year, pages)
			) if v}  # Format items as kwargs

		items = db.select(**kwargs)
		self.Parent.SetItems(items)
		self.EndModal(0)


class NewDialog(gui.LookupDialog):
	""" Dialog for creating items, inherits from the general lookup-dialog """

	def __init__(self, parent):
		gui.LookupDialog.__init__(self, parent)
		self.return_button.SetLabel("Indsæt")  # Manually set the return button text to fit the dialog
		self.id_box.Disable()  # User should not set id's for new items

	def Return(self, event):
		""" Return function, inserts new item into the database and returns """

		index = self.id_box.GetValue()
		name = self.name_box.GetValue()
		author = self.author_box.GetValue()
		year = self.year_box.GetValue()
		pages = self.pages_box.GetValue()

		kwargs = {
			k: v for k, v in zip(
				("id", "navn", "forfatter", "år", "sider"),
				(index, name, author, year, pages)
			) if v}  # Format items as kwargs

		db.insert(**kwargs)
		db.commit()
		self.Parent.ResetSearch(event)
		self.EndModal(0)


class UpdateDialog(gui.LookupDialog):
	""" Dialog for updating items, inherits from the general lookup-dialog """

	def __init__(self, parent):
		gui.LookupDialog.__init__(self, parent)
		self.return_button.SetLabel("Updater")  # Manually set the return button text

	def Return(self, event):
		""" Return functions, updates item given index with given values """

		index = self.id_box.GetValue()

		if not index:
			return

		name = self.name_box.GetValue()
		author = self.author_box.GetValue()
		year = self.year_box.GetValue()
		pages = self.pages_box.GetValue()

		kwargs = {
			k: v for k, v in zip(
				("id", "navn", "forfatter", "år", "sider"),
				(index, name, author, year, pages)
			) if v}  # Format items as kwargs

		db.update(index, **kwargs)
		db.commit()
		self.Parent.ResetSearch(event)
		self.EndModal(0)


class ReplaceDialog(gui.ApprovalDialog):
	def __init__(self, parent):
		gui.ApprovalDialog.__init__(self, parent)
		self.validate_text.SetLabel("Er du sikker på, at du vil overskrive din database? "
									"Denne handling kan ikke omvendes. "
									"Overvej at eksporterer din nuværende database først.")
		self.validate_text.Wrap(250)  # Generalize ApprovalDialog for future use, manually set test and wrap it

	def Accept(self, event):
		self.EndModal(0)

	def Cancel(self, event):
		self.EndModal(-1)


if __name__ == "__main__":
	db = Database()
	app = wx.App()
	frame = MainFrame(None, "-dbg" in sys.argv)
	frame.Show(True)
	app.MainLoop()
