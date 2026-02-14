def count_substrings(s):
    frequency_map = {}
    for char in s:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
            
    total_count = 0
    
    for count in frequency_map.values():
        total_count += (count * (count + 1)) // 2
        
    return total_count

s = input("Enter a string : ")
print("Total substring count = ",count_substrings(s))
