import turtle
fin = turtle.Turtle()
s = turtle.Screen()
  
# Turtle to draw a spiral
def drawSpiral(myTurtle, linelen):
    fin.forward(linelen)
    fin.right(90)
    drawSpiral(fin, linelen-5)
  
drawSpiral(fin, 80)
s.exitonclick()

