numbers = []  


for _ in range(10): 
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)


print("საპირისპირო  სია არის:")
for i in range(len(numbers)-1, -1, -1): 
    print(numbers[i])