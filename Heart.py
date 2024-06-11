import turtle
pen = turtle.Turtle()
def curve() :
    for i in range(200):
        
        pen.right(1)
        pen.forward(1)

def heart() :
       
        pen.fillcolor('red')
        pen.left(135)
        pen.forward(135)
        curve()
        pen.left(135)
        curve()
        pen.forward(135)
        pen.end_fill()

def txt():
       
        pen.up()
        pen.setpos(-68 , 95)
        pen.down()
        pen.color('lightgreen')
        pen.write("Palak Chandak ", font = ("Verdana" , 12 , "bold"))    

heart()
txt()
pen.ht()