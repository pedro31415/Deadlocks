import random

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, origem, destino):
        if origem not in self.adjacencia:
            self.adjacencia[origem] = []
        self.adjacencia[origem].append(destino)

    def detectar_ciclo(self):
        for no in self.adjacencia:
            if self._buscar_ciclo(no):
                return True
        return False

    def _buscar_ciclo(self, inicio):
        caminho = []
        arestas_marcadas = {origem: {destino: False for destino in destinos} 
                            for origem, destinos in self.adjacencia.items()}
        
        def explorar(no):
            caminho.append(no)
            if caminho.count(no) > 1:
                print("Ciclo encontrado:", caminho[caminho.index(no):])
                return True
            
            if no in self.adjacencia:
                destinos = [dest for dest, marcado in arestas_marcadas[no].items() if not marcado]
                
                if destinos:
                    destino = random.choice(destinos)
                    arestas_marcadas[no][destino] = True
                    if explorar(destino):
                        return True

            caminho.pop()
            return False

        return explorar(inicio)

grafo = Grafo()
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'A')  
grafo.adicionar_aresta('B', 'D')

if grafo.detectar_ciclo():
    print("Ciclo detectado no grafo.")
else:
    print("Nenhum ciclo detectado no grafo.")
