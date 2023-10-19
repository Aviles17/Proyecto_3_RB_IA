from Nodo import nodo

#Definir modulo que contiene definición del objeto Grafo
class grafo:
    #Constructor
    def __init__(self, nodos: list):
        self.nodos = self.veryfix_nodos(nodos)
        self.root = self.get_root()
        self.size = len(self.nodos)
    
    #Definir impresion del grafo
    def __str__(self) -> str:
        return str(self.nodos)
    
    #Definir funcionamiento del operador '=='
    def __eq__(self, value) -> bool:
        
        if isinstance(value,grafo):
            if self.nodos == value.nodos:
                return True
            else:
                return False
    
    #Metodo para arreglar lista de nodos en caso de no ser integros
    def veryfix_nodos(self, nodos: list) -> list:
        new_nodos = []
        for n in nodos:
            if isinstance(n, nodo):
                new_nodos.append(n)
        return new_nodos
    
    #Metodo para establecer un nodo raiz
    def get_root(self) -> nodo:
        root = []
        for n in self.nodos:
            if n.cardinal_padres() == 0:
                root.append(n)
        
        if len(root) == 1:
            return root[0]
        else:
            raise ValueError("No hay una raiz en el grafo, error al crear")
            
    def get_query_prob(self, query: str, evidence: list, hidden: list, capa: str):
        
        for node in self.nodos:
            if node.evento == capa:
                n = node
                break
                
        estado_anterior = []
        Valor_Total = 1
        for e in evidence:
            for node in self.nodos:
                for param in node.params:
                    if param == e:
                        estado_anterior.append(e)
                        Valor_Total *= node.table[tuple(estado_anterior)]
        
        caminos_escondidos = {}
        Valor_Oculto = Valor_Total
        for h in hidden:
            for node in self.nodos:
                if h == node.evento:
                    for param in node.params:
                        estado = estado_anterior.copy()
                        estado.append(param)
                        Valor_Oculto *= node.table[tuple(estado)]
                        caminos_escondidos[tuple(estado)] = Valor_Oculto
        Suma = 0
        for camino in caminos_escondidos.keys():
            camino_temp = list(camino)
            camino_temp.append(query)
            lpadre = len(n.padres) + 1
            Suma += caminos_escondidos[camino] * n.table[tuple(camino_temp[-lpadre:])]
        
        return Suma
            
            
                        
                        
            
            
        
                
            
        
    
        