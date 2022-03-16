nombres = []
edades = []

while True:

    nombre = input('Nombre del estudiante: ')
    if nombre == '*': 
      break
    edad = int(input('Ingrese edad del estudiante: '))
    if edad > 0:
      nombres.append(nombre)
      edades.append(edad)
    else:
      print('Estudiante no valido (verifique edad)')
  

mayores = []
edad_mayor = 0
edad_mayor_ind = 0

for j, edad in enumerate(edades):
  if edad >= 18:
    mayores.append(j)
  if edad > edad_mayor:
    edad_mayor = edad
    edad_mayor_ind = j

print('los estudiantes mayores de edad son:')
for j in mayores:
  print('*',nombres[j], edades[j])
print('*'*20)
print('Estudiante de mayor de edad:', nombres[edad_mayor_ind], '-', edades[edad_mayor_ind], 'años')
print"hola"