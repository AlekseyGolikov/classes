"""
    Пример переопределения функции isinstance()
"""
from abc import ABCMeta, ABC
class AbstractClass(ABC):

    @classmethod
    def __subclasshook__(cls, instance):
        attributes = dir(instance)
        print(dir(instance))
        methods = ('header', 'paragraph', 'footer')
        if all(method in attributes for method in methods):
            return True
        return NotImplemented

class MyClass:
    def header(self):
        pass
    def paragraph(self):
        pass
    def footer(self):
        pass

class MyOtherClass:
    def header(self):
        pass

class ClassCheck(AbstractClass):
    @classmethod
    def __call__(cls, inst):
        if isinstance(inst, cls):
            print('Object {} has all methods (header, paragraph, footer)'.format(inst))
        else:
            print('Object {} do not have any methods (header, paragraph, footer)'.format(inst))


ClassCheck()(MyClass())
ClassCheck()(MyOtherClass())