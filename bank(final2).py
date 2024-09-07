from logging import log
from tkinter import * 
import mysql.connector as con
from tkinter import messagebox
from datetime import *
mycon=con.connect(host="localhost",user="root",password="sood@mysql",
database="project")
def dashboard():
 dashboard_w = Tk()
 dashboard_w.state('zoomed')
 dashboard_w.geometry("1500x1250")
 dashboard_w.title("TTM Bank")
 lb1 = Label(dashboard_w,text = "DASHBOARD", font = ("Comic Sans MS",34),padx=5,pady=5,borderwidth=10,relief='ridge')
 lb1.pack(pady = 40)
 btn1 = Button(dashboard_w, text = "Update Personal Data", width=18, pady = 20,font=('Comic Sans MS bold',22),borderwidth=5,command=update)
 btn1.pack(pady=10)
 btn2 = Button(dashboard_w, text = "Transactions", width=18, pady = 20,font=('Comic Sans MS bold',22),borderwidth=5,command=transaction)
 btn2.pack(pady=10)

 
 btn3 = Button(dashboard_w, text = "Deposit", width=18, pady = 20,font=('Comic Sans MS bold',22),borderwidth=5,command=deposite)
 btn3.pack(pady=10)
 btn4 = Button(dashboard_w, text = "Go Back",bg="red", width=18, pady = 20,font=('Comic Sans MS bold',22),borderwidth=5,command=dashboard_w.destroy)
 btn4.pack(pady=10)
def login():
 login_window=Tk()
 login_window.state('zoomed')
 login_window.geometry("1500x1250")
 login_window.title("LOGIN")
 lb1=Label(login_window,text='ACCOUNT LOGIN',font = ("Comic Sans MS bold",40),padx=20,pady=10,borderwidth=3,relief='solid')
 
 lb1.place(x=500,y=40)
 
 lb2=Label(login_window, text = "ENTER NAME:", font = ("Comic Sans MS bold",20),padx=5,pady=5,width=20,bg='red')
 
 lb2.place(x=300,y=250)
 lb3=Label(login_window, text = "ENTER PASSWORD:", font = ("Comic Sans MS bold",20),padx=5,pady=5,width=20,bg='red')
 
 lb3.place(x=300,y=400)

 #TEXT BOX
 t1=Entry(login_window,width=22,font = ("Comic Sans MS bold",20),highlightthickness=4)
 t1.place(y=250,x=800)
 t2=Entry(login_window,width=22,font = ("Comic Sans MS bold",20),highlightthickness=4,show='*')
 t2.place(y=400,x=800)
 
 def mapb():
     u_name=t1.get()
 p_word=t2.get()
 cur = mycon.cursor()
 cur.execute("select name,password,account_no from password")
 l=cur.fetchall()
 flag=False
 for i in l:
     if i[0]==u_name and i[1]==p_word:
         flag=True
         global account_number
         account_number=i[2]
         break
 if flag==True:
     messagebox.showinfo(title='login status',message="You ave logged in",parent=login_window)
     login_window.destroy()
     dashboard()
 else:
     messagebox.showerror(title='login status',message="Password/Username Incorrect",parent=login_window)
 
 btn1=Button(login_window,text='LOGIN',bg="green",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,command=mapb)
 btn1.place(y=550,x=420)
 btn2=Button(login_window,text='GO BACK',bg="red",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,command=login_window.destroy)
 btn2.place(y=550,x=840)
 
 login_window.mainloop()
 
def update():
    update = Tk() 
    update.state('zoomed')
    update.geometry("1500x1250")
    update.title("TTM Bank")
    lbl1=Label( update,text = "ONLY FILL THE FIELDS THAT YOU WANT TO UPDATE", height="2",font=('bold',20))
    lbl1.grid(column=0,row=0,padx=10)
    lbl3 = Label( update,text = "Enter Your New Name : " ,width="30", height="2",font=(15))
    lbl3.grid(column= 0, row =1)
    ent1 = Entry(update, width="30")
    ent1.grid(column=1,row=1)

 
    lbl4 = Label( update ,text = "Enter Your New Date of Birth(YYYY-MM-DD) : ",height="2", font =(15))
    lbl4.grid(column= 0, row =2,padx=10)
 
    ent2 = Entry(update, width="30")
    ent2.grid(column=1,row=2)
 
    lbl5 = Label( update ,text = "Enter Your New Address : " ,width="30", height="2", font =(15))
    lbl5.grid(column= 0, row =3)
 
    ent3 = Entry(update, width="30")
    ent3.grid(column=1,row=3)
 
    lbl6 = Label( update ,text = "Enter Your New Aadhar Number : " ,width="30", height="2", font =(15))
    lbl6.grid(column= 0, row =4)
 
    ent4 = Entry(update, width="30")
    ent4.grid(column=1,row=4)
 
    lbl7 = Label( update ,text = "Enter Your New Phone Number : " ,width="30", height="2", font =(15))
    lbl7.grid(column= 0, row =5)
 
    ent5 = Entry(update, width="30")
    ent5.grid(column=1,row=5)
