import turtle
t = turtle.Pen()
colors = ["red", "purple", "blue", "yellow"]
turtle.bgcolor("black")
sides = 6
for x in range(360):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.right(91)