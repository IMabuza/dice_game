# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView

def main():

	# create the application window
	win = GraphWin("Dice Roller",)
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	# draw the interface widgets

	Button(win, Point(4,2), 3, 2, "Roll")
	Button(win, Point(8,2), 3, 2, "Quit")

	DieView(win, Point(3,6), 3)
	DieView(win, Point(7,6), 3)

	# event loop

	# close the window
	win.getMouse()
	win.close()

main()
