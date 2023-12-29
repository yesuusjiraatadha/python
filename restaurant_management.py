#        group name   id 
# 1, Dereje shibiru    2558/14
# 2, Bilise melkamu    22347/14
# 3, Degafa denbob     2527/14
# 4, Darara takele     2493/14
# 5, Bilisuma fufa     2350/14

from tkinter import *
from tkinter import filedialog, messagebox
import random
import time



# Functions

def reset():
   textReceipt.delete(1.0, END)
   e_firfir.set('0')
   e_shiro.set('0')
   e_pasta.set('0')
   e_tibsi.set('0')
   e_dulet.set('0')
   e_beyayenet.set('0')
   e_atikilt.set('0')
   e_tegabino.set('0')
   e_doro.set('0')

   e_pepsi.set('0')
   e_coffee.set('0')
   e_coca.set('0')
   e_walia.set('0')
   e_fanta.set('0')
   e_mirinda.set('0')
   e_tea.set('0')
   e_milk.set('0')
   e_bedele.set('0')


   textshiro.config(state=DISABLED)
   textfirfir.config(state=DISABLED)
   textpasta.config(state=DISABLED)
   texttibsi.config(state=DISABLED)
   textdulet.config(state=DISABLED)
   texttegabino.config(state=DISABLED)
   textdoro.config(state=DISABLED)
   textatikilt.config(state=DISABLED)
   textbeyayenet.config(state=DISABLED)

   textpepsi.config(state=DISABLED)
   textcoffee.config(state=DISABLED)
   textmirinda.config(state=DISABLED)
   textwalia.config(state=DISABLED)
   textfanta.config(state=DISABLED)
   textmilk.config(state=DISABLED)
   texttea.config(state=DISABLED)
   textcoca.config(state=DISABLED)
   textbedele.config(state=DISABLED)



   var1.set(0)
   var2.set(0)
   var3.set(0)
   var4.set(0)
   var5.set(0)
   var6.set(0)
   var7.set(0)
   var8.set(0)
   var9.set(0)
   var10.set(0)
   var11.set(0)
   var12.set(0)
   var13.set(0)
   var14.set(0)
   var15.set(0)
   var16.set(0)
   var17.set(0)
   var18.set(0)
   var19.set(0)
   var20.set(0)
   var21.set(0)
   var22.set(0)
   var23.set(0)
   var24.set(0)
   var25.set(0)
   var26.set(0)
   var27.set(0)

   costofdrinksvar.set('')
   costoffoodvar.set('')


   subtotalvar.set('')
   servicetaxvar.set('')
   totalcostvar.set('')


def send():
   if textReceipt.get(1.0, END) == '\n':
       pass
   else:
       def send_msg():
           message = textarea.get(1.0, END)
           number = numberfield.get()
           auth = 'woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
           url = 'https://www.fast2sms.com/dev/bulk'

           params = {
               'authorization': auth,
               'message': message,
               'numbers': number,
               'sender-id': 'FSTSMS',
               'route': 'p',
               'language': 'english'
           }
       ''' response = requests.get(url, params=params)
           dic = response.json()
           result = dic.get('return')
           if result == True:
               messagebox.showinfo('Send Successfully', 'Message sent succesfully')

           else:
               messagebox.showerror('Error', 'Something went wrong')'''

       root2 = Toplevel()

       root2.title("Send Bill")
       root2.config(bg='red4')
       root2.geometry('485x620+50+50')

       logoImage = PhotoImage(file='sender.png')
       label = Label(root2, image=logoImage, bg='red4')
       label.pack(pady=5)

       numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='#42c2f5', fg='white')
       numberLabel.pack(pady=5)

       numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
       numberfield.pack(pady=5)

       billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='#42c2f5', fg='white')
       billLabel.pack(pady=5)

       textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
       textarea.pack(pady=5)
       textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

       if costoffoodvar.get() != '0 Rs':
           textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
       if costofdrinksvar.get() != '0 Rs':
           textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')


       textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
       textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
       textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

       sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE
                           , command=send_msg)
       sendButton.pack(pady=5)

       root2.mainloop()


def save():
   if textReceipt.get(1.0, END) == '\n':
       pass
   else:
       url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
       if url == None:
           pass
       else:

           bill_data = textReceipt.get(1.0, END)
           url.write(bill_data)
           url.close()
           messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')


