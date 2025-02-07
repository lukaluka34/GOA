numbers = []  


for _ in range(10):  
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)


to_find = int(input("რომელ რიცხვს ეძებთ? "))  


found = False 
for num in numbers:
    if num == to_find:
        found = True
        break  


if found:
    print(f"{to_find} არის სიაში.")
else:
    print(f"{to_find} არ არის სიაში.")

