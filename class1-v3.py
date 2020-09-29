import tkinter

  
m=tkinter.Tk()
m.geometry('300x300') 

response=tkinter.StringVar()
response.set('Welcome. Type above to speak to me')


t=tkinter.Entry(m)


def speak():
  user_input=t.get().lower()
  if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
    response.set("Hi, How can I assist you")
  

b=tkinter.Button(m,text="Submit" , font='Times 15 bold' ,command=speak)

l=tkinter.Label(m,textvariable=response)


t.pack(pady=20)
b.pack(pady=20)
l.pack(pady=20)
m.mainloop()


#ask the student to keep adding more commands which will ask different questions, return respones thus creaating an ai chatbot