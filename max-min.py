numberOne = int(input("შეიყვანე პირველი რიცხვი:"))
numberTwo = int(input("შეიყვანე მეორე რიცხვი:"))
numberThree = int(input("შეიყვანე მესამე რიცხვი:"))

arr = [numberOne,numberTwo, numberThree]
arr.sort()
print(f"{arr[0]} - უმცირესი რიცხვი ")
# {arr[-1]} - ნიშნავს რომ ბოლო ელემენტს გამოაკლდება 1 და მიბვიღებთ იმ ელემენტს len(arr) - 1 -ასე იწერება 
print(f"{arr[-1]} - უდიდესი რიცხვი")
 