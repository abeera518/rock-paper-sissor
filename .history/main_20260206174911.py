from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('ROCK PAPER SCISSORS')
root.geometry('500x500')
root.configure(bg='lightblue')
rock_img = ImageTk.PhotoImage(Image.open('.png'))
paper_img = ImageTk.PhotoImage(Image.open('ROCK.png'))
scissors_img = ImageTk.PhotoImage(Image.open('scissors.png'))
rock_button = Button(root, image=rock_img, command=lambda: play('rock'))
paper_button = Button(root, image=paper_img, command=lambda: play('paper'))
scissors_button = Button(root, image=scissors_img, command=lambda: play('scissors'))
rock_button.pack(side=LEFT, padx=10)    
paper_button.pack(side=LEFT, padx=10)
scissors_button.pack(side=LEFT, padx=10)
def play(user_choice):
    import random
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        messagebox.showinfo('Result', f'It\'s a tie! Both chose {user_choice}.')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        messagebox.showinfo('Result', f'You win! {user_choice} beats {computer_choice}.')
    else:
        messagebox.showinfo('Result', f'You lose! {computer_choice} beats {user_choice}.')
root.mainloop()
