class RandomizedSet(object):

    def __init__(self):
        self.obj = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.obj:
            return False
        self.obj.add(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.obj:
            return False
        self.obj.remove(val)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.obj))