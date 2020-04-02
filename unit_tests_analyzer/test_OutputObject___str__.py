import unittest
from analyzer import OutputObject as OO

KEY_WORDS = ["auto", "break", "case", "char", "continue", "do", "default", "const", "double", "else", "enum", "extern",
             "for", "if", "goto", "float", "int", "long", "register", "return", "signed", "static", "sizeof", "short",
             "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "NULL", "bool", "false",
             "true"
             ]
DELIMITERS = [";", "{", "}", ","]
OPERATORS = ["+", "-", "/", "*", "%", "=", "(", "[", "]", ")", '<', '>']
STRING_DELIMITERS = ["\""]
COMMENTS = ['#', "//", "/*"]


class Unit_Test__str_(unittest.TestCase):
    """
    This class makes unit tests for get_next_word function from LexicalAnalyser class
    """

    def test_case_1__str_(self):
        """
        Checls if the word is a key_word
        """
        full_word = ']'
        token_type = 'token_type'
        token_length = len(full_word)
        current_line = 1
        error = ''
        output_object = OO(full_word, token_type, token_length, current_line, current_line, error)
        self.assertEqual(
            str(output_object), "[] -> token_type de lungime {0} la linia {1}".format(token_length, current_line+1)
        )

    def test_case_2__str_(self):
        """
        Checls if the word is a key_word
        """
        full_word = ')'
        token_type = 'token_type'
        token_length = len(full_word)
        current_line = 1
        error = ''
        output_object = OO(full_word, token_type, token_length, current_line, current_line, error)
        self.assertEqual(
            str(output_object), "() -> token_type de lungime {0} la linia {1}".format(token_length, current_line+1)
        )

    def test_case_3__str_(self):
        """
        Checls if the word is a key_word
        """

        # Test case specific configuration
        full_word = 'token@@'
        token_type = 'token_type'
        token_length = len(full_word)
        current_line = 7
        error = ''
        output_object = OO(full_word, token_type, token_length, current_line, current_line, error)
        self.assertEqual(
            str(output_object), "token@@ -> token_type de lungime {0} la linia {1}".format(token_length, current_line+1)
        )

    def test_case_4__str_(self):
        """
        Checls if the word is a key_word
        """
        full_word = 'token@@'
        token_type = 'token_type'
        token_length = len(full_word)
        current_line = 1

        # Test case specific configuration
        error = 'error_message'

        output_object = OO(full_word, token_type, token_length, current_line, current_line, error)
        self.assertEqual(
            str(output_object), "token@@ -> token_type de lungime {0} la linia {1} eroare: {2}".format(
                token_length, current_line+1, error)
        )
        print('\n')
if __name__ == '__main__':
    unittest.main()
