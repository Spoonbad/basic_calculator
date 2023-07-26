from tkinter import *
from math import sqrt
window=Tk() #creating a window 
window.title("Calculator")
icon= PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background='gray')
window.geometry("388x430")
window.resizable(0,0)
#entry widget 
entry=Entry(window,width=55,relief=SUNKEN,bd=10,bg="#50C7C7",disabledbackground='lightblue',state=DISABLED)
entry.grid(column=0,row=0,columnspan=5,padx=10,pady=10)
string=""
b=0
# main function that uses the entry as token
def main():
    global string
    string_array=string.split( )
    print(string.split( ))
    
    print(len(string_array))
    global b
    sum=0
    a=len(string_array)
    for i in range(a) :
     #if ('√' in string_array):
      #  j=string_array.index('√')
       # sum=sqrt(float(string_array[j+1]))
        #string_array.pop(j)
        #string_array.pop(j)
        
        #string_array.insert(j,sum)
        #print(string_array)
     if ('^' in string_array):
        j=string_array.index('^')
        sum=pow(float(string_array[j-1]),float(string_array[j+1]))
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.insert(j-1,sum)
        print(string_array)
     elif ('/' in string_array):
        j=string_array.index('/')
        sum=float(string_array[j-1])/float(string_array[j+1])
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.insert(j-1,sum)
        print(string_array)
     elif ("*" in string_array):
        j=string_array.index('*')
        sum=float(string_array[j-1])*float(string_array[j+1])
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.insert(j-1,sum)
        print(string_array)
         
     elif ('-' in string_array):
        j=string_array.index('-')
        sum=float(string_array[j-1])-float(string_array[j+1])
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.insert(j-1,sum)
        print(string_array) 
     elif ('+' in string_array):
        j=string_array.index('+')
        sum=float(string_array[j-1])+float(string_array[j+1])
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.pop(j-1)
        string_array.insert(j-1,sum)
        print(string_array)
      
    
     else:
        break
    b=string_array[0]
     
#function
def click(num) :
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(num))
    
def add():
    previos=entry.get()
    entry.delete(0,END)
    global string
    string=previos + ' '+ '+' + ' '
    entry.insert(0,string)
def equal():
    global string
    previos=entry.get()
    string = previos
    main()
    global b
    entry.delete(0,END)
    entry.insert(0,b)
def multiply():
    global string
    previos=entry.get()
    entry.delete(0,END)
    string =previos + ' '+ '*' + ' '
    entry.insert(0,string) 
def divide():
    global string
    previos=entry.get()
    entry.delete(0,END)
    string =previos + ' '+ '/' + ' '
    entry.insert(0,string) 
def decrease():
    global string
    previos=entry.get()
    entry.delete(0,END)
    string =previos + ' '+ '-' + ' '
    entry.insert(0,string)
def power():
    global string
    previos=entry.get()
    entry.delete(0,END)
    string =previos + ' '+ '^' + ' '
    entry.insert(0,string) 
def clearall():
    global string
    string=''
    entry.delete(0,END)
def clearlast():
    global string
    entry.delete(0,END)
    entry.insert(0,string)
def delete():
    global string
    string=entry.get()
    string=string[0:(len(string)-1)]
    entry.delete(0,END)
    entry.insert(0,string)
#def msqrt():
#global string
 #   previos=entry.get()
  #  entry.delete(0,END)
   # string =previos + ' '+ '√' + ' '
    #entry.insert(0,string)    

    
button1=Button(window,text="1",padx=40,pady=25,command=lambda: click(1),)
button2=Button(window,text="2",padx=40,pady=25,command=lambda: click(2))
button3=Button(window,text="3",padx=40,pady=25,command=lambda: click(3))
button4=Button(window,text="4",padx=40,pady=25,command=lambda: click(4))
button5=Button(window,text="5",padx=40,pady=25,command=lambda: click(5))
button6=Button(window,text="6",padx=40,pady=25,command=lambda: click(6))
button7=Button(window,text="7",padx=40,pady=25,command=lambda: click(7))
button8=Button(window,text="8",padx=40,pady=25,command=lambda: click(8))
button9=Button(window,text="9",padx=40,pady=25,command=lambda: click(9))
button0=Button(window,text="0",padx=40,pady=25,command=lambda: click(0))
button_equal=Button(window,text="=",padx=40,pady=25,command=equal,bg='blue')
button_add=Button(window,text="+",padx=40,pady=25,command=add)
button_multiply=Button(window,text="*",padx=40,pady=25,command=multiply)
button_divide=Button(window,text="/",padx=40,pady=25,command=divide)
button_decrease=Button(window,text="-",padx=40,pady=25,command=decrease)
button_clearall=Button(window,text='CE',padx=36,pady=25,command=clearall)
button_clearlast=Button(window,text='C',padx=40,pady=25,command=clearlast)
button_delete=Button(window,text='del',padx=34,pady=25,command=delete)
button_power=Button(window,text='x^y',padx=34,pady=25,command=power)
#button_sqrt=Button(window,text='√',padx=40,pady=25,command=msqrt)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button0.grid(row=5,column=0)
#button_sqrt.grid(row=4,column=3)
button_equal.grid(row=5,column=2)
button_add.grid(row=3,column=3)
button_decrease.grid(row=2,column=3)
button_divide.grid(row=5,column=1)
button_multiply.grid(row=4,column=3)
button_clearall.grid(row=1,column=2)
button_clearlast.grid(row=1,column=1)
button_power.grid(row=1,column=0)
button_delete.grid(row=1,column=3)
window.mainloop() #show window 
