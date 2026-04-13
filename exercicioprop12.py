##EXERCÍCIO PROPOSTO 12##

sbruto = float(input("Digite seu salário bruto: "))
imposto = (sbruto*0.07)

##SEGUINDO A TABELA DO ENUNCIADO##
if (sbruto<=350):
    print(f"Seu salário final será {(sbruto+100)-(imposto)}")

elif (350<sbruto<600):
    print(f"Seu salário final será {(sbruto+75)-(imposto)}")

elif (600<=sbruto<=900):
    print(f"Seu salário final será {(sbruto+50)-(imposto)}")

else:
    print(f"Seu salário final será {(sbruto+35)-(imposto)}")
