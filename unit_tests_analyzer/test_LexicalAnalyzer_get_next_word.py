import unittest
from analyzer import LexicalAnalyser as LA

KEY_WORDS = ["auto", "break", "case", "char", "continue", "do", "default", "const", "double", "else", "enum", "extern",
             "for", "if", "goto", "float", "int", "long", "register", "return", "signed", "static", "sizeof", "short",
             "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "NULL", "bool", "false",
             "true"
             ]
DELIMITERS = [";", "{", "}", ","]
OPERATORS = ["+", "-", "/", "*", "%", "=", "(", "[", "]", ")", '<', '>']
STRING_DELIMITERS = ["\""]
COMMENTS = ['#', "//", "/*"]


class Unit_Test_get_next_word(unittest.TestCase):
    """
    This class makes unit tests for get_next_word function from LexicalAnalyser class
    """

    def test_case_1_get_next_word(self):
        """
        Checls if the word is a key_word
        """
        c_text = 'int a=0;'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, c_text)

        self.assertEqual(str(LA_.get_next_word()), "int -> cuvant cheie de lungime 3 la linia 1")
        self.assertEqual(str(LA_.get_next_word()), "a -> identificator de lungime 1 la linia 1")
        self.assertEqual(str(LA_.get_next_word()), "= -> operator de lungime 1 la linia 1")
        self.assertEqual(str(LA_.get_next_word()), "0 -> numar de lungime 1 la linia 1")
        self.assertEqual(str(LA_.get_next_word()), "; -> delimitator de lungime 1 la linia 1")

    def test_case_2_get_next_word(self):
        """
        Checls if the word is a key_word
        """
        c_text = ' "sir_de_caractere" '
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, c_text)

        self.assertEqual(
            str(LA_.get_next_word()), '"sir_de_caractere" -> constanta sir de caractere de lungime 16 la linia 1'
        )
        print('\n')



if __name__ == '__main__':
    unittest.main()
