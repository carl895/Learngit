# 父类 或 基类
class personmessage:
    '''记录信息   职业'''
    def __init__(self,name,age,phonenumber):
        self.name = name
        self.age = age
        self.phonenumber =phonenumber
        print('name',self.name)

    def tell(self):
        '''个人信息'''
        print('name:"{}" , age:"{}" , phonenumber:"{}"'.format(self.name,self.age,self.phonenumber),end='')

# 子类 或 派生类
class teather(personmessage):
    '''老师工资'''
    def __init__(self,name,age,phonenumber,salary):
        personmessage.__init__(self,name,age,phonenumber)
        self.salary = salary
        print('salary',self.salary)

    def tell(self):
        '''工资'''
        personmessage.tell(self)
        print('salary:"{}"'.format(self.salary))

class IT(personmessage):
    '''程序员工资'''
    def __init__(self,name,age,phonenumber,lotsalary):
        personmessage.__init__(self,name,age,phonenumber)
        self.lotsalary = lotsalary
        print('lotsalary',lotsalary)

    def tell(self):
        '''高工资'''
        personmessage.tell(self)
        print('lotsalary:"{}"'.format(self.lotsalary))  


j = teather('Mrs.Li',25,'131****1314',5000)
I = IT('LiMing',22,'131****5200',30000)

otherjob = [j,I]

for othersjob in otherjob:
    othersjob.tell()