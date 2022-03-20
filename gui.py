from tkinter import *
#------------------GUI----------------------
def place(elem, x, y):
    elem.place(relx=x,rely=y)
def CreateWindow():   
    window = Tk()
    #---------------func---------------------------
    def gener_var():
        print()
    
    #---------------init elements-----------
    #string_Gen = StringVar()
    #string_Gen.set("What should I learn")
        
    label_gener = Label(text="Сгенерировать варианты")
    place(label_gener, 0.1, 0.05)
    
    label_que_var = Label(text="Количество вариантов")
    
    place(label_que_var, 0.1, 0.1)
    
    label_gener_func = Label(text="Функ строка")
    place(label_gener_func, 0.1, 0.2)


    
    
    en_que_var = Entry(window,width=15)
    place(en_que_var,  0.3,0.1)

    btn_gen_var= Button(window, text="Сгенерировать", command = gener_var)
    place(btn_gen_var, 0.3, 0.2)




    window.resizable(width=False, height=False)
    window.title("GenerHash")
    window.geometry('800x600')
 

    window.mainloop()


CreateWindow()
