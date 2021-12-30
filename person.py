#!/usr/local/bin/python3.9
class Person:
    def __init__(self,name,job,pay=0,age = 26):
        self.name = name
        self.pay = pay
        self.age = age
        self.job = job

    def __str__(self):
        return '%s,%s,%.2f,%d' % (self.name, self.job,self.pay, self.age)

    def payRise(self, percent='.1'):
        self.pay *= 1 + float(percent)

class  Manager(Person):
    def __init__(self,name,pay=0,age=26):
        # super().__init__(name, "Product Manager", pay, age)
        Person.__init__(self,name,"Product Manager",pay,age)

    def payRise(self,percent='.1',bonus=float('.2')):
        # super().payRise(float(percent) + bonus)
        Person.payRise(self,float(percent) + bonus)



if __name__ == '__main__':
    ui_designer = Person('pinkman','UI Design',14000,22)
    # ui_designer.payRise()
    # print(ui_designer)

    algorithm_expert = Person('scofield', 'Algorithm Expert', 150000, 35)
    # algorithm_expert.payRise()
    # print(algorithm_expert)

    product_manager = Manager("old white",14000,30)
    # product_manager.payRise()
    # print(product_manager)

    for object in [ui_designer, algorithm_expert,product_manager]:
        object.payRise()
        print(object)


