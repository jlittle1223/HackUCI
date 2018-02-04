from course import Course

and_string = " and "
or_string = " or "


test_string = "CS177:MATH2B and STATS67 and ICS6B and ICS6D and (MATH 3A or ICS6N)"

#test_string = "ICS51:ICS31 and ICS6B"

test_string = "blah blah aldsf;j"


def remove_spaces(prerequisite_string):
    '''
    if you find a space and the next word is not "and" or "or",
    then remove that space except after one of those words
    '''
    space_index = None
    end_index = 0
    start_index = 0
    
    new_string = ""
    final_string = ""
    
    temp_string = ""
    bool_tracker = ""
    
    has_and = False
    has_or = False
    
    c = 0
    
    for i in range(len(prerequisite_string)):
        
        if c >= len(prerequisite_string):
            return final_string
        temp_string += prerequisite_string[c]
        bool_tracker += prerequisite_string[c]
        end_index += 1
        
            
        if and_string in bool_tracker:
            has_and = True
            new_string = temp_string[:-len(and_string)]
            new_string = new_string.replace(" ", "")
            new_string = new_string.replace(" ", "")
            if new_string != new_string.upper():
                bool_tracker = ""
                temp_string = ""
                final_string = final_string[:-len(and_string)]
                break
            new_string += and_string
            final_string += new_string
            #c += len(and_string)
            bool_tracker = ""
            temp_string = ""
            continue
        
        if or_string in bool_tracker:
            has_or = True
            new_string = temp_string[:-len(or_string)]
            print("new string = ", new_string)
            new_string = new_string.replace(" ", "")
            new_string = new_string.replace(" ", "")
            if new_string != new_string.upper():
                bool_tracker = ""
                temp_string = ""
                final_string = final_string[:-len(or_string)]
                break
            new_string += or_string
            final_string += new_string
            print("final string in or loop",final_string)
            #c += len(or_string)
            bool_tracker = ""
            temp_string = ""
            continue
        
        c += 1
        
    if (not has_and and not has_or):
        final_string = temp_string.strip().replace(" ", "")
        

    if has_and:
        if final_string[-len(and_string):] == and_string:
            return final_string[:-len(and_string)] + "\n"
    if has_or:
        if final_string[-len(or_string):] == or_string:
            return final_string[:-len(or_string)] + "\n"
    
        
    '''
    if final_string[len(final_string) - len(and_string):] == and_string:
        final_string = final_string[:len(final_string) - len(and_string)]
    elif final_string[len(final_string) - len(or_string):] == or_string:
        final_string = final_string[:len(final_string) - len(or_string)]
    '''
    
        
    final_string += "\n"
    print("final_string = {}".format(final_string))
    return final_string
            





def make_course_list_from_file(filename:str):
    course_list = []
    file = open(filename, 'r')
    
    for line in file:
        line = line.replace("\n", "")
        if (contains_course_name(line)):
            course = make_course_from_line(line)
            course_list.append(course)
    
    file.close()
    
    return course_list



def contains_course_name(course_string:str):
    max_course_name_length = 10
    for i in range(len(course_string)):
        if course_string[i] == ":":
            return True
        if and_string in course_string:
            return True
        if or_string in course_string:
            return True
        if i > max_course_name_length:
            return False
        
    return False



def make_course_from_line(course_string:str):
    course_name = ""
    finished_course_name = False
    index = 0
    for char in course_string:
        if not (finished_course_name):
            if char == ":":
                finished_course_name = True
                index += 1
                break
            else:
                course_name += char
        index += 1
    
    course = Course(course_name.upper())
    
    prerequisite_list = get_prerequisite_list_from_line(course_string[index:])
    
    
    course.addPrerequisites(prerequisite_list)
    
    
    
    
    
    return course



def get_index_of_end_of_first_course_name(course_string):
    temp = ''
    for i in range(len(course_string)):
        temp += course_string[i]
        if course_string[i] == ":":
            return i - 1
        if ")" in temp:
            i -= 1
                
            return i
        if and_string in temp:
            return i - len(and_string)
        if or_string in temp:
            return i - len(or_string)
        
    return len(course_string) - 1
            
        
        
def course_already_in_list(course, course_list):
    for c in course_list:
        if course.name == c.name:
            return True
        
    return False


