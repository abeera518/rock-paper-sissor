from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('ROCK PAPER SCISSORS')
root.geometry('500x500')
root.configure(bg='lightblue')
rock_img = ImageTk.PhotoImage(Image.open('rock.png'))