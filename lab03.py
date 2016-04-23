# lab03.py for Jacob Leonard
# CS20, Spring 2016, Instructor: Phill Conrad
# Draw some initials using turtle graphics

import turtle

t=turtle.Turtle()

def drawJ(t,w,h):
    """
    draw the letter J using t, with some width and height
    """
    #pick up pen
    t.up()
    #prepare to move
    t.left(90)
    #position t for hook preparing the radius to complete the height
    t.forward(w*3.0/8.0)
    #prepare to draw hook
    t.right(180)
    t.down()
    #make hook preparing the width for the extra at the top
    t.circle(w*3.0/8.0,180.0)
    #make the neck
    t.forward(h-w*3.0/8.0)
    #position t for the top
    t.left(90.0)
    #make the top
    t.forward(w/4.0)
    t.right(180)
    t.forward(w/2.0)
    #pick up pen
    t.up()
    #prepare to go to lower right
    t.right(90)
    #go to the lower right
    t.forward(h)
    #get in position
    t.left(90)
    t.down()

def drawL(t,w,h):
    """
    draw the letter J using t, with some width and height
    """
    #position t for neck
    t.left(90)
    #make the neck full height and come back
    t.forward(h)
    t.backward(h)
    #position t for bottom
    t.right(90)
    #make bottom end up at lower right
    t.forward(w)
    
def drawJL(t,w,h):
    """
    draw the initials JL using t, with some width and height
    """
    #draw J
    drawJ(t,w,h)
    #prepare for spacing
    t.up()
    #make spacing
    t.forward(w/4.0)
    #put down pen
    t.down()
    #draw L
    drawL(t,w,h)

def go():
    """
    draw the initials three times, with different sizes
    """
    #draw first
    drawJL(t,30.0,50.0)
    #pick up pen
    t.up()
    #move for next one
    t.goto(120.0,50.0)
    #put down pen
    t.down()
    #draw second
    drawJL(t,80.0,170.0)
    #move for nex#pick up pen
    t.up()
    #move for next one
    t.goto(-180.0,10.0)
    #put down pen
    t.down()
    #draw third
    drawJL(t,50.0,100.0)

go()

