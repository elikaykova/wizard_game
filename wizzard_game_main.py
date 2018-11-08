import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header();
    game_loop();

def print_header():
    print('-----------------------')
    print('     Wizard Game')
    print('-----------------------')
    print('\n')

def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, False),
        Wizard('Evil Wizard', 100)]
    hero = Wizard('Hero', random.randint(0, 100))

    while True:
        active_creature = random.choice(creatures)
        print("A {} of level {} has appear from the dark... "
            .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? Or you want to e[x]it? ')
        if cmd == 'a' :
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard needs to recover. The wizard runs and hides... ')
                time.sleep(5)
                print('The wizard returns revitalized! ')

        elif cmd == 'r' :
            print('The wizard')
        elif cmd == 'l' :
            print('The wizard takes a look and sees... ')
            for creature in creatures:
                print(' * A {} of level {} * '.format(creature.name, creature.level))
        elif cmd == 'x' :
            print("It's sad to see you go. Bye ;( ...")
            break
        else :
            print('Unknown command. Try again.')

        if not creatures:
            print("CONGRATULATIONS!!! You've won the GAME!!!")
            break


if __name__ == '__main__':
    main()
