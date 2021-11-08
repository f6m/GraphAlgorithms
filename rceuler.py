#https://docs.python.org/2/tutorial/datastructures.html
# compilacion: $python3 creuler.py

#LISTA DOBLE LIGADA PARA EL CAMINO P
class Node: #self refiere a la instancia de la clase
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None


class doubly_linked_list:
   def __init__(self):
      self.head = None #Se invoca al principio
      self.longitud = 0 #Longitud de la lista
# Adding data elements		
   def push(self, NewVal):
      self.longitud = self.longitud + 1
      NewNode = Node(NewVal)
      NewNode.next = self.head #NewNode.next -> head
      if self.head is not None:
         self.head.prev = NewNode # head tiene prev puesto que ya apunta a un nodo head.prev -> NewNode
      self.head = NewNode #NewNode.next -> head -> NewNode

   def insertar(self,prev_node,NewVal):
      if prev_node is None:
         return
      self.longitud = self.longitud + 1
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

# Imprimir la lista doble ligada		
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next #Desplazamiento hacia la derecha

# LISTAS DE ADYACENCIA PARA LA GRAFICA G

# Clase para los nodos en las lista de adyacencia de un vertice
# (vertex,next)
class AdjNodo:
    def __init__(self, data):
        self.vertex = data
        self.next = None
  
  
# Una clase para representar la grafica mediante sus listas 
# de adyacencia. El tamano del arreglo sera el numero de vertices V

class Graph:
    def __init__(self, vertices):
        self.V = vertices #orden de la grafica
        self.graph = [None] * self.V #no es necesario inidicar de que tipo de dato es una variable 
        self.Ady = [[None]*self.V for i in range(self.V)] #Arreglo bidimensional para la matriz de adyacencia en lugar de una lista anidada

    #Tipo de dato none: declara un arreglo de V None's

    # Funcion para agregar una arista
    def add_edge(self, src, dest):
        # Agregar el nodo destino al nodo origen src
        node = AdjNodo(dest) #Crea el dato vertice adyacente a src el primero.
        node.next = self.graph[src] #node.next es/apunta al array graph con indice src
        self.graph[src] = node #graph[src] contiene node con data=dest,next=graph[src]
        self.Ady[src][dest]=1	
	#Los indices para las etiquetas son 0,1,2,3,...,V-1
  	# Cuando se vuelve agregar otro con mismo src remplaza el actual graph[src]
	# pero antes se enlaza con node.next=graph[src] apuntando al actual, despues se remplaza.
        # Agrega el nodo origen al nodo destino pues es una grafica simple
        node = AdjNodo(src) #vuelve a usar la var. node y crea la otra direccion de la arista
        node.next = self.graph[dest]
        self.graph[dest] = node #el arreglo en posicion dest tiene el nodo src,
        self.Ady[dest][src]=1
    
    # Funcion para determinar los vertices (si existen de grado impar) o si existen mas de tres
    # o si todos son pares.
    def gradosimpar(self):
        d = [0] * self.V
        impares = [None,None]
        totimpar=0
        for i in range(self.V):
                j=0
                temp = self.graph[i]
                while temp:
                  temp = temp.next
                  j = j + 1
                if(j%2==0):
                  d[i]=i #asignamos i pues es el indice del vertice
                else:
                  d[i]=i
                  impares[totimpar]=i #estoy usando totimpar auxiliarmente como indice pues son 2
                  totimpar = totimpar + 1
        
        if(totimpar == 0):
           return 0 #Regresa
        if(totimpar == 2):
           return impares #Regresa los dos impares
        if(totimpar > 2):
           return 1 #Regresa la advertencia
	
  
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
        temp = self.graph[v]
        return temp
    
        
 

#dllist = doubly_linked_list()
#dllist.push(12)
#dllist.push(8)
#dllist.push(62)
#dllist.listprint(dllist.head)

 
# This code is contributed by Kanav Malhotra


