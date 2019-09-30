def best(name,score):
    #User story
    #เพื่อให้มีการบันทึกคะแนนที่ดีที่สุด
    #ในฐานะผู้เล่น
    #จะต้องใส่ชื่อและเล่นให้คะแนนมากว่าผู้เล่นคนอื่นก่อนหน้า

    #Scenario 1 (ผู้เล่น ก ทำคะแนนได้ 10 ผู้เล่น ข ทำคะแนนได้ 5)
    #ให้ผู้เล่น ก ทำคะแนนได้ 10 ผู้เล่น ข ทำคะแนนได้ 5
    #เมื่อทำการคำนวน
    #จากนั้นจะแสดง "You get hight score than ข"

    #purpose: บันทึกคะแนนที่ดีที่สุด
    #input: name(str),score(int)
    #output: "You get hight score than name(str)"
    #contract: best(name,score)-->best.txt and ("You get hight score than ...")
    #example: best(test,15)-->best.txt and "You get hight score than"
    best = open("best.txt")
    get = best.read()
    highscore = get.split("\n")
    remove_space = highscore.pop()

    clear = open("best.txt","w")
    clear.close()

    for line in highscore:
        best_name, best_score = line.split(" - ")
        if score > int(best_score):
            target = open("best.txt","a")
            print("You get hight score than %s"%best_name)
            target.write("%s - %s\n"%(name,score))
            name = best_name
            score = int(best_score)
       
        else:
            target = open("best.txt","a")
            target.write("%s - %s\n"%(best_name,best_score))
            target.close()
    
    show_best()

def show_best():
    
    print("\n__________#TOP 5:__________")
    best = open("best.txt")
    get = best.read()
    highscore = get.split("\n")
    remove_space = highscore.pop()

    num = 0

    for line in highscore:
        num += 1
        best_name,best_score = line.split(" - ")
        print(" Number %d: %s score: %s "%(num, best_name,best_score))
    
    best.close()