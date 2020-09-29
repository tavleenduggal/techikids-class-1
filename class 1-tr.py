import tkinter
  
m=tkinter.Tk()
  

def l():
  a=tkinter.Label(text="Hello")
  a.pack()

b=tkinter.Button(text="Submit" ,command=l, font='Times 15 italic')

b.pack()
m.mainloop()