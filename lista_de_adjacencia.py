def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
      grafo[vertice] = []
    else:
      print(f"O vértice '{vertice}' já existe no grafo.")

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
  if origem not in grafo:
    inserir_vertice(grafo, origem)

  if destino not in grafo:
    inserir_vertice(grafo, destino)

  if nao_direcionado:
    grafo[origem].append(destino)
    grafo[destino].append(origem)
  else:
    grafo[origem].append(destino)

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]

    return f"Vértice '{vertice}' não encontrado no grafo."

def listar_vizinhos(grafo, vertice):
    lista = vizinhos(grafo, vertice)

    return f"{vertice} -> {lista}"

def exibir_grafo(grafo):
  print("Grafo:")
  for vertice in grafo:
    print(listar_vizinhos(grafo, vertice))

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
  if origem not in grafo:
    print(f"O vértice '{origem}' não existe no grafo.")
    return

  if destino not in grafo:
      print(f"O vértice '{destino}' não existe no grafo.")
      return

  if destino in grafo:
    grafo[origem].remove(destino)

    if nao_direcionado:
      grafo[destino].remove(origem)

def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
      print(f"O vértice '{vertice}' não existe no grafo.")
      return

    for vertice_presente in grafo:
        if vertice in vizinhos(grafo, vertice_presente):
          remover_aresta(grafo, vertice_presente, vertice)

    grafo.pop(vertice)

def existe_aresta(grafo, origem, destino):
  if origem not in grafo:
    print(f"O vértice '{origem}' não existe no grafo.")
    return

  for aresta in grafo[origem]:
    if aresta == destino:
      return True

  return False

def grau_vertices(grafo):
  grau = {}

  print("Grau de cada vértice:")
  for vertice in grafo:
    grau[vertice] = {"out": len(grafo[vertice]), "in": 0, "total": 0}

    for aresta in grafo[vertice]:
      grau[aresta]["in"] += 1

    grau[vertice]["total"] = grau[vertice]["in"] + grau[vertice]["out"]

    print(f"{vertice}: {grau[vertice]}")

  return grau

def percurso_valido(grafo, caminho):
  if len(caminho) < 2:
    return True

  for i in range(len(caminho)-2):
    origem = caminho[i]
    destino = caminho[i+1]

    if not existe_aresta(grafo, origem, destino):
      return False

  return True

def main():
  while(True):
    print("Escolha uma opção:")
    print("1 - Criar Grafo")
    print("2 - Inserir Vértice")
    print("3 - Inserir Aresta")
    print("4 - Exibir Grafo")
    print("5 - Remover Aresta")
    print("6 - Remover Vértice")
    print("7 - Grau de Vértice")
    print("8 - Percurso Válido")
    print("0 - Sair")
    op = int(input())

    print("\n===========================================\n")

    match op:
      case 1:
        grafo = criar_grafo()
        print("Grafo criado com sucesso!")
      case 2:
        vertice = input("Digite o vértice: ")
        inserir_vertice(grafo, vertice)
        print(f"Vértice '{vertice}' inserido com sucesso!")
      case 3:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        inserir_aresta(grafo, origem, destino, nao_direcionado)
      case 4:
        exibir_grafo(grafo)
      case 5:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        remover_aresta(grafo, origem, destino, nao_direcionado)
      case 6:
        vertice = input("Digite o vértice: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        remover_vertice(grafo, vertice, nao_direcionado)
      case 7:
        grau_vertices(grafo)
      case 8:
        caminho = input("Digite o caminho: ").split()
        if percurso_valido(grafo, caminho):
          print("O percurso é válido.")
        else:
          print("O percurso não é válido.")
      case 0:
        break
      case _:
        print("Opção inválida!")

    print("\n===========================================\n")

if __name__ == "__main__":
    main()