from tkinter import *

class Box:
    def __init__(self, size, stake_size):
        self.size = size
        self.stake_size = stake_size*2
        
    def in_horizontal_contact(self, x):
        return x <= 0 or x >= self.size
        
    def in_vertical_contact(self, y):
        return y <= 0 or y >= self.size

    def ball_contact(self,x,y): #이걸 가로랑 세로로 쪼개라
        
        return self.size/2-self.stake_size <= x <= self.size/2+self.stake_size\
                and  self.size/2-self.stake_size <=  y <= self.size/2+self.stake_size
        
class Ball2Ball:
    
    def __init__(self,ball,ball2):
         self.ball = ball
         self.ball2 = ball2

    def ball2ball_contact(self):
        x = self.ball.x
        y = self.ball.y
        x2 = self.ball2.x
        y2 = self.ball2.y

        if x == x2 and y == y2:
            self.ball.xv = -self.ball.xv
            self.ball.yv = -self.ball.yv
            self.ball2.xv = -self.ball2.xv
            self.ball2.yv = -self.ball2.yv




class MovingBall:
    def __init__(self, x, y, xv, yv, color, size, box):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.color = color
        self.size = size
        self.box = box


    def move(self, time_unit):
        self.x = self.x + self.xv * time_unit
        if self.box.in_horizontal_contact(self.x): #수평방향에 부딪혔는가? 장애물이 있는 좌표 범위 내에 들어왔는가? 로 확인
            self.xv = - self.xv
        self.y = self.y + self.yv * time_unit
        if self.box.in_vertical_contact(self.y):
            self.yv = - self.yv

        if self.box.ball_contact(self.x,self.y):
             self.xv = -self.xv
             self.yv = -self.yv


    



class AnimationWriter:
    def __init__(self, root, ball, ball2, box):
        size = box.size
        self.canvas = Canvas(root, width=size, height=size)
        self.canvas.grid()
        self.ball = ball
        self.ball2 = ball2
            
    def animate(self):
        self.canvas.delete(ALL)
        self.ball.move(1)
        self.ball2.move(1)
        x = self.ball.x
        y = self.ball.y
        x2 = self.ball2.x
        y2 = self.ball2.y
        d = self.ball.size * 2

        c = self.ball.color
        e = self.ball2.color

        self.canvas.create_oval(x, y, x+d , y+d, outline=c, fill=c)
        self.canvas.create_oval(x2, y2, x2+d, y2+d, outline=e, fill=e)
        self.canvas.create_rectangle(180,220,220,180, outline = 'blue', fill = 'blue')
        Ball2Ball.ball2ball_contact(self)
        self.canvas.after(10, self.animate)
        
class BounceController:
    def __init__(self):
        box_size = 400
        ball_size = 10
        ball_color = 'red'
        ball_color2 = 'green'
        s_size = 20
        s_color = 'blue'
        x_velocity, y_velocity = 2, 5
        root = Tk()
        root.title("Bouncing Ball")
        root.geometry(str(box_size+10)+"x"+str(box_size+10))
        box = Box(box_size, ball_size)
        #장애물을 생성하고, 애니메이션라이터에 기둥 객체 인자로 전달을 하고, 애니메이트 함수에서 박스를 그리고 공 클래스에서 무브메소드에서 닿았는지 체크후에 공방향을 바꾼다.
        # stake = create_rectangle(x0,y0,x1,y1,outline = 'blue', fill = 'blue')
        # stake = Box(s_size,s_color)
        ball = MovingBall(box_size//3, box_size//5, x_velocity, y_velocity, ball_color, ball_size, box)
        ball2 = MovingBall(box_size//3,box_size//5, x_velocity, -y_velocity, ball_color2, ball_size, box)
        AnimationWriter(root, ball, ball2, box).animate()
        root.mainloop()
    
BounceController()


