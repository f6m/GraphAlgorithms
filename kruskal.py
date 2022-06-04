# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:47:47 2022

@author: usuario
"""

# Programa que aplica el algoritmo de Krushkal para determinar
# el arbol recubridor de peso minimo.

# LISTA CON DOBLE ENLACE 
# Un vértice:
class Nodo: #self refiere a la instancia de la clase
   def __init__(self, data):
      self.data = data
      self.next = None #apuntador sig.
      self.prev = None #apuntador prev.

# Clase para la lista con enlace doble
class doble_link_lista:
   def __init__(self): #Constructor
      self.head = None #Se invoca al principio
      self.longitud = 0 #Longitud de la lista
    
   # Agregar elementos a la lista doble	
   def push(self, NewVal):
      self.longitud = self.longitud + 1 #incrementa la longitud en 1
      NewNode = Nodo(NewVal) #Crea un vertice/nodo
      NewNode.next = self.head #NewNode.next -> head, head es una var general, head es el ultimo nodo asigndado
      if self.head is not None: # es decir ya se le asigno un nodo, la primera vez que entra aqui salta este if
         self.head.prev = NewNode # head tiene prev puesto que ya apunta a un nodo head.prev -> NewNode
      self.head = NewNode #NewNode.next -> head -> NewNode

   # Insertar elementos indicando un nodo previo
   def insertar(self,prev_node,NewVal):
      if prev_node is None:
         return
      self.longitud = self.longitud + 1 #inc longitud de la lista doble
      NewNode = Nodo(NewVal) #nuevo nodo
      NewNode.next = prev_node.next #Un enlace entre sigs
      prev_node.next = NewNode #
      NewNode.prev = prev_node # prev_node <-NewNode.prev
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

   #Busca un valor en la lista
   def buscarv(self,val):
      if(head == None): return 0
      NewNode = Nodo(val)
      NewNode.next = self.head.prev
      if(NewNode.next.value == val): return 1
      NewNode.next=NewNode.next.prev
      while(NewNode.next is not None):
        if(NewNode.next.value == val): 
         return 1
        NewNode.next = NewNode.next.prev
      return 0
	  
   # Imprimir la lista doble ligada		
   def listprint(self, node):
      print("Lista doble actual:")
      while (node is not None):
         print(node.data, end = ' ')
         last = node
         node = node.next #Desplazamiento hacia la derecha
      print('\n')
# LISTAS DE ADYACENCIA PARA LA GRAFICA G donde se busca el ARM

# Clase para los nodos en las lista de adyacencia de un vertice
# (vertex,next)
class AdjNodo:
    def __init__(self, data):
        self.vertex = data
        self.next = None
  
  
# Una clase para representar la grafica mediante sus listas 
# de adyacencia. El tamano del arreglo sera el numero de vertices indicado como V

class Graph:
    def __init__(self, vertices):
        self.V = vertices #orden de la grafica
        self.graph = [None] * self.V #no es necesario inidicar de que tipo de dato es una variable 
        self.Ady = [[float('inf')]*self.V for i in range(self.V)] #Arreglo bidimensional para la matriz de adyacencia en lugar de una lista anidada
        self.K = doble_link_lista() # para la cola de prioridad de las aristas
    #Tipo de dato none: declara un arreglo de V None's

    # Funcion para agregar una arista con un peso c(u,v) tanto a la matriz de adyacencia como a 
    # una cola de prioridades implementada por medio de la lista doble.
    def add_edge(self, u, v, c):
        # Agregar el nodo destino al nodo origen src
        node = AdjNodo(v) #Crea el dato vertice adyacente a src el primero.
        node.next = self.graph[u] #node.next es/apunta al array graph con indice src, inicialmente es none
        self.graph[u] = node #graph[src] contiene node con data=dest,next=graph[src]
        self.Ady[u][v]=c	
	#Los indices para las etiquetas son 0,1,2,3,...,V-1
  	# Cuando se vuelve agregar otro con mismo src remplaza el actual graph[src]
	# pero antes se enlaza con node.next=graph[src] apuntando al actual, despues se remplaza.
        # Agrega el nodo origen al nodo destino pues es una grafica simple
        node = AdjNodo(u) #vuelve a usar la var. node y crea la otra direccion de la arista
        node.next = self.graph[v]
        self.graph[v] = node #el arreglo en posicion dest tiene el nodo src,
        self.Ady[v][u]=c
        if(self.K.head == None):
            self.K.push(v) #colocamos los dos vertices primero el destino
            self.K.push(u)
        else:
                tmp = self.K.head
                s = tmp.data
                tmp = tmp.next
                t = tmp.data
                print("(u,v,c)",u,v,c)
                print("head (s,t,c):",s,t,self.Ady[s][t])
                if(c>self.Ady[s][t]):
                    while(c>self.Ady[s][t] and tmp != None and tmp.next != None):
                        tmp = tmp.next
                        s = tmp.data
                        tmp = tmp.next
                        t = tmp.data
                    print("inserta en :",t)
                    if(tmp == None or tmp.next == None):
                        self.K.insertar(tmp,v) #Insertar la arista despues de tmp
                        self.K.insertar(tmp,u)
                    tmp = tmp.prev
                    tmp = tmp.prev
                    self.K.insertar(tmp,v) #Insertar la arista despues de tmp
                    self.K.insertar(tmp,u)
                else:
                    self.K.push(v) #no hay nodos insertamos dos cono peso 0
                    self.K.push(u)
        self.K.listprint(self.K.head)


    # Funcion para imprimir las listas de la grafica
    def print_graph(self):
        for i in range(self.V):
            print("Lista de adjacencia del vertice {}\n".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
   
    def recorreListav(self,v):
        temp = self.graph[v] #Regresa el vertice en la posicion v de lista
        return temp
    
        
 

#dllist = doubly_linked_list()
#dllist.push(12)
#dllist.push(8)
#dllist.push(62)
#dllist.listprint(dllist.head)

#Algoritmo greedy de Krushkal
class kruskal:
   # Constructor funcion llamada cuando se crea una instancia de la clase
   def __init__(self,vertices,aristas):
        self.G = Graph(vertices) #Grafica a determinar el ciclo/recorrido de Euler
        self.P = doble_link_lista() #Lista doblemente ligada para guardar los vertices explorados del arbol recubridor
        self.TV = [[None]*3 for i in range(vertices)] #[[None] * 3] * vertices #Tabla para las banderas de cada vertice
        self.L = [None] * vertices #Lista de vertices visitados

   #Elige el vertice con peso minimo vecino a v que no esta en P
   def crearMST(self,vertices,aristas):
       node=self.G.K.head
       self.P.push(node.data) #Metemos los vertices de las aristas, por pares
       self.L.append(node.data)
       self.P.push(node.next.data)
       self.L.append(node.next.data)
       print("Primer arista:",node.data,node.next.data)
       cc=0 #numero de componentes conexas
       C=[[node.data,node.next.data]] #primer cc
       print("Componente conexa inicial",C)
       #Debemos tener en todo momento un bosque: aristas < vertices - 1
       while (self.P.longitud/2 < vertices - 1):
         node = node.next.next
         visitados = sum(x is not None for x in self.L)
         print("Arista a explorar:",node.data,node.next.data)
         print("Longitud aristas actuales",self.P.longitud)
         print("Longitud visitados",visitados)

           #Caso: los dos vertices estan en los visitados
         if(node.data in self.L and node.next.data in self.L):
               i=0
               j=0
               print("Total componentes",len(C))
               while(i < len(C)):
                    if(node.data in C[i]): break
                    else:i=i+1
               while(j < len(C)):
                    if(node.next.data in C[j]): break
                    else:j=j+1
               print("indices",i,j)
               print("Componentes",C)

               if(i != j):#distinta componente conexa
                   C[i]=(C[i]+C[j]) #concatenamos las listas
                   C.remove(C[j]) #borramso la lista 
                   print("Componente conexa actualizada con la nueva arista",C)
                   print("Caso (1,1)")
                   self.P.push(node.data)
                   node = node.next
                   self.P.push(node.data)
                   node = node.prev
                   #and not (((self.P.longitud + 2)/2 == visitados) 
                   #         or ((self.P.longitud + 2)/2 > visitados))) :
                   
           #Caso: uno de los dos vertices estan en los visitados -> agregar 
         if(node.data not in self.L and node.next.data in self.L):
               print("Caso (0,1)")
               i=0
               while(i < len(C)):
                    if(node.next.data in C[i]): break
                    else:i=i+1
               if(node.next.data in C[i]):
                   C[i].append(node.data) #agregamos el vertice a la componente
               else: C[i].append(node.next.data)
               self.P.push(node.data)
               self.L.append(node.data)
               node = node.next
               self.P.push(node.data)
               node = node.prev
           #Caso: uno de los dos vertices estan en los visitados -> agregar         
         if(node.data in self.L and node.next.data not in self.L):
               print("Caso (1,0)")
               i=0
               while(i < len(C)):
                    if(node.data in C[i]): break
                    else:i=i+1
               if(node.data in C[i]):
                   C[i].append(node.next.data) #agregamos el vertice a la componente
               else: C[i].append(node.data)
               self.P.push(node.data)
               node = node.next
               self.P.push(node.data)
               self.L.append(node.data)
               node = node.prev
           #Caso: los dos vertices no estan en los visitados -> agregar
         if(node.data not in self.L and node.next.data not in self.L
              and (self.P.longitud + 2)/2 <= visitados + 1 + 2):
               print("Caso (0,0)")
               C.append([node.data,node.next.data]) #primer cc
               cc = cc + 1
               self.P.push(node.data) #Metemos los vertices de las aristas, por pares
               self.L.append(node.data)
               self.P.push(node.next.data)
               self.L.append(node.next.data)
               
 

   def costoMST(self):
        nodo=self.P.head #iniciamos en la cabeza del camino principal
        costo = 0
        if(nodo == None): #inicialmente P esta vacia solo hay que copiar
            print("Arbol vacio")
            return
        while(nodo is not None):
                costo = costo + self.G.Ady[nodo.data][nodo.next.data]
                nodo = (nodo.next).next
        print("El costo del arbo recubridor minimo es:",costo)
          
  
# Asignar los vertices y aristas de la grafica 

"""  
if __name__ == "__main__": 
    V = 5
    E = 7
    eu = creuler(V,E)
    eu.G.add_edge(0, 1)
    eu.G.add_edge(0, 3)
    eu.G.add_edge(0, 4)
    eu.G.add_edge(1, 2)
    eu.G.add_edge(1, 3)
    eu.G.add_edge(1, 4)
    eu.G.add_edge(2, 3)
    eu.G.add_edge(3, 4)
    print(eu.G.Ady)
