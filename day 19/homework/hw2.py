numbers = []  


for _ in range(10): 
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)


max_num = numbers[0] 

for num in numbers:  
    if num > max_num:  
        max_num = num 

print("მაქსიმალური რიცხვი არის:", max_num) 