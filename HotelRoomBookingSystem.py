from tkinter import *
from tkinter import messagebox
import time
import random

#Main Window
win = Tk()
win.geometry('1400x800+0+0')
win.title('Hotel Management System')

tops = Frame(win, width=1600, height=50)
tops.pack(side=TOP)

design1 = Label(win, width=30, height=800, bg='steel blue3')
design1.pack(side=RIGHT)

design2 = Label(win, width=30, height=800, bg='steel blue3')
design2.pack(side=LEFT)

design3 = Label(win, width=1600, height=5, bg='black')
design3.pack(side=BOTTOM)

design4 = Label(win, width=10, height=800, bg='deep sky blue4').pack(side=LEFT)
design5 = Label(win, width=10, height=800, bg='deep sky blue4').pack(side=RIGHT)

lb = Label(tops,font=('arial',50,'bold'), text= 'Frozen Flame',fg='steel blue', bd=10, anchor='w')
lb.grid(column=0, row=0)

operator = ""

#Commands
def reservation(): #Command for reservation 
    reserve = Toplevel(win)
    reserve.geometry('820x450+270+150')
    reserve.title('Reservations')

    design_reserve = Label(reserve, width=5, height=700, bg='steel blue').pack(side=RIGHT)

    lb_reserve = Label(reserve, font=('arial',30,'bold'), text = 'Reservation', fg='steel blue')
    lb_reserve.place(relx=0.38)

    #Name   
    lb_name = Label(reserve, font=('arial',12,'bold'), text = 'Enter Your Name: ', fg='steel blue')
    lb_name.place(rely=0.15)

    name = Entry(reserve, width=40, justify=LEFT)
    name.place(relx=0.2, rely=0.15)

    #Address
    lb_add = Label(reserve, font=('arial',12,'bold'), text = 'Enter Your Address: ', fg='steel blue')
    lb_add.place(rely=0.2)

    add = Entry(reserve, width=90, justify=LEFT)
    add.place(relx=0.2, rely=0.2)

    #Phone number
    lb_ph = Label(reserve, font=('arial',12,'bold'), text = 'Enter Your Phone no: ', fg='steel blue')
    lb_ph.place(rely=0.25)

    ph = Entry(reserve, width=40, justify=LEFT)
    ph.place(relx=0.2,rely=0.25)

    #Total people
    lb_people = Label(reserve, font=('arial',12,'bold'), text = 'Total people: ', fg='steel blue')
    lb_people.place(rely=0.3)

    people = Spinbox(reserve, from_=1, to_=12, width=10)
    people.place(relx=0.2, rely=0.3)

    #Rooms
    lb_room = Label(reserve, font=('arial',12,'bold'), text = 'Room Type: ', fg='steel blue')
    lb_room.place(rely=0.35)
    
    room1 = Radiobutton(reserve, text = 'Single Room - 2200 PNPH',value=1)
    room1.place(relx=0.2, rely=0.35)
    
    room2 = Radiobutton(reserve, text = 'Double Room - 2900 PNPH',value=2)
    room2.place(relx=0.2, rely=0.4)

    room3 = Radiobutton(reserve, text = 'Deluxe Room - 3800 PNPH',value=3)
    room3.place(relx=0.2, rely=0.45)

    room4 = Radiobutton(reserve, text = 'Suite - 3600 PNPH',value=4)
    room4.place(relx=0.2, rely=0.5)

    #Date of arrival (doa)
    lb_doa = Label(reserve, font=('arial',12,'bold'), text = 'Date of arrival: ', fg='steel blue')
    lb_doa.place(rely=0.55)

    lb_date = Label(reserve, font=('arial',12,'bold'), text = 'Date: ', fg='steel blue')
    lb_date.place(relx=0.2,rely=0.55)

    doa_date = Spinbox(reserve, from_=1, to_=31, width=10)
    doa_date.place(relx=0.3, rely=0.55)

    lb_month = Label(reserve, font=('arial',12,'bold'), text = 'Month: ', fg='steel blue')
    lb_month.place(relx=0.2,rely=0.6)
    
    doa_month = Spinbox(reserve, from_=1, to_=12, width=10)
    doa_month.place(relx=0.3, rely=0.6)

    lb_year = Label(reserve, font=('arial',12,'bold'), text = 'Year: ', fg='steel blue')
    lb_year.place(relx=0.2,rely=0.65)
    
    doa_year = Spinbox(reserve, from_=2021, to_=2025, width=10)
    doa_year.place(relx=0.3, rely=0.65)

    #Date of departure (dod)
    lb_dod = Label(reserve, font=('arial',12,'bold'), text = 'Date of Departure: ', fg='steel blue')
    lb_dod.place(relx=0.5,rely=0.55)

    lb_date2 = Label(reserve, font=('arial',12,'bold'), text = 'Date: ', fg='steel blue')
    lb_date2.place(relx=0.7,rely=0.55)

    dod_date2 = Spinbox(reserve, from_=1, to_=31, width=10)
    dod_date2.place(relx=0.8, rely=0.55)

    lb_month2 = Label(reserve, font=('arial',12,'bold'), text = 'Month: ', fg='steel blue')
    lb_month2.place(relx=0.7,rely=0.6)
    
    dod_month2 = Spinbox(reserve, from_=1, to_=12, width=10)
    dod_month2.place(relx=0.8, rely=0.6)

    lb_year2 = Label(reserve, font=('arial',12,'bold'), text = 'Year: ', fg='steel blue')
    lb_year2.place(relx=0.7,rely=0.65)
    
    dod_year2 = Spinbox(reserve, from_=2021, to_=2025, width=10)
    dod_year2.place(relx=0.8, rely=0.65)

    #Time of arrival (toa)
    lb_toa = Label(reserve, font=('arial',12,'bold'), text = 'Time of arrival: ', fg='steel blue')
    lb_toa.place(rely=0.7)

    lb_time = Label(reserve, font=('arial',12,'bold'), text = 'Time: ', fg='steel blue')
    lb_time.place(relx=0.2,rely=0.7)
    
    toa_time = Spinbox(reserve, from_=1, to_=12, width=10)
    toa_time.place(relx=0.3, rely=0.7)

    am = Checkbutton(reserve, text = 'AM')
    am.place(relx=0.4, rely=0.7)

    pm = Checkbutton(reserve, text = 'PM')
    pm.place(relx=0.45, rely=0.7)

    #Confirm button
    global final_exit
    def exit_win(): #Command for pop-up window and exit
        exitwin = Toplevel(win)
        exitwin.geometry('500x90+430+300')
        exitwin.title("Confirm Reservation")
    
        lb_exit = Label(exitwin, font =('arial',12,'bold') ,text = 'Confirm Reservation?')
        lb_exit.pack()
        
        def final_exit():
            reserve.destroy()
            exitwin.destroy()
            time.sleep(2)
            messagebox.showinfo('Reservation Successful','Your room booking has been confirmed and your Reservation Id is '+ str(random.randint(2000,12000))+
                                '. You will need this ID when you check-in. \nAlso bring necessary details like your ID card, Aadhar Card, Passport or any other '
                                'trusted and valid verification proof.')
                                
            time.sleep(1)
            messagebox.showinfo('Advance Payment','You have to pay 30% amount in form of advance. You will receive the amount and payment link on your given '
                                'phone number and if you fail to pay the advance amount within 2 hours, your reservation will get cancelled.')
            
        bt_yes = Button(exitwin, font =('arial',12,'bold'), fg='Green' ,text = 'Yes',command = final_exit)
        bt_yes.place(relx=0.1, rely=0.5, width=70, height=40)
    
        def cancel_exit(): #Command for cancelling the exit
            exitwin.destroy()

        bt_no = Button(exitwin, font =('arial',12,'bold'), fg='Red' ,text = 'No',command = cancel_exit)
        bt_no.place(relx=0.8, rely=0.5, width=70, height=40)
            
    bt_confirm = Button(reserve, font =('arial',12,'bold'),text = 'Confirm Reservation',bg='powder blue',command = exit_win)
    bt_confirm.place(relx=0.4, rely=0.9)
    