class creuler: 
   def __init__(self,vertices,aristas):
        self.G = Graph(vertices) #Grafica a determinar el ciclo/recorrido de Euler
        self.P = doubly_linked_list() #Lista doblemente ligada
        self.TV = [[None]*3 for i in range(vertices)] #[[None] * 3] * vertices #Tabla para las banderas de cada vertice
        self.L = [None] * vertices #Lista de vertices visitados

   def recorreListavNoVisitada(self,v):
        temp=self.G.recorreListav(v)
        print("VERTICE HEAD",v) 	
        print("VERTICE A EXPLORAR",temp.vertex) 	
        while(self.G.Ady[v][temp.vertex] == 2 and self.G.Ady[temp.vertex][v] == 2 and temp.next != None): #arista vistada y no es el final 
          print("Entra while recorreListavVisitada vertice",v)
          temp = temp.next
          print("VERTICE CON ARISTA EXPLORADA",temp.vertex)
        print("VERTICE CON ARISTA NO EXPLORADA",temp.vertex)
        return temp

   def incorporar(self,Pi,inc):
        nodo=self.P.head #iniciamos en la cabeza del camino principal
        if(nodo == None): #inicialmente P esta vacia solo hay que copiar
          tempo=Pi.head #recorremos los nodos de Pi para copiarlos a P
          while(tempo.next != None):
            self.P.push(tempo.data) #pushamos 
            tempo=tempo.next #avanzamos
          self.P.push(tempo.data)
          return	
        while (nodo is not None and nodo.data != inc): #Busca el nodo en la lista con data=inc
          nodo = nodo.next #Desplazamiento hacia la derecha en P
        tmp = Pi.head
        print("DATO A INSERTAR:",tmp.data)
        self.P.insertar(nodo.prev,tmp.data) #mandamos a insertar en el anterior
        while(tmp != None and nodo != None): #mientras no llege al final de Pi
          print("A insertar:",nodo,tmp.data)
          if(nodo.prev is not None):
            self.P.insertar(nodo.prev,tmp.data)
            self.P.listprint(self.P.head)
            nodo=nodo.prev #retrocedemos para cazar los índices.
          tmp=tmp.next #avanza en Pi
          nodo = nodo.next #avanza en P
          
	
   def trazarP(self,v,Pi):
        Ev = None #Arista sobre la lista doble del camino inicial, incidente con v
        Pi.push(v) #Acts en Pi luego copiamos en el respectivo vertice a P
        Nv=self.recorreListavNoVisitada(v)
        inc=v #indice a incorporar   
        #Repeat
        i=1
        while(self.G.Ady[v][Nv.vertex]!=2 and Nv != None):
          print('\x1b[6;30;42m' + "Entra al while it:" + '\x1b[0m',i)
          print(self.G.Ady)
          if(self.TV[v][0]==None):#La primera bandera de la tabla TV es si v esta visitado
            self.TV[v][0]=1 #Visitado
            self.L.append(v)
            self.L.remove(None)
          while(self.G.Ady[v][Nv.vertex]==2 and Nv.next != None):
            Nv=self.recorrerlistaNoVisitada(Nv.vertex)
            #Nv=Nv.next
          if(self.G.Ady[v][Nv.vertex]==2 and Nv.next == None): #vertex visitado y no hay siguiente:FIN
            print("Fin del ciclo")
            return
          e=Nv.vertex
          print("Actual vértice",v)
          print("Siguiente vértice",e)
          Pi.push(e) #Colocamos el siguiente vertice en la lista doble del camino inicial
          if(Ev==None):
            Ev=e #Ev apunta una arista sobre P que ha sido recorrida desde v
          self.G.Ady[v][e]=2 #Arista e visitada
          self.G.Ady[e][v]=2 #Arista e visitada
          v=e #Escalar
          Nv=self.recorreListavNoVisitada(v)
          print("Vertice terminal de la arista visitada e:",Nv.vertex)
          i=i+1
          print("Valor de la matriz de Ady",self.G.Ady[v][Nv.vertex])
        #self.G.print_graph()
        print("Lista a incoroporar")
        Pi.listprint(Pi.head)
        self.incorporar(Pi,inc) #Al final asignamos una copia del camino inicial self.P
        print("Lista del camino actual")
        self.P.listprint(self.P.head)
        #print("Lista incorporada")
        #self.P.listprint(self.P.head)

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
    V=10
    E=15
    eu = creuler(V,E)
    eu.G.add_edge(0,1)
    eu.G.add_edge(1,2)
    eu.G.add_edge(2,3)
    eu.G.add_edge(3,4)
    eu.G.add_edge(4,0)
    eu.G.add_edge(0,5)
    eu.G.add_edge(1,5)
    eu.G.add_edge(1,6)
    eu.G.add_edge(2,6)
    eu.G.add_edge(2,7)
    eu.G.add_edge(3,7)
    eu.G.add_edge(3,8)
    eu.G.add_edge(4,8) 
    eu.G.add_edge(4,9)
    eu.G.add_edge (0,9) 
"""
if __name__ == "__main__":
    V = 5
    E = 7
    eu = creuler(V,E)
    eu.G.add_edge(0, 1)
    eu.G.add_edge(0, 4)
    eu.G.add_edge(1, 2)
    eu.G.add_edge(1, 3)
    eu.G.add_edge(1, 4)
    eu.G.add_edge(2, 3)
    eu.G.add_edge(3, 4)
    print(eu.G.gradosimpar())

    if(eu.G.gradosimpar()==1):
        print("G no tiene recorrido ni circuito de Euler!!")
    else:
        if(eu.G.gradosimpar()==0):
            v=0#eu.G.graph[0]
            print("G tiene un circuito de Euler!! Lo iniciamos en",v)
        else:
            d=eu.G.gradosimpar()
            v=d[0]
            print("G tiene un recorrido de Euler!! Lo iniciamos en",v,d)
    Pi = doubly_linked_list() #Lista doble ligadura
    eu.trazarP(v,Pi)
    print("Vertices visitados:",eu.L)
    print("Camino P actual:")
    eu.P.listprint(eu.P.head)
    print("Longitud de P:")
    print(eu.P.longitud)

    if(eu.P.longitud == E+1):
        print("El recorrido/circutio euleriano se encontro en el recorrido inicial P")
        eu.P.listprint(eu.P.head)
        exit(1)       
    else:
       print("Se agregarán circuitos")
       for i in range(len(eu.L)):
         while(eu.P.longitud < E+1):
           Pi = doubly_linked_list()
           eu.trazarP(eu.L[i],Pi)

    #Revisar la conexidad con la lista de vertices visitados.
    #Subrecorrido
