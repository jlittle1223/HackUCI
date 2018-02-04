
class Vertex():
    ''' This class represents a vertex in a graph '''

    def __init__(self, num:int, data=None):
        ''' initialize the vertex '''
        
        self._num = num
        self._edges = []
        self._data = data

    #Getters
    def get_num(self) -> int:
        ''' get the ID for the vertex '''
        return self._num

    def get_edges(self) -> ['Edge']:
        ''' get the edges connected to this vertex '''
        return self._edges
    
    def get_data(self):
        return self._data

    #Setters
    def add_edge(self, inEdge:'Edge') -> None:
        ''' add an edge to this vertex '''
        self._edges.append(inEdge)

    def remove_edge(self, inEdge:'Edge') -> None:
        ''' remove an edge from this vertex '''
        self._edges.remove(inEdge)
    
    def add_data(self, data):
        self._data = data
    
    
    #functions for printing
    def __str__(self) -> str:
        return "Vertex({num}, {data}, {edges})".format(
            num = self._num,
            data = self._data,
=======
            data = self.data,
            edges = ["Edge({n}, {v})".format(n = x.get_num(), v = x.get_vertices()) for x in self._edges])
