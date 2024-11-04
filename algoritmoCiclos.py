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
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'A')  
grafo.adicionar_aresta('B', 'D')

grafo.detectar_e_mostrar_ciclo()
