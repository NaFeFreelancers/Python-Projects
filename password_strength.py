print('\t\tSee how strong your password is ??')
print()
print('''1.password must be atleast 8 characters long
2.It must contain letters,special characters and numbers
3.use of blank space is not allowed ''')
print()
correct=0
print()
print('1.enter password')
print('2.display entered password with strength')
print()

while True:
    ch=int(input('enter your choice'))
    if ch==1:
        upper=0
        lower=0
        digit=0
        special=0
        total_upper=0
        total_lower=0
        total_digit=0
        total_special=0
        accept=0
        password=input('enter the password')
        if len(password)<8:
            print('length of password less than 8 ... please enter a stronger password')
            print()
            
        else:
            for i in password:
                if i.isupper():
                    upper=1
                    total_upper+=1
                if i.islower():
                    lower=1
                    total_lower+=1
                if i.isdigit():
                    digit=1
                    total_digit+=1
                if i in '@#$%^&*()_=+<>?,./;:[]{}\|':
                    special=1
                    total_special+=1
                if i.isspace():
                    print('please enter password again as blank spaces are not allowed')
                    break
            if upper==1 and lower==1 and digit==1 and special==1:
                accept=1
                print('password accepted')
                print()
                k=password
            else:
                print('your password has been declined as it lacks basic requirements')
                print()
                accept=0
    elif ch==2:
        if accept==1:
            print('your accepted password is :',k)
            print()
            if total_upper>2 and total_lower>2 and total_special>2 and total_digit>2:
                print('your password is very strong')
                print()
            else:
                print('your password is moderately strong')
                print()
        else:
            print('your password was declined .. please try again with valid password')
            print()

        
