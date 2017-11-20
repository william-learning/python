from tkinter import *

window=Tk()

def kg_convert():
    t1.delete(1.0, END)
    g=float(e1_value.get())*1000
    t1.insert(END, g)

    t2.delete(1.0,END)
    pound=float(e1_value.get())*2.20462
    t2.insert(END,pound)
    
    t3.delete(1.0,END)
    ounce=float(e1_value.get())*35.274
    t3.insert(END,ounce)

b1=Button(window,text="Convert",command=kg_convert)
# b1.pack()
b1.grid(row=0,column=2)

e=Label(window,text="kg")
e.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
