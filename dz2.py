# Завдання 1

onechyslo = int(input("Введіть перше число "))
dwachyslo = int(input("Введіть друге число "))
truchyslo = int(input("Введіть третє число "))

suma = onechyslo + dwachyslo + truchyslo
dobutok = onechyslo * dwachyslo * truchyslo

print("Сума чисел:",suma, "Добуток чисел:",dobutok)


# Завдання 2

zarplata = int(input("Введіть вашу зарплату за цей місяць "))
kredut = int(input("Введіть сума місячного платежу за кредитом у банку "))
komunalka = int(input("Введіть заборгованість за комунальні послуги "))

zalushok = zarplata - kredut - komunalka

if zalushok >= 0:
    print("У вас залишиться", zalushok, "грн")
elif zalushok < 0:
    print("У вас не залишиться грошей і буде", zalushok, "грн")


# Завдання 3

diagonal1 = float(input("Введіть першу діагональ ромба "))
diagonal2 = float(input("Введіть другу діагональ ромба "))

ploshcha = 0.5 * (diagonal1 * diagonal2)

print("Площа ромба:", ploshcha)