print('\t\t ROCK PAPER SCISSOR')
print(''' are you ready to beat the three time world champion "THE COMPUTER " in a game of rock paper scissor.... 
\t\tINSTRUCTIONS 
1.Enter your name 
2.Input your desired choice ie "rock paper or scissor" 
3.Enter invalid input and you loose
4.The first to get 10 points win ''')
import random
print()
name=input('enter your name : ')
print()
print(name, ', are you ready to test your luck ??')
l=['rock','paper','scissor']
computer=0
user=0

while computer<10 or user<10:
    ch=input('enter rock paper or scissor : ')
    l2=random.shuffle(l)
    if ch.lower()==l[0].lower():
        print('same input .... no points given to each ')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='rock'and l[0].lower()=='scissor':
        computer=computer+1
        print('computer gained +1 point')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='paper'and l[0].lower()=='scissor':
        user=user+1
        print('user gained +1 point ')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='rock'and l[0].lower()=='paper':
        user=user+1
        print('you have gained +1 point')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='paper'and l[0].lower()=='rock':
        computer=computer+1
        print('comupter have gained +1 point')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='scissor'and l[0].lower()=='paper':
        computer=computer+1
        print('comupter have gained +1 point')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    elif ch.lower()=='scissor'and l[0].lower()=='rock':
        user=user+1
        print('you have gained +1 point')
        print()
        print('current points are:')
        print('user :',user)
        print('computer:',computer)
    else:
        print('invalid input... you loose ')
        print('better luck next time ')
        print()
        break
    if computer==10 or user==10:
        print('final score is :')
        print()
        from tabulate import tabulate
        a=[['computer',computer],[name,user]]
        print(tabulate(a,headers=['name','score'],tablefmt='pretty'))
        if computer==10:
            print('you loose!!')
            print('better luck next time')
        else:
            print('new world champion is',name)
        break
    print()






    
        








