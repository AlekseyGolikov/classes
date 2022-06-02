# Пример динамического объявления класса Student, наследующего от метакласса MyMetaClass
# Вывод:
#         Creating a new object of Student
#         Initialising class Student
#         Alex
#         Type of Student __doc__ qwery
#         Type of Student object <class '__main__.Student'>
#         Type of Student class <class '__main__.MyMetaClass'>
#
#         Process finished with exit code 0

class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        print('Creating a new object of %s' % name)
        return super(MyMetaClass, cls).__new__(cls, name, bases, dict)
    def __init__(cls, name, bases, dict):
        print('Initialising class %s' % name)
        super(MyMetaClass, cls).__init__(name, bases, dict)

def init(obj, name):
    obj._name = name
def get_name(obj):
    return obj._name
Student = MyMetaClass('Student', (), {})
setattr(Student,'__doc__', "qwery")
setattr(Student, '__init__', init)
setattr(Student, 'get_name', get_name)

stud = Student('Alex')
print(stud.get_name())
print('Type of Student __doc__ %s' % Student.__doc__)
print('Type of Student object %s' % type(stud))
print('Type of Student class %s' % type(Student))
