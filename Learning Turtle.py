import turtle

window = turtle.Screen()
window.bgcolor("dark green")
window.title("Turtle")
tortuguis = turtle.Turtle()

x, y = 1, 1
tortuguis.home()
tortuguis.speed(1)
for i in range(6):
    tortuguis.goto(10*x,10*y)
    # tortuguis.fd(2*x)
    # tortuguis.left(90)
    x, y = y, x+y

turtle.done()

# for i in range(3):
#     tortuguis.forward(100)
#     tortuguis.right(360/3)


# for i in range(90):
#     tortuguis.forward(10 + 5*i)
#     tortuguis.left(90)

