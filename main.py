from datetime import datetime
from playsound import playsound 
from tkinter import *
alarm = Tk()

def update_time(): #функция которая показывает текущее время с точностью до секунд
    current_time.config(text=f"{datetime.now():%H:%M:%S}")
    alarm.after(100, update_time)

def alarm_clock(): #реализация звона будильника
    alarm_time = time.get() #фиксируем время, которое ввел пользователь
    l1.config(text=f'Начну мяукать в {alarm_time}! А пока отдыхай.')
    # alarm.update() это возможно и не нужно 
    time.delete(0, END)
    while True:  #лучше вынести этот цикл в отдельный метод
        now = datetime.now().time() #время с точноть до милисекунд
        alarm.update()  #обновляется текущее время во время ожидания звонка       
        if str(now)[:8] == alarm_time: #время с точностью до секунд равно введенному времени
            l1.config(text='МЯУМЯУМЯУ!!!')
            alarm.update() #обновление слов кота, мяумяумяу появляется сразу во время звонка, а не после
            return play_ring() #возврат функции нужен для завершения цикла

            
def play_ring(): 
    print('meow')
    playsound('C:/Users/Valery/Desktop/Alarm/myiu.mp3')

current_time = Label(alarm, font=("helvetica", 15))
current_time.pack()

alarm.title('Будильник')
alarm.geometry('900x650')

kit1 = Canvas(alarm, height=450, width=700)
img = PhotoImage(file='pngwing.com.png')
image = kit1.create_image(0, 0, anchor=NW, image=img)
kit1.pack()

l1 = Label(alarm,text='Привет, я - твой котик-будильник!\nНачну мяукать,\
 только когда тебе удобно.\nЗадай время будильника в формате HH:MM:SS',
            font = ('Comic Sans MS', 20))
l1.pack()

fr = Frame(width=30, height=2) #рамка нужна т.к. она находится в центре, а внутри нее поле ввода и кнопка
fr.pack(anchor=CENTER)

time = Entry(fr,width=10, justify=CENTER, font=('Comic Sans MS', 20, 'bold'))
time.pack(ipadx=50, side=LEFT)

bt = Button(fr,text='Сохранить', command = lambda: alarm_clock(), font=('Comic Sans MS', 20))
bt.pack(side=LEFT)

update_time()
alarm.mainloop()

#---------------ДЛЯ ОПТИМИЗАЦИИ КОДА, ВАЛИДАЦИЯ ДАТЫ--------------------------
# def validate_time(alarm_time):
#      if len(alarm_time) != 8:
#          return 'Неверный формат времени'
#      else:
#          if int(alarm_time[0:2]) > 23:
#              return 'Неверный формат часа'
#          elif int(alarm_time[3:5]) > 59:
#              return 'Неверный формат минут'
#          elif int(alarm_time[6:]) > 59:
#              return 'Неверный формат секунд'
#          else:
#             return 'ok'
# # alarm_clock()
# print(datetime.now().time() == time.get())
# print(type(datetime.now().time()))
# print(str(datetime.now().time())[:8])
# print(type(time.get()))
# print(time.get())

        # if current_minute == alarm_minute:
        #     if current_sec == alarm_sec:

            # current_hour = now.hour
    # current_minute = now.minute
    # current_sec = now.second