def get_prerequisite_list_from_line(prerequisite_string):
    start_index = 0
    end_index = 0
    temp_string = ""
    prerequisite_list = []
    last_logic = None
    
    disjunction = False
    open_paren_index = 0
    close_paren_index = 0
    in_parens = False
    
    
    
    for i in range(len(prerequisite_string)):
        end_index += 1
        temp_string += prerequisite_string[i]
        
        if(prerequisite_string[i] == "("):
            open_paren_index = i
            in_parens = True
            
        
        
        if and_string in temp_string:
            last_logic = and_string
            
            
            
            slice_to_index = end_index - len(and_string)
            
            while prerequisite_string[start_index] == "\"":
                start_index += 1
            
            while prerequisite_string[slice_to_index - 1] == "\"":
                slice_to_index -= 1
                
            while prerequisite_string[start_index] == ",":
                start_index += 1
            
            while prerequisite_string[slice_to_index - 1] == ",":
                slice_to_index -= 1
            
            while prerequisite_string[start_index] == "(":
                start_index += 1
            
            while prerequisite_string[slice_to_index - 1] == ")":
                slice_to_index -= 1
            
            
            prerequisite_name = prerequisite_string[start_index:slice_to_index]
                        
            print("AND PREREQUISITE NAME = {}".format(prerequisite_name))
            
            start_index = end_index
            temp_string = ""
            
            prerequisite = Course(prerequisite_name)
            prerequisite_list.append(prerequisite)
            
            
            
            
        elif or_string in temp_string:
            
            last_logic = or_string
            disjunction_list = []
            disjunction = True
            
            slice_to_index = end_index - len(or_string)
            
            while prerequisite_string[slice_to_index - 1] == "\"":
                print("subtracted")
                slice_to_index -= 1
            
            while prerequisite_string[start_index] == "\"":
                start_index += 1
                
            while prerequisite_string[slice_to_index - 1] == ",":
                print("subtracted")
                slice_to_index -= 1
            
            while prerequisite_string[start_index] == ",":
                start_index += 1
            
            
            while prerequisite_string[slice_to_index - 1] == ")":
                print("subtracted")
                slice_to_index -= 1
            
            while prerequisite_string[start_index] == "(":
                start_index += 1
            
            prerequisite_name = prerequisite_string[start_index:slice_to_index]
            
            print("first prerequisite name = {}".format(prerequisite_name))
            
            prerequisite = Course(prerequisite_name)
            
            start_index = end_index
            
            while prerequisite_string[start_index] == "(":
                start_index += 1
            
            if not course_already_in_list(prerequisite, disjunction_list):
                disjunction_list.append(prerequisite)
            
            
            after_string = prerequisite_string[start_index:]
            after_name_index = get_index_of_end_of_first_course_name(after_string) + 1
            
            while after_string[after_name_index - 1] == ")":
                print("subtracted")
                after_name_index -= 1
            
            second_prerequisite_name = after_string[:after_name_index]
            second_prerequisite = Course(second_prerequisite_name)
            print("Second course name = {}".format(second_prerequisite.name))
            
            print("Second prerequisite name = {}".format(second_prerequisite_name))
            
            if not course_already_in_list(second_prerequisite, disjunction_list):
                disjunction_list.append(second_prerequisite)
            
            
            print("DISJUNCTION LIST", disjunction_list)
            
            temp_string = ""
            
            
            prerequisite_list.append(disjunction_list)
        
        
        
        if i == len(prerequisite_string) - 1:
            prerequisite_name = prerequisite_string[start_index:]
            prerequisite = Course(prerequisite_name)
            if last_logic == and_string or last_logic == None:
                if len(prerequisite_name.strip()) > 0:
                    prerequisite_list.append(prerequisite)
    
        
    return prerequisite_list


def get_disjunction_list_from_line(prerequisite_string):
    '''
    if you see an ' or ', add the course before the ' or '
    to the disjunction list and check if the course after is
    followed by an ' or '. If it is NOT, add the course to the
    disjunction list and continue searching the string. If it IS 
    followed by an ' or ' then add the course to the disjunction 
    list and continue to check the courses after 
    '''
    
    disjunction_list = []
    
    


if __name__ == "__main__":
    filename = "testPrerequisites.txt"
    path = "majors/"
    course_list = make_course_list_from_file(path + filename)
    







            



