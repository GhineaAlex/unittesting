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

    def test_return_value(self):
        """ Constructorul Mock poate primi diverse argumente optionale pentru a controla comportamentul obiectului
        return_value ofera posibilitatea de a controla ce returneaza cand obiectul Mock este apelat ca o functie"""
       
        m = MagicMock(return_value=123)
        self.assertEqual(123, m())
        m.return_value = 345
        self.assertEqual(345, m())

    def test_mock_kwargs_constructor(self):
        "Constructorul Mock suporta 6 argumente, mai exact "
        " return_value, side_effect, spec, spec_set, wraps, name"
        " dar pe langa acestia se pot transmite un numar nelimitat de argumente, iar acestia pot fi utilizati in child mocks dupa creare"
        
        m = Mock(**{'first_name': 'owned',
                    'calculate_minimum.return_value': 456,
                    'company.xyz.get_url.side_effect': Exception})
        self.assertEqual('owned', m.first_name)
        #self.assertEqual('notOwned', m.first_name) #test pica deoarece atributul nu este corect
        self.assertEqual(456, m.calculate_minimum())
        self.assertRaises(Exception, m.company.xyz.get_url)

    def test_mock_called(self):
        """Cu apelul .called poti vedea daca mock object-ul a fost apelat pana acum"""
        m = Mock()
        self.assertFalse(m.called)
        m()
        #self.assertTrue(m.called)
        print("Rezultatul  este %r" % self.assertTrue(m.called))
        #print("Rezultatul  este %r" % self.assertFalse(m.called))

    def test_mock_asserts(self):
        """Obiectul mock are 4 helperi (assert_called_with, assert_called_once_with, assert_any_call, assert_has_calls),
        se pot face diverse assert-uri si sa vedem cum a fost apelat un mock de cand a fost instantiat"""
    
        m = Mock()
        m(1)

        m.assert_called_with(1)
        self.assertRaises(AssertionError, m.assert_called_with, 2)

        # assert_called_with cel mai recent apel al obiectului Mock, nu conteaza daca a existat un apel vreodata
        # apelul cu 1 va ridica eroare
        m(2)
        m.assert_called_with(2)
        self.assertRaises(AssertionError, m.assert_called_with, 1)

        # assert_called_once_with daca a fost apelat o singura data
        # specified argument. ambele teste vor da fail
        self.assertRaises(AssertionError, m.assert_called_once_with, 1)
        self.assertRaises(AssertionError, m.assert_called_once_with, 2)

        # assert_any_call daca a fost chemat cu argumentele respective vreodata de cand a fost creat obiectul
        m.assert_any_call(1)
        m.assert_any_call(2)
        self.assertRaises(AssertionError, m.assert_called_with, 3)

        # use assert_has_calls toate apeluri de cand a fost creat obiectul
        m.assert_has_calls([mock.call(1), mock.call(2)])

        #testul va da fail deoarece apelul a fost m(1), dupa m(2) si default any_order = False
        self.assertRaises(AssertionError, m.assert_has_calls, [mock.call(2), mock.call(1)])

        #  aici e adevarat deoarece nu conteaza ordinea in care a fost apelat obiectul Mock
        m.assert_has_calls([mock.call(2), mock.call(1)], any_order=True)
    

if __name__ == '__main__':
    unittest.main()