def update_work():
    u_name=ent1.get()

    dob=ent2.get()
    address=ent3.get()
    aadhar=ent4.get()
    ph_no=ent5.get()
    cur = mycon.cursor()
 
    if u_name!='':
         cur.execute("update DETAILS set name='{}' where account_no='{}'".format(u_name,account_number))
         cur.execute("update password set name='{}' where account_no='{}'".format(u_name,account_number))
         cur.execute("update transaction set name='{}' where account_no='{}'".format(u_name,account_number))
         mycon.commit()
    if dob!='':
         cur.execute("update DETAILS set dob='{}' where account_no='{}'".format(dob,account_number))
         mycon.commit()
    if address!='':
         cur.execute("update DETAILS set address='{}' where account_no='{}'".format(address,account_number))
         mycon.commit()
    if aadhar!='':
         cur.execute("update DETAILS set aadhar_no='{}' where account_no='{}'".format(aadhar,account_number))
         mycon.commit() 
    if ph_no!='':

         cur.execute("update DETAILS set phone_no='{}' where account_no='{}'".format(ph_no,account_number))
         mycon.commit()
    messagebox.showinfo(title='Update Status',message='Data Updated',parent=update)
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
 
    btn1=Button(update,text="UPDATE",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,command= update_work)
    btn1.grid(row=6, column = 3)
    btn5=Button(update,text="GO BACK",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,bg="red",command=update.destroy)
    btn5.grid(row=6, column = 4)
def loan():
    loan = Tk()
    loan.state('zoomed')
    loan.geometry("1500x1250")
    loan.title(" TTM Bank")
    lbl3 = Label( loan,text = "Name" ,width="30", height="2",font=(15))
    lbl3.grid(column= 0, row =2)
    ent1 = Entry(loan, width="30")

    ent1.grid(column=1,row=2)
    lbl4 = Label( loan ,text = "Account No",width="30", height="2", font =(15))
    lbl4.grid(column= 0, row =3)
    ent2 = Entry(loan, width="30")
    ent2.grid(column=1,row=3)
    lbl5 = Label( loan ,text = "Address" ,width="30", height="2", font =(15))
    lbl5.grid(column= 0, row =4)
    ent3 = Entry(loan, width="30")
    ent3.grid(column=1,row=4)
    lbl6 = Label( loan ,text = "DOB" ,width="30", height="2", font =(15))
    lbl6.grid(column= 0, row =5)
    ent4 = Entry(loan, width="30")
    ent4.grid(column=1,row=5)
    lbl7 = Label( loan ,text = "Salary" ,width="30", height="2", font =(15))
    lbl7.grid(column= 0, row =6)
    lbl8 = Label( loan ,text="Amount" ,width="30", height="2", font =(15))
    lbl8.grid(column= 0, row =7)
    ent5 = Entry(loan, width="30")
    ent5.grid(column=1,row=6)
    ent4 = Entry(loan, width="30")
    ent4.grid(column=1,row=7)
 
def accepted():
     messagebox.showinfo(title='loan status',message="request accepted",parent=loan)
     loan.destroy()
     dashboard()
 
     btn1=Button(loan,text="Request for Loan", height="2", width="20" , font =(10),command=accepted)
     btn1.grid(row=8, column = 3)

     btn5=Button(loan,text="GO BACK", height="2", width="20",bg="red", font =(10), command=loan.destroy)
     btn5.grid(row=8, column = 5)
 
     lbl1 = Label( loan,text = "Fill The Following Form", width="30", height="2",font=(15))
     lbl1.grid(coloumn=3, row=1)
 
 
