class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, value):
        self._calories = value
    
    def is_healthy(self):
        if self._calories is not None and isinstance(self._calories, (int, float)):
            return self._calories < 200
        return False
    
    def is_delicious(self):
        return True

dessert1 = Dessert("Пирожное", 150)
print(dessert1.name)          
print(dessert1.calories)      
print(dessert1.is_healthy())  
print(dessert1.is_delicious()) 

dessert2 = Dessert()
dessert2.name = "Торт"
dessert2.calories = 300
print(dessert2.is_healthy()) 

dessert3 = Dessert("Пудинг", "двести") 
print(dessert3.is_healthy())  