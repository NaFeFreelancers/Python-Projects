import random
d=['A','B','C','D','E','F','G','H','J','1','2','3','4','5','6','7','8','9','0','K','!','@','#','$','%','^','&','*','(',')','_','+','=','-','?','>','<','.','/','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('''\t\t menu
1.generate password
2.exit from program''')
print()
while True:
    ch=int(input('enter your choice'))
    if ch==1:
        i=int(input('enter the length of password you would like to have :'))
        password=''
        for i in range(i):
            password=password+(random.choice(d))
        print()    
        print('the random password generated is :', password)
    elif ch==2:
        print()
        print('exiting from program')
        break
    else:
        print()
        print('please enter a valid input ')
