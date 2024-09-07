# map_bank_project
INTRODUCTION TO THE PROJECT:
The project aim is to build a GUI based interactive bank named “TTM BANK”

ABOUT THE BANK:
On starting the program, we go to main menu wherein we can create a new 
account in the bank or we can login with pre existing account in the bank or 
we can delete our pre existing account .
In this menu ,the data is stored into tables in MYSQL using python’s MYSQL 
Connector. This data consists of details of account holder like account no. , 
aadhar no. , phone no. etc. This is the part where everything related to 
account holder is used. After accessing login with your account no. and 
password if we have entered correct id and password you get a message box 
showing that your id and password is correct otherwise it will show incorrect 
after entering correct values you will be on next page where there will be four 
option ‘update personal data’, ’transactions’ ,’deposit’ and ‘go back’. After 
accessing ‘update personal data’ we go to next window where we can update 
only required fields. After accessing ‘transaction’ we get 3 option ‘bank 
statement’ and ‘send money’ and ‘go back’ In ‘bank statement’ we get to 
know user’s account no. , name , money sent, money received , 
balance(amount left).
In ‘send money’ we can transfer money from user’s account to another user 
account of the same bank. After accessing ‘deposit’ we can deposit money 
into our account. After using ‘go back’ in every window we go to previous 
window. After accessing ‘create account’ we can create a new account by 
filling details like name , date of birth , address , aadhar id , phone no. , the 
setting your own password and rechecking it by filling password in ‘confirm 
password’ after writing details properly new account id created which will be 
saved in tables in MYSQL

After accessing ‘ delete account ‘ we can delete account by entering few 
details ,all the details will also be deleted by the table. After using ‘go back’ in 
every window we go to previous window.
