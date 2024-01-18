class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_age(self, newage):
        self.age = newage
    
    def get_name(self):
        return self.name