def send():
    send = Tk() 
    send.state('zoomed')
    send.geometry("1500x1250")
    send.title(" TTM Bank")
    lbl3 = Label( send,text = "Receiver's Account No" ,width="30", height="2",font=(15))
    lbl3.grid(column= 0, row =1)
    ent1 = Entry(send, width="30")
    ent1.grid(column=1,row=1)
    lbl4 = Label( send ,text = "Receiver's Name" ,width="30", height="2", font =(15))
    lbl4.grid(column= 0, row =2)
    ent2 = Entry(send, width="30")
    ent2.grid(column=1,row=2)
    lb = Label( send,text = "Sender's Account No" ,width="30", height="2",font=(15))
    lb.grid(column= 0, row =3)
    ent = Entry(send, width="30")
    ent.grid(column=1,row=3)

    lbl5 = Label( send ,text = "Amount" ,width="30", height="2", font =(15))
    lbl5.grid(column= 0, row =4)
    ent3 = Entry(send, width="30")
    ent3.grid(column=1,row=4)
 
def send_work():
     reciever_acc_no=ent1.get()
     amount=ent3.get()
     sender_acc_no=ent.get()
 
     cur = mycon.cursor()
     cur.execute("update DETAILS set BALANCE=BALANCE+{} where ACCOUNT_NO={}".format(amount,reciever_acc_no))
     cur.execute("update TRANSACTION set BALANCE=BALANCE+{},MONEY_RECEIVED=MONEY_RECEIVED+{} where ACCOUNT_NO={}".format(amount,amount,reciever_acc_no))
     cur.execute("update DETAILS set BALANCE=BALANCE-{} where ACCOUNT_NO={}".format(amount,sender_acc_no))
     cur.execute("update TRANSACTION set BALANCE=BALANCE-{},MONEY_SENT=MONEY_SENT+{} whereACCOUNT_NO={}".format(amount,amount,sender_acc_no))
     mycon.commit()
     messagebox.showinfo(title='money status',message="Money sent",parent=send)
     send.destroy()
     dashboard()
 
     btn1=Button(send,text="SEND", height="2", width="20" , font =('Comic Sans MS bold',14),command=send_work)
     btn1.grid(row=6, column = 3)
     btn5=Button(send,text="GO BACK", height="2", width="20",bg="red",font =('Comic Sans MS bold',14),command=send.destroy)
     btn5.grid(row=6, column = 4)
def delete():
     delete = Tk()
     delete.state('zoomed')
     delete.geometry("1500x1250")
     delete.title(" TTM Bank")
     lb1=Label(delete,text='ACCOUNT DELETE',font = ("Comic Sans MS bold",40),padx=20,pady=10,borderwidth=3,relief='solid')
 
     lb1.place(x=500,y=40)
 
     lb2=Label(delete, text = "ENTER NAME:", font = ("Comic Sans MS bold",20),padx=5,pady=5,width=20,bg='red')
 
     lb2.place(x=300,y=250)
     lb3=Label(delete, text = "ENTER PASSWORD:", font = ("Comic Sans MS bold",20),padx=5,pady=5,width=20,bg='red')
 
     lb3.place(x=300,y=400)
 
     t1=Entry(delete,width=22,font = ("Comic Sans MS bold",20),highlightthickness=4)
     t1.place(y=250,x=800)
     t2=Entry(delete,width=22,font = ("Comic Sans MS bold",20),highlightthickness=4,show='*')

     t2.place(y=400,x=800)
 
def mapd():
     u_name=t1.get()
     p_word=t2.get()
     cur = mycon.cursor()
     cur.execute("select name,password,account_no from password")
     l=cur.fetchall()
     flag=False
     for i in l:
         if i[0]==u_name and i[1]==p_word:
             flag=True
             global account_number
             account_number=i[2]
             break
         if flag==True:
             cur = mycon.cursor()
             cur.execute("delete from DETAILS where name='{}'".format(u_name))
             cur.execute("delete from PASSWORD where name='{}'".format(u_name))
             cur.execute("delete from TRANSACTION where name='{}'".format(u_name))
             mycon.commit()
             messagebox.showinfo(title='ldeletion status',message="Account deleted",parent=delete)
             delete.destroy()
             dashboard()
         else:
             messagebox.showerror(title='deletion status',message="Password/Username Incorrect",parent=delete)

             btn1=Button(delete,text='DELETE',bg="green",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,command=mapd)
             btn1.place(y=550,x=420)
             btn2=Button(delete,text='GO BACK',bg="red",font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3,command=delete.destroy)
             btn2.place(y=550,x=840)
 
             delete.mainloop()
 
