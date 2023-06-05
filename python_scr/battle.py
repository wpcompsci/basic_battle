import random
import time

pikachu_hp = 100
bulbasaur_hp = 100

print('A pikachu and bulbasaur meet on the field! \nIt\'s time to battle!')
time.sleep(1)

# LOOP
while True:
    # GET PLAYER 1 ATTACK
    print('Pikachu attacks. \n')
    time.sleep(1)
    print('Pick your attack:')
    print('a) Thunderbolt')
    print('b) Volt Tackle')
    p1_attack = input('-->')

    time.sleep(2)
    # DO DAMAGE TO PLAYER 2
    if p1_attack == 'a':
        damage = random.randint(0, 20)
        bulbasaur_hp = bulbasaur_hp - damage
        print(f'\nPikachu hits bulbasaur for {damage} damage.')
    elif p1_attack == 'b':
        damage = random.randint(5, 15)
        bulbasaur_hp = bulbasaur_hp - damage
        print(f'\nPikachu hits bulbasaur for {damage} damage.')
    else:
        print('\nPikachu misses.')

    # CHECK IF PLAYER 2 HAS FAINTED
    if bulbasaur_hp <= 0:
        time.sleep(2)
        print('\n\nBulbasaur has fainted. \nPikachu wins!')
        break

        # GET PLAYER 2 ATTACK
        print('Bulbasaur attacks. \n')
        time.sleep(1)
        print('Pick your attack:')
        print('a) Water Jet')
        print('b) Water Blast')
        p1_attack = input('-->')

        time.sleep(2)
        # DO DAMAGE TO PLAYER 1
        if p2_attack == 'a':
            damage = random.randint(0, 20)
            pikachu_hp = pikachu_hp - damage
            print(f'\nBulbasaur hits pikachu for {damage} damage.')
        elif p1_attack == 'b':
            damage = random.randint(5, 15)
            bulbasaur_hp = bulbasaur_hp - damage
            print(f'\nBulbasaur hits pikachu for {damage} damage.')
        else:
            print('\nBulbasaur misses.')

        # CHECK IF PLAYER 1 HAS FAINTED
        if pikachu_hp <= 0:
            time.sleep(2)
            print('\n\nPikachu has fainted. \nBulbasaur wins!')
            break

# END
