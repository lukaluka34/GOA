user_numbers = []


while True:
    user_input = input("შეიყვანეთ რიცხვი (ან უბრალოდ დააჭირეთ Enter, რომ შეწყვიტოთ): ")
    
   
    if user_input == "":
        break
    
    try:
        
        number = float(user_input)
        user_numbers.append(number)
    except ValueError:
        
        print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")


if any(num > 10 for num in user_numbers):
    print("სიაში არის 10-ზე მეტი რიცხვი.")
else:
    print("სიაში 10-ზე მეტი რიცხვი არ არის.")


print(f"შეყვანილი რიცხვები: {user_numbers}")
print(f"რიცხვების ჯამი: {sum(user_numbers)}")