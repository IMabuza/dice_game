from graphics import *

class Button:
	""" A button is a labeled rectangle in a window. It is activated or deactivated
	with the activate() and deactivate() methods. The clicked (p) method returns
	true if the button is active and p is inside it. """

	def __init__ (self, win, center, width, height, label):
		"""" creates a rectangualr button, eg:"""
		""" qp = Button (myWin, centerPoint, width, height, 'quit')"""

		#set attributes here


		self.win = win

		self.width = width/2
		self.height = height/2
		
		centerX = center.getX()
		centerY = center.getY()

		self.x1 = centerX - self.width
		self.x2 = centerX + self.width
		self.y1 = centerY - self.height
		self.y2 = centerY + self.height

		self.rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
		self.rect.setFill("white")
		self.rect.draw(win)
		self.label = Text(center, label)
		self.label.draw(self.win)
		self.activate()

		

	def clicked(self, p):
		"""returns true if the button active and p is inside"""

		if self.active and self.x1 <= p.getX() <= self.x2 and self.y1 <= p.getY() <= self.y2:
			return True

	#CODE

	def getLabel(self):
		"""returns the label string of the button"""
		return self.label.getText()

	#CODE

	def activate(self):
		"""Sets this button to 'active'"""
		self.rect.setFill("white")
		self.active = True


	#CODE

	def deactivate (self):
		"""Sets this button to 'inactive'"""
		self.rect.setFill("grey")
		self.active = False
		
	
	#CODE