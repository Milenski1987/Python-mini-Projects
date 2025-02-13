import random
import time


reels_possible_result = ['🍋', '🍇', '🍑', '🍒', '🍓', '🍍']

balance = float(input('Enter your balance: ')) #Enter desired balance into your account.

while balance > 0:
    print(f'Your current balance is: {balance:.2f}')

    time.sleep(1)
    bet = float(input('Place your bet: '))

    while bet > balance:
        print(f'Insufficient balance. Please place a bet within your balance.')

        #Place your bet if you have enough money.
        bet = float(input('Place your bet: '))

    # Computer randomly choose sign for four reels
    reel1 = random.choice(reels_possible_result)
    reel2 = random.choice(reels_possible_result)
    reel3 = random.choice(reels_possible_result)
    reel4 = random.choice(reels_possible_result)

    print (f"\r{reel1}", end = "")
    time.sleep(1)
    print (f"\r{reel1}{reel2}", end = "")
    time.sleep(1)
    print(f"\r{reel1}{reel2}{reel3}", end="")
    time.sleep(1)
    print(f"\r{reel1}{reel2}{reel3}{reel4}", end="")
    time.sleep(1)
    print()

    #Get result and check for win combination
    if reel1 == reel2 == reel3 == reel4:
        print(f'Jackpot! You have won - {bet * 50:.2f}')
        balance += bet * 50

    elif reel1 == reel2 == reel3 or reel2 == reel3 == reel4:
        print(f'You have won the amount of {bet * 10:.2f}')
        balance += bet * 10

    elif reel1 == reel2 or reel2 == reel3 or reel3 == reel4:
        print(f'You have won the amount of {bet * 2:.2f}')
        balance += bet * 2

    else:
        print('Sorry you lost! Try again!')
        balance -= bet

if balance <= 0:
    print(f'Game over! Your final balance is: {balance:.2f}')