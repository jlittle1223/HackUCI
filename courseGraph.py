from vertex import Vertex
from edge import Edge
from edge import DirectedEdge
from edge import DirectedDisjunctionEdge
from graph import DirectedGraph
from course import Course



class CourseGraph(DirectedGraph):
    def __init__(self, vertex_nums:[int] = [], edges_to_add:[(int,int)] = []):
        DirectedGraph.__init__(self, vertex_nums, edges_to_add)
        
        
        
    def add_vertex(self, vertex_num:int, data, edges_to_add:[int] = []) -> None:
        ''' add a vertex to the graph 
        Here the edges to add will flow from the new vertex to the indicated vertices. '''
        
        v = Vertex(vertex_num)
        v.add_data(data)
        self._vertices.append(v)
        
        for item1 in edges_to_add:
            for item2 in self._vertices:
                if item2.get_num() == item1:
                    v_to_add = item2
            
            self.add_edge(v, v_to_add)
            
            
    def add_disjunction_edge(self, source:'Vertex', destination:'Vertex', disjunctionID) -> None:
        ''' add an edge to the graph ''' 
        
        self._edge_counter += 1
        
        e = DirectedDisjunctionEdge(self._edge_counter, source, destination, disjunctionID)
        self._edges.append(e)
        source.add_edge(e)
        destination.add_edge(e)
            
    
        
    def __str__(self) -> str:
        return "DirectedGraph({num}, {vertices}, {edges})".format(
            num = self._num, 
            vertices = ["Vertex({n} = {data})".format(n = x.get_num(), data = x.get_data()) for x in self._vertices],
            edges = ["DirectedEdge({n}, {v1} -> {v2})".format(n = y.get_num(), v1 = y.get_vertices()[0].get_data(), v2 = y.get_vertices()[1].get_data()) for y in self._edges])






if __name__ == "__main__":
    ics6b = Course("ICS6B")
    ics6d = Course("ICS6D")
    math2b = Course("MATH2B")
    ics6n = Course("ICS6N")
    math3a = Course("MATH3A")
    ics46 = Course("ICS46")
    
    cs161 = Course("CS161")
    
    cs161.addPrerequisite(ics6b)
    cs161.addPrerequisite(ics6d)
    cs161.addPrerequisite(math2b)
    cs161.addPrerequisiteDisjunction([ics6n, math3a])
    cs161.addPrerequisite(ics46)
    
    g1 = CourseGraph()
    g1.add_vertex(0, cs161)
    g1.add_vertex(1, ics6b, [0])
    g1.add_vertex(2, ics6d, [0])
    g1.add_vertex(3, math2b, [0])
    
    g1.add_vertex(4, ics6n)
    g1.add_vertex(5, math3a)
    ics6n_vertex = g1.get_vertex(4)
    math3a_vertex = g1.get_vertex(5)
    g1.add_disjunction_edge(ics6n_vertex, g1.get_vertex(0), 0)
    g1.add_disjunction_edge(math3a_vertex, g1.get_vertex(0), 0)
    
    g1.add_vertex(6, ics46, [0])
    
    print(g1)
    
    




