# SEMINÁRIO DE SISTEMA OPERACIONAL

Este seminário tem como objetivo, ministrar o capítulo 6, do livro  Sistema Operacioanis Modernos, escrito por Tanenbaum. Nosso grupo ficou encarregado de explicar a respeito de Deadlocks(impasses).


## DETECÇÃO DE IMPASSES (Pedro Henrique Araujo Cardoso)

Detecção de impasses é uma técnica que normalmente é usada quando o sistema não tenta evitar a ocorrência dos impasses. O que ocorre é que ele deixa que aconteça os impasses para que possa detectá-los e assim tentar recupera-se após o ocorrido.


## Algoritmo para detectar ciclos

1. Para cada nó, N, no grafo, execute os cinco pas-sos a seguir com N como o nó de partida.
2. Inicialize L como uma lista vazia e designe todosos arcos como desmarcados.
3. Adicione o nó atual ao final de L e confira paraver se o nó aparece agora em L duas vezes. Se eleaparecer, o grafo contém um ciclo (listado em L)e o algoritmo termina.
4. A partir do referido nó, verifique se há algumarco de saída desmarcado. Se afirmativo, vá parao passo 5; se não, vá para o passo 6.
5. Escolha aleatoriamente um arco de saída desmar-cado e marque-o. Então siga-o para gerar o novonó atual e vá para o passo 3.
6. Se esse nó é o inicial, o grafo não contém cicloalgum e o algoritmo termina. De outra maneira chegamos agora a um beco sem saída. Remova-o e volte ao nó anterior, isto é, aquele que era atual imediatamente antes desse, faça dele o nó atual e vá para o passo 3.



## REFERÊNCIAS 

- TANENBAUM, A.; BOS, H. Sistemas Operacionais Modernos. 4ª Edição. São Paulo: Pearson Education do Brasil, 2016.
- https://www.youtube.com/watch?v=yaJ6FgyoXCw 
- https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
- https://networkx.org/documentation/stable/tutorial.html
