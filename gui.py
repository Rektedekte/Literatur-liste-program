# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LLP - Literatur Liste Program", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.new = wx.Button( self, wx.ID_ANY, u"Ny", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer2.Add( self.new, 0, wx.ALL, 5 )

		self.update_item = wx.Button( self, wx.ID_ANY, u"Opdater", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer2.Add( self.update_item, 0, wx.ALL, 5 )

		self.delete = wx.Button( self, wx.ID_ANY, u"Slet", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer2.Add( self.delete, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer2, 1, 0, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.advanced_search = wx.Button( self, wx.ID_ANY, u"Søg", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer17.Add( self.advanced_search, 0, wx.ALL, 5 )

		self.reset_search = wx.Button( self, wx.ID_ANY, u"Nulstil Søgning", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer17.Add( self.reset_search, 0, wx.ALL, 5 )

		self.id_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.id_input, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer17, 1, 0, 5 )


		bSizer1.Add( bSizer16, 1, 0, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		data_viewChoices = []
		self.data_view = wx.ListBox( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 600,300 ), data_viewChoices, 0 )
		bSizer3.Add( self.data_view, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.TOP, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.import_menu = wx.Menu()
		self.append_import_button = wx.MenuItem( self.import_menu, wx.ID_ANY, u"Tilføj", wx.EmptyString, wx.ITEM_NORMAL )
		self.import_menu.Append( self.append_import_button )

		self.replace_import_button = wx.MenuItem( self.import_menu, wx.ID_ANY, u"Erstat", wx.EmptyString, wx.ITEM_NORMAL )
		self.import_menu.Append( self.replace_import_button )

		self.m_menu1.AppendSubMenu( self.import_menu, u"Importer" )

		self.export_button = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Eksporter", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.export_button )

		self.exit_button = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Luk", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.exit_button )

		self.m_menubar1.Append( self.m_menu1, u"Fil" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.new.Bind( wx.EVT_BUTTON, self.New )
		self.update_item.Bind( wx.EVT_BUTTON, self.UpdateItem )
		self.delete.Bind( wx.EVT_BUTTON, self.DeleteItem )
		self.advanced_search.Bind( wx.EVT_BUTTON, self.Search )
		self.reset_search.Bind( wx.EVT_BUTTON, self.ResetSearch )
		self.id_input.Bind( wx.EVT_TEXT, self.IdChange )
		self.Bind( wx.EVT_MENU, self.AppendImport, id = self.append_import_button.GetId() )
		self.Bind( wx.EVT_MENU, self.ReplaceImport, id = self.replace_import_button.GetId() )
		self.Bind( wx.EVT_MENU, self.Export, id = self.export_button.GetId() )
		self.Bind( wx.EVT_MENU, self.Exit, id = self.exit_button.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSize( self, event ):
		event.Skip()

	def New( self, event ):
		event.Skip()

	def UpdateItem( self, event ):
		event.Skip()

	def DeleteItem( self, event ):
		event.Skip()

	def Search( self, event ):
		event.Skip()

	def ResetSearch( self, event ):
		event.Skip()

	def IdChange( self, event ):
		event.Skip()

	def AppendImport( self, event ):
		event.Skip()

	def ReplaceImport( self, event ):
		event.Skip()

	def Export( self, event ):
		event.Skip()

	def Exit( self, event ):
		event.Skip()


###########################################################################
## Class FileDialog
###########################################################################

class FileDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vælg fil", pos = wx.DefaultPosition, size = wx.Size( 300,120 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer21.Add( self.file_picker, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.accept_button = wx.Button( self, wx.ID_ANY, u"Accepter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.accept_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.accept_button.Bind( wx.EVT_BUTTON, self.Accept )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Accept( self, event ):
		event.Skip()


###########################################################################
## Class ApprovalDialog
###########################################################################

class ApprovalDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Er du sikker?", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.validate_text = wx.StaticText( self, wx.ID_ANY, u"Placeholder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.validate_text.Wrap( 250 )

		bSizer18.Add( self.validate_text, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.accept_button = wx.Button( self, wx.ID_ANY, u"Accepter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.accept_button, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Nej", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.cancel_button, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		bSizer21.Add( bSizer20, 1, wx.ALIGN_CENTER, 5 )


		bSizer17.Add( bSizer21, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Cancel )
		self.accept_button.Bind( wx.EVT_BUTTON, self.Accept )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Cancel( self, event ):
		event.Skip()

	def Accept( self, event ):
		event.Skip()



###########################################################################
## Class LookupDialog
###########################################################################

class LookupDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 200,280 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.id_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer11.Add( self.id_box, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Navn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.name_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 100,-1 ), 0 )
		bSizer12.Add( self.name_box, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer6.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Forfatter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.author_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer13.Add( self.author_box, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer7.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"År", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.year_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer14.Add( self.year_box, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer8.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Sider", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.pages_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer15.Add( self.pages_box, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer9.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.return_button = wx.Button( self, wx.ID_ANY, u"Søg", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.return_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.return_button.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Return( self, event ):
		event.Skip()


###########################################################################
## Class LogFrame
###########################################################################

class LogFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Log", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.log_label = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.log_label.Wrap( -1 )

		bSizer23.Add( self.log_label, 0, wx.ALL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


