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


class Unit_Test_check_word(unittest.TestCase):
    """
    This class makes unit tests for check_for_word function from LexicalAnalyser class
    """

    def test_case_1_test_check_word(self):
        """
        Checls if the word is a key_word
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = 'break'

        self.assertEqual(LA_.check_word(word), "cuvant cheie")

    def test_case_2_test_check_word(self):
        """
        Checls if the word is a delimiter
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = '{'

        self.assertEqual(LA_.check_word(word), "delimitator")

    def test_case_3_test_check_word(self):
        """
        Checls if the word is an operator
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = '+'

        self.assertEqual(LA_.check_word(word), "operator")

    def test_case_4_test_check_word(self):
        """
        Checls if the word is a number
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = '25'
        self.assertEqual(LA_.check_word(word), "numar")

    def test_case_5_test_check_word(self):
        """
        Checls if the word is a float number
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = '25.32'

        self.assertEqual(LA_.check_word(word), "numar in virgula mobila")

    def test_case_6_test_check_word_test(self):
        """
        Checls if the word is a identifier (i.e variable name)
        """
        text = 'Dummy_text'
        LA_ = LA(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

        # Test case specific configuration
        word = 'nume_variabila'

        self.assertEqual(LA_.check_word(word), "identificator")
        print('\n')
        
if __name__ == '__main__':
    unittest.main()
    