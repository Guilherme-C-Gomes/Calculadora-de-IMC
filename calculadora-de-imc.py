#entrada de dados
altura = float(input("Qual é sua altura?:"))
peso = float(input("Qual é seu peso?:"))

#conversão de valores
altura = altura/100
peso = int(peso)

#calculo do IMC
IMC = peso / altura **2

#dados de comparação 
Abaixo_do_peso = 18.5
acima_Peso_normal = 24.9
Sobrepeso = 29.9
obesidade1 = 34.9
obesidade2e3 = 40

#resultado do IMC
print("Seu IMC é:{:.2f}".format(IMC))
if Abaixo_do_peso <= IMC:
    print("Abaixo do peso")
elif Abaixo_do_peso <= IMC > acima_Peso_normal:
    print("Peso normal")
elif acima_Peso_normal<= IMC >Sobrepeso:
    print("Sobrepeso")
elif Sobrepeso<= IMC >obesidade1:
    print("obesidade 1")
else:
    print("Obsidade 2 e 3")