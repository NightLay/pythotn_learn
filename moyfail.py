
import time



health = 100
exp = 0
food_suply = 50
energy = 50

notes = []
acheves = []

lutiy, mega, goodNight, poel = False

if exp >= 100:
    lutiy = True
elif exp > 500:
    lutiy == False
    mega == True




def hunting():
    global exp, food_suply, energy, health

    #time.sleep(5)
    health -= 10
    exp += 50
    food_suply += 25
    energy -= 20
    print("хорошо поохотились!")




def slepping():
    global exp, food_suply, energy, health

    #time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 10
    energy += 60
    print("хорошо поспали!")
    goodNight == True



def eating():
    global exp, food_suply, energy, health

    #time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 25
    energy += 100
    print("хорошо поспали!")
    poel == True



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


def aceve():
    print()
    print("---------------------------")
    if lutiy == True:
        print("ЛЮТЫЙ. получить 100 очков опыта.")
    elif mega == True:
        print("МОЩНЫЙ. получить 500 очков опыта.")
    elif goodNight == True:
        print("СПОКОЙНОЙ НОЧИ. поспать.")
    elif poel == True:
        print("ПОЕЛ. перекусить.")




while True:

    print("----- список действий -----")
    print("1. охотиться")
    print("2. спать" )
    print("3. есть" )
    print("4. открыть дневник")
    print("5. открыть список достижений")



    action = input("напишите номер действия ")
    action = int(action)
    print("---------------------------")

    if action == 1:
        if energy < 20:
            print("слишком мало энергии")
        else: 
            hunting()
    elif action == 2:
        slepping()
    elif action == 3:
        if food_suply < 25:
            print("слишком мало еды")
        else:
            eating()
    elif action == 4:
        writing()
    elif action == 5:
        aceve()


    print("---------------")
    print("здоровье: " + str(health))
    print("энергия: " + str(energy))
    print("опыт: " + str(exp))
    print("запас еды: " + str(food_suply))
    print("---------------")