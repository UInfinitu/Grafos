def criar_grafo():
  matriz = []
  vertices = []

  return (matriz, vertices)

def inserir_vertice(matriz, vertices, vertice):
  if vertice in vertices:
    print(f"O vértice '{vertice}' já existe no grafo.")
    return

  vertices.append(vertice)

  for linha in matriz:
    linha.append(0)

  nova_linha = [0] * (len(matriz) + 1)
  matriz.append(nova_linha)

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
  if origem not in vertices:
    inserir_vertice(matriz, vertices, origem)
  if destino not in vertices:
    inserir_vertice(matriz, vertices, origem)

  index_origem = vertices.index(origem)
  index_destino = vertices.index(destino)
  matriz[index_origem][index_destino] = 1
  if nao_direcionado:
    matriz[index_destino][index_origem] = 1

def exibir_grafo(matriz, vertices):
  print("Grafo: ")
  for vertice in vertices:
    listar_vizinhos(matriz, vertices, vertice)

def remover_vertice(matriz, vertices, vertice):
  if vertice not in vertices:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return
  for linha in matriz:
    linha.remove(vertices.index(vertice))
  matriz.pop(vertice)
  vertices.remove(vertice)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
  if origem not in vertices:
    print(f"O vértice '{origem}' não existe no grafo.")
    return

  if destino not in vertices:
    print(f"O vértice '{destino}' não existe no grafo.")
    return

  index_origem = vertices.index(origem)
  index_destino = vertices.index(destino)
  matriz[index_origem][index_destino] = 0

  if nao_direcionado:
    matriz[index_destino][index_origem] = 0

def vizinhos(matriz, vertices, vertice):
  if vertice not in vertices:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return

  index_vertice = vertices.index(vertice)
  vizinhos = []
  for i, coluna in enumerate(matriz[index_vertice]):
    if coluna == 1:
      vizinhos.append(vertices[i])

  return vizinhos

def existe_aresta(matriz, vertices, origem, destino):
  if origem not in vertices:
    print(f"O vértice '{origem}' não existe no grafo.")
    return
  if destino not in vertices:
    print(f"O vértice '{destino}' não existe no grafo.")
    return

  index_origem = vertices.index(origem)
  index_destino = vertices.index(destino)

  return matriz[index_origem][index_destino] == 1

def grau_vertices(matriz, vertices):
  n = len(vertices)
  graus = {}

  for i in range(n):
    saida = sum(matriz[i])
    entrada = sum(matriz[j][i] for j in range(n))
    grau = saida + entrada
    graus[vertices[i]] = {"saida": saida, "entrada": entrada, "total": saida + entrada}

  return graus

def percurso_valido(matriz, vertices, caminho):
  if len(caminho) < 2:
    return True

  for i in range(len(caminho) - 1):
    origem = caminho[i]
    destino = caminho[i+1]
    if not existe_aresta(matriz, vertices, origem, destino):
      return False
  return True

def listar_vizinhos(matriz, vertices, vertice):
  lista = vizinhos(matriz, vertices, vertice)

  print(f"Vizinhos de {vertice}: {lista}")

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
        matriz, vertices = criar_grafo()
        print("Grafo criado com sucesso!")
      case 2:
        vertice = input("Digite o vértice: ")
        inserir_vertice(matriz, vertices, vertice)
        print(f"Vértice '{vertice}' inserido com sucesso!")
      case 3:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)
      case 4:
        exibir_grafo(matriz, vertices)
      case 5:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        remover_aresta(matriz, vertices, origem, destino, nao_direcionado)
      case 6:
        vertice = input("Digite o vértice: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        remover_vertice(matriz, vertice, nao_direcionado)
      case 7:
        print(grau_vertices(matriz, vertices))
      case 8:
        caminho = input("Digite o caminho: ").split()
        if percurso_valido(matriz, vertices, caminho):
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