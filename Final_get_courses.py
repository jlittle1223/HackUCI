
import Courses
import bs4 as bs
import urllib.request
import re

string = '''
http://catalogue.uci.edu/allcourses/ac_eng/
http://catalogue.uci.edu/allcourses/afam/
http://catalogue.uci.edu/allcourses/anatomy/
http://catalogue.uci.edu/allcourses/anthro/
http://catalogue.uci.edu/allcourses/arabic/
http://catalogue.uci.edu/allcourses/art/
http://catalogue.uci.edu/allcourses/art_his/
http://catalogue.uci.edu/allcourses/arts/
http://catalogue.uci.edu/allcourses/asianam/
http://catalogue.uci.edu/allcourses/bana/
http://catalogue.uci.edu/allcourses/bats/
http://catalogue.uci.edu/allcourses/bio_sci/
http://catalogue.uci.edu/allcourses/biochem/
http://catalogue.uci.edu/allcourses/bme/
http://catalogue.uci.edu/allcourses/bsemd/
http://catalogue.uci.edu/allcourses/cbems/
http://catalogue.uci.edu/allcourses/chc_lat/
http://catalogue.uci.edu/allcourses/chem/
http://catalogue.uci.edu/allcourses/chinese/
http://catalogue.uci.edu/allcourses/classic/
http://catalogue.uci.edu/allcourses/clt_thy/
http://catalogue.uci.edu/allcourses/cogs/
http://catalogue.uci.edu/allcourses/com_lit/
http://catalogue.uci.edu/allcourses/compsci/
http://catalogue.uci.edu/allcourses/critism/
http://catalogue.uci.edu/allcourses/crm_law/
http://catalogue.uci.edu/allcourses/cse/
http://catalogue.uci.edu/allcourses/dance/
http://catalogue.uci.edu/allcourses/dev_bio/
http://catalogue.uci.edu/allcourses/drama/
http://catalogue.uci.edu/allcourses/e_asian/
http://catalogue.uci.edu/allcourses/earthss/
http://catalogue.uci.edu/allcourses/eco_evo/
http://catalogue.uci.edu/allcourses/econ/
http://catalogue.uci.edu/allcourses/ecps/
http://catalogue.uci.edu/allcourses/educ/
http://catalogue.uci.edu/allcourses/eecs/
http://catalogue.uci.edu/allcourses/english/
http://catalogue.uci.edu/allcourses/engr/
http://catalogue.uci.edu/allcourses/engrcee/
http://catalogue.uci.edu/allcourses/engrmae/
http://catalogue.uci.edu/allcourses/engrmse/
http://catalogue.uci.edu/allcourses/epidem/
http://catalogue.uci.edu/allcourses/euro_st/
http://catalogue.uci.edu/allcourses/fin/
http://catalogue.uci.edu/allcourses/flm_mda/
http://catalogue.uci.edu/allcourses/french/
http://catalogue.uci.edu/allcourses/gen_sex/
http://catalogue.uci.edu/allcourses/german/
http://catalogue.uci.edu/allcourses/glblclt/
http://catalogue.uci.edu/allcourses/glblme/
http://catalogue.uci.edu/allcourses/greek/
http://catalogue.uci.edu/allcourses/hebrew/
http://catalogue.uci.edu/allcourses/history/
http://catalogue.uci.edu/allcourses/human/
http://catalogue.uci.edu/allcourses/i_c_sci/
http://catalogue.uci.edu/allcourses/in4matx/
http://catalogue.uci.edu/allcourses/intl_st/
http://catalogue.uci.edu/allcourses/italian/
http://catalogue.uci.edu/allcourses/japanse/
http://catalogue.uci.edu/allcourses/korean/
http://catalogue.uci.edu/allcourses/latin/
http://catalogue.uci.edu/allcourses/linguis/
http://catalogue.uci.edu/allcourses/lit_jrn/
http://catalogue.uci.edu/allcourses/lps/
http://catalogue.uci.edu/allcourses/m_mg/
http://catalogue.uci.edu/allcourses/math/
http://catalogue.uci.edu/allcourses/mgmt/
http://catalogue.uci.edu/allcourses/mgmt_ep/
http://catalogue.uci.edu/allcourses/mgmt_fe/
http://catalogue.uci.edu/allcourses/mgmt_hc/
http://catalogue.uci.edu/allcourses/mgmtmba/
http://catalogue.uci.edu/allcourses/mgmtphd/
http://catalogue.uci.edu/allcourses/mol_bio/
http://catalogue.uci.edu/allcourses/mpac/
http://catalogue.uci.edu/allcourses/music/
http://catalogue.uci.edu/allcourses/net_sys/
http://catalogue.uci.edu/allcourses/neurbio/
http://catalogue.uci.edu/allcourses/nur_sci/
http://catalogue.uci.edu/allcourses/path/
http://catalogue.uci.edu/allcourses/ped_gen/
http://catalogue.uci.edu/allcourses/persian/
http://catalogue.uci.edu/allcourses/pharm/
http://catalogue.uci.edu/allcourses/philos/
http://catalogue.uci.edu/allcourses/phrmsci/
http://catalogue.uci.edu/allcourses/phy_sci/
http://catalogue.uci.edu/allcourses/physics/
http://catalogue.uci.edu/allcourses/physio/
http://catalogue.uci.edu/allcourses/pol_sci/
http://catalogue.uci.edu/allcourses/portug/
http://catalogue.uci.edu/allcourses/pp_d/
http://catalogue.uci.edu/allcourses/psy_beh/
http://catalogue.uci.edu/allcourses/psych/
http://catalogue.uci.edu/allcourses/pub_pol/
http://catalogue.uci.edu/allcourses/pubhlth/
http://catalogue.uci.edu/allcourses/rel_std/
http://catalogue.uci.edu/allcourses/rotc/
http://catalogue.uci.edu/allcourses/russian/
http://catalogue.uci.edu/allcourses/soc_sci/
http://catalogue.uci.edu/allcourses/socecol/
http://catalogue.uci.edu/allcourses/sociol/
http://catalogue.uci.edu/allcourses/spanish/
http://catalogue.uci.edu/allcourses/spps/
http://catalogue.uci.edu/allcourses/stats/
http://catalogue.uci.edu/allcourses/tox/
http://catalogue.uci.edu/allcourses/ucdc/
http://catalogue.uci.edu/allcourses/uni_aff/
http://catalogue.uci.edu/allcourses/uni_stu/
http://catalogue.uci.edu/allcourses/vietmse/
http://catalogue.uci.edu/allcourses/vis_std/
http://catalogue.uci.edu/allcourses/writing/
'''

ignore = ["Placement", "Satisfactory", "One", "Basic", "C++", "An", "Undergraduate-level", "Successful", "Prior",
          "Limited", "Three", "Completion", "Two", "High", "Recommended", "Advancement", "Prerequisites",
          "Student", "Prerequisite"]

f = open("big_dict.txt","w")

for url in string.split('\n'):
##    print(url)
    try:
        source = urllib.request.urlopen(url).read()

        soup = bs.BeautifulSoup(source, 'lxml')

        tags = soup.find_all('p')

        L = []
        name = ''
        flag = False
        for i in tags:
            if 'courseblocktitle' in str(i):
                pattern = re.compile('>([a-zA-Z0-9\s]+).')
                m = pattern.search(str(i))
                name = str(m.group(1))
            if 'Prerequisite: ' in str(i):
                preq = i.text
                temp = preq[:]
                temp = temp[14:].split()
                if temp[0] in ignore:
                    pass
                else:
                    course = Courses.Course(name, preq.rstrip('\n'))
                    L.append(course)

        for i in L:
            f.write(i.return_info())
    except:
        pass

f.close()
        
        

