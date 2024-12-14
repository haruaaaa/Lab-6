class Firearms:
    className = "Огнестрельное оружие"
    objectsCount = 0

    def __init__(self, bullet_number, speed, distance):
        self.bullet_number = bullet_number
        self.speed = speed
        self.distance = distance
        Firearms.objectsCount +=1

    def time(self):
        if self.speed !=0:
            return round(self.bullet_number/self.speed, 2)
        else:
            return False
        
    def ratio(self):
        if self.distance !=0:
            return round(self.speed/self.distance, 2)
        else:
            return False
        
    def info(self):
        print(f'Количество патронов в магазине: {self.bullet_number}')
        print(f'Скорострельность: {self.speed}')
        print(f'Дальность стрельбы: {self.distance}')

class AssaultRifle(Firearms):
    className = "Штурмовая винтовка"

    def __init__(self, bullet_number, speed, distance):
        super().__init__(bullet_number, speed, distance)

    def info(self):
        print(AssaultRifle.className)
        super().info()

class SniperRifle(Firearms):
    className = "Снайперская винтовка"

    def __init__(self, bullet_number, speed, distance):
        super().__init__(bullet_number, speed, distance)

    def info(self):
        print(SniperRifle.className)
        super().info()

    
#проверка 

first = AssaultRifle(10, 15, 12)
second = SniperRifle(5, 17, 45)

firearm = []
firearm.append(first)
firearm.append(second)
for weapon in firearm:
    weapon.info()
    if weapon.time():
        print(f'Магазин опустеет за {weapon.time()} секунд')

    if weapon.ratio():
        print(f'Соотношение скорострельности к дальности стрельбы: {weapon.ratio()}')
    print('')