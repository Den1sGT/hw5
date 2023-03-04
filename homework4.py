class Class1:
    def __init__(self,name):
        self.name = name

class Class2:
    def __init__(self,age):
        self.age = age

class Class3:
    def Ggg(self):
        print(f'привет ! {self.name}')

class Class4:
    def aged(self):
        print(f'я живу {self.age} лет')

class Class5(Class1, Class2, Class3, Class4):
    def __init__(self, name, age):
        Class1.__init__(self,name)
        Class2.__init__(self,age)

f = Class5("Denis", 22)
f.Ggg()
f.aged()

with open('ge.txt', 'w', encoding='UTF-8') as file:
    file.write(
        '''git init
        git add .
        git commit -m ""
        git  rm --cached
        git push origin название ветки 
        git branch
        '''
    )