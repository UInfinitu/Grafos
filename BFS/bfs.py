def bfs(grafo):
  fila = [list(grafo.keys())[0]]
  visitados = []

  while(len(fila) > 0):
    vertice = fila.pop(0)

    if vertice not in visitados:
      visitados.append(vertice)
      vizinhos = grafo[vertice]

    for vizinho in vizinhos:
      if vizinho not in visitados and vizinho not in fila:
        fila.append(vizinho)

  return visitados

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

print(bfs(grafo))