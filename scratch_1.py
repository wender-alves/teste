idade= int(input("Digite a idade do nadador?"))
if idade >= 5 and idade <=7:
    print("Infantil A")
if idade == 12 or idade == 13:
    print("Juvenil A")
if idade >= 18:
    print("Adultos")
if idade < 5 or (idade >= 8 and idade <= 11) or (idade >= 14 and idade <=17):
    print("Não pode competir")
