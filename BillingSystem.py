from tkinter import *

root=Tk()
root.geometry("900x500")
root.title("Billing Management System") 
root.resizable(False,False)
def Reset():
    entry_dosa.delete(0,END)
    entry_idli.delete(0,END)
    entry_meduWada.delete(0,END)
    entry_maggie.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_poha.delete(0,END)
    entry_misal.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except: a1=0
    try:a2=int(idli.get())
    except: a2=0
    try:a3=int(meduWada.get())
    except: a3=0
    try:a4=int(maggie.get())
    except: a4=0
    try:a5=int(tea.get())
    except: a5=0
    try:a6=int(coffee.get())
    except: a6=0
    try:a7=int(poha.get())
    except: a7=0
    try:a8=int(misal.get())
    except: a8=0

    c1=120*a1
    c2=50*a2
    c3=70*a3
    c4=40*a4
    c5=20*a5
    c6=35*a6
    c7=50*a7
    c8=120*a8

    lb1_total= Label(f2, font=('aria',20),text="Total", width="16", fg="Black", )
    lb1_total.place(x=20, y=50)
    entry_total= Entry(f2, font=('aria',20), textvariable=Total_bill,bd=6, width=15, bg="#256D85", fg="white")
    entry_total.place(x=20, y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7+c8
    string_bill = "Rs.",str('%f'%totalcost)
    Total_bill.set(string_bill)

Label(text = "Billing Management System" ,bg="#256D85", fg="white", font=("calibri", 31), width="300", height="2").pack()
#MENU CARD

f= Frame(root, bg="#8FE3CF", highlightbackground="black", highlightthickness=1, width="300", height="370")
f.place(x=10, y=118)

Label(f,text="MENU", fg="black" , font=("Rubik Vinyl", 22), bg="#8FE3CF").place(x=10, y=0)
Label(f,text="DOSA ----------------- 120 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=50)
Label(f,text="IDLI -------------------- 50 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=90)
Label(f,text="MEDU WADA ------- 70 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=130)
Label(f,text="MAGGIE -------------- 40 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=170)
Label(f,text="TEA -------------------- 20 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=210)
Label(f,text="COFFEE -------------- 35 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=250)
Label(f,text="POHA ------------------ 50 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=290)
Label(f,text="MISAL ----------------- 120 Rs", fg="#002B5B" , font=("Raleway", 16),bg="#8FE3CF").place(x=20, y=330)

#ENTRY WORK
f1 =Frame(root, border =5, height =500, width =330,relief="ridge", bg="#8FE3CF", highlightbackground="black" , highlightthickness=0.5)
f1.place(x=320,y=118)



dosa = StringVar()
idli =StringVar()
meduWada = StringVar()
maggie = StringVar()
tea = StringVar()
coffee = StringVar()
poha = StringVar()
misal = StringVar()
Total_bill = StringVar()

lb = Label(f1,text="ITEMS", fg="#002B5B" , font=("Rubik Vinyl", 12), bg="#8FE3CF").grid(row=1,column=0)
lb1_dosa = Label(f1, font=("aria", 16), text ="dosa", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=2, column=0)
lb1_idli = Label(f1, font=("aria", 16), text ="idli", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=3, column=0)
lb1_meduWada = Label(f1, font=("aria", 16), text ="meduWada", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=4, column=0)
lb1_maggie = Label(f1, font=("aria", 16), text ="maggie", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=5, column=0)
b1_tea = Label(f1, font=("aria", 16), text ="tea", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=6, column=0)
lb1_coffee = Label(f1, font=("aria", 16), text ="coffee", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=7, column=0)
lb1_poha = Label(f1, font=("aria", 16), text ="poha", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=8, column=0)
lb1_misal = Label(f1, font=("aria", 16), text ="misal", width=12, fg="#002B5B",bg="#8FE3CF").grid(row=9, column=0)
#ENTRY

entry_dosa = Entry(f1, font=("aria", 16),textvariable=dosa, width=8,bd=6, bg="#fff")
entry_idli = Entry(f1, font=("aria", 16),textvariable=idli, width=8,bd=6, bg="#fff")
entry_meduWada = Entry(f1, font=("aria", 16),textvariable=meduWada,bd=6, width=8, bg="#fff")
entry_maggie = Entry(f1, font=("aria", 16),textvariable=maggie, width=8,bd=6, bg="#fff")
entry_tea = Entry(f1, font=("aria", 16),textvariable=tea, width=8,bd=6, bg="#fff")
entry_coffee = Entry(f1, font=("aria", 16),textvariable=coffee,bd=6, width=8, bg="#fff")
entry_poha = Entry(f1, font=("aria", 16),textvariable=poha,bd=6, width=8, bg="#fff")
entry_misal = Entry(f1, font=("aria", 16),textvariable=misal,bd=6, width=8, bg="#fff")
entry_dosa.grid(row=2, column=1)
entry_idli.grid(row=3, column=1)
entry_meduWada.grid(row=4, column=1)
entry_maggie.grid(row=5, column=1)
entry_tea.grid(row=6, column=1)
entry_coffee.grid(row=7, column=1)
entry_poha.grid(row=8, column=1)
entry_misal.grid(row=9, column=1)
#BUTTON
btn_reset = Button(f1, bd=5, fg="white", bg="#002B5B", width=10, text="Reset" , command=Reset).grid(row=10, column=0)
btn_total = Button(f1, bd=5, fg="white", bg="#002B5B", width=10, text="Total" , command=Total).grid(row=10, column=1)

#BILL
f2 = Frame(root, bg="#8FE3CF", width=290, highlightbackground="black", highlightthickness=1, height=370)
f2.place(x=600, y=118)

Bill = Label(f2,text="Bill",bg="lightyellow")
Bill.place(x=120, y=10)

root.mainloop()