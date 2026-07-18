import mysql.connector as sqlconn
import pandas as pd

conn = sqlconn.connect( user='root',password='Engineer',host='localhost' )

cur = conn.cursor()

def initials():

    cur.execute('CREATE DATABASE IF NOT EXISTS Banking_IP;')
    cur.execute('USE Banking_IP;')

    cur.execute('''
        
        CREATE TABLE IF NOT EXISTS Accounts(

            Account_no INT Primary Key,
            Name VARCHAR(50),
            PIN INT,
            Balance DECIMAL(10,2)
                
        );
        
    ''')

    cur.execute('''
        
        CREATE TABLE IF NOT EXISTS Transactions(

            Tid INT Primary Key,
            TfromAccount INT,
            TFrom VARCHAR(50),
            Tto VARCHAR(50),
            Ttype VARCHAR(15),
            Amount DECIMAL(10,2),
            Tdate Date,
            Ttime TIME
                
        );
        
    ''')

def count_records(table_name):

    cur.execute('USE Banking_IP;')
    cur.execute('SELECT COUNT(*) FROM ' + str(table_name) + ';')

    output = cur.fetchone()[0]

    return int(output)

def insert_record(table_name,data):

    cur.execute('USE Banking_IP;')

    query = "INSERT INTO " + str(table_name) + " VALUES ( " + '%s, '*(len(data)-1) + "%s );"

    cur.execute(query,data)

    conn.commit()

def get_fullTable(Table_name):

    cur.execute('USE Banking_IP;')
    
    cur.execute('SELECT * FROM ' + str(Table_name) + ';')

    output = cur.fetchall

    return output()

def search_account():

    name = ''

    while name == '':

        name = str(input('Enter your PyBank account name: '))

        if name == '':

            print('\n','Please Enter your PyBank account name to search your account','\n')

    cur.execute('SELECT * FROM accounts WHERE Name=%s;',(name,))

    output = cur.fetchall()

    if len(output) == 0:

        print('\n','Sorry No PyBank Account Found with the name', name, '\n')
    
    elif len(output) == 1:

        print('-'*50,'\n')

        print('Your Account Found with details:', '\n')
        print('Account_No:', output[0][0])
        print('Name:', output[0][1])
        print('PIN:', output[0][2])
        print('Balance:', output[0][3])

        print('\n', 'Thanks !', '\n' + '-'*50)

    elif len(output) > 1:

        check_account_no = str(input('Do you remember your Account Number ? '))

        if check_account_no.lower() == 'yes':

            account_no = int(input('Enter your PyBank account number: '))

            cur.execute('SELECT * FROM accounts WHERE Name=%s and Account_no=%s;',(name,account_no) )

            output = cur.fetchall()

            if len(output) == 0:

                print('\n','Sorry No PyBank Account Found with the Account number', account_no, 'and name', name,'\n')

            elif len(output) == 1:

                print('-'*50,'\n')

                print('Your Account Found with details:', '\n')
                print('Account_No:', output[0][0])
                print('Name:', output[0][1])
                print('PIN:', output[0][2])
                print('Balance:', output[0][3])

                print('\n', 'Thanks !', '\n' + '-'*50)

            else:

                print('\n','Sorry we cannot help you in this case....','\n')

        else:

            check_pin = str(input('Do you remember your PIN ? '))

            if check_pin.lower() == 'yes':

                pin = int(input('Please enter your PyBank account PIN: '))

                cur.execute('SELECT * FROM accounts WHERE Name=%s and PIN=%s;',(name,pin))

                output = cur.fetchall()

                if len(output) == 0:

                    print('\n','Sorry No PyBank Account Found with the PIN', pin, 'and name', name,'\n')

                elif len(output) == 1:

                    print('-'*50,'\n')

                    print('Your Account Found with details:', '\n')
                    print('Account_No:', output[0][0])
                    print('Name:', output[0][1])
                    print('PIN:', output[0][2])
                    print('Balance:', output[0][3])

                    print('\n', 'Thanks !', '\n' + '-'*50)

                else:

                    print('\n','Sorry we cannot help you in this case....','\n')

            else:

                print('\n','Sorry we cannot help you in this case...', '\n')

    else:

        print('\n','Sorry, an Error occured...','\n')

def deposit_money():

    name = str(input('Enter your PyBank account name: '))

    cur.execute('SELECT * FROM accounts WHERE Name=%s;',(name,))

    output = cur.fetchall()

    if len(output) == 0:

        print('\n', 'No PyBank account found with the name', name, '\n')
    
    elif len(output) > 0:

        pin = int(input('Enter your PIN: '))

        cur.execute('SELECT * FROM accounts WHERE Name=%s and PIN=%s;',(name,pin))

        output = cur.fetchall()

        if len(output) == 0:

            print('\n', 'No PyBank account found with the Name:', name, 'and', 'PIN:', pin)

        elif len(output) == 1:

            amount = round(float(input('How much money you want to deposit: ')),2)

            cur.execute('UPDATE accounts SET Balance=Balance+%s WHERE Name=%s and PIN=%s;',(amount,name,pin))

            total_transactions = count_records('Transactions')

            cur.execute('SELECT DATE(NOW());')

            date = cur.fetchone()[0]

            cur.execute('SELECT TIME(NOW());')

            time = cur.fetchone()[0]

            data = ((total_transactions+1),int(output[0][0]),name,None,'Deposit',amount,date,time)

            insert_record('Transactions',data)

            print(('\n' + '-'*60),'\n',amount, 'has been deposited into your account')

            print( '\n' + 'Transaction', (total_transactions + 1), 'has been made by depositing', amount )
            print('to account', output[0][0], 'with name', name, 'on', date, 'at', time, '\n' + '-'*60)

        else:

            print('\n','Duplicate Accounts found with same PIN and same name...', '\n')

    else:

        print('\n','Sorry an error occured from our side...', '\n')

def personal_transaction():

    name = str(input('Enter your PyBank Account name: '))
    pin = int(input('Enter your PyBank account PIN: '))

    cur.execute('SELECT * FROM Accounts WHERE Name = %s and PIN = %s;', (name,pin))

    output = cur.fetchall()

    if len(output) == 0:

        print('No such account with these details found !!')

    elif len(output) == 1:

        account_id = output[0][0]

        cur.execute('SELECT * FROM Transactions WHERE TFrom=%s and TfromAccount=%s;', (name,account_id))

        output = cur.fetchall()

        if len(output) == 0:

            print('No Transactions from this account had been made yet !!')

        else:

            new_output = [row[1:] for row in output]

            data = pd.DataFrame(new_output, index=[row[0] for row in output], columns=[

                'Account ID', 'FROM', 'TO', 'Transaction Type', 'Amount', 'Date', 'Time'

            ])

            print('\n', '-'*60, '\n', data)

    else:

        print('Sorry ! Found 2 similar accounts with same name and PIN... :(')