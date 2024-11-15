'''
def junta_ordenados(l1,l2):
    lista = l1+l2
    return list(set(l1+l2))
'''
def junta_ordenados(lista1, lista2):
  if not lista1:
    return lista2
  if not lista2:
    return lista1
  if lista1[0] < lista2[0]:
    return [lista1[0]] + junta_ordenados(lista1[1:], lista2)
  elif lista1[0] > lista2[0]:
    return [lista2[0]] + junta_ordenados(lista1, lista2[1:])
  else:
    return [lista1[0], lista2[0]] + junta_ordenados(lista1[1:], lista2[1:])  # Concatena ambos elementos na lista resultante

print(junta_ordenados([2,3,5,1,6],[1,2,4,1,8]))