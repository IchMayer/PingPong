{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import math\n",
    "#Класс мяча\n",
    "class Ball:\n",
    "    def __init__(self, surface, position):\n",
    "        self.radius = 20 \n",
    "        self.surface = surface\n",
    "        self.position = position\n",
    "        self.speed = 4\n",
    "        \n",
    "        angle = random.randint(-45, 45) + random.randint(0, 1) * 180\n",
    "        \n",
    "        self.velocity_x = self.speed * math.cos(angle * math.pi / 180)\n",
    "        self.velocity_y = self.speed * math.sin(angle * math.pi / 180)\n",
    "        \n",
    "        self.color = (255,0,0) #Красный\n",
    "\n",
    "    def draw(self):  \n",
    "        pygame.draw.circle(self.surface, \n",
    "                           self.color, \n",
    "                           (int(self.position[0]), int(self.position[1])), \n",
    "                           self.radius)\n",
    "\n",
    "    def setPosition(self, position):\n",
    "        self.position = position\n",
    "        \n",
    "        angle = random.randint(-45, 45) + random.randint(0, 1) * 180\n",
    "        \n",
    "        self.velocity_x = self.speed * math.cos(angle * math.pi / 180)\n",
    "        self.velocity_y = self.speed * math.sin(angle * math.pi / 180)\n",
    "\n",
    "   #def get_dir():\n",
    "    \n",
    "   # def first_move():\n",
    "       # import random\n",
    "        #choice = [-1, 0, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