def receipt():
   global billnumber, date
   if costoffoodvar.get() != ''  or costofdrinksvar.get() != '':
       textReceipt.delete(1.0, END)
       x = random.randint(100, 10000)
       billnumber = 'BILL' + str(x)
       date = time.strftime('%d/%m/%Y')
       textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
       textReceipt.insert(END, '***************************************************************\n')
       textReceipt.insert(END, 'Items:\t\t Cost Of Items(Br)\n')
       textReceipt.insert(END, '***************************************************************\n')
       if e_shiro.get() != '0':
           textReceipt.insert(END, f'shiro\t\t\t{int(e_shiro.get()) * 10}\n\n')

       if e_firfir.get() != '0':
           textReceipt.insert(END, f'firfir\t\t\t{int(e_firfir.get()) * 60}\n\n')

       if e_tibsi.get() != '0':
           textReceipt.insert(END, f'tibsi\t\t\t{int(e_tibsi.get()) * 100}\n\n')

       if e_beyayenet.get() != '0':
           textReceipt.insert(END, f'beyayenet:\t\t\t{int(e_beyayenet.get()) * 30}\n\n')

       if e_pasta.get() != '0':
           textReceipt.insert(END, f'pasta:\t\t\t{int(e_pasta.get()) * 50}\n\n')

       if e_tegabino.get() != '0':
           textReceipt.insert(END, f'tegabino:\t\t\t{int(e_tegabino.get()) * 100}\n\n')

       if e_dulet.get() != '0':
           textReceipt.insert(END, f'dulet:\t\t\t{int(e_dulet.get()) * 40}\n\n')

       if e_doro.get() != '0':
           textReceipt.insert(END, f'doro:\t\t\t{int(e_doro.get()) * 120}\n\n')

       if e_atikilt.get() != '0':
           textReceipt.insert(END, f'atikilt:\t\t\t{int(e_atikilt.get()) * 120}\n\n')

       if e_pepsi.get() != '0':
           textReceipt.insert(END, f'pepsi:\t\t\t{int(e_pepsi.get()) * 50}\n\n')

       if e_coffee.get() != '0':
           textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

       if e_coca.get() != '0':
           textReceipt.insert(END, f'coca:\t\t\t{int(e_coca.get()) * 80}\n\n')

       if e_fanta.get() != '0':
           textReceipt.insert(END, f'fanta:\t\t\t{int(e_fanta.get()) * 30}\n\n')

       if e_mirinda.get() != '0':
           textReceipt.insert(END, f'mirinda:\t\t\t{int(e_mirinda.get()) * 40}\n\n')

       if e_walia.get() != '0':
           textReceipt.insert(END, f'walia:\t\t\t{int(e_walia.get()) * 60}\n\n')

       if e_tea.get() != '0':
           textReceipt.insert(END, f'teaChai:\t\t\t{int(e_tea.get()) * 20}\n\n')

       if e_milk.get() != '0':
           textReceipt.insert(END, f'Milk:\t\t\t{int(e_milk.get()) * 50}\n\n')

       if e_bedele.get() != '0':
           textReceipt.insert(END, f'bedele:\t\t\t{int(e_bedele.get()) * 80}\n\n')



       textReceipt.insert(END, '***************************************************************\n')
       if costoffoodvar.get() != '0 Br':
           textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Br\n\n')
       if costofdrinksvar.get() != '0 Br':
           textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Br\n\n')


       textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Br\n\n')
       textReceipt.insert(END, f'Service Tax\t\t\t{50}Br\n\n')
       textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Br\n\n')
       textReceipt.insert(END, '***************************************************************\n')

   else:
       messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
   global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
   if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
           var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
           var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
           var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
           var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
           var26.get() != 0 or var27.get() != 0:

       item1 = int(e_shiro.get())
       item2 = int(e_firfir.get())
       item3 = int(e_tibsi.get())
       item4 = int(e_pasta.get())
       item5 = int(e_dulet.get())
       item6 = int(e_beyayenet.get())
       item7 = int(e_atikilt.get())
       item8 = int(e_tegabino.get())
       item9 = int(e_doro.get())

       item10 = int(e_pepsi.get())
       item11 = int(e_coffee.get())
       item12 = int(e_coca.get())
       item13 = int(e_fanta.get())
       item14 = int(e_mirinda.get())
       item15 = int(e_walia.get())
       item16 = int(e_tea.get())
       item17 = int(e_milk.get())
       item18 = int(e_bedele.get())



       priceofFood = (item1 * 10) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (
                   item7 * 120) \
                     + (item8 * 100) + (item9 * 120)

       priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                       + (item16 * 20) + (item17 * 50) + (item18 * 80)



       costoffoodvar.set(str(priceofFood) + ' Br')
       costofdrinksvar.set(str(priceofDrinks) + ' Br')


       subtotalofItems = priceofFood + priceofDrinks
       subtotalvar.set(str(subtotalofItems) + ' Br')

       servicetaxvar.set('50 Br')

       tottalcost = subtotalofItems + 50
       totalcostvar.set(str(tottalcost) + ' Br')

   else:
       messagebox.showerror('Error', 'No Item Is selected')