def final_exit2(): #Command for exiting the window
    win.destroy()

def exit_win2(): #Command for pop-up window and exit
    exitwin2 = Toplevel(win)
    exitwin2.geometry('500x90+430+300')
    exitwin2.title("Confirm Exit")
    
    lb_exit2 = Label(exitwin2, font =('arial',12,'bold') ,text = 'Confirm cancellation?')
    lb_exit2.pack()
    
    bt_yes2 = Button(exitwin2, font =('arial',12,'bold'), fg='Red' ,text = 'Yes',command = final_exit2)
    bt_yes2.place(relx=0.1, rely=0.5, width=70, height=40)
    
    def cancel_exit2(): #Command for cancelling the exit
        exitwin2.destroy()
        
    bt_no2 = Button(exitwin2, font =('arial',12,'bold'), fg='Green' ,text = 'No',command = cancel_exit2)
    bt_no2.place(relx=0.8, rely=0.5, width=70, height=40)

# SECTION FOR SERVICES
def services(): #Commands for displaying services
    ser_text = ('Frozen Flames is an international 5-Star Hotel located in one of the prime location of Mumbai.'
                '\n\nWe provide 5-Star services like:'
                '\n\n -24-hour reception, room service, valet parking, butler and doorman.'
                '\n -Daily housekeeping that is also available upon request at any time.'
                '\n -Fine dining restaurants and a standalone lounge.'
                '\n -More than 200 available rooms.'
                '\n -Choices of rooms from Single Room to Suite.'
                '\n -World-Class food from some of the best and well known chefs.')
           
    ser = Toplevel(win)
    ser.geometry('500x150+430+300')
    ser.title('Facilities of our hotel')
    
    lb_ser = Label(ser, text = ser_text, bg ='powder blue')
    lb_ser.pack()

