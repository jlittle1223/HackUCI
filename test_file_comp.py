import file_util

filepath_bdict = "githubtemp/HackUCI-master/HackUCI-master/big_dict.txt"
filepath_major = "githubtemp/HackUCI-master/HackUCI-master/Major_Classes/schoolofphysicalsciencesdepartmentofmathematics.txt"
filepath_new = "TEST.txt"


        
        
            
    







bdict = open(filepath_bdict, 'r')
major = open(filepath_major, 'r')
test = open(filepath_new, 'w')




removed_character_list = []
for line in bdict:
    line = line.replace("&", "")
    removed_character_list.append(line)
    
bdict.close()
bdict = open(filepath_bdict, 'w')    

    
for i in range(len(removed_character_list)):
    bdict.write(removed_character_list[i])
    
bdict.close()
bdict = open(filepath_bdict, 'r')



bdict_line_list = []
major_line_list = []


for bdict_line in bdict:
    bdict_line_split = bdict_line.split(':')
    
    bdict_line_list.append(bdict_line_split)
    
    major_line_scoped = ""
    for major_line in major:
        major_line = major_line.strip()
        major_line_scoped = major_line.replace("\n", "")
        major_line_scoped = major_line.replace(" ", "")
        major_line_scoped = major_line.replace(" ", "")
        
        major_line_list.append(major_line_scoped)
        
        
    

major.close()
bdict.close()






for bdict_line in bdict_line_list:
    #print("bdict = {}".format(bdict_line))
    for major_line in major_line_list:
        #print("{} == {}".format(bdict_line, major_line))
        if bdict_line[0] == major_line:
            #print("MATCH")
            #print("{} == {}".format(bdict_line[0], major_line))
            prerequisite_string = file_util.remove_spaces(bdict_line[1])
            test.write(bdict_line[0] + ":" + prerequisite_string)



test.close()










