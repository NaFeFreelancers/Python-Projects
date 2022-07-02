while True:   
    a=int(input('enter your atm pin'))
    b=str(a)
    guess='1234567890'
    pin=''
    
    for i in range(len(b)):
        for j in guess:
            if b[i]==j:
                pin+=j   
    print(''' warning ! your atm pin has been cracked 
    ATM PIN :  ''', pin)
