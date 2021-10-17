import turtle
import sys
import random
import time

t=turtle.Turtle()
t.speed(0)
words=["cat","hat","desk","house","water","python","computer"]


#걸이 만들기
def bar():
    t.penup()
    t.goto(-200,200)
    t.pendown()
    t.fd(200)
    t.goto(-200,200)
    t.rt(90)
    t.fd(500)
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.rt(90)

#선그리기
def line(x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    if x2 == None and y2 == None:
        t.lt(90)
        t.fd(200)
    else:
        t.goto(x2,y2)
    
#사람 만들기
try_num=0
def hangman():
    if try_num==1:
        t.circle(50)
    elif try_num==2:
        line(0,100,None,None)
    elif try_num==3:
        line(0,50,-50,-50)
    elif try_num==4:
        line(0,50,50,-50)
    elif try_num==5:
        line(0,-100,-50,-200)
    elif try_num==6:
        line(0,-100,50,-200)

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
def chat():
    typing(name,"어떻게 해주면 되는데?")
    typing("행맨이", "주어진 영어단어가 완성될 때까지 알파벳을 하나씩 맞추시면 돼요!")
    typing("행맨이", "만약 단어에 들어있지 않은 알파벳을 쓰시면 제 몸이 하나씩 처형대에 걸려져요.")
    typing("행맨이", "몸이 완성되면 저는 죽는답니다ㅠㅠ 살려주세요 제발~~!!")
    typing(name,"오케이!! 가즈아~!!")


#게임작동
def game():   
    t.reset()
    turtle.bgcolor("white")
    global try_num
    try_num=0
    bar()
    word=random.choice(words)
    l=len(word)
    check=[]
    for i in range(l):
        check.append("_")
    answer_check=""
    for i in check:
        answer_check+=i
    print(answer_check)

    while answer_check!=word:
        answer=input("알파벳을 입력해주세요!")
        if answer in word:
            p=word.index(answer)
            check[p]=answer

        else:
            try_num+=1
            hangman()

        answer_check=""
        for i in check:
            answer_check+=i
        print(answer_check)          

        if try_num==7 and answer not in word:
            break

    global start
    global score
    
    if answer_check==word:
        print("정답입니다!")
        typing("행맨이", "살려줘서 고마워요!")
        score+=100
        typing("행맨이", "한번 더?(yes/no)")
        start=input()
            
    else:
        turtle.bgcolor("red")
        print("THE END")
        typing("행맨이", "ㅠㅠ...한번 더?(yes/no)")
        start=input()
    
#게임 시작
typing("행맨이", "누구..세요??(이름을 입력해주세요!)")
name=input()
typing("행맨이", name + "님 저 좀 구해주시겠어요...?ㅠㅠ(yes/no)")
start=input()
if start=="yes":
    chat()
else:
    while start=="no":        
        typing("행맨이", "잠깐만!!! 다시 생각해봐요ㅠㅠ")
        typing("행맨이", name + "님 저 좀 구해주시겠어요...?ㅠㅠ(yes/no)")
        start=input()
    chat()

score=0
while start=="yes":
    game()

if start=="no":
    typing("행맨이","다음에 또 만나요~♥")
    print(name+"님의 score :",score)
    sys.exit()
