from datetime import date, timedelta

class Person:
    def __init__(self, name, lastname, birthday):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
    def __str__(self):
        return '{} {}'.format(type(self).__name__, self.__dict__)

class Student(Person):
    def __init__(self, *args):
        super().__init__(*args[:-1])
        self.lectures = args[-1]
    def _average(self):
        return sum([y for x, y in self.lectures.items()])/len(self.lectures)
    average = property(_average, None, None, 'Average grade.')

class Worker(Person):
    def __init__(self, *args):
        super().__init__(*args[:-1])
        self.pay_per_hour = args[-1]

    @property
    def day_salary(self):
        return self.pay_per_hour * 8
    @day_salary.setter
    def day_salary(self, v):
        self.pay_per_hour = v / 8

    @property
    def week_salary(self):
        return self.day_salary * 5
    @week_salary.setter
    def week_salary(self, v):
        self.day_salary = v / 5

    @property
    def month_salary(self):
        return self.week_salary * 4
    @month_salary.setter
    def month_salary(self, v):
        self.week_salary = v / 4

    @property
    def year_salary(self):
        return self.month_salary * 12
    @year_salary.setter
    def year_salary(self, v):
        self.month_salary = v / 12

class Wizard(Person):
    class AgeDescriptor():
        def __get__(self, instance, owner):
            return date.today().year - instance.birthday.year
        def __set__(self, instance, years):
            instance.birthday = date(date.today().year - years, instance.birthday.month, instance.birthday.day)
    age = AgeDescriptor()


if __name__ == '__main__':
    print(Person('John', 'Rambo', date(1980, 1, 10)))
    s = Student('John', 'Travolta', date(1999, 4, 5), {'Chemistry': 30, 'Mathematics':28})
    print(s)
    print(s.average)
    w = Worker('John', 'Bolton', date(1945, 6, 7), 30)
    print(w)
    print(w.day_salary)
    w.day_salary = 150
    print(w.day_salary, w.pay_per_hour)
    print(w.year_salary)
    w.year_salary = 100000
    print(w.year_salary, w.pay_per_hour)
    wiz = Wizard('John', 'Cena', date(1985, 1, 3))
    print(wiz)
    print(wiz.age)
    wiz.age = 45
    print(wiz.birthday)
