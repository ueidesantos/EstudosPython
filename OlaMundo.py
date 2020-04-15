# -*- coding: utf-8 -*-

#Teste mensagem 
print("Hello world !")


Nome = "Ueide"
SobreNome = "Santos"
Idade = 0

"""------------------------------------------
Operadores matemáticos
+ Adição
- Subtração
* Multiplicação
/ Divisão
** Exponenciação
% Módulo 
---------------------------------------------"""

"""------------------------------------------
Operadores relacionais
== Igual
!= Diferente
> Maior
< Menor
>= Maior igual
<= Menor igual 
---------------------------------------------"""

"""------------------------------------------
Operadores lógicos
AND 	Duas condições sejam verdadeiras
OR 		Pelo menos uma condição seja verdadeira
NOT		Inverte o valor
---------------------------------------------"""

print(Nome + " " + SobreNome + " Idade:" + str(Idade))

if Idade>18 : 
	print("Maior de idade.")
else:
	if Idade<1:
		print("Recém-nascido")
	else:
		print("Menor de idade.")


"""------------------------------------------
Laços de repetição

	while

---------------------------------------------"""

x=0
while x<10:
	print(x)
	x +=1

"""------------------------------------------
Laços de repetição
	for
---------------------------------------------"""

lista1 = [1,2,3,4,5]
lista2 = ["str1", "str2", "str3"]

for i in lista2:
	print(i)

for x in range(10,20):
	print(x)

	
# from urllib.request import urlopen
# with urlopen('http://www.terra.com.br') as response:
# 	for line in response:
# 		line = line.decode('utf-8')
# 		if 'EST' in line or 'EDT' in line:
# 			print(line)