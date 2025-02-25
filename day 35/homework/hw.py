surname = input("enter your surname:")
age = int(input("enter your age:"))
create_password =input("create password:")
repeat_password =input("repeat password:")

def checkregister():
    if age <15:
        print("არ შეგიძლია შესვლა უნდა იყოს 15+")
        return False
    
if create_password != repeat_password:
    print("გთხოვთ სცადეთ ხელახლა")
    return False
elif create_password == repeat_password:
    print("რეგისტრაციამ წარმატებით ჩაიარა")


checkregister()