numbers_input = input("შეიყვანეთ რიცხვები, გამოყოფილი მსჯავრით (მაგალითად: 1, 2, 3): ")


numbers = [int(num) for num in numbers_input.split(",")]


total_sum = sum(numbers)


print("რიცხვების ჯამი არის:", total_sum)