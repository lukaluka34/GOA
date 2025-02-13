def simple_calculator(num1, num2 ,operation):
    if operation =="გამოკლება":
        return num1-num2
    elif operation =="დამატება":
        return num1+num2
    elif operation == "გამრავლება":
        return num1*num2
    elif operation == "გაყოფა":
        if num2 == 0:
            print("0ზე გაყოფა შეუძლებელია")
            return False
print(simple_calculator(20,0,"გაყოფა"))