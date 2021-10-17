from tkinter import *
import turtle
import random
import time

t=turtle.Turtle()

words=["cat","hat","desk","house","water","python","computer"]

#꽃잎 그리기
def petal():
    t.begin_fill()
    t.fillcolor("red")
    t.rt(100)
    t.circle(50,250)
    t.end_fill()

    for i in range(6):
        t.begin_fill()
        t.fillcolor("red")
        t.rt(200)
        t.circle(50,250)
        t.end_fill()

#꽃 얼굴 그리기
def flower_face():
    t.penup()
    t.home()
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(100)
    t.end_fill()

    #꽃 눈 그리기
    t.penup()
    t.goto(-40,100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(40,100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.circle(10)
    t.end_fill()

#꽃 웃는 입 그리기
def flower_smile(a,b):
    t.penup()
    t.goto(0,50)
    t.pendown()
    for x in range(a):
        y=x**2+50
        t.goto(-x*b,y)

    t.penup()
    t.goto(0,50)
    t.pendown()
    for x in range(a):
        y=x**2+50
        t.goto(x*b,y)

#꽃 우는 입 그리기
def flower_cry(a,b):
    t.penup()
    t.goto(0,50)
    t.pendown()
    for x in range(a):
        y=-(x**2)+50
        t.goto(-x*b,y)

    t.penup()
    t.goto(0,50)
    t.pendown()
    for x in range(a):
        y=-(x**2)+50
        t.goto(x*b,y)

#줄기 그리기
def stem():
    t.penup()
    t.home()
    t.pendown()
    t.begin_fill()
    t.color("green")
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(300)
    t.end_fill()

#잎 그리기
def leaf():
    t.begin_fill()
    for x in range(6):
        y=3**x-300
        t.goto(30*x,y)
    t.goto(0,-250)
    t.end_fill()

    t.begin_fill()
    for x in range(6):
        y=3**x-300
        t.goto(-30*x,y)
    t.goto(-20,-250)
    t.end_fill()

#꽃 그리기
def flower():
    petal()
    flower_face()
    flower_smile(7,10)
    stem()
    leaf()

#꽃잎 지우기
def erase_petal(a,b):
    global miss_num
    t.penup()
    t.home()
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.rt(100)
    t.circle(50,250)
    t.end_fill()
    for i in range(miss_num-1):
        t.begin_fill()
        t.color("white")
        t.rt(200)
        t.circle(50,250)
        t.end_fill()
    
    t.color("black")
    flower_face()
    if miss_num<=3:
        flower_smile(a,b)
    else:
        flower_cry(a,b)

#대화 타이핑 효과 
def typing(who, sentence):
    print(who + " : " , end="")
    time.sleep(0.5)
    for i in range(0,len(sentence)):
        time.sleep(0.05)
        print(sentence[i], end="")
    time.sleep(0.5)
    print()


#게임방법설명
def rule():
    name=e.get()
    typing("꽃님이", "안녕 " + name + "아(야)? 나는 꽃님이라고해.")
    typing("꽃님이", "내 꽃잎들이 떨어지지 않게 좀 도와줄래? 주어진 단어를 찾을 때 까지 알파벳 입력창에 알파벳을 입력해주면 돼!")
    typing("꽃님이", "만약 단어에 없는 알파벳을 입력하면 내 꽃잎이 한 장씩 사라져...ㅠㅠ 그러니 신중히 생각해서 입력해줘!")


#입력버튼
def put():
    a=e2.get()
    answer=a
    e2.delete(0,END)
    global miss_num
    global answer_check
        
    if answer in word:
        p=word.index(answer)
        check[p]=answer
        answer_check=""
        for i in check:
            answer_check+=i
        print(answer_check)

    else:
        print("땡!")
        
        miss_num+=1
        
        if miss_num==1:
            erase_petal(7,10)
        elif miss_num==2:
            erase_petal(5,15)
        elif miss_num==3:
            erase_petal(3,30)
        elif miss_num==4:
            erase_petal(3,30)
        elif miss_num==5:
            erase_petal(5,15)
        elif miss_num==6:
            erase_petal(7,10)
        else:
            erase_petal(7,10)
            t.shape("circle")
            t.color("blue")
            t.penup()
            t.goto(40,70)
            t.stamp()
            t.goto(40,40)
            t.stamp()
            t.goto(-40,70)
            t.stamp()
            t.goto(-40,40)
            t.stamp()
            print("THE END")
            window2.destroy()
            typing("꽃님이","나만 없어...꽃잎...ㅠㅠ")
        
    if answer_check==word:
        print("정답!!")
        window2.destroy()
        typing("꽃님이","고마워! 덕분에 꽃잎을 "+ str(7-miss_num)+"장 지켰어ㅎㅎ")
        
#게임작동
def game():
    global window2
    global e2
    global word
    global check
    global answer_check
    global miss_num
    answer=""
    miss_num=0
    name=e.get()
    word=random.choice(words)
    l=len(word)
    check=[]
    for i in range(l):
        check.append("_")
    answer_check=""
    for i in check:
        answer_check+=i
    print(answer_check)

    window2=Tk()
    window2.title("알파벳 입력창")

    l2=Label(window2,text=name+"님 알파벳을 입력하세요")
    l2.grid(row=0,column=0)

    e2=Entry(window2)
    e2.grid(row=0,column=1)

    b2=Button(window2,text="입력",command=put)
    b2.grid(row=1,column=1)

    window2.mainloop()
    
#게임시작 버튼
def start():
    t.reset()
    t.speed(0)
    flower()
    rule()
    game()
    
#게임 시작
window=Tk()
window.title("꽃잎을 지켜라!")

l=Label(window,text="이름을 입력하세요")
l.grid(row=0,column=0)

e=Entry(window)
e.grid(row=0,column=1)

b=Button(window, text="게임시작",command=start)
b.grid(row=1,column=1)

window.mainloop()

