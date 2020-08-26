c_n={'sam':0000,'jam':11111,'cam':333333}
x=0
while x<5:
    name=input("plz enter your name ( press ENTER to EXIT..): ")
    if name=='':
        break
    if name in c_n:
        print(f'The contact No. of {name} is {c_n[name]}')
    else:
        print('There is no such neme in the phone book')
        decision=input('Do you want to add this name into phone book? type ; yes/no ')
        if decision.lower()=='yes':
            num=int(input(f"enter the number of {name} : "))
            c_n[name]=num
            print('phone book is updated')
            f_q=input('Do you want to keep searching? yes/no')
            if f_q.lower()=='no':
                break
        elif decision.lower()=='no':
            f_q=input('Do you want to keep searching : ? yes/no')
            if f_q.lower()=='no':
                break


    x+=1
