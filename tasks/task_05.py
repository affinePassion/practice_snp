from datetime import datetime, timedelta

def date_in_future(days):
    current_date = datetime.now()
    
    if not isinstance(days, int):
        return current_date.strftime('%d-%m-%Y %H:%M:%S')
    
    future_date = current_date + timedelta(days=days)
    
    return future_date.strftime('%d-%m-%Y %H:%M:%S')

print(date_in_future([]))
print(date_in_future(2))  
print(date_in_future(5.5)) 
print(date_in_future(0))  