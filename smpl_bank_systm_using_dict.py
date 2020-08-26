# Banking System:

bank_user = {'sajjad':10000, 'nafiul': 120000, 'zahan': 150000}
print('Welcome to this banking system : ')
while True:
    desc = int(input(f'What do you like to do ?\n'
                     f'  press 1 for view balance\n'
                     f'  press 2 for view all bank info\n'
                     f'  press 3 for update balance\n'
                     f'  press 4 for create account\n'
                     f'  press 5 for Exit ..\n   '))
    if desc==1:
        name = input(f'Enter your user name : ')
        if name in bank_user.keys():
            print(f'{name} Your Current balance is {bank_user[name]} TK only.')
            desc = input(f'Would You like to exit ? \n'
                         f'type yes or no : \n')
            if desc.lower() == 'yes':
                break

        else:
            desc = input(f'user name don\'t exist in  banking system database...\n'
                         f'Would You like to add this user to the account ?\n'
                         f'type Yes or No..\n  ')
            if desc.lower()=='yes':
                x=input(f'Enter Username : \n  ')
                y=int(input(f'Enter Balance:   \n'))
                bank_user.update({x:y})
                print(bank_user)
                print(f'Account has been Created ! \n'
                      f'{x} your account balance is {bank_user[x]} Tk only\n\n\n')
                desc = input(f'Would You like to exit ? \n'
                             f'type yes or no : \n')
                if desc.lower() == 'yes':
                    break
            else:
                desc=input(f'Would You like to exit ? \n'
                           f'type yes or no : \n')
                if desc.lower()=='yes':
                    break
    elif desc==2:
        for x,y in bank_user.items():
            print(f'Name : {x},  Balance : {y} Tk only.\n')
    elif desc==3:
        name=input(f'Enter your name: \n  ')
        if name in bank_user.keys():
            desc=input(f'If want to Add Tk with balance Type add\n'
                       f'And if want to subtract Tk form balance type sub \n  ')
            if desc.lower()=='add':
                extra = int(input("Enter The Amount ,want to add: \n  "))
                bank_user[name]= bank_user[name] + extra
                print(f'Balance is updated ! \n'
                      f'your banlance is now: {bank_user[name]}')

            elif desc.lower()=='sub':
                extra = int(input("Enter The Amount ,want to subtract : \n  "))
                bank_user[name]= bank_user[name] - extra
                print(f'Balance is updated ! \n'
                      f'your banlance is now: {bank_user[name]}')
            else:
                desc = input(f'Would You like to exit ? \n'
                             f'type yes or no: \n')
                if desc.lower() == 'yes':
                    break

        else:
            print(f'user name don\'t exist in banking system database..\n'
                  f'please create an accaount first..\n')

    elif desc==4:
        name=input('Enter name : \n')
        balance = int(input('Enter balance : \n '))
        bank_user[name]=balance
        print(f'Account has been Created ! \n'
              f'{name} your account balance is { bank_user[name] } Tk only\n\n\n')
        desc = input(f'Would You like to exit ? \n'
                     f'type yes or no : \n')
        if desc.lower() == 'yes':
            break

    else:
        break




