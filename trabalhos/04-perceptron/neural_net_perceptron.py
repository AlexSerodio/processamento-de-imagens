# Author: Alex Serodio Gonçalves

inputs_t = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
outputs_t = [0, 0, 1, 1]

inputs_c = [[0, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1]]

weights = [0, 0, 0]

def treinar(input, outputEsperado):
    valor = funcaoAtivacao(somaPonderada(input))

    print("Input:", input, "| Output esperado:", outputEsperado, "| Output alcançado:", valor, "| Pesos:", weights)
    
    if(valor == outputEsperado): 
        return False
    else: 
        if(valor == 0):
            for j in range(len(weights)):
                weights[j] += input[j]
        else:
            for j in range(len(weights)):
                weights[j] -= input[j]

        return True

def somaPonderada(i):
    return (i[0] * weights[0]) + (i[1] * weights[1]) + (i[2] * weights[2])

def funcaoAtivacao(valor):
    return 1 if valor > 0 else 0

print("Treinamento...")
repeat = True
while repeat:
    repeat = False
    for i in range(len(inputs_t)):
        error = treinar(inputs_t[i], outputs_t[i])
        if(error): repeat = True

print("-----------------------")
print("Pesos após treinamento: ", weights)
print("-----------------------")

print("Classificação...")
for i in inputs_c:
    print("Input:", i, "Classe:", funcaoAtivacao(somaPonderada(i)))