class EvenNumbers:
    def __init__(self, n):
        self.n = n    
        self.current = 0 
        self.count = 0  
    
    def __iter__(self):
        return self     
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration  
        
        result = self.current    
        self.current += 2        
        self.count += 1          
        return result

evens = EvenNumbers(5)
for num in evens:
    print(num)  


