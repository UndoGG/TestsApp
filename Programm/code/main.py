from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from threading import Thread
from PIL import ImageTk, Image
import os
import tkinter
import keyboard
import time
import json
import tempfile
import ast

#Иницилизация констант
COLOR_GREEN_LIGHT = "#c5deab"
COLOR_GREEN_DARK = "#95c365"
COLOR_GREEN_FOREGROUND = "#467a15"

COLOR_BLUE_LIGHT = "#a7dcfb"
COLOR_BLUE_DARK = "#54bcf8"
COLOR_BLUE_FOREGROUND = "#0882c9"

COLOR_RED_LIGHT = "#ff9494"
COLOR_RED_DARK = "#ff4747"
COLOR_RED_FOREGROUND = "#800000"

COLOR_YELLOW_LIGHT = "#ffe770"
COLOR_YELLOW_DARK = "#f5cc00"
COLOR_YELLOW_FOREGROUND = "#a38800"

COLOR_GOLD_LIGHT = "#e3be02"
COLOR_GOLD_DARK = "#c0a002"
COLOR_GOLD_FOREGROUND = "#a23f02"

COLOR_GRAY_LIGHT = "#c2c2c2"
COLOR_GRAY_DARK = "#c2c2c2"
COLOR_GRAY_FOREGROUND = "#3b3b3b"



#                                   #
# Вычислиение глобальной директории #
#                                   #
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
out = ''
globalPath = dir_path.split('\\')
globalPath[0] = globalPath[0].upper()
del globalPath[-1]
# del globalPath[-1]
globalPath = str(globalPath)
deny = ['\'',' ', ']', '[']
ps = False
for l in globalPath:
    if l == ',':
        ps = True
    if l not in deny:
        out += l
    if l == ' ' and not ps:
        out += l
    if l == ' ' and ps:
        ps = False
globalPath = out
globalPath = globalPath.replace(',','\\')
print(f'Global path is {globalPath}')


#Вычисление данных
try:
    with open(globalPath + '\\data\\user.json', 'r', encoding='utf-8') as file:
        file.read()
        print('User data file find')
except:
    with open(globalPath + '\\assets\\DEFAULT.json', 'r', encoding='utf-8') as file:
        settings = json.loads(file.read())
        print('Setting to default user')
        with open(globalPath + '\\data\\user.json', 'w+', encoding='utf-8') as fl:
            fl.write(str(settings))
            print('Completed')

global USER_SETTINGS
with open(globalPath + '\\data\\user.json', 'r', encoding='utf-8' ) as file:
    USER_SETTINGS = dict(ast.literal_eval(file.read()))


#Очистка временного файла
with open(globalPath + '\data\\Temp.txt', 'w+', encoding='utf-8') as file:
    print('Cleaned temp file')


#         #
# Фнукции #
#         #
def to_json(obj):
     if isinstance(obj, Test):
         result = obj.__dict__
         result["className"] = obj.__class__.__name__
         return result

def raise_above_all(window):
    window.attributes('-topmost', 1)
    #print('Raised window')
    window.attributes('-topmost', 0)


def render_animation(window=None, towindow=None, wait=0.001):
    print(f'Started animation with tine {wait}')
    if window != None:
        window.wm_attributes('-alpha',0.95)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.9)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.8)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.7)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.6)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.5)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.4)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.3)
        time.sleep(wait)
        window.wm_attributes('-alpha',0.2)
        time.sleep(wait)
        window.destroy()
    if towindow != None:
        raise_above_all(towindow)
        towindow.wm_attributes('-alpha',0.1)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.2)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.3)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.4)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.5)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.6)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.7)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.8)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',0.9)
        raise_above_all(towindow)
        time.sleep(wait)
        towindow.wm_attributes('-alpha',1)
        raise_above_all(towindow)
        time.sleep(wait)
        raise_above_all(towindow)
    print(f'Animation finished')

