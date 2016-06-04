__author__ = 'Ashwini Rajesh Singh'

"""
CSCI-603: Assignment 1
Author: Ashwini Singh

This is a program to display Name of Author.

"""



import turtle
import math

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
def init(x,y,z):
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (north), up
    :return: None
    """

    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    turtle.setheading(0)
    turtle.hideturtle()
    turtle.title('Name')
    turtle.up()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(z)
    turtle.speed(0)
    turtle.left(90)
    turtle.down()


def setPos(x):
    """
    Set position for turtle after drawing any letter
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (north), up
    :return: None
    """


    turtle.up()
    turtle.forward(x/3)
    turtle.left(90)
    turtle.down()

    pass

def drawA(x):
    """
    Draw A.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """

    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x/1.5)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/1.5)
    turtle.right(180)
    turtle.forward(x/1.5)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.left(90)
    pass

def drawS(x):
    """
    Draw S.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """


    turtle.right(90)
    turtle.forward(x/1.5)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x/1.5)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/1.5)
    turtle.right(90)
    turtle.up()
    turtle.forward(x)
    turtle.left(90)
    turtle.down()

    pass

def drawH(x):
    """
    Draw H.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """


    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x/1.5)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(180)
    turtle.forward(x)
    turtle.left(90)

    pass

def drawW(x):
    """
    Draw W.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """


    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x)
    turtle.left(135)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.left(135)
    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x)
    turtle.left(90)
pass

def drawI(x):
    """
    Draw I.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """


    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x)
    turtle.left(90)

    pass

def drawN(x):
    """
    Draw N.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """


    turtle.forward(x)
    turtle.right(150)
    turtle.forward(x/math.cos(math.radians(30)))
    turtle.left(150)
    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x)
    turtle.left(90)


    pass

def drawR(x):

    """
    Draw R.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """

    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.left(135)
    turtle.forward((x)*math.cos(math.radians(45)))
    turtle.left(45)

    pass

def drawG(x):

   """
    Draw I.
    :pre: (relative) pos (0,0), heading (north), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """

   turtle.forward(x)
   turtle.right(90)
   turtle.forward(x/2)
   turtle.right(90)
   turtle.forward(x/4)
   turtle.right(180)
   turtle.forward(x/4)
   turtle.left(90)
   turtle.forward(x/2)
   turtle.left(90)
   turtle.forward(x)
   turtle.left(90)
   turtle.forward(x/4)
   turtle.left(90)
   turtle.forward(x/3)
   turtle.right(90)
   turtle.forward(x/4)
   turtle.right(90)
   turtle.forward(x/3)
   turtle.left(90)



   pass

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    init(-180,100,'green')
    drawA(50)
    setPos(50)
    drawS(50)
    setPos(50)
    drawH(50)
    setPos(50)
    drawW(50)
    setPos(50)
    drawI(50)
    setPos(50)
    drawN(50)
    setPos(50)
    drawI(50)
    setPos(50)
    init(-50,0,'red')
    drawR(50)
    turtle.up()
    turtle.forward(5)
    turtle.down()
    turtle.dot(5)
    init(-140,-100,'blue')
    drawS(50)
    setPos(50)
    drawI(50)
    setPos(50)
    drawN(50)
    setPos(50)
    drawG(50)
    setPos(50)
    drawH(50)


    input('Hit enter to close...')

    turtle.bye()
main()

