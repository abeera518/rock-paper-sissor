from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('ROCK PAPER SCISSORS')
root.geometry('400x400')
root.configure(bg='lightblue')
rock_img = ImageTk.PhotoImage(Image.open('rock.jpg').resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open('paper.jpg') .resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open('scissor.jpg').resize((100, 100)))

def play(user_choice):
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        messagebox.showinfo('Result', "It's a tie!")

    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        messagebox.showinfo('Result', 'You win!')

    else:
        messagebox.showinfo('Result', 'Computer wins!')
rock_button = Button(root, image=rock_img, command=lambda: play('rock'))
paper_button = Button(root, image=paper_img, command=lambda: play('paper'))
scissors_button = Button(root, image=scissors_img, command=lambda: play('scissor'))

rock_button.pack(side=LEFT, padx=10)
paper_button.pack(side=TOP, padx=10)
scissors_button.pack(side=RIGHT, padx=10)

root.mainloop()
