import tkinter

m = tkinter.Tk()
 

tf = tkinter.Entry(m,width = 40)
tf.grid(row = 0 , columnspan = 10, ipadx = 6 , ipady = 8)


btn7 = tkinter.Button(m, text = '7' , width = 5 )
btn7.grid(row = 1 , column = 0 ,ipady = 4 , ipadx = 2)

btn8 = tkinter.Button(m, text = '8' , width = 5  )
btn8.grid(row = 1 , column = 1 ,ipady = 4, ipadx = 2)

btn9 = tkinter.Button(m, text = '9' , width = 5 )
btn9.grid(row = 1 , column = 2,ipady = 4, ipadx = 2)

btnmines = tkinter.Button(m, text = '-' , width = 8  )
btnmines.grid(row = 1 , column = 3 , ipady = 3, ipadx = 2)

btnmul = tkinter.Button(m, text = '*' , width = 8  )
btnmul.grid(row = 1 , column = 4 , ipady = 3, ipadx = 2)

btn4 = tkinter.Button(m, text = '4' , width = 5  )
btn4.grid(row = 2 , column = 0 ,ipady = 4 , ipadx = 2)

btn5 = tkinter.Button(m, text = '5' , width = 5  )
btn5.grid(row = 2 , column = 1 ,ipady = 4, ipadx = 2)

btn6 = tkinter.Button(m, text = '6' , width = 5  )
btn6.grid(row = 2 , column = 2,ipady = 4, ipadx = 3)



btnplus = tkinter.Button(m, text = '+' , width = 5)
btnplus.grid(row = 2 , column = 3,ipady = 4, ipadx = 10)



btndiv = tkinter.Button(m, text = '/' , width = 5 )
btndiv.grid(row = 2 , column = 4,ipady = 4, ipadx = 10)



btnequal = tkinter.Button(m, text = 'Enter' , width = 5)
btnequal.grid(row = 3 , column = 4,ipady = 4, ipadx = 10)



btn0= tkinter.Button(m, text = '0' , width = 5)
btn0.grid(row = 3 , column = 3,ipady = 4, ipadx = 10)



btn3 = tkinter.Button(m, text = '3' , width = 5)
btn3.grid(row = 3 , column = 0 ,ipady = 4 , ipadx = 2)


btn2 = tkinter.Button(m, text = '2' , width = 5 )
btn2.grid(row = 3 , column = 1 ,ipady = 4, ipadx = 2)





btn1 = tkinter.Button(m, text = '1' , width = 5 )
btn1.grid(row = 3 , column = 2,ipady = 4, ipadx = 2)


btnclr = tkinter.Button(m, text = 'Clear' , width = 5  )
btnclr.grid(row = 4 , columnspan = 6,ipady = 4, ipadx = 108)



m.mainloop()