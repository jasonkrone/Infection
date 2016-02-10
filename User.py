'''
By Jason Krone for Khan Academy

Defines User class
'''



class User(object):
'''
Representation of Khan Academy User 
'''  

    def __init__(self, site_version, coaches=None, students=None):
        '''
        coached_by : the coaches for this user
        coach_for  : who this user coaches
        ''' 

        self.site_version = site_version
        self.coaches = coaches
        self.students = 


    def set_site_version(site_version):
        self.site_version = site_version


    def add_coaches(new_coaches):
        self.coaches = self.coaches + new_coaches


    def add_students(new_students):
        self.students = self.students + new_students


    def remove_coaches(rm_coaches):
        self.coaches = [x for x in self.coaches if x not in rm_coaches]


    def remove_students(rm_students):
        self.students = [x for x in self.students if x not in rm_students]








