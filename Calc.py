
from tkinter import*
root=Tk()
root.title("Simple calc")
#Setup Display:
Display=Entry(root,width=35,borderwidth=5)
Display.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
try:
    #Setup function:
def clic_me(number):
    current=Display.get()
    Display.delete(0,END)
    Display.insert(0,str(current)+str(number))

#Clear key:
def clear_key():
    Display.delete(0,END)
#Add function:
def add_key():
    first_num=Display.get()
    global f_num
    global math
    math="Addition"
    f_num=int(first_num)
    Display.delete(0,END)
    
#Subtract function:
def sub_key():
    first_num=Display.get()
    global f_num
    global math
    math="Subtraction"
    f_num=int(first_num)
    Display.delete(0,END)
   
 #Multipication function:
def mul_key():
    first_num=Display.get()
    global f_num
    global math
    math="Multiplication"
    f_num=int(first_num)
    Display.delete(0,END)
#Division function:
def div_key():
    first_num=Display.get()
    global f_num
    global math
    math="Division"
    f_num=int(first_num)
    Display.delete(0,END)
#define equal key:
def equal_key():
    second_num=Display.get()
    Display.delete(0,END)
    if math=="Addition":
        Display.insert(0,int(f_num)+int(second_num))

    if math=="Subtraction":
        Display.insert(0,int(f_num)-int(second_num))

    if math=="Multiplication":
        Display.insert(0,int(f_num)*int(second_num))

    if math=="Division":
        Display.insert(0,int(f_num)/int(second_num))
    
#Setup buttons:
button1=Button(text='1',padx=20,pady=10,bg="purple",fg="white",command=lambda:clic_me(1))
button2=Button(text='2',padx=20,pady=10,bg="blue",fg="white",command=lambda:clic_me(2))
button3=Button(text='3',padx=20,pady=10,bg="skyblue",fg="white",command=lambda:clic_me(3))
button4=Button(text='4',padx=20,pady=10,bg="green",fg="white",command=lambda:clic_me(4))
button5=Button(text='5',padx=20,pady=10,bg="yellow",fg="white",command=lambda:clic_me(5))
button6=Button(text='6',padx=20,pady=10,bg="orange",fg="white",command=lambda:clic_me(6))
button7=Button(text='7',padx=20,pady=10,bg="red",fg="white",command=lambda:clic_me(7))
button8=Button(text='8',padx=20,pady=10,bg="pink",fg="white",command=lambda:clic_me(8))
button9=Button(text='9',padx=20,pady=10,bg="black",fg="white",command=lambda:clic_me(9))
button0=Button(text='0',padx=20,pady=10,bg="gray",fg="white",command=lambda:clic_me(0))
buttonx1=Button(text='.',padx=20,pady=10,fg="black")
buttonx2=Button(text='=',padx=20,pady=10,bg="violet",fg="white",command=equal_key)
buttonadd=Button(text='+',padx=40,pady=20,bg="orange",fg="white",command=add_key)
buttonsub=Button(text='-',padx=23,pady=12,bg="lightgreen",fg="white",command=sub_key)
buttonmul=Button(text='X',padx=23,pady=12,bg="orange",fg="white",command=mul_key)
buttondiv=Button(text='/',padx=23,pady=12,bg="purple",fg="white",command=div_key)
buttonclear=Button(text='clear',pady=12,bg="black",fg="red",command=clear_key)

#Setup grid layout:
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button7.grid(row=5,column=0)
button8.grid(row=5,column=1)
button9.grid(row=5,column=2)
button0.grid(row=6,column=1)
buttonx1.grid(row=6,column=0)
buttonx2.grid(row=6,column=2)
buttonadd.grid(row=6,column=3)
buttonsub.grid(row=5,column=3)
buttonmul.grid(row=4,column=3)
buttondiv.grid(row=3,column=3)
except:
buttonclear.grid(row=2,column=3)
root.mainloop()


    
