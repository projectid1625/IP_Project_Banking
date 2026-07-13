import SQL_connector, time

def create():

    print('\n' + '-'*50)

    name = ''

    while name == '':

        name = str(input('Enter your new account name: '))

        if name == '':

            print('\n','Please Enter your name...', '\n')
    
    balance = float(input('Enter balance of this account: '))

    Pin = int(input('Create your own PIN for your bank account: '))

    Account_No = SQL_connector.count_records('accounts') + 1

    balance = round(balance,2)

    SQL_connector.insert_record('accounts',(Account_No,name.capitalize(),Pin,balance))

    print('-'*50)

    print(str(name.capitalize()) + ", Your Account number is", Account_No)
    print('Do not share your PIN with someone else, its personal...')
    print('Thank You for creating account in PyBank')

    print('-'*50, '\n')
    
    time.sleep(1)

    print('Account created Successfully !!','\n')