def deposite():
 deposite = Tk()
 deposite.state('zoomed')
 deposite.geometry("1500x1250")
 deposite.title(" TTM Bank")
 lbl3 = Label( deposite,text = "AMOUNT: " ,width="30", height="2",font=(20))
 lbl3.grid(column= 0, row =1)
 amount = Entry(deposite, width="30")
 amount.grid(column=1,row=1)
def deposite_work():
 
 cur = mycon.cursor()
 amt=amount.get()

 cur.execute("update DETAILS set BALANCE=BALANCE+{} where account_no='{}'".format(amt,account_number))
 cur.execute("update TRANSACTION set BALANCE=BALANCE+{} where account_no='{}'".format(amt,account_number))
 mycon.commit()
 messagebox.showinfo(title='Deposit Status',message="Money Deposited",parent=deposite)
 deposite.destroy()
 dashboard()
 
 btn1=Button(deposite,text="DEPOSITE", height="2", width="20" , font =('Comic Sans MS bold',14),command=deposite_work)
 btn1.grid(row=6, column = 3)
 btn5=Button(deposite,text="GO BACK", height="2", width="20",bg="red", font =('Comic Sans MS bold',14),command=deposite.destroy)
 btn5.grid(row=6, column = 4)
 
def statement():
 statement = Tk()
 statement.state('zoomed')
 statement.geometry("1500x1250")
 statement.title("TTM Bank")
 cur = mycon.cursor()
 cur.execute("select * from TRANSACTION where ACCOUNT_NO={}".format(account_number))
 for l in cur:
     lb = Label(statement,text="BANK STATEMENT",width="50",height="2",font=(20))
     lb.grid(column=0,row=3)
     lb1 = Label(statement,text="S.no: "+str(l[0]),width="50",height="2",font=(20))
     lb1.grid(column=0,row=4)
     lb2 = Label(statement,text="Name: "+str(l[1]),width="50",height="2",font=(20))
     lb2.grid(column=0,row=5)
     lb3= Label(statement,text="Account Number: "+str(l[2]),width="50",height="2",font=(20))
     lb3.grid(column=0,row=6)
     lb4 = Label(statement,text="Money Sent: "+str(l[4]),width="50",height="2",font=(20))
     lb4.grid(column=0,row=7)
     lb5 = Label(statement,text="Money Received: "+str(l[5]),width="50",height="2",font=(20))
     lb5.grid(column=0,row=8)
     lb6 = Label(statement,text="Balance: "+str(l[6]),width="50",height="2",font=(20))
     lb6.grid(column=0,row=9)
 
     btn2= Button(statement,text="GO BACK", height="2", width="20",bg="red", font =('Comic Sans MS bold',14),command=statement.destroy)
     btn2.grid(column=1,row=10)
def transaction():
    transaction = Tk()
    transaction.state('zoomed')
    transaction.geometry("1500x1250")
    transaction.title("TTM Bank")
    lbl1 = Label(transaction,text="Choose One Of The Following", width="30", height="2", font=('bold',25))
    lbl1.grid(column= 10, row = 0)
    btn1= Button(transaction,text="Bank Statement",height="2", width="20" , font =('Comic Sans MS bold',14),command= statement)
    btn1.grid(row=8, column = 9)
    btn2= Button(transaction,text="Send Money",height="2", width="20" , font =('Comic Sans MS bold',14), command= send)
    btn2.grid(row=8, column = 11)
    btn3= Button(transaction,text="GO BACK", height="2", width="20",bg="red", font =('Comic Sans MS bold',14),command=transaction.destroy)
    btn3.grid(column=10,row=9)
def create_acc():
    create_acc = Tk()
    create_acc.state('zoomed') 
    create_acc.geometry("1500x1250")
    create_acc.title("TTM BANK")
