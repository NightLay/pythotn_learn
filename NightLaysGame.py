
import time
import random



health = 100
exp = 0
food_suply = 50
energy = 50

exprazb = 0

notes = []
acheves = []

#lutiy, mega, goodNight, poel = False

# if exp >= 100:
#     lutiy = True
# elif exp > 500:
#     lutiy == False
#     mega == True




def hunting():
    global exp, food_suply, energy, health

    
    health -= 10
    exp += 50
    food_suply += 25
    energy -= 20
    print("хорошо поохотились!")



def stroll():
    global exp, energy, food_suply, health

    r = random.randint(1, 5)

    if r == 1:
        print("вы нашли клад")
        exp += 20
    else:
        print("хорошо погуляли!")




def slepping():
    global exp, food_suply, energy, health

    #time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 10
    energy += 60
    print("хорошо поспали!")
    #goodNight == True



def eating():
    global exp, food_suply, energy, health

    #time.sleep(5)

    health += 40
    exp += 10
    food_suply -= 25
    energy += 100
    print("хорошо поспали!")
    #poel == True



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



# def aceve():
#     print()
#     print("---------------------------")
#     if lutiy == True:
#         print("ЛЮТЫЙ. получить 100 очков опыта.")
#     elif mega == True:
#         print("МОЩНЫЙ. получить 500 очков опыта.")
#     elif goodNight == True:
#         print("СПОКОЙНОЙ НОЧИ. поспать.")
#     elif poel == True:
#         print("ПОЕЛ. перекусить.")



def trevel():
    global exp, food_suply, energy, exprazb, health
    
    #y = random.randint(1, 10)
    y = 1
    exprazb = random.randint(110, 900)

    if y == 1 and exp > exprazb:
        print("вы встретили разбойников, но победили их и утопили ящеров в воде байкальской")
        health -= 45
        energy -= 50
    elif y == 1 and exp <= exprazb:
        health -= 100
        energy -= 70
        food_suply -= 30
    # elif y == 2:
    #     print("вы нашли ягоды, но пока вас небыло разбойники ограбили ваш дом")
    #     food_suply = 15
    #     exp -= 40
    #     energy -= 50
    # elif y == 3:
    #     print("пока вас небыло ваш дом ограбили разбойники")
    #     food_suply = 0
    #     exp -= 50
    #     energy -= 30
    # elif y > 5:
    #     print("вы нашли вкусные ягоды!")
    #     energy -= 30
    #     food_suply += 30
    # else:
    #     print("вы ничего не нашли")
    #     energy -= 30



while True:

    print("----- список действий -----")
    print("1. охотиться")
    print("2. спать" )
    print("3. есть" )
    print("4. открыть дневник")
    print("5. открыть список достижений")
    print("6. погулять")
    print("7. пойти  в поход")



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
    # elif action == 5:
    #     aceve()
    elif action == 6:
        stroll()
    elif action == 7:
        if energy <= 70 or exp < 100 or health < 50:
            print("вы не можете пойти в поход")
        else:
            trevel()


    print("---------------")
    print("здоровье: " + str(health))
    print("энергия: " + str(energy))
    print("опыт: " + str(exp))
    print("запас еды: " + str(food_suply))
    print("---------------")

    time.sleep(2)