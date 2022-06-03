import math
from tkinter import *

root = Tk()

def my_function(num):
  current=input1.get()
  input1.delete(0,END)
  input1.insert(0,str(current)+str(num))
  print(num)

def clear():
  input1.delete(0,END)


def addition():
  first_num=input1.get()
  global f_num
  global match
  match="add"
  f_num=int(first_num)
  input1.delete(0,END)

def sub():
  first_num=input1.get()
  global f_num
  global match
  match="sub"
  f_num=int(first_num)
  input1.delete(0,END)


def mul():
  first_num=input1.get()
  global f_num
  global match
  match="mul"
  f_num=int(first_num)
  input1.delete(0,END)


def div():
  first_num=input1.get()
  global f_num
  global match
  match="div"
  f_num=int(first_num)
  input1.delete(0,END)

def per():
  first_num=input1.get()
  global f_num
  global match
  match="per"
  f_num=int(first_num)
  input1.delete(0,END)

def eqal():
  second_num=input1.get()
  input1.delete(0,END)

  if(match=="add"):
    input1.insert(0, f_num + int(second_num))

  if (match == "sub"):
    input1.insert(0, f_num - int(second_num))

  if (match == "mul"):
      input1.insert(0, f_num * int(second_num))

  if (match == "div"):
      input1.insert(0, f_num / int(second_num))

  if (match == "per"):
      input1.insert(0, f_num % int(second_num))




root.title("Calculator")
root.geometry("300x470")

input1=Entry(root,width=40,)
input1.place(x=25,y=10)

btn1=Button(root,text="1",height=4,width=6,command=lambda : my_function(1))
btn1.place(x=25,y=60)

btn2=Button(root,text="2",height=4,width=6,command=lambda : my_function(2))
btn2.place(x=95,y=60)

btn3=Button(root,text="3",height=4,width=6,command=lambda : my_function(3))
btn3.place(x=160,y=60)

btn4=Button(root,text="4",height=4,width=6,command=lambda : my_function(4))
btn4.place(x=230,y=60)

btn5=Button(root,text="5",height=4,width=6,command=lambda : my_function(5))
btn5.place(x=25,y=140)

btn6=Button(root,text="6",height=4,width=6,command=lambda : my_function(6))
btn6.place(x=95,y=140)

btn7=Button(root,text="7",height=4,width=6,command=lambda : my_function(7))
btn7.place(x=160,y=140)

btn8=Button(root,text="8",height=4,width=6,command=lambda : my_function(8))
btn8.place(x=230,y=140)

btn9=Button(root,text="9",height=4,width=6,command=lambda : my_function(9))
btn9.place(x=25,y=220)

btn0=Button(root,text="0",height=4,width=6,command=lambda : my_function(0))
btn0.place(x=95,y=220)

btnequal=Button(root,text="=",height=4,width=6,command=eqal)
btnequal.place(x=160,y=220)

btnsum=Button(root,text="+",height=4,width=6,command=addition)
btnsum.place(x=230,y=220)

btnsub=Button(root,text="-",height=4,width=6, command=sub)
btnsub.place(x=25,y=300)

btnmulti=Button(root,text="x",height=4,width=6,command=mul)
btnmulti.place(x=95,y=300)

btndiv=Button(root,text="/",height=4,width=6,command=div)
btndiv.place(x=160,y=300)

btnclear=Button(root,text="C",height=4,width=6,command=clear)
btnclear.place(x=230,y=300)

btnper=Button(root,text="%",height=4,width=6,command=per)
btnper.place(x=25,y=380)


root.mainloop()