global init_test
global init_testsList
#               #
# Список тестов #
#               #
def init_testsList(main=None, Back=False, backname=None):
    tL = Tk()
    #Располоение окна по центру экрана
    w = tL.winfo_screenwidth()
    h = tL.winfo_screenheight()
    w = w//2
    h = h//2
    w = w - 300
    h = h - 300
    tL.geometry(f'600x600+{w}+{h}')

    tL.title('Тесты')
    tL.state('normal')
    tL.wm_attributes('-alpha',0)
    tL.iconbitmap(globalPath + '\\assets\\appIcon.ico')
    tL.resizable(width=False, height=False)
    if not Back:
        render_animation(main, tL)
    if Back:
        render_animation(backname, tL)
    page = 1
    #Текст
    #"Список тестов"
    Welcome = Label(tL, text=f"Список тестов\n Страница {page}", font = ("Times 20 bold", 30))
    Welcome.place(relx=0.29, rely=0.01)
    #Кнопки
    #"Назад"
    def btn_click_return():
        init_main(tL)


    def r_on_enter(event):
        btn_return['background'] = '#ad1414'

    def r_on_leave(event):
        btn_return['background'] = '#e41b1b'

    btn_return = Button(tL, text="Назад", command=btn_click_return, font='Times 20', background="#e41b1b", foreground='#ffffff')
    btn_return.place(relx=0.5, rely=0.95, anchor="c", width=100, height=40)
    btn_return.bind("<Enter>", r_on_enter)
    btn_return.bind("<Leave>", r_on_leave)

    #Сканирование папки тестов
    def ScanTests(tL):
        content = os.listdir(globalPath + '\\Tests')
        buttons = 0
        next_rely = 0.22
        total_buttons = len(content)

        for f in content:
            next_rely = round(next_rely, 2)
            dir = globalPath + '\\Tests\\' + f
            with open(dir, "r", encoding='utf-8') as fl:
                data = json.loads(fl.read())
                nick = data["NICK"]
                id = data["ID"]
                ID = data["ID"]
                name = data["NAME"]
                description = data["DESCRIPTION"]
                with open(globalPath + '\\data\\user.json', 'r', encoding='utf-8') as file:
                    filedata = USER_SETTINGS
                    completed_list = filedata["Completed"]
                    if ID in completed_list:
                        with open(globalPath + '\data\\Temp.txt', 'r', encoding='utf-8') as file:
                            fileinfo = file.read()
                            with open(globalPath + '\data\\Temp.txt', 'w+', encoding='utf-8') as file:
                                file.writelines([fileinfo, "btn" + str(buttons) + " = Button(tL, bg='" + COLOR_GOLD_LIGHT + "', font = 'Times 15', fg = '"+ COLOR_GOLD_FOREGROUND + "',text='" + name + "', command=lambda:open_test('"+ nick + "','" + name + "'))\n", "btn" + str(buttons) + ".place(relx=0.5, rely=" + str(next_rely) + ", anchor='c', width=400, height=40)\n"])
                                file.seek(0)
                    else:
                        with open(globalPath + '\data\\Temp.txt', 'r', encoding='utf-8') as file:
                            fileinfo = file.read()
                            with open(globalPath + '\data\\Temp.txt', 'w+', encoding='utf-8') as file:
                                file.writelines([fileinfo, "btn" + str(buttons) + " = Button(tL, bg='" + COLOR_BLUE_LIGHT + "', font = 'Times 15', fg = '"+ COLOR_BLUE_FOREGROUND + "',text='" + name + "', command=lambda:open_test('"+ nick + "','" + name + "'))\n", "btn" + str(buttons) + ".place(relx=0.5, rely=" + str(next_rely) + ", anchor='c', width=400, height=40)\n"])
                                file.seek(0)
            next_rely += 0.1
            buttons += 1
        global open_test
        global btn_bind_enter
        global btn_gind_leave

        def open_test(nick, name):
            print(f'Initilizating test "{name}" with nick {nick} ...')
            init_test(name, tL, main, nick)

        with open(globalPath + '\data\\Temp.txt', 'r', encoding='utf-8') as file:
                    file_split = file.read().split('\n')
                    for line in file_split:
                        exec(line)
        print(f'Successfuly loaded {buttons} tests')
    ScanTests(tL)


