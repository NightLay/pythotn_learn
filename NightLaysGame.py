
import time
import random

going = True


# добытые ресурсы
all_food = 0
all_energy = 0
all_health = 0



health = 100
exp = 0
food_suply = 50
energy = 50

exprazb = 0

notes = []






#охота
def hunting():
    global exp, food_suply, energy, health, all_health, all_energy


    health -= 10
    exp += 50
    food_suply += 25
    energy -= 20

    all_health += 10
    all_energy += 20
    print("хорошо поохотились!")



#прогулка
def stroll():
    global exp, energy, food_suply, health, all_energy

    r = random.randint(1, 5)

    if r == 1:
        print("вы нашли клад")
        exp += 20
    else:
        print("хорошо погуляли!")
    energy -= 30

    all_energy += 30



#сон
def slepping():
    global exp, food_suply, energy, health, all_food


    health += 40
    exp += 10
    food_suply -= 10
    energy += 60


    print("хорошо поспали!")
    all_food += 10



# ням-ням
def eating():
    global exp, food_suply, energy, health, all_food

    energy += 50
    health += 40
    exp += 10
    food_suply -= 25
        
    print("хорошо поели!")

    all_food += 25



# ведение дневника
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



# Поход 
def trevel():
    global exp, food_suply, energy, exprazb, health, all_food, all_health, all_energy

    y = random.randint(1, 10)

    exprazb = random.randint(10, 300)

    if y == 1 and exp > exprazb:
        print("вы встретили разбойников, но победили их и утопили ящеров в воде байкальской")
        health -= 45
        energy -= 50
        food_suply += 30
        exp += 50

        all_health += 45
        all_energy += 50

    elif y == 1 and exp <= exprazb:
        print("вы проиграли, но в следующий раз победа будет вашей!")
        health -= 100
        energy -= 70
        food_suply -= 30

        all_energy += 70
        all_health += 100
        all_food += 30

    elif y == 2:
        print("вы нашли ягоды, но пока вас небыло разбойники ограбили ваш дом")
        food_suply = 15
        energy -= 50

        all_energy += 50
        all_food += food_suply - 15

    elif y == 3:
        print("пока вас небыло ваш дом ограбили разбойники")
        food_suply = 0
        energy -= 30

        all_food += food_suply
        all_energy += 30

    elif y > 5:
        print("вы нашли вкусные ягоды!")
        energy -= 30
        food_suply += 30

        all_energy += 30

    else:
        print("вы ничего не нашли")
        energy -= 30

        all_energy += 30

    


# Действия Игры

while going == True:



    print("----- список действий -----")
    print("1. охотиться")
    print("2. спать" )
    print("3. есть" )
    print("4. открыть дневник")
    print("5. погулять")
    print("6. пойти  в поход")



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
            if energy < 30:
                print("слишком мало еды")
            else:
                stroll()
    elif action == 6:
        if energy <= 70 or exp < 100 or health < 50:
            print("вы не можете пойти в поход")
        else:
            trevel()


    if energy < 20 and food_suply < 25:
        going == False
            
        

    if health <= 0:
        going = False

    
    if energy > 200:
        energy = 200
    if health > 350:
        health = 350

    print("---------------")
    print("здоровье: " + str(health))
    print("энергия: " + str(energy))
    print("опыт: " + str(exp))
    print("запас еды: " + str(food_suply))
    print("---------------")

    time.sleep(2)


print("ну типо конец игры")
print("ваш опыт:", exp)
print("еды потрачено:", all_food)
print("потрачено енергии:", all_energy)
print("потрачено жизней:", all_health)
