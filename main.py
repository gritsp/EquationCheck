import random
def login(name):
    #User story
    #เพื่อให้มีการเก็บข้อมูลของผู้่เล่นและแสดงข้อความต้อนรับ
    #ในฐานะผู้เล่น
    #จะต้องกรอกชื่อของผู้เล่น

    #Scenario
    #ให้ชื่อของผู็เล่นคือ TEST
    #เมื่่อกรอกเสร็จ
    #จากนั้นจะแสดงข้อความ "Wellcome TEST"

    #purpose: เก็บข้อมูลของผู้่เล่นและแสดงข้อความต้อนรับ
    #input: name(string)
    #output: "Wellcome " name(string)
    #contract: login(string) --> string
    #example: login(TEST) --> "Wellcome TEST"

    print("Hello %s :)\n"%name)
    return name

def EquationCreate(num1,num2,num3,symbol1,symbol2,lv):
    #User stroy
    #เพื่อสร้างคำตอบของสมการ
    #ในฐานะผู้เล่น
    #จะต้องสร้างสมการแล้วหาคำตอบของสมการ

    #Scenario 1 lv = "1"
    #ให้ 1+2+3
    #เมื่อหาคำตอบของสมการ
    #จากนั้นคำตอบของสมการคือ 3

    #Scenario 2 lv = "2"
    #ให้ 1+2+3
    #เมื่อหาคำตอบของสมการ
    #จากนั้นคำตอบของสมการคือ 6

    #purpose: เพื่อหาคำตอบของสมการ
    #input: num1(int), num2(int), num3(int), symbol1(char), symbol2(char) ,lv(char)
    #output: Equation(int)
    #contract: EquationCreate(num1,num2,num3,symbol1,symbol2,lv) --> Equation(int)
    #example: EquationCreate(1,2,3,+,+,1) --> 3
    #         EquationCreate(1,2,3,+,+,2) --> 6
    global Equation
    if symbol1 == "+":
        Equation = num1+num2
    elif symbol1 == "-":
        Equation = num1-num2
    elif symbol1 == "*":
        Equation = num1*num2
    elif symbol1 == "/":
        Equation = num1/num2
    if lv == "2":
        if symbol2 == "+":
            Equation = Equation + num3
            return Equation
        elif symbol2 == "-":
            Equation = Equation - num3
            return Equation
        elif symbol2 == "*":
            Equation = Equation * num3
            return Equation 
        elif symbol2 == "/":
            Equation = Equation / num3
            return Equation
    return Equation 

def answer(num1,num2,num3,symbol1,symbol2,lv,Equation):
    #User story
    #เพื่อสุ่มคำตอบของสมการออกมา
    #ในฐานะผู้ใช้
    #จะต้องสุ่มคำตอบออกมา

    #Scinario 1
    #ให้คำตอบที่สุ่มมาตรงกับคำตอบของสมาการ
    #เมื่อทำการสุ่ม
    #จะได้คำตอบที่สุ่มมาตรงกับคำตอบของสมาการ

    #Scinario 2
    #ให้คำตอบที่สุ่มมามากกว่าคำตอบของสมาการ
    #เมื่อทำการสุ่ม
    #จะได้คำตอบที่สุ่มมามากกว่าคำตอบของสมาการ

    #Scinario 3
    #ให้คำตอบที่สุ่มมาน้อยกว่าคำตอบของสมาการ
    #เมื่อทำการสุ่ม
    #จะได้คำตอบที่สุ่มมาน้อยกว่าคำตอบของสมาการ

    #purpose: สุ่มคำตอบของสมการออกมา
    #input num1,num2,num3,symbol1,symbol2,lv,Equation
    #output answer_show(int)
    #contract: answer(num1,num2,num3,symbol1,symbol2,lv,Equation) --> ans_show(int)
    #example: answer(1,2,3,+,+,"1",3) --> 3
    #         answer(1,2,3,+,+,"1",3) --> 4
    #         answer(1,2,3,+,+,"1",3) --> 2

    global answer_show
    if lv == "1":
        answerlist = []
        answerlist.append(Equation)
        # answerlist.append(Equation - 1) ใส่คอมเม้นเพื่อให้ตอนเทสสามารถสุ่มมาได้ 1 ตัว
        # answerlist.append(Equation + 1)
        answer_show = random.choice(answerlist)
        print("%s %s %s = %s"%(num1,symbol1,num2,answer_show))
        return answer_show
    if lv == "2":
        answerlist = []
        answerlist.append(Equation)
        # answerlist.append(Equation - 5) ใส่คอมเม้นเพื่อให้ตอนเทสสามารถสุ่มมาได้ 1 ตัว
        # answerlist.append(Equation + 5)
        answer_show = random.choice(answerlist)
        print("(%s %s %s) %s %s = %s"%(num1,symbol1,num2,symbol2,num3,answer_show))
        return answer_show

def answer_check(Equation,answer_show,answer_input):
    #User story
    #เพื่อเช็คว่าผู้เล่นตอบถูกหรือไม่
    #ในฐานะผู้ใช้
    #ต้องตอบ T หรือ F

    #Scinario 1
    #ให้ผู้ใช้ตอบ T และ สมการถูกต้อง
    #เมื่อประมาวผล
    #จากนั้นจะ return True

    #Scinario 2
    #ให้ผู้ใช้ตอบ F และ สมการผิด
    #เมื่อประมาวผล
    #จากนั้นจะ return True

    #Scinario 3
    #ให้ผู้ใช้ตอบ T และ สมการผิด
    #เมื่อประมาวผล
    #จากนั้นจะ return False

    #Scinario 4
    #ให้ผู้ใช้ตอบ F และ สมการถูก
    #เมื่อประมาวผล
    #จากนั้นจะ return False

    #purpose: เช็คว่าผู้เล่นตอบถูกหรือไม่
    #input: Equation(int), answer_show(int), answer_input(char)
    #output: if user True return True
    #        else user False return False
    #contract: answer_check(Equation,answer_show,answer_input) --> boolean
    #example: answer_check(3,3,"T")--> True
    #         answer_check(3,3,"T")--> True
    #         answer_check(3,3,"T")--> True
    #         answer_check(3,3,"T")--> True
    if (Equation == answer_show and answer_input == "T") or (Equation != answer_show and answer_input == "F"):
        return True
    else:
        return False