def shiro():
   if var1.get() == 1:
       textshiro.config(state=NORMAL)
       textshiro.delete(0, END)
       textshiro.focus()
   else:
       textshiro.config(state=DISABLED)
       e_shiro.set('0')


def firfir():
   if var2.get() == 1:
       textfirfir.config(state=NORMAL)
       textfirfir .delete(0, END)
       textfirfir .focus()

   else:
       textfirfir.config(state=DISABLED)
       e_firfir.set('0')


def tibsi():
   if var3.get() == 1:
       texttibsi.config(state=NORMAL)
       texttibsi  .delete(0, END)
       texttibsi .focus()

   else:
       texttibsi.config(state=DISABLED)
       e_tibsi.set('0')


def pasta():
   if var4.get() == 1:
       textpasta.config(state=NORMAL)
       textpasta  .focus()
       textpasta .delete(0, END)


   elif var4.get() == 0:
       textpasta.config(state=DISABLED)
       e_pasta.set('0')


def dulet():
   if var5.get() == 1:
       textdulet.config(state=NORMAL)
       textdulet.focus()
       textdulet.delete(0, END)
   elif var5.get() == 0:
       textdulet.config(state=DISABLED)
       e_dulet.set('0')


def beyayenet():
   if var6.get() == 1:
       textbeyayenet.config(state=NORMAL)
       textbeyayenet .focus()
       textbeyayenet.delete(0, END)


   elif var6.get() == 0:
       textbeyayenet.config(state=DISABLED)
       e_beyayenet.set('0')


def atikilt():
   if var7.get() == 1:
       textatikilt.config(state=NORMAL)
       textatikilt.focus()
       textatikilt.delete(0, END)
   elif var7.get() == 0:
       textatikilt.config(state=DISABLED)
       e_atikilt.set('0')


def tegabino():
   if var8.get() == 1:
       texttegabino.config(state=NORMAL)
       texttegabino.focus()
       texttegabino.delete(0, END)
   elif var8.get() == 0:
       texttegabino.config(state=DISABLED)
       e_tegabino.set('0')


def doro():
   if var9.get() == 1:
       textdoro.config(state=NORMAL)
       textdoro.focus()
       textdoro.delete(0, END)
   elif var9.get() == 0:
       textdoro.config(state=DISABLED)
       e_doro.set('0')


def pepsi():
   if var10.get() == 1:
       textpepsi.config(state=NORMAL)
       textpepsi.focus()
       textpepsi.delete(0, END)
   elif var10.get() == 0:
       textpepsi.config(state=DISABLED)
       e_pepsi.set('0')


def coffee():
   if var11.get() == 1:
       textcoffee.config(state=NORMAL)
       textcoffee.focus()
       textcoffee.delete(0, END)
   elif var11.get() == 0:
       textcoffee.config(state=DISABLED)
       e_coffee.set('0')


def coca():
   if var12.get() == 1:
       textcoca.config(state=NORMAL)
       textcoca.focus()
       textcoca.delete(0, END)
   elif var12.get() == 0:
       textcoca.config(state=DISABLED)
       e_coca.set('0')


def fanta():
   if var13.get() == 1:
       textfanta.config(state=NORMAL)
       textfanta.focus()
       textfanta.delete(0, END)
   elif var13.get() == 0:
       textfanta.config(state=DISABLED)
       e_fanta.set('0')


