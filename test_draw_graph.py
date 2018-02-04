import file_util
from courseGraph import CourseGraph
import drawGraph
from course import Course
import networkx as nx




if __name__ == "__main__":
    filename = "TEST.txt"
    path = ""
    
    filepath_in = "simple_graph_copy.dot"
    
    course_list = file_util.make_course_list_from_file(path + filename)
    for course in course_list:
        #print(course, "prerequisites =")
        for prerequisite in course.prerequisites:
            #print("    ", prerequisite)
            pass
    
    #print(course_list[1].prerequisites[0])
    #print(course_list[0])
    
    
    g1 = CourseGraph([], [], course_list)
    
    filename = "simple_graph"
    path = "graphs/" + filename
    
    
    drawGraph.draw_graph(g1)
    #drawGraph.write_graph_to_dot(g1, path)
    #drawGraph.write_graph_to_png(g1, path)
    
    drawGraph.write_from_file_to_png("graphs/" + filepath_in, 'MathGraph')
    





