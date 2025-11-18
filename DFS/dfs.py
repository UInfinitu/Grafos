def dfs(grafo):
  pilha = [list(grafo.keys())[0]]
  visitados = []

  while(len(pilha) > 0):
    vertice = pilha.pop(-1)

    if vertice not in visitados:
      visitados.append(vertice)
      vizinhos = grafo[vertice]

    for vizinho in vizinhos:
      if vizinho not in visitados and vizinho not in pilha:
        pilha.append(vizinho)

  return visitados

grafo = {
    "A": ["B", "C", "F"],
    "B": ["A", "C", "D", "F", "G"],
    "C": ["A", "B"],
    "D": ["B", "E"],
    "E": ["D", "F", "H"],
    "F": ["A", "B", "E", "G"],
    "G": ["B", "F", "H"],
    "H": ["E", "G"]
}

print(dfs(grafo))