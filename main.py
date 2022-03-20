from tkinter import *
import gui
#------------------GUI----------------------
def CreateWindow():
    def work():
        print('gui')
        s = gui.her(1)
        my_string_var.set(s)
        print('hui')

        
    window = Tk()

    my_string_var = StringVar()
    my_string_var.set("What should I learn")
    label1 = Label(text="Hello Python", fg="#eee", bg="#333", textvariable = my_string_var)
    label1.place(relx=0.5,rely=0.1)





    
    window.title("KnowEver")
    window.geometry('800x600')
    buttonAdd = Button(window, text="Добавить строку",command = work)
    buttonAdd.place(relx=0.85, rely=0.7)

    window.mainloop()


CreateWindow()
