class House:
    '''Описание нашего дома'''
    def __init__(self,street,number,year):
        self.street = street
        self.number = number
        self.year = year
        
    def get_information(self):
        return f"я живу на улице {self.street} под номером {self.number}"
    
    def get_year(self,year):
        age = year + self.age
    
House1 = House("Абдрахманова", "101/1")
print(House1.get_information())
House2 = House.get_year(2025)
print()
    
    