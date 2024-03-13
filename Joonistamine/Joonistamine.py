from tkinter import *
def FromEntryToLabel(event):
    tekst=e.get()
    l.configure(text=tekst)
def valik():
    arv=var.get()
    e.delete(0,END)
    e.insert(END,arv)
showflag=False
def naitatarnid(event):
    global showflag
    if showflag:
        e.configure(show="")
        showflag=False
    else:
        e.configure(show="*")
        showflag=True
def chekbutton_select(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    l.delete(0,1)
    for item in jarjend:
        lb.insert(END,item)
    

#окно 
aken=Tk()
#свойство (прописываются внутри скобок) и методы (что объект имеет делать)
aken.geometry("600x400")
#заголовок 
aken.title("Tkinteri kasutamine. See on pealkiri")
aken.iconbitmap("icon.ico")
#рамка. указываем все свойства для дизайна. bg(background)-фон  
f=Frame(aken,bg="#6aa84f",border=50,height=50, width=600) 
f_all=Frame(aken,bg="#f44336",border=50,height=200, width=600)
t="Minu esimene aken Tkinteri abil"
l=Label(f,text=t,bg="#ead1dc",fg="#fff2cc",font="Algerian 16",height=3,width=len(t))
#текст 
e=Entry(f_all,bg="#fff2cc",fg="#ead1dc",font="Baguet_Script 20", width=30,justify=CENTER)#show="&"
#включать и выключать звездочку
e.bind("<Return>", naitatarnid)# Entri peale vajutamine
b=Button(f_all,text="Vajuta siia",bg="purple",font="Bodoni_MT 20", relief=RAISED)#SUNKER,GROOVE
#программируем кнопку bind-любое событие ("<Button-1>")левая кнопка мыши
b.bind("<Button-1>",FromEntryToLabel)
b.bind("<Button-3>",chekbutton_select)#("<Button-3>") правая кнопка мыши
#считываем текст в виде текста или в виде чисел
var=IntVar()#StringVar()
#радио кнопка 
r1=Radiobutton(f_all,text="Esimene",font="Bodoni_MT 20",bg="#fff2cc", variable=var,value=1, command=valik)
r2=Radiobutton(f_all,text="Teine", font="Bodoni_MT 20",bg="#fff2cc", variable=var,value=2,command=valik)
r3=Radiobutton(f_all,text="Kolmas", font="Bodoni_MT 20",bg="#fff2cc", variable=var,value=3, command=valik)
#добавляем картинки 
img1=PhotoImage(file="cap.png")
img2=PhotoImage(file="game.png")
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f_all,image=img1, variable=var1, onvalue="Paike paistab", offvalue="Paike ei paista")
c2=Checkbutton(f_all,image=img2, variable=var1, onvalue="Sajab vihma", offvalue="Paike ei paista")
c1.deselect()
c2.deselect()
lb=Listbox(f_all, height=2, width=20)






#размещать объекты
f.grid(row=0,column=0)# place()-koordinaadid, pack()- nii nagu nimekirjas
l.pack()

f_all.grid(row=1, column=0)
obj=[e,b, r1,r2,r3,c1,c2,lb]
for o in obj:
    o.pack()



aken.mainloop() #самая последняя команда!  майн - запуск, лооп - повторение программы. самая последняя команда 