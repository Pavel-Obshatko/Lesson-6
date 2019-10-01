# Задание easy

# class Car:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police

#     def go(self):
#         print('Машина {} поехала!'.format(self.name))

#     def stop(self):
#         print('Машина {} остановилась!'.format(self.name))

#     def turn(self, direction):
#         print('Машина {} повернула {}!'.format(self.name, direction))

# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         Car.__init__(self, speed, color, name, is_police=False)

# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         Car.__init__(self, speed, color, name, is_police=False)

# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         Car.__init__(self, speed, color, name, is_police=False)

# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         Car.__init__(self, speed, color, name, is_police=True)

# car1 = Car(100, 'red', 'Honda')
# car1.stop()
# car2 = Car(100, 'yellow', 'BMW')
# car2.go()
# car3 = Car(100, 'yellow', 'CAT')
# car3.turn('на право')
# car4 = Car(100, 'yellow', 'Police')
# car4.turn('назад')

# Задание normal

import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _income_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage*random.uniform(0.1, 1.0))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage*random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print('{} получил урон и теперь имеет {} здоровья, {} армора'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._income_damage(self.damage)


class Player(Person):
    # можно использовать pass
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    # можно использовать pass
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Fight:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print('игрок {} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print('игрок {} победил!'.format(person2.name))


player = Player('Павел Сергеевич', 100, 10, 50)
enemy = Enemy('Виктор Генадьевич', 100, 10, 50)

new_fight = Fight(player, enemy)
new_fight.start(player, enemy)