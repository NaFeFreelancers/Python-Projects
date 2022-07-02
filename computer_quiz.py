from tabulate import tabulate
print('\t\tAre you ready to become the millionaire??')
print()
print('\t\t INSTRUCTIONS')
print('1.This quiz contains 15 questions and with each correct answers you will be given a sum of money')
print('2.If you answer any question wrong you will be terminated and you will recieve no cash prize ')
print('3.you are free to quit in any stage of the game and the money that you have accumulated will be rewarded')
print('4.you have 20 seconds to answer each question')
print('5.spelling mistakes while typing will be considered as wrong answer .')
print('6.Please dont enter spacebar after any answer')
print('7.The prize distribution is given below:')
print()
a = [[1,1000],[2,2000],[3,6000],[4,12000],[5,25000],[6,50000],[7,100000],[8,300000],[9,600000],[10,1200000],[11,2400000],[12,4000000],[13,6000000],[14,7500000],[15,10000000]]
print(tabulate(a,headers=['question number','prize money'],tablefmt='pretty'))
name=input('enter your name : ')
print()
global total 
correct=0
total=0
while True:
    ch=input('do you want to play or not (yes/no)?  ')
    if ch=='yes':
        q1=input('question_1. what is the full form of TCP?  ')
        if q1.lower()=='transmission control protocol':
            print('ohh hoo ... correct answer ... you have won 1000 rs')
            total=1000
            print('your total prize money is :',total)
            print()
        else:
            print('you have given the wrong ans... you have lost all your prize...')
            total=0
            print()
            break
        key=input('do you want to continue (yes/no)?  ')
        print()
        if key=='yes':
            q2=input('question_2. what is the full form of SMTP?  ')
            if q2.lower()=='simple mail transfer protocol':
                print('ohh hoo ... correct answer ... you have won 2000 rs')
                total=2000
                print('your total prize money is :',total)
                print()
            else:
                print('you have given the wrong ans... you have lost all your prize...')
                total=0
                print()
                break
            key=input('do you want to continue(yes/no)??  ')
            if key=='yes':
                q3=input('question_3. what is the full form of URL?  ')        
                if q3.lower()=='uniform resource locator':
                    print('ohh hoo.. you have given the correct answer... you have won 6000rs')
                    total=6000
                    print('your total prize money is :',total)
                    print()
                else:
                    print('you have given the wrong answer... all your price money is lost...')
                    total=0
                    print()
                    break
                key=input('do you want to continue(yes/no  ')
                print()
                if key=='yes':
                    q4=input('what is the network device that is used to amplify the signal of data transmitted ?  ')
                    if q4.lower()=='repeater':
                        print('correct answer ...you have won 12000 rs')
                        total =12000
                        print('your total prize money is :',total)
                        print()
                    else:
                        print('you have given the wrong answer... you have lost all your prize money')
                        total=0
                        print()
                        break
                    key=input('do you wish to continue(yes/no)?  ')
                    print()
                    if key=='yes':
                        q5=input('what is the full form of XML? ')
                        if q5.lower()=='extensible markup language':
                            print('ohh hoo ... you have given the right answer... you have won 25000 rs')
                            total=25000
                            print('you total prize money is :',total)
                            print()
                        else:
                            print('you have given the wrong aswer... all your prize money is lost')
                            total=0
                            print()
                            break
                        key=input('do you want to continue or not (yes/no) ')
                        print()
                        if key=='yes':
                            q6=input('___________ is considered as unintelligent device?  ( hub/switch)? ')
                            if q6.lower()=='hub':
                                print('your answer is correct .... you have won 50000 rs')
                                total=50000
                                print('your total earning is :',total)
                                print()
                            else:
                                print('you have given the wrong answer .. you have lost all your money')
                                total=0
                                print()
                                break
                            key=input('do you want to continue(yes/no) ')
                            if key=='yes':
                                q7=input('what is full form of dbms? ')
                                if q7.lower()=='database management system':
                                    print('you have given the correct answer.... you have won 100000 rs')
                                    total=100000
                                    print('your total prize money is : ',total)
                                    print()
                                else:
                                    print('you have given the wrong answer... you have lost all your money')
                                    total=0
                                    print()
                                    break
                            key=input('do you want to continue playing (yes/no) ')
                            print()
                            if key=='yes':
                                q8=input('stack works on the principle of _______(abbreviation only required) ')
                                if q8.lower()=='lifo':
                                    print('you have given the correct answer.... you have won 300000rs')
                                    total=300000
                                    print('your total prize money is :',total)
                                    print()
                                else:
                                    print('you have given the wrong answer... you have lost all your prize money')
                                    total=0
                                    print()
                                    break
                                key=input('do you want to continue playing(yes/no) ')
                                print()
                                if key=='yes':
                                    q9=input('In a stack pushing and popping of elements take place from one end _________  ')
                                    if q9.lower()=='top':
                                        print('you have given the right answer...you have won 600000 rs'   )
                                        total=600000
                                        print('your total prize money is : ',total)   
                                        print()                    
                                    else:
                                        print('you have given the wrong answer... you have lost all your money..')
                                        total=0
                                        print()
                                        break
                                    key=input('do you want to continue(yes/no)  ')
                                    print()
                                    if key=='yes':
                                        q10=input('Queue works on the principle of ____________(only abbreviation required)  ')
                                        if q10.lower()=='fifo':
                                            print('you have given the right answer... you have won 1200000 rs')
                                            total=1200000
                                            print('your total money is :',total)
                                            print()
                                        else:
                                            print('you have given the wrong answer... you have lost all your money')
                                            total=0
                                            print()
                                            break
                                        key=input('do you want to continue(yes/no)  ')
                                        print()
                                        if key=='yes':
                                            q11=input('___________ function is used to display the topmost element of the stack?  ')
                                            if q11.lower()=='peek':
                                                print('you have given the right answer... you have won 2500000 rs')
                                                total=2500000
                                                print('your total prize money is ',total)
                                                print()
                                            else:
                                                print('you have given the wrong answer... you have lost all your prize money')
                                                total=0
                                                print()
                                                break
                                            key=input('do you want to continue(yes/no)  ')
                                            print()
                                            if key=='yes':
                                                q12=input('IP address is provided by whom? (abbreviation only)  ')
                                                if q12.lower()=='isp':
                                                    print('you have given the right answer... you have won 4000000 rs')
                                                    total=4000000
                                                    print('your total prize money is ',total)
                                                    print()
                                                else:
                                                    print('you have given the wrong answer... you have lost all your prize money')
                                                    total=0
                                                    print()
                                                    break
                                                key=input('do you want to continue(yes/no)  ')
                                                print()
                                                if key=='yes':
                                                    q13=input('Another name for workstation?  ')
                                                    if q13.lower()=='node':
                                                        print('you have given the right answer... you have won 6000000 rs')
                                                        total=6000000
                                                        print('your total prize money is ',total)
                                                        print()
                                                    else:
                                                        print('you have given the wrong answer... you have lost all your prize money')
                                                        total=0
                                                        print()
                                                        break
                                                    key=input('do you want to continue(yes/no)  ')
                                                    print()
                                                    if key=='yes':
                                                        q14=input('short range unguided media?  ')
                                                        if q14.lower()=='infrared':
                                                            print('you have given the right answer... you have won 7500000 rs')
                                                            total=7500000
                                                            print('your total prize money is ',total)
                                                            print()
                                                        else:
                                                            print('you have given the wrong answer... you have lost all your prize money')
                                                            total=0
                                                            print()
                                                            break
                                                        key=input('do you want to continue(yes/no)  ')
                                                        print()
                                                        if key=='yes':
                                                            q15=input('fastest guided transmission media?  ')
                                                            if q15.lower()=='optic fibre':
                                                                print('you have given the right answer... you have won 10000000 rs')
                                                                total=10000000
                                                                print('your total prize money is ',total)
                                                                print('you have become a millionaire....')
                                                                print()
                                                                break
                                                            else:
                                                                print('you have given the wrong answer... you have lost all your prize money')
                                                                total=0
                                                                print()
                                                                break
                                                        else:
                                                            print('you have decided to quit ... your prize money will not be affected')
                                                            print()
                                                            break
                                                    else:
                                                        print('you have decided to quit ...  your prize money will not be affected')
                                                        print()
                                                        break
                                                else:
                                                    print('you have decided to quit ... your prize money will not be lost ')
                                                    print()
                                                    break
                                            else:
                                                print('you have decided to quit .... ur price money will not be affected ')
                                                print()
                                                break     
                                        else:
                                            print('you have decided to quit ... your money will not be lost')
                                            print()
                                            break   
                                    else:
                                        print('you have decided to quit ... your money will not be lost...')
                                        print()
                                        break
                                else:
                                    print('you have decided to quit...your prize money will not be affected..')
                                    print()
                                    break         
                            else:
                                print('you have decided to quit ... your prize money is unaffected')
                                print()
                                break                  
                        else:
                            print('you have decided to quit .... your prize money will remain unaffected')
                            print()
                            break  
                    else:
                        print('you have decided to quit .... ur price money is not affected ')
                        print()
                        break
                else:
                    print('you have decided to quit ... your prize money will not be affected')
                    print()
                    break
            else:
                print('you have decided to quit... your prize money will not be affected')
                print()
                break
        else:
            print('you have decided to quit ...')
            print('your prize remains unaffected')
            print()
            break
    else:
        print('you have decided to quit .... ur prize money will not be affeced ')
        print()
        break
d=[[name,total]]
print()
print("you have won:")
print(tabulate(d,headers=['name','prize money'],tablefmt='pretty'))


        
    
