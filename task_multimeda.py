from tkinter import *
import webbrowser

root = Tk()
root.geometry('500x400')
root.title('home')

def fun():
 webbrowser.open ('https://www.youtube.com/watch?v=WVO2Dx10d7E')

btn = Button(root, command=fun, text='click me', width=12, height=3,fg='white', bg='black', font='25')
btn.pack(pady=20)

root.mainloop()
#  احمد مصطفي علي محمد 
# سكشن 3 