import pgzrun 

WIDTH = 870
HEIGHT = 650


marquee_box = Rect(0,0,880,80)

question_box = Rect(20,100,650,150)

answer_box1 = Rect(20,270,300,150)
answer_box2 = Rect(360,270,300,150)
answer_box3 = Rect(20,450,300,150)
answer_box4 = Rect(360,450,300,150)

skip_box = Rect(690,270,150,330)
timer_box = Rect(688,100,150,150)

def draw(): 
    screen.fill(color= "black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navyblue")
    screen.draw.filled_rect(answer_box1, "darkorange")
    screen.draw.filled_rect(answer_box2, "darkorange")
    screen.draw.filled_rect(answer_box3, "darkorange")
    screen.draw.filled_rect(answer_box4, "darkorange")
    screen.draw.filled_rect(skip_box, "darkgreen")
    screen.draw.filled_rect(timer_box, "navyblue")


pgzrun.go()