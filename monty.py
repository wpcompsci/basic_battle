import random

while True:
    
    stick = 0
    switch = 0
    counter = 0
    choices = "abc"

    users_value = input("How many times would you like to run the loop? ")

    while counter < int(users_value):
        counter = counter + 1
        correct = random.choice(choices)
        choice = random.choice(choices)

        if choice == correct:
            stick = stick + 1
        else:
            switch = switch + 1

    print(f"\nIn {users_value} tries,")
    print(f"Stiking won {stick} times,")
    print(f"Switching won {switch} times.")
