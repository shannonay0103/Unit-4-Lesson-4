from turtle import *

toht = Turtle()

toht.color('blue')
toht.pensize(5)
toht.speed(9)
toht.shape('turtle')

for x in range(4):
	toht.circle(25)
	toht.circle(50)
	toht.forward(80)
	toht.left(50)
	toht.forward(200)
	toht.right(150)
	toht.forward(50)
	toht.backward(30)



mainloop()