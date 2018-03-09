class Set(object):

    def __init__(self, elements=None):

        self.list = list()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.list.append(elements):
                self.size += 1


    def contains(self, element):
        '''cheks to see if the item is contained in the list of elemennts, important becuase a set can only have one'''
        for items in self.list:
            if element == items:
                return True
        return False


    def add(self, element):
        '''adds an element to the end of the list, shoud thonk about a prepend method'''
        if self.contains(element):
            raise ValueError('Set already have', element)
        else:
            self.list.append(element)
            self.size += 1
    def prepend(self, element):
        '''adds an element to the end of the list, shoud thonk about a prepend method'''
        if self.contains(element):
            raise ValueError('Set already have', element)
        else:
            self.list.prepend(element)
            self.size += 1

    def remove(self, element):
        '''removes an element based on the value.'''
        self.list.remove(element)
        self.size -= 1
    def removeIndex(self, index):
        '''loops through and removes by index, may or maynot return'''
        #TODO: MAKESURE YOU CAN REMOVE BY INDEX
        pass
    def union(self, other_set):
        '''adds items from one set to this one'''
        new_set = Set(self.list)
        for item in other_set.list:
            if not new_set.contains(item):
                new_set.add(item)
        return new_set


    def intersection(self, other_set):
        '''if the items are in both sets, it adds it to a list, basically check for like terms'''
        new_set = Set()
        for item in other_set.list:
            if self.contains(item):
                new_set.add(item)
        return new_set


    def difference(self, other_set):
        ''' checks both sets, and if one isnt in the other, it adds all the difrent terms into the new list'''
        new_set = Set()
        for item in self.list():
            if not self.contains(item):
                new_set.add(item)
        for item in other_set.list:
            if not new_set.contains(item):
                new_set.add(item)
        return new_set


    def is_subset(self, other_set):
        '''Checks if all itemsa in one list are in another, therefore making it a subset'''
        for item in other_set.list:
            if not self.contains(item):
                return False
        return True
