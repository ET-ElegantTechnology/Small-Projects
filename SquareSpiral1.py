# SpiralSquare.py - Draws a square spiral
import turtle

t = turtle.Pen()
t.pencolor("Purple")
for x in range(100):
    t.circle(x)
    t.left(91)
