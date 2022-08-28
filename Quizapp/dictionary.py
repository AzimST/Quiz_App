import sqlite3

import time

class Word():

    def __init__(self, turkish, english,index):

        self.turkish = turkish
        self.english = english
        self.index = index

    def __str__(self):

        return f"{self.english}: {self.turkish}"


class Dictionary():

    def __init__(self):

        self.make_connection()


    def make_connection(self):

        self.con = sqlite3.connect("dictionary.db")

        self.cursor = self.con.cursor()

        query = "Create Table If not exists dictionary (English TEXT,Turkish TEXT)"

        self.cursor.execute(query)

        self.con.commit()

    def stop_connection(self):
        self.con.close()

    def show_info(self):

        query = "Select * From dictionary"

        self.cursor.execute(query)

        words = self.cursor.fetchall()

        if (len(words) == 0):
            print("there's no word...")
        else:
            for i in range(len(words)):

                word = Word(words[i][1], words[i][0], i)
                print(word)

    def questionFind(self, index):


        query = f"Select * From dictionary where İndex = {index}"

        self.cursor.execute(query)
        words = self.cursor.fetchall()

        if (len(words) == 0):
            print("no such word in the dictionary.....")
        else:
            word = Word(words[0][2], words[0][1],words[0][0])

        return word


    def answerFind(self,index1,index2,index3):

        query = f"Select Turkish From dictionary where İndex = {index1} or İndex = {index2}" \
                f" or İndex = {index3}"

        self.cursor.execute(query)
        words = self.cursor.fetchall()

        return words[0][0],words[1][0],words[2][0]


    def add_words(self, Word):

        index = self.databaseCounter() + 1


        query = "Insert into dictionary Values(?,?,?)"

        self.cursor.execute(query,(index, Word.english, Word.turkish))

        self.con.commit()

    def delete_words(self,word):  # silmek istediğimiz kelimenin türkçesini vercez

        sorgu = "Delete From dictionary where Turkish = ?"

        self.cursor.execute(sorgu,(word,))

        self.con.commit()



    def databaseCounter(self):
        query = "SELECT COUNT(*) FROM dictionary"

        self.cursor.execute(query)
        size = self.cursor.fetchall()[0][0]

        return size