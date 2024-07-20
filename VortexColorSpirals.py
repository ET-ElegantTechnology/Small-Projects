import turtle
t = turtle.Pen()
turtle.bgcolor("black")

# You can choose between 2 and 6 sides for some interesting shapes
sides = 3
colors = ["red", "purple", "green", "yellow", "blue", "orange", "white", "teal"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(int(x * sides/200))
