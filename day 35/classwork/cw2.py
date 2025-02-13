heigh = int(input("enter your heigh:"))
weigh = int(input("enter yourweigh:"))
sum = weigh/heigh

if sum<18.5:
    print("underweight")
elif sum>18.5 and "weight" <25:
    print("normal")
elif sum> 25 and sum <30:
    print("overweight")
else:
    print("obesity")