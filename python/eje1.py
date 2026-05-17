# promedio de duracion
otro_cursos_min = 2.5
otro_cursos_max = 7
otro_cursos_promedio = 4

dalto_curso = 1.5
#diferencias de la duracion
diferencia_con_min = 100 - (dalto_curso/otro_cursos_min)*100
diferencia_con_max = 100 - (dalto_curso * 1000//otro_cursos_max)/10
diferencia_con_promedio = 100 - (dalto_curso/otro_cursos_promedio)*100

print(f'El curso de dalto dura un {diferencia_con_min}% menos, que el curso mas rapido')
print(f'El curso de dalto dura un {diferencia_con_max}% menos, que el curso mas lento')
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos, que el curso en promedio')

# duracion de crudos (videos editar)
crudo_promedio = 5
crudo_dalto = 3.5

#calculando el porcentaje de tiempo vacio 
tiempo_vacio_promedio = 100 - (otro_cursos_promedio/crudo_promedio)*100
print(f'El curso promedio elmina un  {tiempo_vacio_promedio}% de tiempo vacio ')
tiempo_vacio_dalto = 100 - (dalto_curso * 1000//crudo_dalto)/10
print(f'El curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio ')