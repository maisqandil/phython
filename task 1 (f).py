num1 = int(input("الرجاء إدخال الرقم الأول: "))
num2 = int(input("الرجاء إدخال الرقم الثاني: "))

if num1 < num2:
    print("الرقم الأصغر هو:", num1)
elif num2 < num1:
    print("الرقم الأصغر هو:", num2)
else:
    print("الأرقام متساوية")
