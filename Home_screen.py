import Create_account, SQL_connector, time

SQL_connector.initials()

time.sleep(1)

print('-'*60)

print(r"""

    |```|  \   /  |```|   |```|   |\   |   || //
    |___|   \ /   |___|   |___|   | \  |   ||//
    |        V    |   |   |   |   |  \ |   ||\\
    |        |    |___|   |   |   |   \|   || \\
      
""")

print('\n',' '*4,'IP Project by Ujjwal Pratap Singh','\n', ' '*10 , 'and Kashish Singh', '\n' + '-'*60)

print(r"""

SELECT AN OPERATION TO PROCEED WITH:

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Make Transactions
6. Show all Transactions
7. Show Personal Transactions    
8. Show All Accounts
9. Search Account
10. DELETE ACCOUNT
11. Exit

""")

operation = int(input('Enter the operation index number to proceed with: '))

match operation:

    case 1:

        Create_account.create()

    case 2:

        SQL_connector.deposit_money()

    case 7:

        SQL_connector.personal_transaction()

    case 9:

        SQL_connector.search_account()

    case 11:

        exit('Program executed')