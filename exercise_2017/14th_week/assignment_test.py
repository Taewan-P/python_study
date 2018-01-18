from tkinter import *

class Box:
    def __init__(self, size):
        self.size = size

    def in_horizontal_contact(self, x):
        return x <= 0 or x >= self.size

    def in_vertical_contact(self, y):
        return y <= 0 or y >= self.size

class MovingBall:
    def __init__(self, x, y, xv, yv, color, size, box):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.color = color
        self.size = size
        self.box = box

    def move(self, time_unit, x, y):
        self.x = self.x + self.xv * time_unit
        if self.box.in_horizontal_contact(self.x) or 150 <= self.x <= 250 and 150 <= self.y <= 250 :
            self.xv = - self.xv
        self.y = self.y + self.yv * time_unit
        if self.box.in_vertical_contact(self.y) or 150 <= self.x <= 250 and 150 <= self.y <= 250 :
            self.yv = - self.yv
        if (self.x - 10) <= x <= (self.x + 10) and (self.y - 10) <= y <= (self.y + 10) :
            self.yv = - self.yv
            self.xv = - self.xv

class AnimationWriter:
    def __init__(self, root, ball1, ball2, box):
        size = box.size
        self.canvas = Canvas(root, width=size, height=size)
        self.canvas.grid()
        self.ball1 = ball1
        self.ball2 = ball2

    def animate(self):
        self.canvas.delete(ALL)

        x1 = self.ball1.x
        y1 = self.ball1.y
        d1 = self.ball1.size * 2
        c1 = self.ball1.color

        x2 = self.ball2.x
        y2 = self.ball2.y
        d2 = self.ball2.size * 2
        c2 = self.ball2.color

        self.ball1.move(1, x2, y2)
        self.ball2.move(1, x1, y1)

        self.canvas.create_oval(x1, y1, x1+d1 , y1+d1, outline=c1, fill=c1)
        self.canvas.create_oval(x2, y2, x2+d2 , y2+d2, outline=c2, fill=c2)

        self.canvas.after(10, self.animate)

        self.canvas.create_rectangle(150, 150, 250, 250, fill='blue')

class BounceController:
    def __init__(self):
        box_size = 400
        ball_size = 10
        ball_color1 = 'red'
        ball_color2 = 'green'
        x_velocity, y_velocity = 5, 3
        root = Tk()
        root.title("Bouncing Ball")
        root.geometry(str(box_size+10)+"x"+str(box_size+10))
        box = Box(box_size)
        ball1 = MovingBall(box_size//3, box_size//5, x_velocity, y_velocity, ball_color1, ball_size, box)
        ball2 = MovingBall(box_size//5, box_size//3, x_velocity, y_velocity, ball_color2, ball_size, box)
        AnimationWriter(root, ball1, ball2, box).animate()
        root.mainloop()

BounceController()