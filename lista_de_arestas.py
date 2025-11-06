def criar_grafo():
  lista = []
  vertices = []
  return (lista, vertices)

def inserir_vertice(vertices, vertice):
  if vertice in vertices:
    print(f"O vértice '{vertice}' já existe no grafo.")
    return

  vertices.append(vertice)

def remover_vertice(lista, vertices, vertice):
    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return

    nova_lista = [aresta for aresta in lista if vertice not in aresta]

    lista[:] = nova_lista

    vertices.remove(vertice)

def inserir_aresta(lista, vertices, origem, destino, nao_direcionado=False):
  if origem not in vertices:
    inserir_vertice(vertices, origem)

  if destino not in vertices:
    inserir_vertice(vertices, destino)

  lista.append([origem, destino])

  if nao_direcionado:
    lista.append([destino, origem])

def remover_aresta(lista, vertices, origem, destino, nao_direcionado=False):
  if origem not in vertices:
    print(f"O vértice '{origem}' não existe no grafo.")
    return

  if destino not in vertices:
    print(f"O vértice '{destino}' não existe no grafo.")
    return

  lista.remove([origem,destino])

  if nao_direcionado:
    lista.remove([destino, origem])

def vizinhos(lista, vertices, vertice):
  if vertice not in vertices:
    print(f"O vértice '{vertice}' não existe no grafo.")
    return

  return [aresta[1] for aresta in lista if aresta[0] == vertice]

def existe_aresta(lista, origem, destino):
  if [origem, destino] in lista:
    return True

  return False

def listar_vizinhos(lista, vertices, vertice):
  lista = vizinhos(lista, vertices, vertice)

  print(f"Vizinhos de {vertice}: {lista}")

def exibir_grafo(lista, vertices):
  print("Grafo: ")
  for vertice in vertices:
    listar_vizinhos(lista, vertices, vertice)

def grau_vertices(lista, vertices):
  n = len(lista)
  graus = {}

  for v in vertices:
    entrada = sum(1 for aresta in lista if aresta[1] == v)
    saida = sum(1 for aresta in lista if aresta[0] == v)
    graus[v] = {"saida": saida, "entrada": entrada, "total": saida + entrada}
  return graus

def percurso_valido(lista, vertices, caminho):
  if len(caminho) < 2:
    return True
    
  print(caminho)
  
  for i in range(len(caminho) - 1):
    origem = caminho[i]
    destino = caminho[i+1]
    if not existe_aresta(lista, origem, destino):
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
        lista, vertices = criar_grafo()
        print("Grafo criado com sucesso!")
      case 2:
        vertice = input("Digite o vértice: ")
        inserir_vertice(vertices, vertice)
        print(f"Vértice '{vertice}' inserido com sucesso!")
      case 3:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        inserir_aresta(lista, vertices, origem, destino, nao_direcionado)
      case 4:
        exibir_grafo(lista, vertices)
      case 5:
        origem = input("Digite o vértice de origem: ")
        destino = input("Digite o vértice de destino: ")
        nao_direcionado = input("O vértice é direcionado? (s/n): ").lower() == "n"
        remover_aresta(lista, vertices, origem, destino, nao_direcionado)
      case 6:
        vertice = input("Digite o vértice: ")
        remover_vertice(lista, vertices, vertice)
      case 7:
        print(grau_vertices(lista, vertices))
      case 8:
        caminho = input("Digite o caminho: ").split()
        if percurso_valido(lista, vertices, caminho):
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