#                    #
# Иницилизация теста #
#                    #
def init_test(test_name, tL, main, nick):
    #Получение информации о тесте
    NUM = 1

    with open(f'{globalPath}\\Tests\\{nick}.json', 'r', encoding='utf-8') as file:
                    data = json.loads(file.read())
    t = Tk()
    #Располоение окна по центру экрана
    w = tL.winfo_screenwidth()
    h = tL.winfo_screenheight()
    w = w//2
    h = h//2
    w = w - 300
    h = h - 300
    t.geometry(f'600x600+{w}+{h}')

    t.title(f'{test_name}')
    t.state('normal')
    t.wm_attributes('-alpha',0)
    t.iconbitmap(globalPath + '\\assets\\appIcon.ico')
    t.resizable(width=False, height=False)
    #Текст
    #Название теста *
    Welcome = Label(t, text=f"Тест\n{test_name}", font = ("Times 20 bold", 30))
    Welcome.pack(side=TOP, pady=130)
    #Кнопки
    #"Назад"
    def r2_click():
        init_testsList(main, True, t)
    def r2_on_enter(event):
        btn_return['background'] = '#ad1414'
    def r2_on_leave(event):
        btn_return['background'] = '#e41b1b'
    btn_return = Button(t, text="Назад", command=r2_click, font='Times 20', background="#e41b1b", foreground='#ffffff')
    btn_return.place(relx=0.5, rely=0.95, anchor="c", width=100, height=40)
    btn_return.bind("<Enter>", r2_on_enter)
    btn_return.bind("<Leave>", r2_on_leave)


    #"Начать"
    def s_click():

        def init_results(Results, fP):
            render_animation(fP)
            def Page(page, rP=None):
                render_animation(rP)
                rP = Tk()
                #Располоение окна по центру экрана
                w = rP.winfo_screenwidth()
                h = rP.winfo_screenheight()
                w = w//2
                h = h//2
                w = w - 300
                h = h - 300
                rP.geometry(f'600x600+{w}+{h}')

                rP.title(f'{test_name}')
                rP.state('normal')
                rP.wm_attributes('-alpha',0)
                rP.iconbitmap(globalPath + '\\assets\\appIcon.ico')
                rP.resizable(width=False, height=False)
                render_animation(towindow=rP)
                Total = (data["QUESTIONS"])["TOTAL"]
                if page == 1:
                    Question = ((data["QUESTIONS"])["1"])["NAME"]
                    RIGHT = (((data["QUESTIONS"])["1"])["VARIANTS"])["RIGHT"]
                    RIGHTTEXT = (((data["QUESTIONS"])["1"])["VARIANTS"])[str(RIGHT)]
                    Answer = Results[1]
                    AnswerWord = Results["1word"]
                    AnswerNum = Results[str(page) + "num"]

                    Q = Label(rP, text=Question, wraplength=570, font = ("Times 10 bold", 20), justify=CENTER, width=35)
                    Q.place(relx=0.03, rely=0.03)
                    if RIGHT == AnswerNum:
                        Text = Label(rP, text="Вы указали верный вариант:", font = ("Times 10 bold", 25))
                        Text2 = Label(rP, text=RIGHTTEXT, font = ("Times 10 bold", 30))
                        Text.place(relx=0.15, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)
                    if RIGHT != AnswerNum:
                        Text = Label(rP, text="Вы указали не правильный вариант:", font = ("Times 10 bold", 20))
                        Text2 = Label(rP, text=AnswerWord, font = ("Times 10 bold", 30))
                        Text.place(relx=0.12, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)

                    def back_on_enter(event):
                        back['background'] = COLOR_RED_DARK
                    def back_on_leave(event):
                        back['background'] = COLOR_RED_LIGHT
                    back = Button(rP, text="В меню", command=lambda:init_testsList(Back=True, backname=rP), font='Times 20', background=COLOR_RED_LIGHT, foreground=COLOR_RED_FOREGROUND)
                    back.place(relx=0.5, rely=0.9, anchor="c", width=150)
                    back.bind("<Enter>", back_on_enter)
                    back.bind("<Leave>", back_on_leave)

                    def next_on_enter(event):
                        next['background'] = COLOR_GREEN_DARK
                    def next_on_leave(event):
                        next['background'] = COLOR_GREEN_LIGHT
                    next = Button(rP, text="Далее", command=lambda:Page(page + 1, rP), font='Times 20', background=COLOR_GREEN_LIGHT, foreground=COLOR_GREEN_FOREGROUND)
                    next.place(relx=0.65, rely=0.8, anchor="c", width=150)
                    next.bind("<Enter>", next_on_enter)
                    next.bind("<Leave>", next_on_leave)

                    def previous_on_enter(event):
                        previous['background'] = COLOR_GRAY_DARK
                    def previous_on_leave(event):
                        previous['background'] = COLOR_GRAY_LIGHT
                    previous = Button(rP, text="Назад",state=["disabled"], font='Times 20', background=COLOR_GRAY_LIGHT, foreground=COLOR_GRAY_FOREGROUND)
                    previous.place(relx=0.35, rely=0.8, anchor="c", width=150)
                    previous.bind("<Enter>", previous_on_enter)
                    previous.bind("<Leave>", previous_on_leave)

                elif page < Total:
                    print(f'Opened page number {page}')
                    Question = ((data["QUESTIONS"])[str(page)])["NAME"]
                    RIGHT = (((data["QUESTIONS"])[str(page)])["VARIANTS"])["RIGHT"]
                    RIGHTTEXT = (((data["QUESTIONS"])[str(page)])["VARIANTS"])[str(RIGHT)]
                    Answer = Results[page]
                    AnswerWord = Results[str(page) + "word"]
                    AnswerNum = Results[str(page) + "num"]
                    print(f'Correct answer is {RIGHT} but selected is {Answer}')

                    Q = Label(rP, text=Question, wraplength=570, font = ("Times 10 bold", 20), justify=CENTER, width=35)
                    Q.place(relx=0.03, rely=0.03)
                    if RIGHT == AnswerNum:
                        Text = Label(rP, text="Вы указали верный вариант:", font = ("Times 10 bold", 25))
                        Text2 = Label(rP, text=RIGHTTEXT, font = ("Times 10 bold", 30))
                        Text.place(relx=0.15, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)
                    if RIGHT != AnswerNum:
                        Text = Label(rP, text="Вы указали не правильный вариант:", font = ("Times 10 bold", 20))
                        Text2 = Label(rP, text=AnswerWord, font = ("Times 10 bold", 30))
                        Text.place(relx=0.12, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)

                    def back_on_enter(event):
                        back['background'] = COLOR_RED_DARK
                    def back_on_leave(event):
                        back['background'] = COLOR_RED_LIGHT
                    back = Button(rP, text="В меню", command=lambda:init_testsList(Back=True, backname=rP), font='Times 20', background=COLOR_RED_LIGHT, foreground=COLOR_RED_FOREGROUND)
                    back.place(relx=0.5, rely=0.9, anchor="c", width=150)
                    back.bind("<Enter>", back_on_enter)
                    back.bind("<Leave>", back_on_leave)

                    def next_on_enter(event):
                        next['background'] = COLOR_GREEN_DARK
                    def next_on_leave(event):
                        next['background'] = COLOR_GREEN_LIGHT
                    next = Button(rP, text="Далее", command=lambda:Page(page + 1, rP), font='Times 20', background=COLOR_GREEN_LIGHT, foreground=COLOR_GREEN_FOREGROUND)
                    next.place(relx=0.65, rely=0.8, anchor="c", width=150)
                    next.bind("<Enter>", next_on_enter)
                    next.bind("<Leave>", next_on_leave)

                    def previous_on_enter(event):
                        previous['background'] = COLOR_BLUE_DARK
                    def previous_on_leave(event):
                        previous['background'] = COLOR_BLUE_LIGHT
                    previous = Button(rP, text="Назад", command=lambda:Page(page - 1, rP), font='Times 20', background=COLOR_BLUE_LIGHT, foreground=COLOR_BLUE_FOREGROUND)
                    previous.place(relx=0.35, rely=0.8, anchor="c", width=150)
                    previous.bind("<Enter>", previous_on_enter)
                    previous.bind("<Leave>", previous_on_leave)

                elif page >= Total:
                    print('Opened last page')
                    Question = ((data["QUESTIONS"])[str(page)])["NAME"]
                    RIGHT = (((data["QUESTIONS"])[str(page)])["VARIANTS"])["RIGHT"]
                    RIGHTTEXT = (((data["QUESTIONS"])[str(page)])["VARIANTS"])[str(RIGHT)]
                    Answer = Results[page]
                    AnswerWord = Results[str(page) + "word"]
                    AnswerNum = Results[str(page) + "num"]

                    Q = Label(rP, text=Question, wraplength=570, font = ("Times 10 bold", 20), justify=CENTER, width=35)
                    Q.place(relx=0.03, rely=0.03)
                    if RIGHT == AnswerNum:
                        Text = Label(rP, text="Вы указали верный вариант:", font = ("Times 10 bold", 25))
                        Text2 = Label(rP, text=RIGHTTEXT, font = ("Times 10 bold", 30))
                        Text.place(relx=0.15, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)
                    if RIGHT != AnswerNum:
                        Text = Label(rP, text="Вы указали не правильный вариант:", font = ("Times 10 bold", 20))
                        Text2 = Label(rP, text=AnswerWord, font = ("Times 10 bold", 30))
                        Text.place(relx=0.12, rely=0.3)
                        Text2.place(anchor='center', rely=0.55, relx=0.5)

                    def back_on_enter(event):
                        back['background'] = COLOR_RED_DARK
                    def back_on_leave(event):
                        back['background'] = COLOR_RED_LIGHT
                    back = Button(rP, text="В меню", command=lambda:init_testsList(Back=True, backname=rP), font='Times 20', background=COLOR_RED_LIGHT, foreground=COLOR_RED_FOREGROUND)
                    back.place(relx=0.5, rely=0.9, anchor="c", width=150)
                    back.bind("<Enter>", back_on_enter)
                    back.bind("<Leave>", back_on_leave)

                    def next_on_enter(event):
                        next['background'] = COLOR_GRAY_DARK
                    def next_on_leave(event):
                        next['background'] = COLOR_GRAY_LIGHT
                    next = Button(rP, text="Далее", state=["disabled"], font='Times 20', background=COLOR_GRAY_LIGHT, foreground=COLOR_GRAY_FOREGROUND)
                    next.place(relx=0.65, rely=0.8, anchor="c", width=150)
                    next.bind("<Enter>", next_on_enter)
                    next.bind("<Leave>", next_on_leave)


                    def previous_on_enter(event):
                        previous['background'] = COLOR_BLUE_DARK
                    def previous_on_leave(event):
                        previous['background'] = COLOR_BLUE_LIGHT
                    previous = Button(rP, text="Назад", command=lambda:Page(page - 1, rP), font='Times 20', background=COLOR_BLUE_LIGHT, foreground=COLOR_BLUE_FOREGROUND)
                    previous.place(relx=0.35, rely=0.8, anchor="c", width=150)
                    previous.bind("<Enter>", previous_on_enter)
                    previous.bind("<Leave>", previous_on_leave)

                else:
                    messagebox.showerror('Ошибка','Unknown error')
            Page(1)


        def FinishedTest(Right, Total, Time, Answers, ID):
            fP = Tk()
            #Располоение окна по центру экрана
            w = fP.winfo_screenwidth()
            h = fP.winfo_screenheight()
            w = w//2
            h = h//2
            w = w - 300
            h = h - 300
            fP.geometry(f'600x600+{w}+{h}')

            fP.title(f'{test_name}')
            fP.state('normal')
            fP.wm_attributes('-alpha',0)
            fP.iconbitmap(globalPath + '\\assets\\appIcon.ico')
            fP.resizable(width=False, height=False)
            render_animation(towindow=fP)

            #Текст - информация
            Text = Label(fP, text="Поздравляем!\nТест завершён", font = ("Times 10 bold", 35))
            Text2 = Label(fP, text=f'     Правильных ответов', font = ("Times 10 bold", 30))
            Text21 = Label(fP, text=f'{Right} из {Total}', font = ("Times 10 bold", 40))
            Text3 = Label(fP, text=f'        Время решения', font = ("Times 10 bold", 30))
            Text31 = Label(fP, text=f'{Time} Минут', font = ("Times 10 bold", 40))
            Text.place(relx=0.22, rely=0.1)
            Text2.place(relx=0.09, rely=0.35)
            Text21.place(relx=0.37, rely=0.42)
            Text3.place(relx=0.112, rely=0.55)
            Text31.place(relx=0.3, rely=0.65)
            with open(globalPath + '\\data\\user.json', 'r', encoding='utf-8') as file:
                filedata = USER_SETTINGS
                completed_list = filedata["Completed"]
                if ID not in completed_list:
                    completed_list.append(str(ID))
                    filedata["Completed"] = completed_list
                    with open(globalPath + '\\data\\user.json', 'w+', encoding='utf-8') as file:
                        file.write(str(filedata))

            #Кнопки
            #Назад
            #Ответы
            def back_on_enter(event):
                back['background'] = COLOR_RED_DARK
            def back_on_leave(event):
                back['background'] = COLOR_RED_LIGHT
            back = Button(fP, text="Назад", command=lambda:init_testsList(Back=True, backname=fP), font='Times 20', background=COLOR_RED_LIGHT, foreground=COLOR_RED_FOREGROUND)
            back.place(relx=0.35, rely=0.9, anchor="c", width=150)
            back.bind("<Enter>", back_on_enter)
            back.bind("<Leave>", back_on_leave)

            def results_on_enter(event):
                results['background'] = COLOR_YELLOW_DARK
            def results_on_leave(event):
                results['background'] = COLOR_YELLOW_LIGHT
            results = Button(fP, text="Ответы", command=lambda:init_results(Answers, fP), font='Times 20', background=COLOR_YELLOW_LIGHT, foreground=COLOR_YELLOW_FOREGROUND)
            results.place(relx=0.65, rely=0.9, anchor="c", width=150)
            results.bind("<Enter>", results_on_enter)
            results.bind("<Leave>", results_on_leave)



        NUM = 1
        RIGHT_ANSWERS = 0
        ANSWERS = {}
        render_animation(t)
        def initPage(NUM, RIGHT_ANSWERS):
            #                 #
            # ИНТЕРФЕЙС ТЕСТА #
            #                 #
            print('Initilizating test interface')
            print('Timer started')
            time_started = time.time()
            tP = Tk()
            Question = ((data["QUESTIONS"])[str(NUM)])["NAME"]
            Total = (data["QUESTIONS"])["TOTAL"]
            RIGHT = (((data["QUESTIONS"])[str(NUM)])["VARIANTS"])["RIGHT"]

            Q = Label(tP, text=Question, wraplength=570, font = ("Times 20 bold", 20), justify=CENTER, width=35)
            Q.place(relx=0.03, rely=0.05)

            def send_var(var, NUM, RIGHT_ANSWERS):
                print(f'Sent var {var}')
                if int(var) == RIGHT:
                    print('This is right answer!')
                    RIGHT_ANSWERS += 1
                    ANSWERS[NUM] = True
                    War = str(NUM) + 'word'
                    War2 = str(NUM) + 'num'
                    ANSWERS[War2] = var
                    ANSWERS[War] = ((((data["QUESTIONS"])[str(NUM)])["VARIANTS"])[str(var)])
                    NUM += 1
                if int(var) != RIGHT:
                    print('This is incorrect answer!')
                    ANSWERS[NUM] = False
                    War = str(NUM) + 'word'
                    War2 = str(NUM) + 'num'
                    ANSWERS[War2] = var
                    ANSWERS[War] = ((((data["QUESTIONS"])[str(NUM)])["VARIANTS"])[str(var)])
                    NUM += 1
                if NUM <= Total:
                    render_animation(tP)
                    initPage(NUM, RIGHT_ANSWERS)
                if NUM > Total:
                    render_animation(tP)
                    print(f'Test finished with {RIGHT_ANSWERS} of {Total} right answers')
                    time_finish = time.time()
                    time_total = round(round(int(time_finish) - int(time_started))/60, 2)
                    ID = data["ID"]
                    FinishedTest(RIGHT_ANSWERS, Total, time_total, ANSWERS, ID)

            def var_on_enter(event):
                var_1['background'] = COLOR_GREEN_DARK
            def var_on_leave(event):
                var_1['background'] = COLOR_GREEN_LIGHT
            var_1 = Button(tP, text=(((data["QUESTIONS"])[str(NUM)])["VARIANTS"])["1"], command=lambda:send_var(1, NUM, RIGHT_ANSWERS), font='Times 20', background=COLOR_GREEN_LIGHT, foreground=COLOR_GREEN_FOREGROUND)
            var_1.place(relx=0.25, rely=0.8, anchor="c", width=300, height=200)
            var_1.bind("<Enter>", var_on_enter)
            var_1.bind("<Leave>", var_on_leave)

            def var2_on_enter(event):
                var_2['background'] = COLOR_BLUE_DARK
            def var2_on_leave(event):
                var_2['background'] = COLOR_BLUE_LIGHT
            var_2 = Button(tP, text=(((data["QUESTIONS"])[str(NUM)])["VARIANTS"])["2"], command=lambda:send_var(2, NUM, RIGHT_ANSWERS), font='Times 20', background=COLOR_BLUE_LIGHT, foreground=COLOR_BLUE_FOREGROUND)
            var_2.place(relx=0.75, rely=0.8, anchor="c", width=300, height=200)
            var_2.bind("<Enter>", var2_on_enter)
            var_2.bind("<Leave>", var2_on_leave)

            def var3_on_enter(event):
                var_3['background'] = COLOR_RED_DARK
            def var3_on_leave(event):
                var_3['background'] = COLOR_RED_LIGHT
            var_3 = Button(tP, text=(((data["QUESTIONS"])[str(NUM)])["VARIANTS"])["3"], command=lambda:send_var(3, NUM, RIGHT_ANSWERS), font='Times 20', background=COLOR_RED_LIGHT, foreground=COLOR_RED_FOREGROUND)
            var_3.place(relx=0.75, rely=0.47, anchor="c", width=300, height=200)
            var_3.bind("<Enter>", var3_on_enter)
            var_3.bind("<Leave>", var3_on_leave)

            def var4_on_enter(event):
                var_4['background'] = COLOR_YELLOW_DARK
            def var4_on_leave(event):
                var_4['background'] = COLOR_YELLOW_LIGHT
            var_4 = Button(tP, text=(((data["QUESTIONS"])[str(NUM)])["VARIANTS"])["4"], command=lambda:send_var(4, NUM, RIGHT_ANSWERS), font='Times 20', background=COLOR_YELLOW_LIGHT, foreground=COLOR_YELLOW_FOREGROUND)
            var_4.place(relx=0.25, rely=0.47, anchor="c", width=300, height=200)
            var_4.bind("<Enter>", var4_on_enter)
            var_4.bind("<Leave>", var4_on_leave)

            #Располоение окна по центру экрана
            w = tP.winfo_screenwidth()
            h = tP.winfo_screenheight()
            w = w//2
            h = h//2
            w = w - 300
            h = h - 300
            tP.geometry(f'600x600+{w}+{h}')
            tP.title(f'{test_name}')
            tP.state('normal')
            tP.wm_attributes('-alpha',0)
            tP.iconbitmap(globalPath + '\\assets\\appIcon.ico')
            tP.resizable(width=False, height=False)
            render_animation(towindow=tP)
        initPage(NUM, RIGHT_ANSWERS)


    def s_on_enter(event):
        btn_start['background'] = '#95c365'
    def s_on_leave(event):
        btn_start['background'] = '#c5deab'
    btn_start = Button(t, text="Начать", command=s_click, font='Times 20', background="#c5deab", foreground='#467a15')
    btn_start.place(relx=0.5, rely=0.43, anchor="c", width=100, height=40)
    btn_start.bind("<Enter>", s_on_enter)
    btn_start.bind("<Leave>", s_on_leave)
    render_animation(tL, t)
    print(f'Initilizated test {test_name} successfuly')





