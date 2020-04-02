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


class Unit_Test_check_for_identifier(unittest.TestCase):
    """
    This class makes unit tests for check_for_identifier function from LexicalAnalyser class
    """

    def test_case_1_check_for_identifier(self):
        """
        Checks if variable name starts with digit:
        Expected behaviour: return un nume de variabila nu poate incepe cu o cifra.
        """
        token_type = 'identificator'

        # Test case specific configuration
        token = '2lungime'
        self.assertEqual(
            LA.check_for_identifier(token, token_type),  "un nume de variabila nu poate incepe cu o cifra"
        )

    def test_case_2_check_for_identifier(self):
        """
        Checks if variable name starts with delimiter:
        Expected behaviour: return "un nume de variabila nu poate contine un delimitator"
        """
        token_type = 'identificator'

        # Test case specific configuration
        token = 'sef;'

        self.assertEqual(
            LA.check_for_identifier(token, token_type),  "un nume de variabila nu poate contine un delimitator"
        )

    def test_case_3_check_for_identifier(self):
        """
        Checks if variable name starts with operator:
        Expected behaviour: return "un nume de variabila nu poate contine un operator"
        """
        # Test case specific configuration
        token_type = 'identificator'
        token = 'nume_variabila+'

        self.assertEqual(
            LA.check_for_identifier(token, token_type), "un nume de variabila nu poate contine un operator"
        )

    def test_case_4_check_for_identifier(self):
        """
        Checks if variable name starts with operator:
        Expected behaviour: return "un nume de variabila nu poate contine un operator"
        """
        # Test case specific configuration
        token_type = 'identificator'
        token = 'nume_variabila'

        self.assertEqual(
            LA.check_for_identifier(token, token_type), ""
        )
        print('\n')

if __name__ == '__main__':
    unittest.main()
