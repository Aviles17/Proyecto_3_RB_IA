import itertools
#Definir modulo que contiene definición del objeto Nodo
class nodo:
    #Constructor
    def __init__(self, nombre: str , dependencias: list, params: list, table: dict = None):
        self.evento = nombre
        self.params = params
        self.padres = dependencias
        self.table = table
    
    #Definir comportamiento de impresion
    def __str__(self) -> str:
        dependencias = []
        for padre in self.padres:
            dependencias.append(padre.evento)
        return f"Nombre: {self.evento} ; Parameters: {self.params} ; Dependencias: {dependencias}"
    
    
    #Metodo para retornar cantidad de dependencias
    def cardinal_padres(self) -> int:
        return len(self.padres)
    
    #Metodo para crear tablas cruzadas
    def cross_table(self, table: dict) -> bool:
        
        empty_dir = self.create_indexes()
        if self.table == None and len(table) == len(empty_dir):
            for key in table.keys():
                for empty_key in empty_dir.keys():
                    if key == empty_key:
                        empty_dir[empty_key] = table[key]
                        break
                    
        #Verificar si la tabla fue cargada correctamente
        for empty_value in empty_dir.values():
            if empty_value == -1:
                return False
        self.table = empty_dir
        return True
                
        
        
    def create_indexes(self) -> dict:
        ret_dir = {}
        dependency_matrix = []
        
        for padre in self.padres:
            dependency_matrix.append(padre.params)
            
        dependency_matrix.append(self.params)
        combinations = list(itertools.product(*dependency_matrix))
        
        for combination in combinations:
            ret_dir[combination] = -1
        
        return ret_dir
        
        
        
                
                     
                     
    
            
        
        
        