# Пример метакласс, который требует, чтобы все наследуемые классы имели строки документирования,
# в противном случае возбуждается исключение TypeError

# Если закомментарить строку документирования в определении класса Student
# Вывод:
#         Traceback (most recent call last):
#           File "E:\Development\Python\different\classes\metaclass-exam.py", line 20, in <module>
#             class Student(metaclass=MyMetaClass):
#           File "E:\Development\Python\different\classes\metaclass-exam.py", line 17, in __init__
#             raise TypeError('%s must have a docstring' % key)
#         TypeError: get_name must have a docstring
#         Creating a new object of Student
#         Initialising class Student
# Если снять комментарий со строки документирования
# Вывод:
#         Creating a new object of Student
#         Initialising class Student
#         Alex
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
        for key, valye in dict.items():
            if key.startswith('__'): continue
            if not hasattr(cls, '__call__'): continue
            if not getattr(cls, '__doc__'):
                raise TypeError('%s must have a docstring' % key)
        super(MyMetaClass, cls).__init__(name, bases, dict)

class Student(metaclass=MyMetaClass):
    "initialising class Student"
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name

stud = Student('Alex')
print(stud.get_name())
print('Type of Student object %s' % type(stud))
print('Type of Student class %s' % type(Student))