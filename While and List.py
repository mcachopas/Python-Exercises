InputVariable = 0.0
InputVariablestring = ""
VariableList = []

print("Digite apenas numeros positivos \nEm caso de numeros negativos o sistema sairá")
while InputVariable >= 0:
    InputVariablestring = input("Digite o próximo Numero")
    try:
        float(InputVariablestring)
        InputVariable = float(InputVariablestring)
        VariableList.append(InputVariable)
    except ValueError:
        print ("Valor não é um Numero")
print (f"Estes são os numeros digitados {VariableList}")