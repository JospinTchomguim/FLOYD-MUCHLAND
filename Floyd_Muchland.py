import timeit

def Floyd_Muchland(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    # Initialisation des matrices dist et pred
    for u in range(n):
        for v in range(n):
            dist[u][v] = graph[u][v]
            if u != v and dist[u][v] != float('inf'):
                pred[u][v] = u
            else:
                pred[u][v] = None

    # Algorithme de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
                    pred[i][j] = pred[k][j]

    # Construction des chemins les plus courts
    paths = [[[] for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and pred[u][v] is not None:
                # Construction du chemin de u à v en suivant les prédecesseurs
                path = [v]
                while path[0] != u:
                    path = [pred[u][path[0]]] + path
                paths[u][v] = path
            else:
                paths[u][v] = None

    return dist, pred, paths

INF= float('inf')
# Test
graph = [
    [0, 3, 8, INF, -4],
    [INF, 0, INF, 1, 7],
    [INF, 4, 0, INF, INF],
    [2, INF, -5, 0, INF],
    [INF, INF, 8, 6, 0]
]

dist, pred, paths = Floyd_Muchland(graph)

# Affichage des résultats

#Matrice poids du plus court chemin entre i et j  
print("Matrice dist :")
for row in dist:
    print(row)
print('\n')

#Matrice predecesseur de j lorsqu'on emprunte le plus court chemin entre i et j
print("Matrice pred :")
for row in pred:
    print(row)
print('\n')

print("Chemins les plus courts :")
for u in range(len(paths)):
    for v in range(len(paths[u])):
        if paths[u][v] is not None:
            print(f"Le plus court chemin de {u} -> {v} est {paths[u][v]}")

# Mesure du temps d'exécution avec timeit
t = timeit.timeit(lambda: Floyd_Muchland(graph), number=1) 
print("Durée d'exécution : %.5f secondes" % t)