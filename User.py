'''
By Jason Krone for Khan Academy

Defines User class
'''


class User(object):

    def __init__(self, site_version, uuid, coaches=None, students=None):
        self.site_version = site_version
        self.coaches = coaches
        self.students = students 
        self.uuid = uuid


    def __eq__(self, other):
        return self.uuid == other.uuid


    def __hash__(self):
        return self.uuid


    # allows us to get print description 
    def __str__(self):
        return 'v: ' + str(self.site_version) + ' id: ' + str(self.uuid)


    def set_site_version(self, site_version):
        self.site_version = site_version


    def add_coaches(self, new_coaches):
        self.coaches = self.coaches + new_coaches


    def add_students(self, new_students):
        self.students = self.students + new_students


    def remove_coaches(self, rm_coaches):
        self.coaches = [x for x in self.coaches if x not in rm_coaches]


    def remove_students(self, rm_students):
        self.students = [x for x in self.students if x not in rm_students]








