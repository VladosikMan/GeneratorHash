from tkinter import *
from tkinter.ttk import Combobox
import hasher
import time
import generator
import threading


    

#------------------GUI----------------------
def place(elem, x, y):
    elem.place(relx=x,rely=y)
def CreateWindow():   
    window = Tk()
    #---------------func---------------------------
    def check(x, ans, data):
        #получить значение проверяемого
        trust = ""
        if x == 1 :
            trust  = hasher.call_sha1(data)
        if x == 2 :
            trust  = hasher.call_sha224(data)
        
        if x == 3 :
            trust  = hasher.call_sha256(data)
        
        if x == 4 :
            trust  = hasher.call_sha384(data)
        
        if x == 5 :
            trust  = hasher.call_sha512(data)
        
        if x == 6 :
            trust  = hasher.call_md5(data)
        
        if x == 7 :
            trust  = hasher.call_whirlpool(data)
        
        if x == 8 :
            trust  = hasher.call_ripemd160(data)
        
        if x == 9 :
            trust  = hasher.call_adler32(data)

        if x == 10 :
            trust  = hasher.call_crc32(data)
        
        txt_trust.delete(1.0,"")
        txt_trust.insert("end", trust)
        if trust == ans:
            return True
        else:
            return False

    
    def gener_var():
        #генерация вариантов
        que = en_que_var.get()
        try:
            x = int (que)
            if x >100 or x<1:
                raise Exception
            generator.gener_variants(x)
            label_gener_func.config(text='Сгенерировано')
        except ValueError:
            label_gener_func.config(text='Ошибка ввода')
        except Exception:
            label_gener_func.config(text='Ошибка ввода')

            
    def check_ans():
        #проверка варинтов
        x = combo_hash.current()
        flag = check(x+1, txt_ans.get("1.0","end-1c"), en_data.get())
        if flag == True:
            label_check_func.config(text='Правильно')
        else:
            label_check_func.config(text='Не правильно')
    


    #---------------init elements-----------
    #string_Gen = StringVar()
    #string_Gen.set("What should I learn")
        
    label_gener = Label(text="Сгенерировать варианты")
    place(label_gener, 0.05, 0.01)
    
    label_que_var = Label(text="Количество вариантов (1-100)")
    place(label_que_var, 0.05, 0.07)

    en_que_var = Entry(window,width=10)
    place(en_que_var,  0.45, 0.072)
    
    
    label_gener_func = Label(text="Функ строка")
    place(label_gener_func, 0.05, 0.15)


    btn_gen_var= Button(window, text="Сгенерировать", command = gener_var)
    place(btn_gen_var, 0.4, 0.15)



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
                                    "adler32 ",
                                    "crc32b"])
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


    window.event_add('<<Paste>>', '<Control-igrave>')
    window.event_add("<<Copy>>", "<Control-ntilde>")
    
    window.resizable(width=False, height=False)
    window.title("GenerHash")
    window.geometry('450x520')
 
    window.mainloop()

print(hasher.call_crc32("Genius is one percent inspiration and ninety-nine percent perspiration"))
my_thread = threading.Thread(target=generator.init_data)
my_thread.start()

#print(hasher.call_crc32('her'))
CreateWindow()



