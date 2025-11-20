def dfs_encontrar_ciclos(grafo):
  pilha = [{"vertice": list(grafo.keys())[0], "pai": None}]
  visitados = []

  while pilha:
    obj = pilha.pop()
    vertice = obj["vertice"]
    pai = obj["pai"]

    if vertice not in visitados:
      visitados.append(vertice)
      vizinhos = grafo[vertice]

      for vizinho in vizinhos:
        print(vizinho)
        print(vertice)
        if vizinho not in visitados and not any(item["vertice"] == vizinho for item in pilha):
          pilha.append({"vertice": vizinho, "pai": vertice})
        else:
          if vizinho != pai:
            return "Ciclo detectado"

  return "Nenhum ciclo detectado"


grafo = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B", "D"],
    "D": ["B", "C"]
}

print(dfs_encontrar_ciclos(grafo))