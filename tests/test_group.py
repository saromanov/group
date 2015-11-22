import groups

class TestGroup:
    def test_abelian(self):
        gr1 = groups.Zn(4)
        assert gr1.isAbelian()

    def test_elements(self):
        gr1 = groups.Zn(2)
        assert gr1.elements() == [0,1]

    def test_properties(self):
        gr1 = groups.Sn(5)
        prop = gr1.properties()
        assert prop['rational']
