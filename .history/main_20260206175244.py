from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('ROCK PAPER SCISSORS')
root.geometry('500x500')
root.configure(bg='lightblue')
rock_img = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper.png')) 
scissors_img = ImageTk.PhotoImage(Image.open('scissors.png'))
rock_button = Button(root, image=rock_img, command=lambda: play('rock'))
