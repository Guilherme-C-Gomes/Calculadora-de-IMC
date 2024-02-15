#entrada de dados
altura = input("Qual é sua altura?:")
peso = input("Qual é seu peso?:")

#conversão de valores
altura = float(altura)/100*2
peso = int(peso)

#divisão de valores
IMC = peso/altura

#dados de comparação 
Abaixo_do_peso = 18,5
acima_Peso_normal = 24,9
Sobrepeso = 29,9
obesidade1 = 34,9
obesidade2e3 = 40

#resultado do IMC
print("Seu IMC é:"+IMC)
if Abaixo_do_peso < IMC:
    print("Abaixo do peso")
elif Abaixo_do_peso < IMC > acima_Peso_normal:
    print("Peso normal")
elif acima_Peso_normal< 