from task_11 import Dessert 

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories) 
        self._flavor = flavor
    
    @property
    def flavor(self):
        return self._flavor
    
    @flavor.setter
    def flavor(self, value):
        self._flavor = value
    
    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True

jelly1 = JellyBean("Жевательная конфета", 150, "strawberry")
print(jelly1.name)            
print(jelly1.calories)        
print(jelly1.flavor)          
print(jelly1.is_healthy())    
print(jelly1.is_delicious())  

jelly2 = JellyBean("Лакричная конфета", 50, "black licorice")
print(jelly2.is_delicious())  

jelly3 = JellyBean()
print(jelly3.is_delicious())