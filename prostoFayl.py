
import time



health = 100
exp = 0
food_suply = 50
energy = 50

notes = []


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



def writing():
    print("----------------")
    print()
    w = len(notes)
    we = w +1
    we = str(we)
    w = str(w)
    for i in notes:
        print(w, ")", i)
    print()
    print("----------------")
    zametka = input('введите заметку # '+ we)
    notes.append(zametka)
    zametka = ("hgb")




while True:
    print("----- список действий -----")
    print("1. охотиться")
    print("2. спать" )
    print("3. есть" )
    print("4. открыть дневник")



    action = input("напишите номер действия ")
    action = int(action)
    print("---------------------------")

    if action == 1:
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
    elif action == 4:
        writing()
