import random
import time
deck=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
deck2={'A':11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10}
dl_deck=[]  
pl_deck=[]
b=0
tmp=0
choice='y'
class player(object):
    def name(self,n):
        self.n=n
    def amount(self,amount):
        self.amount=amount
    def inc_amount(self,inc):
        self.amount+=inc
    def dec_amount(self,dec):
        self.amount-=dec
        if(self.amount<0):
            self.amount=0
    def money(self):
        return self.amount
    def get_name(self):
        return self.n
class dealer(object):
    def amount(self,amount):
        self.amount=amount
    def inc_amount(self,inc):
        self.amount+=inc
    def dec_amount(self,dec):
        self.amount-=dec
        if(self.amount<0):
            self.amount=0
    def money(self):
        return self.amount
def title():
    print('||===============================================================================================================||')
    print('||   ___                  __                   _      _        ______________   __            ______   _      _  ||')
    print('||  |   \    _           /  \         _____    |     /                |        /  \          /         |     /   ||')
    print('||  |    |   |          /    \       /         |    /                 |       /    \        /          |    /    ||')
    print('||  |    |   |         /      \     /          |   /                  |      /      \      /           |   /     ||')
    print('||  |___/    |        /________\   |           |  /                   |     /________\    |            |  /      ||')
    print('||  |   \    |       |          |  |           |_/     =====          |    |          |   |            |_/       ||')
    print('||  |    |   |       |          |  |           | \                    |    |          |   |            | \       ||')
    print('||  |    |   |       |          |   \          |  \                   |    |          |    \           |  \      ||')
    print('||  |___/    |_____| |          |    \_____    |   \         \       /     |          |     \          |   \     ||')
    print('||                                             |    \/        \_____/      |          |      \______   |    \/   ||')
    print('||                                                                                                               ||')
    print('||===============================================================================================================||')

def p_menu():
    print('Select your move:')
    print('1. Hit')
    print('2. Stand')
    ch=int(input('Your Selection: '))
    return ch
def dealer_deck(deck):
    print("Dealer's deck:")
    time.sleep(2)
    print(' ______',)
    print('|      |') 
    print('| ',deck[0],'  |')
    print('|      |')
    print('|______|')
    print(' ______',)
    print('|      |') 
    print('| ',' ','  |')
    print('|      |')
    print('|______|')
def player_deck(deck1,p_name):
    print("{}'s deck:".format(p_name))
    time.sleep(2)
    print(' ______',)
    print('|      |') 
    print('| ',deck1[0],'  |')
    print('|      |')
    print('|______|')
    
    for i in range(1,len(deck1)):
        print(' ______',)
        print('|      |') 
        print('| ',deck1[i],'  |')
        print('|      |')
        print('|______|')
    
    a=total(deck1)
    print("{}'s total= {}".format(p_name,a))

def dealer_deck2(deck1):
    print("Dealer's deck:")
    time.sleep(2)                
    print(' ______',)
    print('|      |') 
    print('| ',deck1[0],'  |')
    print('|      |')
    print('|______|')
    for i in range(1,len(deck1)):
        print(' ______',)
        print('|      |') 
        print('| ',deck1[i],'  |')
        print('|      |')
        print('|______|')
    a=total(deck1)
    print("Dealer's total=",a)

def total(deck3):
    tot=0
    for i in deck3:
       tot=tot+deck2[i]
       
    if(tot==21):
        return tot
    if(tot<21):
        return tot
    if(tot>21 and ('A' not in deck3)):
        return tot
    if(tot>21 and ('A' in deck3)):
        
        for i in deck3:
            if(i=='A'):
                tot-=11
                tot+=1
            if(tot<21 or tot==21):
                break
        return tot        
def result(deck):   
    net=total(deck) 
    if(net>21):
        return 0
    elif(net==21):
        return 1
    else:
        return net
