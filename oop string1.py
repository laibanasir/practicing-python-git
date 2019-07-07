#A class has two methods. First method accept a string from the user, Second method print the string in upper case
#oop
class string:
    def __init__(self):
        self.string = ''

    def get_string(self) :
        self.string = input('Enter string: ')

    def string_upper(self):
        stringUpper = self.string.upper()
        print('upper case string :', stringUpper)

first_string = string()
string.get_string(first_string)
string.string_upper(first_string)