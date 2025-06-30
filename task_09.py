def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    
    priority_dict = dict2 if sum2 >= sum1 else dict1
    secondary_dict = dict1 if priority_dict is dict2 else dict2
    
    result = {}
    
    for key, value in priority_dict.items():
        if value >= 10:
            result[key] = value
    
    for key, value in secondary_dict.items():
        if value >= 10 and key not in result:
            result[key] = value
    
    return dict(sorted(result.items(), key=lambda item: item[1]))

print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})) 
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})) 
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})) 