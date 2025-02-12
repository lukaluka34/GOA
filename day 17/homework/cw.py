
data = [42, 3.14, "Python", True, None, ["apple", "banana"], {"name": "Alice"}, (1, 2, 3), set([1, 2, 3]), bytearray(b"Hello")]

print(data[0]) 
print(data[1])  
print(data[2]) 


data[3] = "Java"
data[4] = "C++"
data[5] = "JavaScript"

data.append([1, 2, 3])  
data.append({"key": "value"})  
data.append("Go")  
data.append(False)  


print(data)