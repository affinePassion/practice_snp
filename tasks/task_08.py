def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    
    product = 1  
    has_digits = False  
    
    str_input = str(inputs)
    
    for char in str_input:
        if char.isdigit():  
            product *= int(char) 
            has_digits = True 
    
    return product if has_digits else None

print(multiply_numbers())         
print(multiply_numbers('ss'))     
print(multiply_numbers('1234'))   
print(multiply_numbers('sssdd34')) 
print(multiply_numbers(2.3))       
print(multiply_numbers([5, 6, 4])) 