import groups


class TestSn:

    ''' Test symmetric groups
    '''

    def test_create(self):
        gr1 = groups.Sn(4)
        assert gr1.name() == 'Sn(4)'
        assert gr1.is_abelian() is False
        assert groups.Sn(2).is_abelian() is True


class TestZn:

    ''' Test cyclic group
    '''

    def test_create(self):
        gr1 = groups.Zn(4)
        assert gr1.name() == 'Zn(4)'
        assert gr1.is_abelian() is True
