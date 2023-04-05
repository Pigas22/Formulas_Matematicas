palavra = input("Digite uma palavra: ")
list = []
listcount = []

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
 

for letra in palavra:
    if not(letra in list):
        list.append(letra)
        print(letra)

for letra1 in list:
    count = 0
    for letra2 in palavra:
        if letra1 == letra2:
            count = count + 1
    listcount.append(count)
    print(listcount)

denominador = 1
for num in listcount:
    denominador = denominador * fatorial(num)
    print(num)

print(fatorial(len(palavra)) / denominador)