def mirinda():
   if var14.get() == 1:
       textmirinda.config(state=NORMAL)
       textmirinda.focus()
       textmirinda.delete(0, END)
   elif var14.get() == 0:
       textmirinda.config(state=DISABLED)
       e_mirinda.set('0')


def walia():
   if var15.get() == 1:
       textwalia.config(state=NORMAL)
       textwalia.focus()
       textwalia.delete(0, END)
   elif var15.get() == 0:
       textwalia.config(state=DISABLED)
       e_walia.set('0')


def tea():
   if var16.get() == 1:
       texttea.config(state=NORMAL)
       texttea.focus()
       texttea.delete(0, END)
   elif var16.get() == 0:
       texttea.config(state=DISABLED)
       e_tea.set('0')


def milk():
   if var17.get() == 1:
       textmilk.config(state=NORMAL)
       textmilk.focus()
       textmilk.delete(0, END)
   elif var17.get() == 0:
       textmilk.config(state=DISABLED)
       e_milk.set('0')


def bedele():
   if var18.get() == 1:
       textbedele.config(state=NORMAL)
       textbedele.focus()
       textbedele.delete(0, END)
   elif var18.get() == 0:
       textbedele.config(state=DISABLED)
       e_bedele.set('0')




root = Tk()

root.geometry('1270x690+0+0')

root.resizable(0, 0)

root.title('Restaurant Management System created by Group 1:')

root.config(bg='firebrick4')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='#ffc300')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Restaurant Management System', font=('arial', 30, 'bold'), fg='yellow', bd=9,
                  bg='#42c2f5', width=51)
labelTitle.grid(row=0, column=0)

# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='#42c2f5')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='#42c2f5', pady=10)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4', )
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE, bg='#42c2f5')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='#42c2f5')
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg='#42c2f5')
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg='#42c2f5')
buttonFrame.pack()

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_shiro= StringVar()
e_firfir = StringVar()
e_pasta = StringVar()
e_beyayenet = StringVar()
e_tibsi = StringVar()
e_atikilt = StringVar()
e_dulet = StringVar()
e_doro = StringVar()
e_tegabino = StringVar()

e_pepsi = StringVar()
e_coffee = StringVar()
e_coca = StringVar()
e_fanta = StringVar()
e_walia = StringVar()
e_mirinda = StringVar()
e_tea = StringVar()
e_milk = StringVar()
e_bedele = StringVar()



costoffoodvar = StringVar()
costofdrinksvar = StringVar()

subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_shiro.set('0')
e_firfir.set('0')
e_pasta.set('0')
e_tibsi.set('0')
e_dulet.set('0')
e_beyayenet.set('0')
e_atikilt.set('0')
e_doro.set('0')
e_tegabino.set('0')

e_pepsi.set('0')
e_coffee.set('0')
e_coca.set('0')
e_walia.set('0')
e_fanta.set('0')
e_mirinda.set('0')
e_tea.set('0')
e_milk.set('0')
e_bedele.set('0')



##FOOD

shiro = Checkbutton(foodFrame, text='shiro', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                  , command=shiro)
shiro.grid(row=0, column=0, sticky=W)

firfir = Checkbutton(foodFrame, text='firfir', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                  , command=firfir)
firfir.grid(row=1, column=0, sticky=W)

tibsi = Checkbutton(foodFrame, text='tibsi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                  , command=tibsi)
tibsi.grid(row=2, column=0, sticky=W)

pasta = Checkbutton(foodFrame, text='pasta', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                   , command=pasta)
pasta.grid(row=3, column=0, sticky=W)

dulet = Checkbutton(foodFrame, text='dulet', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                   , command=dulet)
dulet.grid(row=4, column=0, sticky=W)

beyayenet = Checkbutton(foodFrame, text='beyayenet', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                       , command=beyayenet)
beyayenet.grid(row=5, column=0, sticky=W)

atikilt = Checkbutton(foodFrame, text='atikilt', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                     command=atikilt)
atikilt.grid(row=6, column=0, sticky=W)

tegabino = Checkbutton(foodFrame, text='tegabino', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                      , command=tegabino)
tegabino.grid(row=7, column=0, sticky=W)

doro = Checkbutton(foodFrame, text='doro', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                     , command=doro)
doro.grid(row=8, column=0, sticky=W)


# Entry Fields for Food Items

textshiro = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shiro)
textshiro.grid(row=0, column=1)

