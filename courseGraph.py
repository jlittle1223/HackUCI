from vertex import Vertex
from edge import Edge
from edge import DirectedEdge
from edge import DirectedDisjunctionEdge
from graph import DirectedGraph
from course import Course




class CourseGraph(DirectedGraph):
    def __init__(self, vertex_nums:[int] = [], edges_to_add:[(int,int)] = [], course_list = []):
        DirectedGraph.__init__(self, vertex_nums, edges_to_add)
        
        self.disjunctionCount = 0
        
    
        for i in range(len(course_list)):
            self.add_vertex(i, course_list[i])
        
        for i in range(len(course_list)):
            destination = self.get_vertex_by_data(course_list[i])
            #print("Course = {}. Destination = {}".format(course_list[i], destination.get_data()))
            self.add_prerequisite_list_to_graph(course_list[i].prerequisites, destination, False)
        
            
    
    def add_prerequisite_list_to_graph(self, prerequisite_list, destination, disjunction):
        #print("Course = {}. #Prerequisites = {}".format(destination.get_data(), len(prerequisite_list)))
        for i in range(len(prerequisite_list)):
            if type(prerequisite_list[i]) == list:
                self.add_prerequisite_list_to_graph(prerequisite_list[i], destination, True)
                self.disjunctionCount += 1
            else:
                source = self.get_vertex_by_data(prerequisite_list[i])
                
                if source == None:
                    self.add_vertex(i, prerequisite_list[i])
                    source = self.get_vertex_by_data(prerequisite_list[i])
                
                if (disjunction):
                    try:
                        self.add_disjunction_edge(source, destination, self.disjunctionCount)
                    except:
                        print("Type = {}".format(type(prerequisite_list[i])))
                        print("Caught: {} IS THE PROBLEM COURSE".format(prerequisite_list[i]))
                        print("Their source is {}".format(source))
                else:
                    try:
                        self.add_edge(source, destination)
                    except:
                        print("Type = {}".format(type(prerequisite_list[i])))
                        print("Caught: {} IS THE PROBLEM COURSE".format(prerequisite_list[i].name))
                        print("Their source is {}".format(source))
                
    
    
                
    
    def get_vertex_by_data(self, data) -> 'Vertex':
        ''' returns the vertex object with the given ID '''
        
        vertex_to_return = None
        for item in self._vertices:
            if item.get_data().name == data.name:
                vertex_to_return = item
                
        if(vertex_to_return == None):
            for item in self._vertices:
                pass
                #print("{} == {}".format(item.get_data().name, data.name))
        
        return vertex_to_return 
        
        
        
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
    
    course_list = [ics6b, ics6d, math2b, math2a, ics6n, math3a, ics46,
                   ics45c, ics33, ics32, ics31, cs161]
    
    g1 = CourseGraph([], [], course_list)
    
    
    print(g1)
    
    




