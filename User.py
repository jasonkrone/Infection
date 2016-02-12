'''
By Jason Krone for Khan Academy

Implementation of User class
'''


class User(object):
    
    def __init__(self, uuid, site_version, coaches=set(), students=set(), classes=set()):
        assert type(coaches) == set and type(students) == set

        self.site_version = site_version
        self.coaches = coaches
        self.students = students 
        self.uuid = uuid
        self.classes = classes
  

    def __eq__(self, other):
        try:
            return self.uuid == other.uuid
        except:
            return False


    def __hash__(self):
        return self.uuid


    #  allows for better print description 
    def __str__(self):
        return 'version: ' + str(self.site_version) + ' uuid: ' + str(self.uuid)


    def is_student(self):
        return len(self.coaches) > 0


    def is_coach(self):
        return len(self.students) > 0


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


