'''
By Jason Krone for Khan Academy

Implementation of User class
'''


'''
to serve as a node attribute in the graph
'''

class User(object):

    
    ''' str, str, set, set -> User object '''
    def __init__(self, uuid, site_version, coaches=set(), students=set()):

        self.site_version = site_version
        self.coaches = coaches
        self.students = students 
        self.uuid = uuid


    def __eq__(self, other):
        try:
            return self.uuid == other.uuid
        except:
            return False


    def __hash__(self):
        return self.uuid


    ''' allows better print description '''
    def __str__(self):
        return 'version: ' + str(self.site_version) + ' uuid: ' + str(self.uuid)


    def set_site_version(self, site_version):
        self.site_version = site_version


    def add_coaches(self, new_coaches):
        self.coaches.union(new_coaches)


    def add_students(self, new_students):
        self.students.union(new_students)


    def remove_coaches(self, rm_coaches):
        self.coaches = self.coaches - rm_coaches 


    def remove_students(self, rm_students):
        self.students = self.students - rm_students