def create_submit():
    name=ent1.get()
    dob=ent2.get()
    address=ent3.get()
    aadhar=ent4.get()
    ph_no=ent5.get()
    pwd=ent6.get()
    con_pwd=ent7.get()
    if len(ph_no)!=10:
        messagebox.showerror(title='Account Status',message='Phone Number Can Only Be 10 Digits Long',parent=create_acc)
    else:
        if len(aadhar)!=12:
            messagebox.showerror(title='Account Status',message='Aadhar Number Can Only Be 12 Digits Long',parent=create_acc)
        else:
 
            cur=mycon.cursor()
            cur.execute('select max(sno) from password')
 
            serial_no=cur.fetchone()[0]+1
            current_date=date.today().strftime('%Y-%m-%d')
    if pwd==con_pwd:
        cur.execute("insert into details values({},'{}','{}','{}','{}',{},{},{})".format(serial_no,name,str(serial_no),address,dob,aadhar,ph_no,0))
        cur.execute("insert into PASSWORD values({},'{}','{}','{}')".format(serial_no,name,str(serial_no),pwd))
        cur.execute("insert into TRANSACTION values({},'{}',{},'{}',{},{},{})".format(serial_no,name,str(serial_no),current_date,0,0,0))
        mycon.commit()
        messagebox.showinfo(title='Account Status',message='Account Created Successfully',parent=create_acc)
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        ent7.delete(0,END)
    else:
        messagebox.showerror(title='Account Status',message='Password does not match',parent=create_acc)
        lbl1=Label(create_acc,text='WELCOME TO TTM BANK',font = ("Comic Sans MS",30),padx=20,pady=10,borderwidth=3,relief='solid')
        lbl1.place(x=500,y=40)
        lbl2=Label(create_acc,text='Enter your name:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl2.place(x=350,y=150)
        lbl3=Label(create_acc,text='Enter your date of birth:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl3.place(x=350,y=190)
        lbl4=Label(create_acc,text='Enter your Address:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl4.place(x=350,y=230)
        lbl5=Label(create_acc,text='Enter your Aadhar ID:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl5.place(x=350,y=270)
        lbl6=Label(create_acc,text='Enter your Phone Number:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl6.place(x=350,y=310)
        lbl7=Label(create_acc,text='Set a password: \n(8 characters)',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl7.place(x=350,y=350)
        lbl8=Label(create_acc,text='Confirm Password:',font = ("Comic Sans MS bold",15),padx=20,pady=10)
        lbl8.place(x=350,y=390)
        ent1 = Entry(create_acc, width="30")
        ent1.place(x=750,y=170)
        ent2 = Entry(create_acc, width="30")
        ent2.place(x=750,y=210)
        ent3 = Entry(create_acc, width="30")
        ent3.place(x=750,y=250)
        ent4 = Entry(create_acc, width="30")
        ent4.place(x=750,y=290)
 
        ent5 = Entry(create_acc, width="30")
        ent5.place(x=750,y=330)
        ent6 = Entry(create_acc, width="30",show='*')
        ent6.place(x=750,y=370)
        ent7 = Entry(create_acc, width="30",show='*')
        ent7.place(x=750,y=410)
 
        btn1=Button(create_acc,text='Create Account',font = ("Comic Sans MS bold",20),width=15,pady=5,borderwidth=3,command=create_submit)
        btn1.place(y=550,x=420)
        btn1=Button(create_acc,text='Go Back',bg="red",font = ("Comic Sans MS bold",20),width=15,pady=5,borderwidth=3,command=create_acc.destroy)
        btn1.place(y=550,x=760)
mainscreen = Tk()
mainscreen.state('zoomed')
mainscreen.geometry("1500x1250")
mainscreen.title(" TTM Bank")
P= PhotoImage(file='bank b1.png')
w=Label(mainscreen , image=P)
w.place(x=0,y=0)
lb1 = Label(mainscreen,text = "WELCOME TO TTM BANK", font = ("Comic Sans MS",34),padx=5,pady=5,borderwidth=10,relief='ridge')
lb1.pack(pady = 80)
btn1 = Button(mainscreen, text = "LOGIN", width=18, pady = 20,font=('Comic Sans MS',22),borderwidth=5,command=login)
btn1.pack(pady=10)
btn2 = Button(mainscreen, text = "CREATE ACCOUNT", width=18, pady = 20,font=('Comic Sans MS',22),borderwidth=5,command=create_acc)
btn2.pack(pady=10)
btn4 = Button(mainscreen, text = "DELETE ACCOUNT", width=18, pady = 20,font=('Comic Sans MS',22),borderwidth=5,command=delete)
btn4.pack(pady=10)
btn3 = Button(mainscreen, text = "EXIT", width=18, pady = 20,font=('Comic Sans MS',22),borderwidth=5,command=mainscreen.destroy)
btn3.pack(pady=10)
mainscreen.mainloop()
