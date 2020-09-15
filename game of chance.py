import random

money = 100

#Write your game of chance functions here
#coin_flip
def coin_flip(guess, bet):
#cheaking balance and validity
    if bet == 0:
        print("Bet mustn't be Zero")
        return 0
    if bet > money:
        print("Insifficient Balance")
        return 0
    if (guess != "Head") and (guess != "Tails"):
        print("Guess must be Head or Tails")
        return 0
#cheaking guess result
    num = random.randint(1, 2)
    if (guess == "Head") and (num == 1):
        print("Your guess is " + guess + " Hurrah! You WIN. your won amount $%d" %bet)
        return bet
    elif (guess == "Tails") and (num == 2):
        print("Your guess is " + guess + " Hurrah! You WIN. your won amount $%d" %bet)
        return bet
    else:
        if (guess == "Head") and not(num == 1):
            print("Sorry you lose")
        else:
            print("Sorry you lose")
        return -bet
    
#cllaing function 
money += coin_flip("Head", 20)
print("Your total amount of money " + str(money))
money += coin_flip("Tails", 30)
print("Your total amount of money " + str(money))
money += coin_flip("Head", 50)
print("Your total amount of money " + str(money))

import random
money = 100
#chohan
def chohan(guess, bet):
#cheaking balance and validity
    if (bet < 0):
        print("Insufficent Balace")
        return 0
    if bet > money:
        print("Maximum bet amount" + str(money))
        return 0
    if (guess != "Even") and (guess != "Odd"):
        print("you must chose form EVEN or ODD")
        return 0
#cheaking guess and result
    dic1 = random.randint(1, 6)
    dic2 = random.randint(1, 6)
    result = dic1 + dic2
    mod_result = result % 2
    if (guess == "Even") and (result % 2 == 0):
        print("The dice roll were " + str(dic1) + " and " + str(dic2) + " It's a Even" )
        print("You win!")
        return bet
    elif(guess == "Odd") and (result % 2 != 0):
        print("The dice roll were " + str(dic1) + " and " + str(dic2) + " It's a Odd")
        print("you win!")
        return bet
    else:
        if (guess == "Even") and (mod_result != 0):
            print("your choice is Even and your result is " + str(result) + " Odd! wrong guess")
        else:
            print("your choice is Odd and your result is " + str(result) + " Even! wrong guess")
        return -bet
#calling function
money += chohan("Odd", 30)
print("Your total amount of money " + str(money))
money += chohan("Odd", 30)
print("Your total amount of money " + str(money))

import random
money = 100
def card(guess, bet):
#cheaking balance
    if bet <= 0 and bet > money:
        print("Insufficiant balance")
        return 0
#cheakng guess and result
    main = random.randint(1, 10)
    their = random.randint(1, 10)
    print("Main choice " + str(main))
    print("Their choice " + str(their))
    if main == their:
        print("It's a tie")
        return 0
    if main > their:
        print("You Win!")
        return bet
    if their > main:
        print("You loss")
        return -bet
#calling the function    
money += card(5, 40)
print("Your total amount of money " + str(money))

import random
money = 100

def rulette(guess, bet):
#cheaking guess and ber
    if bet < 0 and bet > money:       
        print("insufficient balance")
    print("Let's play rolette game ")
    result = random.randint(0, 37)
    if result == 37:
        print("The while landed on 00 ")
    else:
        print("The while landed on " + str(result))
    if guess == "Even" and result % 2 == 0 and result != 0:
        print("Your guess is " + str(guess) + " you Won! " + str(bet) + "$")
        return bet
    elif guess == "Odd" and result % 2 == 1 and result != 37:
        print("Your guess is " + str(guess) + " you Won! " + str(bet) + "$")
        return bet
    elif guess == result:
        print("You win!" + str(bet*35) + "$")
        return bet*35
    else:
        print("You lose " + str(-bet) + "$")
        return -bet
    
#calling function
money += rulette("Even", 20)
money += rulette("Odd", 30)
              