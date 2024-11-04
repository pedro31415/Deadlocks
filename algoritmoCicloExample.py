import networkx as nx
import matplotlib.pyplot as plt

class GrafoVisual:
    def __init__(self):
        self.grafo = nx.DiGraph()  

    def adicionar_aresta(self, origem, destino):
        self.grafo.add_edge(origem, destino)

    def detectar_e_mostrar_ciclo(self):
        try:
            ciclo = nx.find_cycle(self.grafo, orientation='original')  
            self.mostrar_grafo(ciclo)
        except nx.NetworkXNoCycle:
            print("Nenhum ciclo detectado no grafo.")
            self.mostrar_grafo()

    def mostrar_grafo(self, ciclo=None):
        pos = nx.spring_layout(self.grafo)
        
        nx.draw(self.grafo, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
        
        if ciclo:
            ciclo_arestas = [(origem, destino) for origem, destino, _ in ciclo]
            nx.draw_networkx_edges(self.grafo, pos, edgelist=ciclo_arestas, edge_color='red', width=2)
            plt.title("Ciclo detectado e destacado em vermelho")
        else:
            plt.title("Grafo sem ciclo")
        
        plt.show()


grafo = GrafoVisual()


grafo.adicionar_aresta('R', 'A')  # A possui R
grafo.adicionar_aresta('A', 'S')  # A solicita S

grafo.adicionar_aresta('B', 'T')  # B solicita T

grafo.adicionar_aresta('C', 'S')  # C solicita S

grafo.adicionar_aresta('U', 'D')  # D possui U
grafo.adicionar_aresta('D', 'S')  # D solicita S
grafo.adicionar_aresta('D', 'T')  # D solicita T

grafo.adicionar_aresta('T', 'E')  # E possui T
grafo.adicionar_aresta('E', 'V')  # E solicita V

grafo.adicionar_aresta('W', 'F')  # F possui W
grafo.adicionar_aresta('F', 'S')  # F solicita S

grafo.adicionar_aresta('V', 'G')  # G possui V
grafo.adicionar_aresta('G', 'U')  # G solicita U


grafo.detectar_e_mostrar_ciclo()
