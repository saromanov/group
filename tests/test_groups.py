import groups
import pytest


class TestSn:
    ''' Test symmetric groups
    '''
    def test_create(self):
        gr1 = groups.Sn(4)
        assert gr1.name() == 'Sn(4)'
        assert gr1.isAbelian() == False
        assert groups.Sn(2).isAbelian() == True


class TestZn:
    ''' Test cyclic group
    '''
    def test_create(self):
        gr1 = groups.Zn(4)
        assert gr1.name() == 'Zn(4)'
        assert gr1.isAbelian() == True