textfirfir = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_firfir)
textfirfir.grid(row=1, column=1)

texttibsi = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tibsi)
texttibsi.grid(row=2, column=1)

textpasta = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pasta)
textpasta.grid(row=3, column=1)

textdulet = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_dulet)
textdulet.grid(row=4, column=1)

textbeyayenet = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_beyayenet)
textbeyayenet.grid(row=5, column=1)

textatikilt = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_atikilt)
textatikilt.grid(row=6, column=1)

texttegabino = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tegabino)
texttegabino.grid(row=7, column=1)

textdoro = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_doro)
textdoro.grid(row=8, column=1)

# Drinks

pepsi = Checkbutton(drinksFrame, text='pepsi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10
                   , command=pepsi)
pepsi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                    , command=coffee)
coffee.grid(row=1, column=0, sticky=W)

coca = Checkbutton(drinksFrame, text='coca', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                  , command=coca)
coca.grid(row=2, column=0, sticky=W)

fanta = Checkbutton(drinksFrame, text='fanta', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                   , command=fanta)
fanta.grid(row=3, column=0, sticky=W)

mirinda = Checkbutton(drinksFrame, text='mirinda', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14
                     , command=mirinda)
mirinda.grid(row=4, column=0, sticky=W)

walia = Checkbutton(drinksFrame, text='walia', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15
                   , command=walia)
walia.grid(row=5, column=0, sticky=W)

tea = Checkbutton(drinksFrame, text='tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                       variable=var16
                       , command=tea)
tea.grid(row=6, column=0, sticky=W)

milk = Checkbutton(drinksFrame, text='Milk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                       variable=var17
                       , command=milk)
milk.grid(row=7, column=0, sticky=W)

bedele = Checkbutton(drinksFrame, text='bedele', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                    variable=var18
                    , command=bedele)
bedele.grid(row=8, column=0, sticky=W)

# entry fields for drink items

textpepsi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pepsi)
textpepsi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textcoca = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coca)
textcoca.grid(row=2, column=1)

textfanta = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_fanta)
textfanta.grid(row=3, column=1)

textmirinda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mirinda)
textmirinda.grid(row=4, column=1)

textwalia = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_walia)
textwalia.grid(row=5, column=1)

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tea)
texttea.grid(row=6, column=1)

textmilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milk)
textmilk.grid(row=7, column=1)

textbedele = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bedele)
textbedele.grid(row=8, column=1)



# costlabels & entry fields

labelCostofFood = Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'), bg='#42c2f5', fg='white')
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=41)

labelCostofDrinks = Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='#42c2f5', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                        textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=41)



labelSubTotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='#42c2f5', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

labelServiceTax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='#42c2f5', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

labelTotalCost = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='#42c2f5', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                     textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)

# Buttons

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='#42c2f5', bd=3, padx=5,
                    command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='#42c2f5', bd=3, padx=5
                      , command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='#42c2f5', bd=3, padx=5
                   , command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='#42c2f5', bd=3, padx=5,
                   command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='#42c2f5', bd=3, padx=5,
                    command=reset)
buttonReset.grid(row=0, column=4)

# textarea for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

# Calculator
operator = ''  # 7+9


def buttonClick(numbers):  # 9
   global operator
   operator = operator + numbers
   calculatorField.delete(0, END)
   calculatorField.insert(END, operator)


def clear():
   global operator
   operator = ''
   calculatorField.delete(0, END)


def answer():
   global operator
   result = str(eval(operator))
   calculatorField.delete(0, END)
   calculatorField.insert(0, result)
   operator = ''


calculatorField = Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6,
                command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6,
                command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                , command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                   , command=lambda: buttonClick('+'))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                , command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                , command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                , command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                    , command=lambda: buttonClick('-'))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                , command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                , command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                , command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                   , command=lambda: buttonClick('*'))
buttonMult.grid(row=3, column=3)

buttonAns = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6,
                  command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                    , command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6
                , command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='yellow', bg='#42c2f5', bd=6, width=6,
                  command=lambda: buttonClick('/'))
buttonDiv.grid(row=4, column=3)

root.mainloop()

