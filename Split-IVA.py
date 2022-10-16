import os
from tkinter import *
import sys
from turtle import color
sys.path.append(os.path.abspath("/Users/italovargas/Library/CloudStorage/GoogleDrive-vargasserrano.asociados@gmail.com/My Drive/1-Contabilidad/2-SGC/PYTHON"))
from DatosClientes import *





root=Tk()

frame=Frame(root)#,bg="black")

frame.pack(fill="both",expand="True")

root.title("VARGAS SERRANO & ASOCIADOS - Split IVA - V:1.1")
root.geometry('400x300+300+100')
root.config(bg="green")
#root.resizable(False,True)





#frame.config(width="300", height="200")

Ins=Label(frame,text="Total Factura").pack()


Tot=Entry(frame,text="Total")
Tot.pack()#,textvariable=NOMBRE)



Ins=Label(frame,text="Total IVA ").pack()

Iva=Entry(frame,text="TOTAL IVA")
Iva.pack()#,textvariable=NOMBRE)
#BuscNombre.grid(row=0,column=2)
E1=Entry(frame, width = 30)
E2=Entry(frame, width = 30)
#E2=Entry(frame, width = 30)


def b1():
    #E1=Entry(root)
    #E1.delete(0,END) 
    E1.delete(0,END)
    E2.delete(0,END)


    TOT=float(Tot.get())
    IVA=float(Iva.get())

    CIVA = IVA / 0.16 
    SIVA = TOT - IVA - CIVA 
    
    

    a=Label(frame,text="SUBTOTAL SIN IVA ").pack()

    E1.insert(0,SIVA)
    E1.pack()
   
    b=Label(frame,text="SUBTOTAL CON IVA ").pack()

    E2.insert(0,CIVA)
    E2.pack()
    
    

#frame.bind('<Return>', b1)


def b2():
    E1.delete(0,END)
    E2.delete(0,END)
   
    return None
      

Boton=Button(frame,text="OBTENER.",command=b1,height = 2, width = 20,fg='green')#,state='disabled')
Boton.pack()



clear=Button(frame,text="Borrar.",command=b2,fg='white')#,state='disabled')
clear.pack()

#root.bind('<Return>', b1)

#Ins.pack()






root.mainloop()

#frame.mainloop()


 

