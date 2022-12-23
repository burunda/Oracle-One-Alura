import matplotlib.pyplot as plt

def calcular_crecimiento_ganancia_neta(ingresos, egresos, costos_logistica, costos_produccion, meses, tasa_crecimiento):
  ganancias_netas = []
  for i in range(1, meses + 1):
    ganancia_neta = ingresos * (1 + tasa_crecimiento)**(i-1) - egresos - costos_logistica - costos_produccion
    ganancias_netas.append(ganancia_neta)
  return ganancias_netas

def optimizar_ganancia_neta(ingresos, egresos, costos_logistica, costos_produccion, meses, tasa_crecimiento):
  ganancias_netas = calcular_crecimiento_ganancia_neta(ingresos, egresos, costos_logistica, costos_produccion, meses, tasa_crecimiento)
  max_ganancia_neta = max(ganancias_netas)
  indice_max_ganancia_neta = ganancias_netas.index(max_ganancia_neta)

  if max_ganancia_neta > 0:
    print(f'Se puede aumentar la ganancia neta a {max_ganancia_neta} dólares al mes realizando los siguientes cambios:')
    if indice_max_ganancia_neta > 0:
      print(f'  - Aumentar los ingresos en el mes {indice_max_ganancia_neta+1}')
    else:
      print(f'  - Mantener los ingresos constantes')
    if max_ganancia_neta < ganancias_netas[indice_max_ganancia_neta-1]:
      print(f'  - Disminuir los egresos en el mes {indice_max_ganancia_neta+1}')
    else:
      print(f'  - Mantener los egresos constantes')
  else:
    print('No se puede aumentar la ganancia neta.')

optimizar_ganancia_neta(8000000, 6000000, 2000000, 0, 6, 0)

