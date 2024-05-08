from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print (e)
                value= "Invalid Input" 
        scvalue.set(value)
        screen.update()      
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.geometry("600x700")
root.title("CALCULATOR")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable= scvalue, font="Arial 30 bold")
screen.pack(fill = X, padx= 15, pady= 10)

fr = Frame(root, bg="grey")

bt = Button(fr, text="9", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="8", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)


bt = Button(fr, text="7", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="+", font= "Arial 20 bold", padx=28, pady= 22, bg="lightblue")
bt.pack(side=LEFT,padx=(60,10),pady=10)
bt.bind("<Button-1>", click)

fr.pack()

fr = Frame(root, bg="grey")

bt = Button(fr, text="6", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="5", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)


bt = Button(fr, text="4", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="-", font= "Arial 20 bold", padx=31, pady= 22, bg="lightblue")
bt.pack(side=LEFT,padx=(60,10),pady=10)
bt.bind("<Button-1>", click)

fr.pack()

fr = Frame(root, bg="grey")

bt = Button(fr, text="3", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="2", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)


bt = Button(fr, text="1", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="*", font= "Arial 20 bold", padx=31, pady= 22, bg="lightblue")
bt.pack(side=LEFT,padx=(60,10),pady=10)
bt.bind("<Button-1>", click)

fr.pack()

fr = Frame(root, bg="grey")

bt = Button(fr, text="0", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text=".", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="C", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="/", font= "Arial 20 bold", padx=34, pady= 22, bg="lightblue")
bt.pack(side=LEFT,padx=(60,10),pady=10)
bt.bind("<Button-1>", click)

fr.pack()

fr = Frame(root, bg="grey")

bt = Button(fr, text="00", font= "Arial 20 bold", padx=28, pady= 22)
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="=", font= "Arial 20 bold", padx=75, pady= 22, bg="Lightgreen")
bt.pack(side=LEFT,padx=10,pady=10)
bt.bind("<Button-1>", click)

bt = Button(fr, text="%", font= "Arial 20 bold", padx=28, pady= 22, bg="lightblue")
bt.pack(side=LEFT,padx=(58,10),pady=10)
bt.bind("<Button-1>", click)

fr.pack()


root.mainloop()