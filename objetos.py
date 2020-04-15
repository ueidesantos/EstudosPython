a = "Ueide"
b = "Santos"

concatenar = a + '_' + b + '\n'

print(concatenar[0:6])

print(concatenar.lower())
print(concatenar)


#strip remove caracteres especiais
print(concatenar.upper().strip())


#split separa strings pelo caracter informado
print(concatenar.upper().strip().split("_"))

#Find retorna a posição do texto
print(concatenar.find("San"))
