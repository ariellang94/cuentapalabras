from time import sleep
from tkinter import*

ventana = Tk()
ventana.geometry("500x300+100+100")
ventana.title("Practica De Tipeo")

hor = StringVar()
min = StringVar()
seg = StringVar()


lblHora = Label(text = "Horas:", font = ("Arial",14)).place(x = 10, y = 10)
txtHora = Entry(ventana, textvariable = hor).place(x = 100, y = 10)
txtHora = int(input("hora"))

lblMinuto = Label(text = "Minutos:", font = ("Arial",14)).place(x = 10, y = 40)
txtMinuto = Entry(ventana, textvariable = min).place(x = 100, y = 40)

lblSegundo = Label(text = "Segundos:", font = ("Arial",14)).place(x = 10, y = 70)
txtSegundo = Entry(ventana, textvariable = seg).place(x = 100, y = 70)


txtMinuto = int(input("minuto"))
txtSegundo = int(input("segundo"))

while hor.get() >= 0:
    while min.get() >= 0:
        while seg.get() >= 0:
            tiempo = 'Tiempo restante {}:{}:{}'.format(hor.get(),min.get(),seg.get())
            print(tiempo)
            seg.set(seg.get() -= 1)
            sleep(1)
        min.set(min.get() -= 1)
        seg.set(59)
    hor.set(hor.get() -= 1)
    min.set(59)

print("Fin Del Tiempo")

ventana.mainloop()
