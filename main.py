from Grafo import grafo
from Nodo import nodo
import argparse
import re

#Santiago Botero, Cesar Maldonado y Santiago Aviles
def manage_script_entry() -> str:
    
    parser = argparse.ArgumentParser()
    parser.add_argument('directorio', type=str, help='Direccion del ejemplo que se quiere ejecutar')
    args = parser.parse_args()
    path = args.directorio
    
    return path

def manage_example_dir(path: str):
    temp_graph = []
    #Primero cargar las relaciones en el archivo relaciones.txt
    PATH_R = path + '/relaciones.txt'
    with open(PATH_R, 'r') as file:
        
        for line in file:
            data = line.split(';')
            anterior_n = None
            for node in data:
                names = re.findall(r"\b\w+\b", node)    
                name = names[0]
                params = names[1:]
                n = nodo(name, [], params)
                if anterior_n == None:
                    anterior_n = n
                else:
                    n.padres.append(anterior_n)
                if len(temp_graph) == 0:
                    temp_graph.append(n)
                else:
                    rep = False
                    for index, node in enumerate(temp_graph):
                        if node.evento == name:
                            rep = True
                            i = index
                    if not rep:
                        temp_graph.append(n)
                    else:
                        temp_graph[i].padres += n.padres
                        
    #Segundo cargar las tablas         
    PATH_T = path + '/tablas.txt'           
    with open(PATH_T, "r") as file:
        lineas = file.readlines()
        new_lineas = []
        for linea in lineas:
            linea = linea[:-1]
            new_lineas.append(linea)
        lineas = new_lineas.copy()
        for index, line in enumerate(lineas):
            if lineas[index] == '#INICIO':
                titulo = lineas[index+1]
                labels = lineas[index+2].split(',')
                new_index = index + 3
                table_matrix = []
                while lineas[new_index] != '#FIN':
                    data = lineas[new_index].split(',')
                    table_matrix.append(data)
                    new_index += 1
                
                new_table = {}
                #Crear tuplas y diccionario
                for row in table_matrix:
                    index_list = []
                    for register in row:
                        try:
                            probability = float(register)
                            temp_list = index_list.copy()
                            temp_list.append(labels[row.index(register)])
                            new_table[tuple(temp_list)] = probability
                        except ValueError:
                            index_list.append(register)
                #Añadir tabla de probabilidades a el nodo
                for node in temp_graph:
                    if node.evento == titulo:
                        node.cross_table(new_table)
            
    return grafo(temp_graph)         
        
                    

if __name__ == '__main__':
    
    PATH = manage_script_entry()
    graph = manage_example_dir(PATH)
    
    c = "Appointment"
    q = "attend"
    e = ["light", "no"]
    h = ["Train"]
    
    value = graph.get_query_prob(q,e,h, c)
    
    print(value)
    
    """
    for node in graph.nodos:
        print(node)
        print(node.table)
        print("")
    """
    
    
    
    