"""
"""
if __name__ == "__main__":
    V = 5
    E = 7
    kr = kruskal(V,E)
    kr.G.add_edge(0, 1, 3)
    kr.G.add_edge(0, 4, 4)
    kr.G.add_edge(1, 2, 1)
    kr.G.add_edge(1, 3, 2)
    kr.G.add_edge(1, 4, 1)
    kr.G.add_edge(2, 3, 5)
    kr.G.add_edge(3, 4, 2)
    #kr.G.print_graph()
""" 
if __name__ == "__main__":
    V=11
    E=17
    kr = kruskal(V,E)
    kr.G.add_edge(0,1,82)
    kr.G.add_edge(1,2,95)
    kr.G.add_edge(2,3,120)
    kr.G.add_edge(3,10,320)
    kr.G.add_edge(0,4,54)
    kr.G.add_edge(1,5,73)
    kr.G.add_edge(2,5,79)
    kr.G.add_edge(2,7,85)
    kr.G.add_edge(2,8,66)
    kr.G.add_edge(3,8,70)
    kr.G.add_edge(3,9,80)
    kr.G.add_edge(4,5,90) 
    kr.G.add_edge(5,7,62)
    kr.G.add_edge(7,8,55)
    kr.G.add_edge(8,9,87)
    kr.G.add_edge(9,10,116)
    kr.G.add_edge(5,6,61) 

    print("Arbol recubridor mínimo:")
    kr.crearMST(V,E)
    kr.P.listprint(kr.P.head)
    kr.costoMST()
   
