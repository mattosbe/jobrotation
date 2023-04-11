#!)
indice = 13
soma = 0
k = 0
while k < indice:
    k += 1
    soma += k
print(soma)
#resultado será 91
#2)
def fibonacci(n):
    f1, f2 = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    while f2 <= n:
        if f2 == n:
            return True
    f1, f2 = f1, f1 + f2
print(fibonacci())
#3)Descubra a lógica e complete o próximo elemento:



#a) 1, 3, 5, 7, 9

#b) 2, 4, 8, 16, 32, 64, 128

#c) 0, 1, 4, 9, 16, 25, 36, 49 

#d) 4, 16, 36, 64, 100

#e) 1, 1, 2, 3, 5, 8, 13

#f) 2,10, 12, 16, 17, 18, 19, 20

#4)


#carro = d / v_carro
#carro = 100 km / 110 km/h
#carro = 0,91 h

#t_caminhao = d / v_caminhao + 2 * (1/12 h)
#t_caminhao = 100 km / 80 km/h + 2/12 h
#t_caminhao = 1,33 h


#d_carro = v_carro * t_carro
#d_carro = 110 km/h * 0,91 h
#d_carro = 100 km


#d_caminhao = v_caminhao * t_caminhao
#d_caminhao = 80 km/h * 1,33 h
#d_caminhao = 106,4 km

#carro estará mais proximo de ribeirão

#5)
texto = input()
texto_invertido = texto[::-1]
print(texto_invertido)

