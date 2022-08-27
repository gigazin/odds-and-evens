from random import randint
user_number = computer_number = user_option_choose = user_option = computer_option_choose = computer_option = 0
wins_count = draws_count = 0
print('=-=' * 10)
print(' ' * 8 + ' Even or Odd ')
print('=-=' * 10)
while True:
    computer_number = randint(0, 10)
    computer_option_choose = randint(0, 1)
    if computer_option_choose == 0:
        computer_option = 'even'
    else:
        computer_option = 'odd'
    user_number = int(input('Enter a number between 0 and 9: '))
    while user_number < 0 or user_number > 9:
        print('ERROR: Value out of range.')
        user_number = int(input('Enter a number between 0 and 9: '))
    user_option_choose = str(input('Enter your option (E for Even, O for Odd): ')).strip().upper()
    while user_option_choose != 'E' and user_option_choose != 'O':
        print('ERROR: Wrong option.')
        user_option_choose = str(input('Enter your option (E for Even, O for Odd): ')).strip().upper()
    if user_option_choose == 'E':
        user_option = 'even'
    else:
        user_option = 'odd'
    print(f'Player has chosen {user_option} and played {user_number}.')
    print(f'Computer has chosen {computer_option} and played {computer_number}.')
    if user_number + computer_number % 2 == 0:
        print(f'{user_number} + {computer_number} equals {user_number + computer_number} and the value is even!')
    elif user_number + computer_number % 2 != 0:
        print(f'{user_number} + {computer_number} equals {user_number + computer_number} and the value is odd!')
    if user_number + computer_number % 2 == 0 and user_option_choose == 'O':
        break
    elif user_number + computer_number % 2 != 0 and user_option_choose == 'E':
        break
    elif user_number + computer_number % 2 == 0 and user_option_choose == 'E':
        wins_count += 1
        print('Congratulations, you won this time!')
    elif user_number + computer_number % 2 != 0 and user_option_choose == 'O':
        wins_count += 1
        print('Congratulations, you won this time!')
    elif user_number + computer_number % 2 == 0 and user_option_choose == computer_option_choose:
        draws_count += 1
        print("It's a draw!")
    elif user_number + computer_number % 2 != 0 and user_option_choose == computer_option_choose:
        draws_count += 1
        print("It's a draw!")
print('Game over, you lose!')
print(f'You won {wins_count} time(s) and the game had a total of {draws_count} draw(s)!')
