class Group(object):

    def __init__(self, group, grtype):
        self._group = group
        self._grtype = grtype
        self.binop = lambda x, y: (x + y) % len(self._group)
        self._abelian = self._is_abelian(self._group)
        self._properties = {}

    def set_binop(self, binop):
        ''' set user binary operation over group
        '''
        self.binop = binop

    def __mul__(self, group):
        ''' Product of two groups
        '''
        pass

    def __str__(self):
        return self._grtype

    def name(self):
        return self._grtype

    def replace(self, item):
        pass

    def is_abelian(self):
        return self._abelian

    def _is_abelian(self, group):
        for item1 in group:
            for item2 in group:
                # Check Commutativity
                commut = all([self.binop(item1[i], item2[i]) == self.binop(
                    item2[i], item1[i]) for i in range(len(item1))])
                if commut is False:
                    return False
                # Check closure
                closure = all(
                    [self.binop(item1[i], item2[i]) in item1
                        for i in range(len(item1))])
                if closure is False:
                    return False
                # Check identity
                ident = all(
                    [self.binop(item1[i], 1) == self.binop(1, item1[i])
                        for i in range(len(item1))])
                if ident is False:
                    return False
                # TODO: Associativity
        return True

    def elements(self):
        if len(self._group) == 0:
            raise Exception("Group not contain any elements")
        return list(sorted(self._group[0]))

    def inverse(self, elem):
        ''' Return inverse element
        '''
        elems = self.elements()
        for item in elems:
            if item * elem == 1:
                return item
        raise Exception("Inverse element is bot found")

    def add_property(self, propertyname, value):
        ''' addProperty stores property valid
            for group
            Args:
                propertyname - name of property
                Example: 'trivial', 'rational'

                value - typical is boolean
        '''
        self._properties[propertyname] = value

    def properties(self):
        ''' Return dictionary of properties
        '''
        return self._properties
