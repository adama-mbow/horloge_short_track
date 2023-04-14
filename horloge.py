from tkinter import *
import time
import datetime
import winsound
#import playsound

montre = Tk()
# titre de l'interface
montre.title("horloge")
#background color
montre.config(bg="black")
# la taille de l'interface
montre.geometry("1000x900+0+0")

#créer une fonction qui permet de recuperer l'heure en temps réel et l'afficher tous les x ms    

"""def alarm(reveille):
    while True:
        time.sleep(1)
        temp_actuel = datetime.datetime.now()
        now = temp_actuel.strftime("%H:%M:%S")
        date = temp_actuel.strftime("%d/%m/%Y")
        #print("The Set Date is:",date)
        print(now)
        if now == reveille:
            print("levez vous")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    reveille = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(reveille)



setYourAlarm = Label(montre,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)"""

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
"""hourTime= Entry(montre,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(montre,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(montre,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)"""



hour = StringVar()
min = StringVar()
sec = StringVar()

def recupererheure(): 
    # on recupère les heures, minutes et secondes sous forme de chaines de caractère
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    #on recupère les labele heure minute et seconde
    lab_heure.config(text=h)
    lab_minute.config(text=m)
    lab_seconde.config(text=s)
    # maintient l'execution de la fonction recupereheure tous les 1000ms
    lab_heure.after(1000, recupererheure)

# définir les label heures minutes et secondes
#heure
lab_heure = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_heure.place(x=400, y=300, width=200, height=130)
heure = Label(montre, text="heures", font =("time new roman", 20,"bold"), bg="#FFFFFF")
heure.place(x=400, y=450, width=200, height=30)
#minute
lab_minute = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_minute.place(x=650, y=300, width=200, height=130)
minute = Label(montre, text="minutes", font =("time new roman", 20,"bold"), bg="#FFFFFF")
minute.place(x=650, y=450, width=200, height=30)
#seconde
lab_seconde = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_seconde.place(x=900, y=300, width=200, height=130)
seconde = Label(montre, text="secondes", font =("time new roman", 20,"bold"), bg="#FFFFFF")
seconde.place(x=900, y=450, width=200, height=30)
recupererheure()




# creer une alarme 

"""hourTime= Entry(montre,textvariable = heure,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(montre,textvariable = minute,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(montre,textvariable = seconde,bg = "pink",width = 15).place(x=200,y=30)
addTime = Label(montre,text = "Hour  Min   Sec",font=60).place(x = 110,)
reveil = Button(montre, text="Alarme", command= actual_time)
reveil.place(x=100, y=70, width=50, height=30,)  """


montre.mainloop()
