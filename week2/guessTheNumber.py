import random

random_number = random.randint(1, 10)

print(random_number)

user_input = int(input('guess the random number: '))

def guess_inputed_num(guess_num, rand_num):
    if (guess_num == rand_num):
        print('you guess the right number!')
    else:
        if(guess_num > rand_num):
            print('number is big')
        else:
            print('number is smaller')



guess_inputed_num(user_input, random_number);