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
    
    #Metodo para verificar si la lista es una lista de nodos
    def verificar_integridad(self) -> bool:
        for n in self.nodos:
            if not isinstance(n, nodo):
                return False
        return True
                
    #Metodo para arreglar lista de nodos en caso de no ser integros
    def veryfix_nodos(self, nodos: list) -> list:
        new_nodos = []
        for n in nodos:
            if self.verificar_integridad(n):
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
            
        
    
        