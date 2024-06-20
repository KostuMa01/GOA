# მომხმარებლისთვის რიცხვების შემოტანინება
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = float(input("შეიყვანეთ მესამე რიცხვი: "))

# რიცხვებზე მათემატიკური ოპერაციების შესრულება
sum_result = num1 + num2 + num3
sub_result = num1 - num2 - num3
mul_result = num1 * num2 * num3
div_result = num1 / num2 / num3

# შედეგების დაბეჭდვა
print(f"დამატება: {num1} + {num2} + {num3} = {sum_result}")
print(f"გამოკლება: {num1} - {num2} - {num3} = {sub_result}")
print(f"გამრავლება: {num1} * {num2} * {num3} = {mul_result}")
print(f"გაყოფა: {num1} / {num2} / {num3} = {div_result}")
