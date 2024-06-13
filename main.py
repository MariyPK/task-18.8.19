tickets = int(input("Введите количество билетов:\n"))
sum=0
i = 0
for age in range(tickets):
    age_t=input(f"Введите возраст посетителя {i+1} \n ")
    age=int(age_t)
    if age < 18:
        sum +=0
    elif 18 <= age <= 25:
        sum += 990
    elif  age > 25:
        sum += 1390
    i += 1
print("Количество билетов:", tickets , "на сумму", sum)
if tickets>3:
    sum_discount=round(sum*0.9, 2)
    print("Итого к оплате с учетом скидки 10%:\n", sum_discount)
if tickets<=3:
    print("Итого к оплате:\n", sum)








