# AULA COMPLETA: NUMEROS EM PYTOHN 
"""
VAMOS APRENDER : 
1 - TIPOS NUMÉRICOS 
2 - CONVERSÕES DE TIPOS 
3 - HIERARQUIA NÚMERICA 
4 - OPERAÇÕES MATEMÁTICAS 
5 - COERÇÃO DE TIPOS 
6- VERIFICAÇÃO DE TIPOS 
7 - ENTRADA DE DADOS 
"""
#===========================
##PASSO 01 - TIPOS NÚMERICOS 
#===========================
#INT -> NÚMEROS INTEIROS 
# FLOAT -> NÚMEROS COM CASAS DECIMAIS 
# COMPLEX -> NÚMEROS COMPLEXOS ( USADOS EM MATEMÁTICA/ ENGENHARIA )

print ("===== TIPOS NÚMERICOS =====")

#exemplo 01 - numero inteiro 

#criamos uma variavel chamada numero_inteiro 
numero_inteiro = 10 

#mostrar o valor 
print ( "valor:", numero_inteiro)

#type ()mostra qual é o tipo da variavel
print ( "tipo :", type (numero_inteiro))

print ("====================================")

# exemplo 02 - numero decimal 

#float é um numero com ponto decimal 
numero_decimal = 3.14 

print ("valor:", numero_decimal)
print ("tipo:",type(numero_decimal))

print ("======================================")

# exemplo 03 - numeros complexos 
# um numero complexo possui duas partes:
#parte real (numero normal)


#estrutura geral: 
#numero = a + bj 

# a = parte real 
#b = parte imaginaria 
# j = unidade imaginaria 

numero_complexo = 2 + 3j

print ("valor:", numero_complexo)
print ("tipo", type(numero_complexo))

print ("====================================")

#EXEMPLO 03 - ACESANDO CADA PARTE DO NÚMERO 

#. real retorna a parte real 
print ("parte real :", numero_complexo .real)

#. imag retorna a parte imaginaria 
print ("parte imaginaria:", numero_complexo.imag)

#apenas para separar visualmente a saida no terminal 
print ("\n\n")

#=====================================
##passo 02 - converão de tipos 
#=====================================

## exemplo classico:
##dados vindos do usuario sao textos (string), muitas vezes é necessario converter eles. 

print ("============ conversões =================")

#float -> int (3.9)

valor = int (3.9)

print ("int(3.9):", valor)
print ("tipo:", type(valor))

#string -> int 
valor1 = "10"
print (type(valor1))

valor2 = int ("10")
print ('int("10"):', valor2)
print ("tipo:",type(valor2))

#int --> float 
valor3 = float (10)
print ("float (10):", valor3)
print ("tipo :", type(valor3))
