
# operadores aritmeticos
valor_1 = 4
valor_2 = 9
suma = valor_1 + valor_2
diferencia = valor_1 - valor_2
multiplicacion = valor_1 * valor_2
modulo = valor_2 % valor_1
potencia = valor_1 ** valor_2

print(f"suma: {suma}")
print(f"diferencia: {diferencia}")
print(f"multiplicacion: {multiplicacion}")
print(f"modulo: {modulo}")
print(f"potencia: {potencia}")


# operadores comparacion
print()
print(f"5 es menor que 5: {5 < 5}")
print(f"5 es mayor que 5: {5 > 5}")
print(f"5 es mayor o igual que 5: {5 >= 5}")
print(f"5 es menor o igual que 5: {5 <= 5}")
print(f"5 es igual que 5: {5 == 5}")
print(f"5 es diferente que 5: {5 != 5}")

# operadores logicos
print()
a = True
b = False
print(('a and b is', a and b))
print(('a or b is', a or b))
print(('not a is', not a))

# operador de identidad
"""
revisa si se hace referencia al mismo objeto.
veremos mas adelante como se define si dos objetos son identicos
"""
print()
val1 = 4
val2 = 7
misma_var = val1 is val2
print(f"{val1} is {val2}: {misma_var}")
misma_var = val1 is not val2
print(f"{val1} is not {val2}: {misma_var}")

# operador de pertenencia
dias_semana = ["lunes", "martes", "miercoles"]
esta_lunes_en_dias_de_la_semana = "lunes" in dias_semana
esta_domingo_en_dias_de_la_semana = "domingo" not in dias_semana
print(f"lunes in dias_semana? {esta_lunes_en_dias_de_la_semana}")
print(f"domingo not in dias_semana? {esta_lunes_en_dias_de_la_semana}")

# incremento/decremento
# no existe la operacion valor = ++valor
valor = 5
valor += 1
print(f"incremento: {valor}")
valor = 5
valor -= 1
print(f"decremento: {valor}")
# porque pasa esto? prime se asigna 3 a valor y despues se evalua la expresion sumando 3
valor = 5
valor =+ 3
print(f"valor =+ 3: {valor}")
