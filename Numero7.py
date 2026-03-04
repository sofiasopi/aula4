#Número 8

valor= int(input("Valor do saque"))
notas_100= valor // 100
notas_50= (valor % 100) // 50
notas_20= ((valor % 100) % 50) // 20
print("Valor: R$: ", valor)
print("R$ 100,00 -- ", notas_100, "-- R$", notas_100 * 100)
print("R$ 50,00 --", notas_50, "--R$", notas_50 * 50)
print("R$ 20,00 --", notas_20, "--R$", notas_20 * 20)

'''
O comando format:===> formata uma string, onde:
exemplo ===> "-- R${:8,2f}".format(notas_100 * 100))
:8 ---> Indica que a string tera 8 caracteres
.2f ---> Indica o total de casas decimais
notas_100 * 100 ---> O valor que será inserido na string formatada
'''