#!/usr/bin/env python

from Tkinter import *
# from ttk import *
from random import randint
# from PIL import Image, ImageTk

class Game(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        # self.geometry("200x200")
        
        self.found_letters = StringVar()
        self.found_letters.set(' '.join(h.found))
        self.found = Label(self,textvariable=self.found_letters,font=("Fira Sans",24,"bold"))
        self.found.grid(columnspan=3)
        
        self.guess_entry = StringVar()
        self.guess_box = Entry(self,textvariable=self.guess_entry)
        self.guess_box.bind("<Return>",self.on_return)        
        self.guess_button = Button(self,text="Guess",command=self.on_guess)
        
        self.guess_box.focus_set()
        # self.guess_box.selection_range(0,END)
        
        self.guess_box.grid(row=1,column=0,columnspan=2)
        self.guess_button.grid(row=1,column=2)
                
        blank = PhotoImage(file="0.gif")
        
        self.picture = Label(image=blank)#,height=100,width=100)
        self.picture.image = blank
        self.picture.grid(row=2,columnspan=2)
        
        self.missed_letters = StringVar()
        self.missed_letters.set(' '.join(h.missed))
        self.missed = Label(self,textvariable=self.missed_letters,font=("Fira Sans",18,"normal"),wraplength=60)
        self.missed.grid(row=2,column=2)
        
        self.message = StringVar()
        self.message_box = Label(self,textvariable=self.message)#,fg="red")
        self.message_box.grid(row=3,columnspan=3)
        
        self.restart_button = Button(self,text="Restart",command=self.on_restart)
        self.new_game_button = Button(self,text="New game",command=self.on_new)
        self.quit_button = Button(self,text="Quit",command=exit)
        self.restart_button.grid(row=4,column=0)
        self.new_game_button.grid(row=4,column=1)
        self.quit_button.grid(row=4,column=2)
        
        self.hard_mode = IntVar()
        self.hard_mode_button = Checkbutton(self,text="Hard mode",variable=self.hard_mode,command=self.on_new)
        self.hard_mode_button.grid(column=1)
        
        # self.grid_columnconfigure(0,weight=5)
        
        self.resizable(False,False)
        # self.geometry(self.geometry())
        
        self.update()
        
    def on_return(self,entry):
        self.on_guess()    
    
    def on_guess(self):
        g = self.guess_entry.get()
        h.guess(g)
        
        if '_' not in h.found:
            game.message.set("You win!")
            
        if len(h.missed) >= Hangman.guess_limit:
            game.message.set("You lose!\nThe word was {}".format(''.join(h.word)))
        
        self.refresh()
        
    def on_restart(self):
        h.restart_game()
        self.message.set("Restarted")
        blank = PhotoImage(file="0.gif")
        self.picture = Label(image=blank)#,height=150,width=100)
        self.picture.image = blank
        self.picture.grid(row=2,columnspan=2)
        self.refresh()

    def on_new(self):
        h.__init__(self.hard_mode.get())
        self.message.set("New game")
        blank = PhotoImage(file="0.gif")        
        self.picture = Label(image=blank)#,height=150,width=100)
        self.picture.image = blank
        self.picture.grid(row=2,columnspan=2)
        self.refresh()
        
    def refresh(self):
        self.found_letters.set(' '.join(h.found))
        self.missed_letters.set(' '.join(h.missed))
        self.guess_entry.set("")
        self.guess_box.focus_set()
        self.guess_box.selection_range(0,END)
        self.update()
                
class Hangman:
    guess_limit = 10
    
    def __init__(self,hard_mode=0):
        if hard_mode == 1:
            file = open('hard.txt')
            words = file.read().split('\n')
            file.close()
        else:
            file = open('words.txt')
            words = file.readline().split(',')
            file.close()
            remove_quotes = lambda s: s[1:-1]
            words = map(remove_quotes,words)

        w = randint(0,len(words)-1)
        
        self.word = list(words[w].upper())
        self.guessed = []
        self.missed = []
        self.found = ['_'] * len(self.word)
    
    def guess(self,g):
        guess = g.upper()
        
        if guess not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            game.message.set("Please guess a letter.")
        elif guess not in self.guessed:
            game.message.set("")
            
            self.guessed.append(guess)

            guess_found = False
            for i, char in enumerate(self.word):
                if char == guess:
                    self.found[i] = char
                    guess_found = True
                
            if not guess_found:
                self.missed.append(guess)
                # self.missed.sort()
                
                n = len(self.missed)
                                
                if n == 1:
                    pic1 = PhotoImage(file="1.gif")
                    game.picture = Label(image=pic1)
                    game.picture.image = pic1
                    game.picture.grid(row=2,columnspan=2)
                if n == 2:
                    pic2 = PhotoImage(file="2.gif")
                    game.picture = Label(image=pic2)
                    game.picture.image = pic2
                    game.picture.grid(row=2,columnspan=2)
                if n == 3:
                    pic3 = PhotoImage(file="3.gif")
                    game.picture = Label(image=pic3)
                    game.picture.image = pic3
                    game.picture.grid(row=2,columnspan=2)
                if n == 4:
                    pic4 = PhotoImage(file="4.gif")
                    game.picture = Label(image=pic4)
                    game.picture.image = pic4
                    game.picture.grid(row=2,columnspan=2)
                if n == 5:
                    pic5 = PhotoImage(file="5.gif")
                    game.picture = Label(image=pic5)
                    game.picture.image = pic5
                    game.picture.grid(row=2,columnspan=2)
                if n == 6:
                    pic6 = PhotoImage(file="6.gif")
                    game.picture = Label(image=pic6)
                    game.picture.image = pic6
                    game.picture.grid(row=2,columnspan=2)
                if n == 7:
                    pic7 = PhotoImage(file="7.gif")
                    game.picture = Label(image=pic7)
                    game.picture.image = pic7
                    game.picture.grid(row=2,columnspan=2)
                if n == 8:
                    pic8 = PhotoImage(file="8.gif")
                    game.picture = Label(image=pic8)
                    game.picture.image = pic8
                    game.picture.grid(row=2,columnspan=2)
                if n == 9:
                    pic9 = PhotoImage(file="9.gif")
                    game.picture = Label(image=pic9)
                    game.picture.image = pic9
                    game.picture.grid(row=2,columnspan=2)
                if n == 10:
                    pic10 = PhotoImage(file="10.gif")
                    game.picture = Label(image=pic10)
                    game.picture.image = pic10
                    game.picture.grid(row=2,columnspan=2)
                
        else:
            game.message.set("You have already guessed {}.".format(guess))
    
    
    def restart_game(self):
        self.guessed = []
        self.missed = []
        self.found = ['_'] * len(self.word)
        
        
if __name__ == "__main__":
    h = Hangman()
    game = Game(None)
    game.title("Hangman")
    game.mainloop()