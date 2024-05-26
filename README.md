import pygame
from random import randrange, randint

width = 1200
height = 700

basket_w = 1000
basket_h = 30
basket = pygame.Rect(width / 2 - basket_w / 2, height - basket_h - 10, basket_w, basket_h)
b_speed = 15

food_r = 20
food_speed = 6
food_d = food_r * 2
food = []
dy = -1

pygame.init()
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Catch")
bg = pygame.Surface((width, height))

score = 0
font = pygame.font.Font(None, 36)
text = font.render("Score: " + str(score), True, "white")
text_rect = text.get_rect()
text_rect.centerx = 60
text_rect.centery = 30

delay = pygame.time.get_ticks() + randint(100, 130)

game_over = False

while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    sc.blit(bg,(0, 0))
    sc.blit(text, text_rect)
    pygame.draw.rect(sc, pygame.Color("white"), basket)

    if pygame.time.get_ticks() > delay:
        new = pygame.Rect(randrange(food_d, width - food_d), 0, food_d, food_d)
        food.append(new)
        delay = pygame.time.get_ticks() + randint(1000, 1300)

    for element in food:
        pygame.draw.circle(sc, pygame.Color("green"), element.center, food_r)
        element.y -= food_speed * dy
        if element.colliderect(basket):
            food.pop(food.index(element))
            score += 1
            text = font.render("Score: " + str(score), True, "white")
        if element.y > basket.y + 50:
            game_over = True

    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT] or key[pygame.K_a]) and basket.left > 0:
        basket.left -= b_speed
    elif(key[pygame.K_RIGHT] or key[pygame.K_d]) and basket.right < width:
        basket.right += b_speed

    pygame.display.flip()
    clock.tick(60)

font = pygame.font.Font(None, 72)
text = font.render("вы набрали: " + str(score), True, "white")
text_rect = text.get_rect()
text_rect.centerx = width / 2
text_rect.centery = width / 2
sc.blit(bg,(0,0))
sc.blit(text, text_rect)
pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()




# import pygame
# from random import randint, randrange

# width = 1200
# height = 700

# basket_w = 150
# basket_h = 30

# basket = pygame.Rect(width / 2 - basket_w / 2, height - basket_h - 10, basket_w, basket_h)
# basket_speed = 15

# food_radius = 20
# food_speed = 6
# food_D = food_radius * 2
# food = []
# dy = -1

# pygame.init()
# sc = pygame.display.set_mode(width, height)
# clock = pygame.time.Clock()
# pygame.display.set_caption("catch")
# bg = pygame.Surface(width, height)

# score = 0
# font = pygame.font.Font(None, 36)
# text = font.render("Score: " + str(score), True, "white")
# text_rect = text.get_rect()
# text_rect.centerx = 60
# text_rect.centery = 30

# delay = pygame.time.get_ticks() + randint(1000, 1300)

# while True:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             exit()
#     sc.blit(bg, (0,0))
#     sc.blit(text, text_rect)
#     pygame.draw.rect(sc, pygame.Color("white"), basket) 

#     if pygame.time.get_ticks() > delay:
#         new = pygame.Rect(randrange(food_D, width - food_D), 0, food_D, food_D)
#         food.append(new)
#         delay = pygame.time.get_ticks() + randint(1000, 1300)

#         for element in food:
#             pygame.draw.circle(sc, pygame.Color("green"), element.center, food_radius)
#             element.y -= food_speed * dy
#             if element.colliderect(basket):
#                 food.pop(food.index(element))
#                 score += 1
#                 text = font.render("Score: " + str(score), True, "white")
#             if element.y > basket.y + 50:
#                 food.pop(food.index(element))

#     key = pygame.key.get_pressed()
#     if (key[pygame.K_LEFT] or key[pygame.K_a]) and basket.left > 0:
#         basket.left -= basket_speed
#     elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and basket.left < width:
#         basket.right += basket_speed

#     pygame. display.flip()
#     clock.tick(60)
