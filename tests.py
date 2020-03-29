import unittest
from unittest import TestCase
import unittest.mock as mock
from unittest.mock import Mock, MagicMock, patch


class MockObjectBasics(TestCase):
    """Demonstates the basics of the 'Mock' class."""

    def test_mock(self):
        "Un obiect de tip Mock poate fi apelat si poti configura valoarea de returnare"
        "In mod normal returneaza o alta instanta de Mock creata la primul acces"
        "Orice alt atribut de acces creeaza si returneaza o alta instanta de mock, astfel ca este creat un arbore de obiect de tip Mock"

        m = Mock()
        self.assertIsInstance(m, Mock)

        
        print("Assert is %r" % self.assertIsInstance(m(), Mock))
        # orice atribut accesat sau invocat va returna alt mock
        self.assertIsInstance(m.xyz, Mock)
        self.assertIsInstance(m.foo(), Mock)
        self.assertIsInstance(m.just.keep.on().trucking, Mock)

        # atribute diferite vor avea diferite obiecte mock returnate
        self.assertNotEqual(m.abcd, m.efgh)

        # but once referenced, the same mock is always returned
        self.assertEqual(m.abcd, m.abcd)
    

if __name__ == '__main__':
    unittest.main()
