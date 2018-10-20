class OurSquad():

    def __init__(self, name, location, members=[]):
        self.name = name
        self.location = location
        self.members = members
        self.size = len(self.members)

    def add_member(self, new_member):
        '''new_member should be a string'''
        self.members.append(new_member)
        self.size = len(self.members)

    def __len__(self):
        return len(self.members)

    def __eq__(self, other):
        return self.members == other.members
    #
    # def __eq__(self, other):
    #     return self.size == other.size
    #
    # def update_squad_size(self, new_size):
    #     self.size = new_size
    #
    # def add_to_squad(self, num_new_students):
    #     self.size += num_new_students

members1 = ['Faith','Ryan']

members2 = ['Leo','Melissa']


squad1 = OurSquad(name='Python Night Class',
                        location='Austin',
                        members=members1)

squad2 = OurSquad(name='Other Night Class',
                        location='Austin',
                        members=members2)

squad1 == squad2
