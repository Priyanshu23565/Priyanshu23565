from turtle import *





#                  DESIGN
'''
bgcolor('black')
speed(120)
hideturtle()
for i in range(220):
    color('red')
    circle(i)
    # color('orange')
    circle(i * 1)
    # right(30)
    forward(3)
done()

'''






# turtle.speed(60)
# turtle.pensize(1)
# colors = ('orange', 'yellow', 'pnk', 'green')
#
# for i in range(200):
#     turtle.forward(i * 4)
#     turtle.right(91)
#     turtle.color(colors[i * 5])
#
#     for x in range(3):
#         turtle.forward(x * 4)
#         turtle.right(91)
#
#         for a in range(2):
#             turtle.forward(a * 4)
#             turtle.right(91)
#
#             for m in range(739):
#                 turtle.forward(m * 4)
#                 turtle.right(891)

#                        Simple Logic star Programe ...
# b.getscreen()
# b.left(45)
# b.forward(100)
# b.right(45)
# b.backward(130)
# b.right(50)
# b.forward(100)


#                        Create A Star Programe using Python ..

# b.forward(200)
# b.left(216)
# b.forward(200)
# b.left(216)
# b.forward(200)
# b.left(216)
# b.forward(200)
# b.left(216)
# b.forward(200)
# b.left(216)


#     Using For Loop   Create a star Programe


# for i in range(5):
#     b.forward(200)
#     b.left(216)
#

#        Create a Function


# def star(a, size):

#                             STAR PROGRAMME IN STAR


'''
def star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(216)


star(b, 200)
turtle.done()
'''

#                     PYTHON FLOWER  DESIGN
'''    

b = turtle.Turtle()
b.getscreen().bgcolor("black")

turtle.speed(10)
turtle.color('red')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 2:
        break

turtle.end()
turtle.done()

'''
