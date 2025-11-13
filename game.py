import random
import time

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')

    print_dramatic_text('Welcome ' + name + ' to my geography trivia game!')
    score = 0

    answer = input('Question 1: What is the capital of the United States? ')
    if answer == 'Washington D.C.':
        print_dramatic_text('Correct!')
        score += 1
    else:
        print_dramatic_text('Dead wrong!')

    answer = input('What is the largest ocean in the world? ')
    if answer == 'Pacific Ocean' :
        print_dramatic_text('Yippee!!')
        score += 1
    else:
        print_dramatic_text ('Nope!')

    # TODO add more questions!

    print_dramatic_text('Congratulations ' + name + ' you scored ' + str(score) + '!')