title()
print('\n\n')
print('!!!Welcome to the game of BlackJack!!!')
print('This game comprises of a Player and a Dealer')
print("Press enter key to continue the game...")
input()
p=player()  
p_name=input("Enter Player's name: ")
p.name(p_name)
print("Player's name added successfully")
d=dealer()
p.amount(100)
d.amount(100)
time.sleep(2)
print('\n')
while(choice=='y' or choice=='Y'):        
    print("Dealer's inital amount is ${}".format(d.money()))
    print("{}'s initial amount is ${}".format(p_name,p.money()))
    while(True):
        b=int(input("\nEnter {}'s bet amount: $".format(p_name)))
        time.sleep(2)
        if(b>p.money()):
            print('\nRetry again....')
            continue
        elif(b>d.money()):
            print('\nRetry again....')
            continue
        else:
            p.dec_amount(b)
            print("\n{}'s money left now is ${}".format(p_name,p.money()))
            break
    print('\n')
    for i in range(2):
        dl_deck.append(deck[random.randint(0,12)])
    for i in range(2):
        pl_deck.append(deck[random.randint(0,12)])
    print('Press enter key to continue the game.....') 
    input()
    print('Please Wait....')
    time.sleep(1)
    print('Shuffling Cards...')
    time.sleep(3)
    print('Distributing cards...')    
    dealer_deck(dl_deck)
    player_deck(pl_deck,p_name)
    res=-1
    while(True):   
        ch=p_menu()
        if(ch==1):
            pl_deck.append(deck[random.randint(0,12)])
            time.sleep(1)
            player_deck(pl_deck,p_name)
            res=result(pl_deck)
            if(res==0 or res==1):
                break
            else:
                continue
        elif(ch==2):
            res=result(pl_deck)
            break
                       
        else:
            time.sleep(1)
            print('\nInvalid selection!!!')
            print('Try again....')
            continue
    while(True):
        res1=result(dl_deck)
        if(res1==0 or res1==1 or res==1 or res==0):
            break
        if(res1>res):
            break
        if(res==res1):
            break
        dl_deck.append(deck[random.randint(0,12)])
        
    if((res==1 and res!=res1) or (res>res1 and res1!=1 and res!=0) or res1==0):
            p.inc_amount(b+b)
            a=p.money()
            g=p.get_name()
            dealer_deck2(dl_deck)
            print('\nGame is finished....')
            print('Hit enter key to generate the results...')
            input()
            if(res==1):
                time.sleep(1)
                print('$$$ BLACKJACK FOR {} $$$'.format(g))
            if(res1==0):
                time.sleep(1)
                print('!!! DEALER BUSTED !!!')
            time.sleep(2)
            print('\nCongratulations to {}...'.format(g))
            print('{} wins the game....'.format(g))
            time.sleep(2)
            print("\n{}'s amount is now ${}".format(g,a))
            d.dec_amount(b)
            a=d.money()
            print("Dealer's amount is now ${}".format(a))
    elif(res==0 or (res1==1 and res1!=res) or (res1>res and res1!=1 and res!=0)):
        d.inc_amount(b)
        a=p.money()
        g=p.get_name()
        dealer_deck2(dl_deck)
        print('\nGame is finished....')
        print('Hit enter key to generate the results...')
        input()
        if(res1==1):
            time.sleep(2)
            print('$$$ BLACKJACK FOR DEALER $$$')
        if(res==0):
            time.sleep(2)
            print('!!! {} BUSTED !!!'.format(g))
        time.sleep(2)
        print('\nCongratulations to Dealer...')
        print('Dealer wins the game....')
        time.sleep(2)
        print("\n{}'s amount is now ${}".format(g,a))
        a=d.money()
        print("Dealer's amount is now ${}".format(a))
    else:
        dealer_deck2(dl_deck)
        time.sleep(3)
        print('\nGame is finished....')
        print('Hit enter key to generate the results...')
        input()
        print('!!!PUSH!!!')
        time.sleep(2)
        print('\nThe match is Draw')
        p.inc_amount(b)
        g=p.get_name()
        a=p.money()
        time.sleep(2)
        print("\n{}'s amount is now ${}".format(g,a)) 
    while(True):
        print('\n\nWant to play the game again? (y/n)')
        choice=input('Your choice: ')
        if(choice=='y' or choice=='Y'):
            break
        elif(choice=='n' or choice=='N'):
            time.sleep(1)
            print('\n.......GAME OVER.......')
            time.sleep(2)
            break
        else:
            print("Invalid choice!!!")
            print('Retry Again....')
            continue
    pm=p.money()
    dm=d.money()
    choice1='n'
    if(choice=='y' or choice=='Y'):
        if(pm==0 or pm<0): 
            print('\n{} is out of money...'.format(p.get_name()))
            while(True):        
                print('\nWant to spin the money wheel to get some money?(y/n)')
                choice1=input('Your choice: ')
                if(choice1=='y' or choice1=='Y'):
                    p.inc_amount(random.randrange(50,500,50))
                    print('\nSpinning the money wheel....')
                    time.sleep(1)
                    print('\nSpinning of wheel done successfully....')
                    time.sleep(2)
                    pl_deck.clear()
                    dl_deck.clear()
                    break
                elif(choice1=='n' or choice1=='N'):
                    break
                else:
                    print('Invalid choice....')
                    print('Retry again.....')
                    continue
        elif(dm==0 or dm<0):
            print('\nDealer is out of money')
            time.sleep(1)
            print('\nReviving Dealer\'s money....')
            print('\nPlease Wait....')
            time.sleep(2)
            d.inc_amount(100)
            pl_deck.clear()
            dl_deck.clear()
            continue
        else:
            pl_deck.clear()
            dl_deck.clear()
            continue
    else:
        print('\nThank you for playing the game.......')
        print('See you next time....')
        print('Alvida...')
        break
    if(choice1=='n' or choice1=='N'):
        time.sleep(1)
        print('\n.......GAME OVER.......')
        time.sleep(2)
        break
    print('\n{}\'s money after spinning the wheel becomes ${}\n'.format(p.get_name(),p.money()))
time.sleep(1) 
print('\n\n\n')
print('Game Credits:-')
print('\n')
print('Coded and Designed by: Anurag Dev')
print('Regerences: Wikipedia')
print('Programmng Language used: Python 3')
input()


    
    
        

    
    



   
        
