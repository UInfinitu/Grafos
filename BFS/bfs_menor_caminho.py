def bfs_menor_caminho(grafo, inicio, destino):
  fila = [(inicio, [inicio])]
  visitados = []

  while len(fila) > 0:
    vertice, caminho = fila.pop(0)

    if vertice == destino:
      return caminho

    visitados.append(vertice)

    for vizinho in grafo[vertice]:
      esta_na_fila = any(v == vizinho for v, _ in fila)

      if (vizinho not in visitados) and (not esta_na_fila):
        fila.append((vizinho, caminho + [vizinho]))

  return []


grafo = {
    "A": ["B", "D"],
    "B": ["C"],
    "C": ["D"],
    "D": ["E", "F", "H"],
    "E": ["A", "G"],
    "F": ["G"],
    "G": ["I"],
    "H": ["I"],
    "I": []
}

print(bfs_menor_caminho(grafo, "A", "G"))