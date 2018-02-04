
import bs4 as bs
import urllib.request
import re

string = '''
http://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofart/#majortext
http://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdance/#majortext
http://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdrama/#majortext
http://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofmusic/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofmolecularbiologyandbiochemistry/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofdevelopmentalandcellbiology/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofdevelopmentalandcellbiology/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofecologyandevolutionarybiology/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/#ExerciseSciences
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofdevelopmentalandcellbiology/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/#humanbiology
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofmolecularbiologyandbiochemistry/#majortext
http://catalogue.uci.edu/schoolofbiologicalsciences/departmentofneurobiologyandbehavior/#majortext
http://catalogue.uci.edu/thepaulmerageschoolofbusiness/undergraduateprograms/#majorstext
http://catalogue.uci.edu/schoolofeducation/#majortext
http://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofbiomedicalengineering/#majorstext
http://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofchemicalengineeringandmaterialsscience/#majorstext
http://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofcivilandenvironmentalengineering/#majorstext
http://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofelectricalengineeringandcomputerscience/#majorstext
http://catalogue.uci.edu/thehenrysamuelischoolofengineering/departmentofmechanicalandaerospaceengineering/#majorstext
http://catalogue.uci.edu/schoolofhumanities/departmentofafricanamericanstudies/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofarthistory/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofasianamericanstudies/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofclassics/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofcomparativeliterature/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofeastasianlanguagesandliteratures/#majorstext
http://catalogue.uci.edu/schoolofhumanities/departmentofenglish/#majorstext
http://catalogue.uci.edu/schoolofhumanities/departmentoffilmandmediastudies/#majortext
http://catalogue.uci.edu/schoolofhumanities/departmentofgenderandsexualitystudies/#majortext
http://catalogue.uci.edu/schoolofhumanities/undergraduateprograminglobalcultures/#majortext
http://catalogue.uci.edu/globalmiddleeaststudies/#majortext
http://catalogue.uci.edu/sueandbillgrossschoolofnursing/#undergraduatetext
http://catalogue.uci.edu/departmentofpharmaceuticalsciences/#undergraduatetext
http://catalogue.uci.edu/schoolofphysicalsciences/departmentofchemistry/#majortext
http://catalogue.uci.edu/schoolofphysicalsciences/departmentofearthsystemscience/#majorstext
http://catalogue.uci.edu/schoolofphysicalsciences/departmentofmathematics/#majorstext
http://catalogue.uci.edu/schoolofphysicalsciences/departmentofphysicsandastronomy/#undergraduatetext
http://catalogue.uci.edu/programinpublichealth/#undergraduatetext
http://catalogue.uci.edu/schoolofsocialecology/#undergraduatetext
http://catalogue.uci.edu/schoolofsocialecology/departmentofcriminologylawandsociety/#majortext
http://catalogue.uci.edu/schoolofsocialecology/departmentofplanningpolicyanddesign/#majortext
http://catalogue.uci.edu/schoolofsocialecology/departmentofpsychologyandsocialbehavior/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofanthropology/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofchicanolatinostudies/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofcognitivesciences/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofeconomics/#majorstext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofpoliticalscience/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/departmentofsociology/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/theundergraduatemajorininternationalstudies/#majortext
http://catalogue.uci.edu/schoolofsocialsciences/theundergraduatemajorinsocialpolicyandpublicservice/#majortext
'''

for url in string.split('\n'):
    try:
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        temp = url.split('/')
        file_name = temp[3] + temp[4]+ '.txt'
        f = open(file_name,'w')

        L = []
        flag = False
        for line in soup.body:
            line = str(line)
            temp = line.split('<')
            for i in temp:
                if ('Requirements for the B.' in i):
                    flag = True
                if flag:
                    L.append(i)

        classes = set()
        for i in L:
            if 'showCourse(this, ' in i:
                pattern = re.compile('title=\"([a-zA-z0-9\s&;]+)')
                m = pattern.search(i)
                if m:
                    classes.add(m.group(1))
        for i in sorted(classes):
            f.write(i + '\n')
        f.close()
    except:
        pass

    


