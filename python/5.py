class person:
    '''表示晋级人与人数'''
    population = 0

    def __init__(self,name):
        '''初始化数据'''
        self.name = name
        print('(initializing {})' .format(self.name))
        # 当前晋级人数+
        person.population += 1

    def die(self):
        '''我淘汰了'''
        print('{} is being destroyed' .format(self.name))
        # 当前晋级人数-
        person.population -= 1

        if person.population == 0:
            print('{} is the last one'.format(self.name))
        else:
            print('we have still {} '.format(self.name))
    def say_hi(self):
        '''感谢你们的支持'''
        print("greeting")
    @classmethod
    def total(cls):
        '''当前剩余人数'''
        print('we  odd {}'.format(cls.population))

mount  = person('LI')
mount1 = person('CHEN')
mount2 = person('WU')
mount3 = person('JU')
mount4 = person('ZHAO')
mount5 = person('YAN')
mount6 = person('ZHOU')
mount7 = person('LING')

mount.say_hi()

mount.die()

person.total()







