#!/usr/bin/env python
# coding: utf-8

# In[216]:


#!pip install pygame


# In[217]:


import pygame
#from ball import Ball
#from cart import Cart
#from agent import Agent


# In[218]:


import random
import math
#Класс мяча
class Ball:
    def __init__(self, surface, position):
        self.radius = 20 
        self.surface = surface
        self.position = position
        self.speed = 4
        
        angle = random.randint(-45, 45) + random.randint(0, 1) * 180
        
        self.velocity_x = self.speed * math.cos(angle * math.pi / 180)
        self.velocity_y = self.speed * math.sin(angle * math.pi / 180)
        
        self.color = (255,0,0) #Красный

    def draw(self):  
        pygame.draw.circle(self.surface, 
                           self.color, 
                           (int(self.position[0]), int(self.position[1])), 
                           self.radius)

    def setPosition(self, position):
        self.position = position
        
        angle = random.randint(-45, 45) + random.randint(0, 1) * 180
        
        self.velocity_x = self.speed * math.cos(angle * math.pi / 180)
        self.velocity_y = self.speed * math.sin(angle * math.pi / 180)

   #def get_dir():
    
   # def first_move():
       # import random
        #choice = [-1, 0, 1]


# In[219]:


#Класс тележки
class Cart:
    def __init__(self, surface, position):
        self.velocity = 5
        self.pygame = pygame
        self.size = [10, 50] 
        self.position = position
        self.surface = surface
        self.color = (0,255,0) 
    
    def draw(self): 
        pygame.draw.rect(self.surface, 
                         self.color, 
                         self.pygame.Rect(self.position[0],  
                                     self.position[1], 
                                     self.size[0], 
                                     self.size[1]))
    def setPosition(self, position):
        self.position = position

    def move_up(self):
        self.position[1] += 1
        print('1')
    def move_down(self):
        self.position[1] -= 1


# In[220]:


#Класс вирутального игрока
class Agent():
    def __init__(self, cart):
        self.cart = cart
        self.last = self.cart.move_up
    #Алгоритм случайной игры    
    def autoplay(self):
        self.last = random.choice((self.cart.move_up, self.cart.move_down, self.last))


# In[221]:


# Функция получения текущей ситуации на игровом поле
def get_obs(cart_1, cart_2, ball):
    return (cart_1.position, cart_2.position, ball.position, ball.direction)


# In[222]:


#Автоигра
def auto_move(ball, cart):
    cart.position[1] = ball.position[1] - ball.radius


# In[223]:


pygame.init()
window_size = 500, 500 
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Ping Pong')

#Создаю тележки
cart_1 = Cart(window, [0, 250]) 
cart_2 = Cart(window, [490, 250])
#Создаю мяч
ball = Ball(window, [250, 250])

#Создаю агента
agent = Agent(cart_2)

#Рисую мяч и тележки
cart_1.draw()
cart_2.draw()
ball.draw()
pygame.display.update()


# In[224]:


def game_cicle():
    game = True
    #Цикл игры
    while game:
        #Чтобы не так быстро
        pygame.time.delay(10)
        #Обработка событий
        for event in pygame.event.get():
            #Выход
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        #Какие кнопки нажаты
        keys = pygame.key.get_pressed()
        #Если нажата вверх
        if keys[pygame.K_UP]:
            #Проверка на выход за границы
            if (cart_1.position[1] >= 0): 
                cart_1.position[1] = cart_1.position[1] - cart_1.velocity
        #Если нажата вниз
        if keys[pygame.K_DOWN]:
            #Проверка на выход за границы
            if cart_1.position[1] <= window_size[1] - cart_1.size[1]:
                cart_1.position[1] = cart_1.position[1] + cart_1.velocity
        #Если нажата W
        if keys[pygame.K_w]:
            #Проверка на выход за границы
            if (cart_2.position[1] >= 0): 
                cart_2.position[1] = cart_2.position[1] - cart_2.velocity
        #Если нажата S
        if keys[pygame.K_s]:
            #Проверка на выход за границы
            if cart_2.position[1] <= window_size[1] - cart_2.size[1]:
                cart_2.position[1] = cart_2.position[1] + cart_2.velocity
        if keys[pygame.K_ESCAPE]:
                game = False
                pygame.quit()
        
        #Если шар касается тележки #Поменяй шар на квадрат, иначе придется тут переписать      
        if (cart_2.position[0] - ball.position[0] - ball.radius <= 0 and cart_2.position[0] + cart_2.size[0]/2 - ball.position[0] - ball.radius > 0 and 
            cart_2.position[1] - ball.position[1] < ball.radius / 1.5 and ball.position[1] - cart_2.position[1] - cart_2.size[1] < ball.radius / 1.5 or
            cart_1.position[0] + cart_1.size[0] - ball.position[0] + ball.radius >= 0 and cart_1.position[0] + cart_1.size[0]/2 - ball.position[0] + ball.radius < 0 and
            cart_1.position[1] - ball.position[1] < ball.radius / 1.5 and ball.position[1] - cart_1.position[1] - cart_1.size[1] < ball.radius / 1.5):
            ball.velocity_x = -1 * ball.velocity_x
            
        #Отражение
        if (ball.position[1] - ball.radius <= 0 or 
            ball.position[1] + ball.radius >= window_size[1]):
            # изменить направление скорости по y
            ball.velocity_y = -1 * ball.velocity_y 
        
        
        #Если шар касается сторон экрана для завершения
        if (ball.position[0] <= 0 or 
            ball.position[0] >= window_size[0]):
            # изменить направление скорости по y
            ball.velocity_y = -1 * ball.velocity_y 
            game = False

        #Это чисто для отладки
        #if (ball.position[0] + ball.radius >= window_size[0]):
            # изменить направление скорости по x
            #ball.velocity_x = -1 * ball.velocity_x
            #game = False


        #Переместить шар
        ball.position[0] += ball.velocity_x
        ball.position[1] += ball.velocity_y 

        #auto_move(ball, cart_2)
        agent.autoplay()

        #Очистка экрана
        window.fill((0,0,0))
        #Заново рисуем тележку
        cart_1.draw()   
        cart_2.draw()

        #Заново рисуем шар
        ball.draw()
        #Обновляем экран
        pygame.display.update()


# In[225]:


while True:
    game_cicle()
    cart_1.setPosition([0, 250])    
    cart_2.setPosition([490, 250])
    ball.setPosition([250,250])
pygame.quit()


# In[ ]:




