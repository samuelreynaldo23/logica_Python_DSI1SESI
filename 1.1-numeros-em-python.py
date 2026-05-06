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

 