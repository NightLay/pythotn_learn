
import time



health = 100
exp = 0
food_suply = 50
energy = 10

def hunting():
    global exp, food_suply, energy, health

    time.sleep(5)
    health -= 10
    exp += 50
    food_suply += 25
    energy -= 20
    print("хорошо поохотились!")


def slepping():
    global exp, food_suply, energy, health

    time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 10
    energy += 60
    print("хорошо поспали!")




def eating():
    global exp, food_suply, energy, health

    time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 25
    energy += 100
    print("хорошо поспали!")



while True:
    print("----- список действий -----")
    print("1. охотиться")
    print("2. спать" )
    print("3. есть" )

    action = input("напишите номер действия ")
    action = int(action)
    print("---------------------------")

    if action == 1 and energy >= 20:
        hunting()
        print("---------------")
        print("здоровье: " + str(health))
        print("энергия: " + str(energy))
        print("опыт: " + str(exp))
        print("запас еды: " + str(food_suply))
        print("---------------")
    elif action == 2:
        slepping()
    elif action == 3:
        eating()
    else:
        print("слишком мало энергии. нужно её восстановить.")
    