def init_main(tL=None):
    #              #
    # Главное меню #
    #              #

    main = Tk()
    raise_above_all(main)
    #Располоение окна по центру экрана
    w = main.winfo_screenwidth()
    h = main.winfo_screenheight()
    w = w//2
    h = h//2
    w = w - 300
    h = h - 300
    main.geometry(f'600x600+{w}+{h}')
    main.wm_attributes('-alpha',0)
    main.title('Тесты')
    main.iconbitmap(globalPath + '\\assets\\appIcon.ico')
    main.state('normal')
    main.resizable(width=False, height=False)
    raise_above_all(main)
    if tL != None:
        render_animation(window=tL, towindow=main)
        raise_above_all(main)
    if tL == None:
        render_animation(towindow=main)
        raise_above_all(main)

    #Стили
    danger = ttk.Style()
    danger.configure("Danger.TLabel", background="#e41b1b", font='Times 15 bold', foreground= '#ffffff')

    dangerDark = ttk.Style()
    dangerDark.configure("DangerDark.TLabel", background="#ad1414", font='Times 15 bold', foreground= '#ffffff')

    DefaultText = ttk.Style()
    DefaultText.configure("DefaultText.TLabel", font='Times 20', background="#c5deab", foreground='#467a15')

    DefaultTextDark = ttk.Style()
    DefaultTextDark.configure("DefaultTextDark.TLabel", font='Times 20', background="#95c365", foreground='#467a15')

    #Текст
    #"Главное меню"
    Welcome = Label(main, text="Главное меню", font = ("Times 20 bold", 30))
    Welcome.place(relx=0.29, rely=0.25)

    #Кнопки
    #Список тестов
    def i_on_enter(event):
        btn_info['style'] = 'DefaultTextDark.TLabel'

    def i_on_leave(event):
        btn_info['style'] = 'DefaultText.TLabel'

    def btn_click_info():
        init_testsList(main)

    btn_info = ttk.Button(text="                    Список тестов", command=btn_click_info, style='DefaultText.TLabel')
    btn_info.place(relx=0.5, rely=0.4, anchor="c", width=450, height=40)
    btn_info.bind("<Enter>", i_on_enter)
    btn_info.bind("<Leave>", i_on_leave)

    #Выход
    def btn_click_exit():
        render_animation(main)
        time.sleep(1)
        exit()

    def e_on_enter(event):
        btn_exit['style'] = 'DangerDark.TLabel'

    def e_on_leave(event):
        btn_exit['style'] = 'Danger.TLabel'

    btn_exit = ttk.Button(text="   Выйти", command=btn_click_exit, style="Danger.TLabel")
    btn_exit.place(relx=0.5, rely=0.95, anchor="c", width=100, height=40)
    btn_exit.bind("<Enter>", e_on_enter)
    btn_exit.bind("<Leave>", e_on_leave)


    main.mainloop()
init_main()
