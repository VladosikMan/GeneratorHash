from tkinter import *
from tkinter.ttk import Combobox
import hasher

#------------------GUI----------------------
def place(elem, x, y):
    elem.place(relx=x,rely=y)
def CreateWindow():   
    window = Tk()
    #---------------func---------------------------
    def gener_var():
        print()

    def check_ans():
        print()
    
    #---------------init elements-----------
    #string_Gen = StringVar()
    #string_Gen.set("What should I learn")
        
    label_gener = Label(text="Сгенерировать варианты")
    place(label_gener, 0.05, 0.01)
    
    label_que_var = Label(text="Количество вариантов")
    place(label_que_var, 0.05, 0.07)

    en_que_var = Entry(window,width=10)
    place(en_que_var,  0.4, 0.072)
    
    
    label_gener_func = Label(text="Функ строка")
    place(label_gener_func, 0.05, 0.15)

    btn_gen_var= Button(window, text="Сгенерировать", command = gener_var)
    place(btn_gen_var, 0.35, 0.15)



    label_check = Label(text="Проверить задание")
    place(label_check, 0.2, 0.27)



    label_choice_hash = Label(text="Выбрать хэш \n функцию")
    place(label_choice_hash, 0.05, 0.37)

    

    combo_hash = Combobox(window, 
                            values=[
                                    "SHA1", 
                                    "SHA224",
                                    "SHA256",
                                    "SHA384",
                                    "SHA512",
                                    "md5",
                                    "Whirlpool",
                                    "ripemd160",
                                    "Whirlpool",
                                    "adler32 ",
                                    "crc32"])
    place(combo_hash, 0.3, 0.37)
    combo_hash.current(0)



    label_data = Label(text="Вставьте хэшируемые данные:")
    place(label_data, 0.05, 0.47)


    en_data = Entry(window,width=65)
    place(en_data,  0.05,0.54)
    

    label_ans = Label(text="Ваш ответ:")
    place(label_ans, 0.05, 0.6)

    label_trust = Label(text="Итоговое значение")
    place(label_trust, 0.52, 0.6)

    

    txt_ans = Text(window, height = 5, width = 24)
    place(txt_ans,  0.05,0.65)

    txt_trust = Text(window, height = 5, width = 24)
    place(txt_trust,  0.52,0.65)


    btn_check_ans= Button(window, text="Проверить", command = check_ans)
    place(btn_check_ans, 0.05, 0.85)

    label_check_func = Label(text="Функ строка")
    place(label_check_func, 0.05, 0.91)
    


    window.resizable(width=False, height=False)
    window.title("GenerHash")
    window.geometry('450x520')
 

    window.mainloop()


print(hasher.call_md5('секиро'))
CreateWindow()


