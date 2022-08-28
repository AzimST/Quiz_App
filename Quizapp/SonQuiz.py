# import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

# import json to use json file for data
import json
# import random to use database index
import random
# import dictionary dictionary our database
import dictionary

class Quiz:
    def __init__(self):
        # CONNECT TO DATABASE
        self.wordDatabase = dictionary.Dictionary()


        # CREATE WİDGETS
        self.disp_title()
        self.display_question()
        self.buttons()
        self.opts = self.radio_buttons()

        # MAX QUESTİON
        # self.total_size = 25
        # QUESTİON COUNTER
        self.qno=0
        # CORRECT COUNTER
        self.correct = 0
        self.wrong = 0
        self.answer = Label(mainS, text="", font="Times 20")
        self.answer.place(x=275, y=110)

    def display_question(self):
        # NUMBER FOR THE QUESTİONS İNDEX
        self.randomIndex = random.randrange(1, self.wordDatabase.databaseCounter())
        # SELECT WORD OF QUESİTON
        self.word = self.wordDatabase.questionFind(index=self.randomIndex)

        self.question = Label(mainS, text=self.word.english, font="Times 25")
        self.question.place(x=75, y=50)


    # DİSPLAY RESULT İNFO
    def display_result(self):
        # wrong_count = self.total_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {self.wrong}"

        score = int(self.correct / self.qno *100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # CHECKİNG THE ANSWER
    def check_Answer(self):
        choice = self.var.get()
        flag = False
        if (choice == self.word.index):
            flag = True
        return flag

    # BUTTON FOR THE NEXT QUESTİON
    def next_button(self):
        if self.check_Answer():
            self.correct += 1
        else:
            self.wrong += 1
        self.qno += 1

        self.clear()
        self.display_isCorrect()
        self.display_question()
        self.radio_buttons()

    # BUTTON DİSPLAY
    def buttons(self):
        next_button = Button(mainS,
                             text="Next",command=self.next_button,
                             width=12,bg="#F2780c",fg="white",font="ariel 16")

        quit_button = Button(mainS,text="quit",command=mainS.destroy,
                             width=8,bg="black",fg="white",font="ariel 16 ")

        add_button = Button(mainS, text="Add Word", command=self.wordAddButton, width=8, bg="red", fg="white", font="ariel 16")

        Rslt_but = Button(mainS, text="Display Result", command=self.display_result, width=12, bg="red", fg="white", font="ariel 16")

        Rslt_but.place(x=350,y=300)

        next_button.place(x=350,y=350)

        quit_button.place(x=640,y=50)

        add_button.place(x=640,y=100)

    def disp_title(self):

        title = Label(mainS,text="English Word Game",width=50,bg="green",
                      fg="white",font="ariel 20 bold")
        title.place(x=0,y=2)

    # RADİO BUTTON DİSPLAY
    def radio_buttons(self):
        # THİS CHAPTER, CHOOSE RANDOM LOCATİONS FOR THE RADİO BUTTONS
        locList = [100, 125, 150, 175]
        loc1 = random.choice(locList)
        locList.remove(loc1)
        loc2 = random.choice(locList)
        locList.remove(loc2)
        loc3 = random.choice(locList)
        locList.remove(loc3)
        loc4 = random.choice(locList)
        locList.remove(loc4)

        # CHOOSE WRONG ANSWER
        fAnswer, fAnswer2, fAnswer3 = self.random_number()
        fAnswerW, fAnswerW2, fAnswerW1 = self.wordDatabase.answerFind(fAnswer, fAnswer2, fAnswer3)

        self.var = IntVar()
        self.rdButton = Radiobutton(mainS, text=self.word.turkish, variable=self.var, value=self.word.index,
                                    command=self.check_Answer)
        self.rdButton1 = Radiobutton(mainS, text=fAnswerW, variable=self.var, value=fAnswer, command=self.check_Answer)
        self.rdButton2 = Radiobutton(mainS, text=fAnswerW1, variable=self.var, value=fAnswer2,
                                     command=self.check_Answer)
        self.rdButton3 = Radiobutton(mainS, text=fAnswerW2, variable=self.var, value=fAnswer3,
                                     command=self.check_Answer)

        self.rdButton1.place(x=75, y=loc1)
        self.rdButton2.place(x=75, y=loc2)
        self.rdButton.place(x=75, y=loc3)
        self.rdButton3.place(x=75, y=loc4)

    def random_number(self):
        rnd1, rnd2, rnd3 = 1, 1, 1
        while (rnd1 == rnd2 == rnd3) and (rnd1 != self.randomIndex) and (rnd3 != self.randomIndex) and \
                (rnd2 != self.randomIndex):
            rnd1 = random.randrange(1, 420)
            rnd3 = random.randrange(1, 420)
            rnd2 = random.randrange(1, 420)
        return rnd1, rnd2, rnd3

    # CLEAR PAGE
    def clear(self):
        self.rdButton1.place_forget()
        self.rdButton2.place_forget()
        self.rdButton.place_forget()
        self.rdButton3.place_forget()
        self.question.place_forget()
        self.answer.place_forget()

    def wordAddButton(self):
        addPage = Tk()

        addPage.title("Add word")
        addPage.geometry("250x200")
        infoLabel = Label(addPage,text="Kelime girin",font="Times 20",width=17,bg="red")

        englishLabel = Label(addPage,text="English",font="Times 12", width=5)
        turkıshLabel = Label(addPage, text="Turkish", font="Times 12", width=5)

        self.wordEntryEnglish = Entry(addPage)
        self.wordEntryTurkısh = Entry(addPage)

        acceptButton = Button(addPage,text="Accept",command=self.wordAddFunction, font="Times 20",bg="green",fg="black",padx=78)

        infoLabel.place(x=0,y=2)
        englishLabel.place(x=20,y=70)
        turkıshLabel.place(x=20,y=95)

        self.wordEntryEnglish.place(x=100,y=75)
        self.wordEntryTurkısh.place(x=100,y=100)

        acceptButton.place(x=-1,y=150)

        addPage.mainloop


    def wordAddFunction(self):
        english = self.wordEntryEnglish.get()
        turkish = self.wordEntryTurkısh.get()

        newWord=dictionary.Word(english=english,turkish=turkish,index=self.wordDatabase.databaseCounter()+1)
        self.wordDatabase.add_words(newWord)


    def display_isCorrect(self):
        if self.check_Answer():
            answer = "CORRECT"
        else:
            answer = "WRONG"

        self.answer = Label(mainS, text=answer, font="Times 15")
        self.answer.place(x=275, y=110)




mainS= Tk()

mainS.title("Quiz App")
mainS.geometry("750x400")


quiz = Quiz()
mainS.mainloop()
