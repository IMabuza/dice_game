# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView
from msdie import MSdie

def main():

	# create the application window
	win = GraphWin("Dice Roller",)
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	# draw the interface widgets

	b1 = Button(win, Point(4,2), 3, 2, "Roll")
	b2 = Button(win, Point(8,2), 3, 2, "Quit")

	d1 = DieView(win, Point(3,6), 3)
	d2 = DieView(win, Point(7,6), 3)

	# event loop

	while True:
		if b1.clicked(win.getMouse()):
			d1.setValue(MSdie(6).roll())
			d2.setValue(MSdie(6).roll())
		elif b2.clicked(win.getMouse()):
			return False

	

	# close the window
	win.close()

main()
