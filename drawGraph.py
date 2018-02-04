
#import matplotlib.pyplot as plt
import networkx as nx
import pydot
import sys

from edge import DirectedEdge
from edge import DirectedDisjunctionEdge
from course import Course
from courseGraph import CourseGraph

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'



def courseGraphToNetworkxDiGraph(CG:"CourseGraph") -> "nx.Digraph":
    DG = nx.DiGraph()
    
    for vertex in CG.get_vertices():
        DG.add_node(vertex.get_data())
        
    for edge in CG.get_edges():
        if type(edge) == DirectedDisjunctionEdge:
            DG.add_edge(edge.get_source().get_data(), edge.get_destination().get_data(), color = get_color_by_ID(edge.disjunctionID))
        else:
            DG.add_edge(edge.get_source().get_data(), edge.get_destination().get_data())

        
    return DG


def get_color_by_ID(ID:int) -> "color":
    colorList = ["blue", "orange", "green", "red", "purple", "yellow"]
    color = colorList[ID % len(colorList)]
    return color

def draw_graph(G:"CourseGraph"):
    DG = courseGraphToNetworkxDiGraph(G)
    nx.draw(DG, with_labels = True)

def write_graph_to_dot(G:"CourseGraph", filepath):
    DG = courseGraphToNetworkxDiGraph(G)
    
    nx.drawing.nx_pydot.write_dot(DG, filepath + ".dot")
    
    
def write_from_file_to_png(filepath_in, filepath_out):
    G = nx.drawing.nx_pydot.read_dot(filepath_in)
    PG = nx.drawing.nx_pydot.to_pydot(G)
    PG.write_png(filepath_out + ".png")
    
    
def write_graph_to_png(G:"CourseGraph", filepath):
    DG = courseGraphToNetworkxDiGraph(G)
    PG = nx.drawing.nx_pydot.to_pydot(DG)
    PG.write_png(filepath + ".png")
    




if __name__ == "__main__":
    
    ics6b = Course("ICS6B")
    ics6d = Course("ICS6D")
    math2b = Course("MATH2B")
    math2a = Course("MATH2A")
    ics6n = Course("ICS6N")
    math3a = Course("MATH3A")
    ics46 = Course("ICS46")
    ics45c = Course("ICS45C")
    ics33 = Course("ICS33")
    ics32 = Course("ICS32")
    ics31 = Course("ICS31")
    cs161 = Course("CS161")
    stats67 = Course("STATS67")
    stats7 = Course("STATS7")
    stats120a = Course("STATS120A")
    cs178 = Course("CS178")
    
    math2b.addPrerequisite(math2a)
    ics46.addPrerequisite(ics45c)
    ics45c.addPrerequisite(ics33)
    ics33.addPrerequisite(ics32)
    ics32.addPrerequisite(ics31)
    stats67.addPrerequisite(math2b)
    cs161.addPrerequisites([ics6b, ics6d, math2b, ics46])
    cs178.addPrerequisites([math2b, [stats67, [stats7, stats120a]], ics6b, ics6d, [math3a, ics6n]])
    

    course_list = [ics6b, ics6d, math2b, math2a, stats67, stats7, stats120a, ics6n, math3a, ics46, ics45c, ics33, ics32, ics31, cs161, cs178]
    
    g1 = CourseGraph([], [], course_list)
    
    filename = "simple_graph.dot"
    path = "graphs/" + filename
    
    write_graph_to_dot(g1, path)