#SECTION FOR AMENITIES
def amenities(): #Command for amenities
    amen_text = ('We provide world class amenities in our hotel. We treat our customers like God and try our best to make them happy.'
                 '\nThe following are some amenities which we provide in our Hotel: '
                 '\n -24x7 WiFi and Telephone services in each and every room.'
                 '\n -Air-Conditioned rooms.'
                 '\n -Large Rooms with a Smart TV with all streaming platforms.'
                 '\n -Sound Proof walls so that you can enjoy your privacy.'
                 '\n -Facility for in-room dining.'
                 '\n -Magnificant view of nature from balconies.'
                 '\n -Hygenic and Clean rooms designed to satisfy and comfort you.')
    amen = Toplevel(win)
    amen.geometry('620x140+370+300')
    amen.title('Amenities')

    lb_amen = Label(amen, text = amen_text, bg='powder blue')
    lb_amen.pack()

#SECTION FOR ORDERS
def orders(): #Command for orders
    root = Toplevel()
    root.geometry("1600x800+0+0")
    root.title("RESTAURANT MANAGEMENT SYSTEMS")

    text_Input = StringVar()
    operator = ""

    Tops = Frame(root, width = 1600,height = 50,bg="powder blue", relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root, width = 900,height = 700, relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(root, width = 300,height = 700,bg="powder blue", relief=SUNKEN)
    f2.place(relx=0.68, rely=0.25)

    #======================================Time====================================
    localtime=time.asctime(time.localtime(time.time()))
    #===========================================Info=====================================
    lblInfo = Label(Tops, font=('arial',30, 'bold'),text="Restaurant Management Systems",fg="Steel Blue", bd=10, anchor='w')
    lblInfo.grid(row=0,column=0)
    lblInfo = Label(Tops, font=('arial',10, 'bold'),text=localtime,fg="Steel Blue", bd=10, anchor='w')
    lblInfo.grid(row=1,column=0)

    #=======================================calculator=======================================
    
    def btnClick(numbers): 
        global operator 
        operator = operator + str(numbers)
        text_Input.set(operator)

    def btnClearDisplay():
        global operator
        operator=""
        text_Input.set("")
    
    def btnEqualsInput():
        global operator
        operator=""
        sumup=str(eval(operator))
        text_Input.set(sumup)
        
    def Ref():
        x = random.randint(10908, 50876)
        randomRef = str(x)
        rand = IntVar()
        rand.set(randomRef)

    def qExit():
        root.destroy()

    def Reset():
        softdrinks.set("")
        fries.set("")
        burger.set("")
        nachos.set("")
        pizza.set("")
        pasta.set("")
        tacos.set("")
        hotdogs.set("")
        noodles.set("")
        ordertotal.set("")
        tax.set("")
        nettotal.set("")
        waffles.set("")
        doughnuts.set("")
        icecream.set("")
        pastry.set("")
        sundae.set("")
        softy.set("")
        cldcffe.set("")
        blizzard.set("")
        fruitjuice.set("")

    #Calculator buttons    
    txtDisplay = Entry(f2,font=('arial',10,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
    txtDisplay.grid(columnspan=4)

    btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="7", bg="powder blue", command=lambda:btnClick(7)).grid(row=2,column=0)

    btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="8", bg="powder blue", command=lambda:btnClick(8)).grid(row=2,column=1)

    btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="9", bg="powder blue", command=lambda:btnClick(9)).grid(row=2,column=2)

    Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="+", bg="powder blue", command=lambda:btnClick("+")).grid(row=2,column=3)

    #-------------------------------------------------------------------------------------------------------------------
    btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="4", bg="powder blue", command=lambda:btnClick(4)).grid(row=3,column=0)

    btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="5", bg="powder blue", command=lambda:btnClick(5)).grid(row=3,column=1)

    btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="6", bg="powder blue", command=lambda:btnClick(6)).grid(row=3,column=2)

    Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="-", bg="powder blue", command=lambda:btnClick("-")).grid(row=3,column=3)

    #-------------------------------------------------------------------------------------------------------------------
    btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="1", bg="powder blue", command=lambda:btnClick(1)).grid(row=4,column=0)

    btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="2", bg="powder blue", command=lambda:btnClick(2)).grid(row=4,column=1)

    btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="3", bg="powder blue", command=lambda:btnClick(3)).grid(row=4,column=2)

    Multiplication=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="*", bg="powder blue", command=lambda:btnClick("*")).grid(row=4,column=3)

    #-------------------------------------------------------------------------------------------------------------------
    btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="0", bg="powder blue", command=lambda:btnClick(0)).grid(row=5,column=0)

    btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="C", bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)

    btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="=", bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
                 
    Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',10,'bold'),
            text="/", bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)

    #--------------------------------------Restaurant Info 1--------------------------------------------------------------------------------
    softdrinks= StringVar()
    fries = StringVar()
    burger = StringVar()
    nachos = StringVar()
    pizza = StringVar()
    pasta = StringVar()
    tacos = StringVar()
    hotdogs = StringVar()
    noodles = StringVar()
    ordertotal = StringVar()
    tax = StringVar()
    nettotal = StringVar()

    #Order labels and buttons
    lblsoftdrinks = Label(f1,font=('arial',10,'bold'),text="Softdrinks 100ml",bd=16, anchor='w')
    lblsoftdrinks.grid(row=0,column=0)
    txtsoftdrinks=Entry(f1,font=('arial',10,'bold'),textvariable=softdrinks,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtsoftdrinks.grid(row=0,column=1)

    #Large Cheese Fries
    lblfries = Label(f1,font=('arial',10,'bold'),text="Large Cheese Fries",bd=16, anchor='w')
    lblfries.grid(row=1,column=0)
    txtfries=Entry(f1,font=('arial',10,'bold'),textvariable=fries, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtfries.grid(row=1,column=1)

    #Double Layer Burger
    lblburger = Label(f1,font=('arial',10,'bold'),text="Double Layer Burger",bd=16, anchor='w')
    lblburger.grid(row=2,column=0)
    txtburger=Entry(f1,font=('arial',10,'bold'),textvariable=burger,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtburger.grid(row=2,column=1)

    #Mexican nachos
    lblnachos = Label(f1,font=('arial',10,'bold'),text="Mexican nachos",bd=16, anchor='w')
    lblnachos.grid(row=3,column=0)
    txtnachos=Entry(f1,font=('arial',10,'bold'),textvariable=nachos, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtnachos.grid(row=3,column=1)

    #Pizza
    lblpizza = Label(f1,font=('arial',10,'bold'),text="Pizza",bd=16, anchor='w')
    lblpizza.grid(row=4,column=0)
    txtpizza=Entry(f1,font=('arial',10,'bold'),textvariable=pizza,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtpizza.grid(row=4,column=1)

    #Macaroni Cheese Pasta
    lblpasta = Label(f1,font=('arial',10,'bold'),text="Macaroni Cheese Pasta",bd=16, anchor='w')
    lblpasta.grid(row=5,column=0)
    txtpasta=Entry(f1,font=('arial',10,'bold'),textvariable=pasta, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtpasta.grid(row=5,column=1)

    #Tacos
    lbltacos = Label(f1,font=('arial',10,'bold'),text="Tacos",bd=16, anchor='w')
    lbltacos.grid(row=6,column=0)
    txttacos=Entry(f1,font=('arial',10,'bold'),textvariable=tacos,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txttacos.grid(row=6,column=1)

    #American Hotdogs
    lblhotdogs = Label(f1,font=('arial',10,'bold'),text=" American Hotdogs",bd=16, anchor='w')
    lblhotdogs.grid(row=7,column=0)
    txthotdogs=Entry(f1,font=('arial',10,'bold'),textvariable=hotdogs, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txthotdogs.grid(row=7,column=1)

    #Veg Noodles
    lblnoodles = Label(f1,font=('arial',10,'bold'),text="Veg Noodles",bd=16, anchor='w')
    lblnoodles.grid(row=8,column=0)
    txtnoodles=Entry(f1,font=('arial',10,'bold'),textvariable=noodles,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtnoodles.grid(row=8,column=1)

    #ORDER TOTAL
    lblordertotal = Label(f1,font=('arial',10,'bold'),text="ORDER TOTAL",bd=16, anchor='w')
    lblordertotal.grid(row=9,column=0)
    txtordertotal=Entry(f1,font=('arial',10,'bold'),textvariable=ordertotal, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtordertotal.grid(row=9,column=1)

    #TAX
    lbltax = Label(f1,font=('arial',10,'bold'),text="TAX",bd=16, anchor='w')
    lbltax.grid(row=10,column=0)
    txttax=Entry(f1,font=('arial',10,'bold'),textvariable=tax, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txttax.grid(row=10,column=1)

    #NET TOTAL
    lblnettotal = Label(f1,font=('arial',10,'bold'),text="NET TOTAL",bd=16, anchor='w')
    lblnettotal.grid(row=11,column=0)
    txtnettotal=Entry(f1,font=('arial',10,'bold'),textvariable=nettotal,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtnettotal.grid(row=11,column=1)

    #--------------------------------------Restaurant Info 2--------------------------------------------------------------------------------

    waffles= StringVar()
    doughnuts = StringVar()
    icecream = StringVar()
    pastry = StringVar()
    sundae = StringVar()
    softy = StringVar()
    cldcffe = StringVar()
    blizzard = StringVar()
    fruitjuice = StringVar()

    #Belgian Waffles
    lblwaffles = Label(f1,font=('arial',10,'bold'),text="Belgian Waffles",bd=16, anchor='w')
    lblwaffles.grid(row=0,column=2)
    txtwaffles=Entry(f1,font=('arial',10,'bold'),textvariable=waffles,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtwaffles.grid(row=0,column=3)

    #Chocolate Doughnuts
    lbldoughnuts = Label(f1,font=('arial',10,'bold'),text="Chocolate Doughnuts",bd=16, anchor='w')
    lbldoughnuts.grid(row=1,column=2)
    txtdoughnuts=Entry(f1,font=('arial',10,'bold'),textvariable=doughnuts, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtdoughnuts.grid(row=1,column=3)

    #Butterscotch Icecream
    lblicecream = Label(f1,font=('arial',10,'bold'),text="Butterscotch Icecream",bd=16, anchor='w')
    lblicecream.grid(row=2,column=2)
    txticecream=Entry(f1,font=('arial',10,'bold'),textvariable=icecream,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txticecream.grid(row=2,column=3)

    #Pineapple Pastry
    lblpastry = Label(f1,font=('arial',10,'bold'),text="Pineapple Pastry",bd=16, anchor='w')
    lblpastry.grid(row=3,column=2)
    txtpastry=Entry(f1,font=('arial',10,'bold'),textvariable=pastry, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtpastry.grid(row=3,column=3)

    #Mango Sundae
    lblsundae = Label(f1,font=('arial',10,'bold'),text="Mango Sundae",bd=16, anchor='w')
    lblsundae.grid(row=4,column=2)
    txtsundae=Entry(f1,font=('arial',10,'bold'),textvariable=sundae,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtsundae.grid(row=4,column=3)

    #Choco-Vanilla Softy
    lblsofty = Label(f1,font=('arial',10,'bold'),text="Choco-Vanilla Softy",bd=16, anchor='w')
    lblsofty.grid(row=5,column=2)
    txtsofty=Entry(f1,font=('arial',10,'bold'),textvariable=softy, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtsofty.grid(row=5,column=3)

    #Cold Coffee
    lblcldcffe = Label(f1,font=('arial',10,'bold'),text="Cold Coffee",bd=16, anchor='w')
    lblcldcffe.grid(row=6,column=2)
    txtcldcffe=Entry(f1,font=('arial',10,'bold'),textvariable=cldcffe,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtcldcffe.grid(row=6,column=3)

    #Butterfinger Ice Blizzard
    lblblizzard = Label(f1,font=('arial',10,'bold'),text=" Butterfinger Ice Blizzard",bd=16, anchor='w')
    lblblizzard.grid(row=7,column=2)
    txtblizzard=Entry(f1,font=('arial',10,'bold'),textvariable=blizzard, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtblizzard.grid(row=7,column=3)

    #Orange Fruit Juice
    lblfruitjuice = Label(f1,font=('arial',10,'bold'),text="Orange Fruit Juice",bd=16, anchor='w')
    lblfruitjuice.grid(row=8,column=2)
    txtfruitjuice=Entry(f1,font=('arial',10,'bold'),textvariable=fruitjuice,bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
    txtfruitjuice.grid(row=8,column=3)

    #============================================BUTTONS==================================================

    btnTotal=Button(f1,padx=10,pady=7, bd=7, fg="black", font=('arial',8,'bold'), width=8,
                text="Total", bg="powder blue", command= Ref).place(relx=0.55, rely=0.78)

    btnReset=Button(f1,padx=10,pady=7, bd=7, fg="black", font=('arial',8,'bold'), width=8,
                text="Reset", bg="powder blue", command= Reset).place(relx=0.70, rely=0.78)

    btnExit=Button(f1,padx=10,pady=7, bd=7, fg="black", font=('arial',8,'bold'), width=8,
                text="Exit", bg="powder blue", command= qExit).place(relx=0.85, rely=0.78)
    root.mainloop()


#============================================ COMMANDS DONE ===========================================


#Reservation button
bt1 = Button(win, text='Reservation', font=('arial', 12,'bold'), bg = 'powder blue', command = reservation)
bt1.place(relx=0.5, rely=0.3,width=150, height= 50, anchor= CENTER, bordermode = OUTSIDE)

#Service button
bt2 = Button(win, text='Services', font=('arial', 12,'bold'), bg = 'powder blue', command = services)
bt2.place(relx=0.5, rely=0.38,width=150, height= 50, anchor= CENTER, bordermode = OUTSIDE)

#Amenities of hotel
bt3 = Button(win, text='Amenities', font=('arial', 12,'bold'), bg = 'powder blue',command = amenities)
bt3.place(relx=0.5, rely=0.46,width=150, height= 50, anchor= CENTER, bordermode = OUTSIDE)

#Orders
bt4 = Button(win, text='Orders', font=('arial', 12,'bold'), bg = 'powder blue', command= orders)
bt4.place(relx=0.5, rely=0.54,width=150, height= 50, anchor= CENTER, bordermode = OUTSIDE)

#Exit
bt5 = Button(win, text='Exit', font=('arial', 12,'bold'), bg = 'powder blue', command = exit_win2)
bt5.place(relx=0.5, rely=0.7,width=150, height= 50, anchor= CENTER, bordermode = OUTSIDE)

win.mainloop()
