import re

FILE_TITLE = "main.c"

KEY_WORDS = ["auto", "break", "case", "char", "continue", "do", "default", "const", "double", "else", "enum", "extern",
             "for", "if", "goto", "float", "int", "long", "register", "return", "signed", "static", "sizeof", "short",
             "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "NULL", "bool"
             ]
DELIMITERS = [";", "{", "}", ",", "'"]
OPERATORS = ["+", "-", "/", "*", "%", "=", "(", "[", "]", ")", "||"]
STRING_DELIMITERS = ["\""]
COMMENTS = ['#', "//", "/*"]


class OutputObject:

    def __init__(self,token,token_type,token_length,current_line,current_pointer,error_message):
        self.token = token
        self.token_type = token_type
        self.token_length = token_length
        self.current_line = current_line
        self.current_pointer = current_pointer
        self.error_message = error_message

    def __str__(self):
        if self.token == "]":
            return "[]" + " -> " + self.token_type + " " + "de lungime" + " " + str(self.token_length) + " " + "la linia" + " " + str(self.current_line+1)
        elif self.token == ")":
            return "()" + " -> " + self.token_type + " " + "de lungime" + " " + str(self.token_length) + " " + "la linia" + " " + str(self.current_line + 1)

        if self.error_message == "":
            return self.token + " -> " + self.token_type + " " + "de lungime" + " " + str(self.token_length) + " " + "la linia" + " " + str(self.current_line + 1)

        return self.token + " -> " + self.token_type + " " + "de lungime" + " " + str(self.token_length) + " " + "la linia" + " " + str(self.current_line + 1) + " " + "eroare:" + " " + self.error_message

class LexicalAnalyser:

    def __init__(self, keywords, delimiters, string_delimiters, operators, text):
        self.keywords = keywords
        self.delimiters = delimiters
        self.string_delimiters = string_delimiters
        self.operators = operators
        self.current_pointer = 0
        self.current_line = 0
        text = self.remove_libraries(text)
        text = self.remove_comments(text)
        self.text = text

    @staticmethod
    def check_for_identifier(token, token_type):
        if token_type == "identificator":
            if token[0].isdigit():
                return "un nume de variabila nu poate incepe cu o cifra"
            elif any(i in token for i in DELIMITERS):
                return "un nume de variabila nu poate contine un delimitator"
            elif any(i in token for i in OPERATORS):
                return "un nume de variabila nu poate contine un operator"
            else:
                return ""

        return ""

    @staticmethod
    def remove_libraries(text):
        def replacer(match):
            s = match.group(0)
            if s.startswith('#'):
                return " "
            else:
                return s

        pattern = re.compile(
            r"#include.*",
            re.MULTILINE
        )
        return re.sub(pattern, replacer, text)

    @staticmethod
    def remove_comments(text):
        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "
            else:
                return s

        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        return re.sub(pattern, replacer, text)

    def check_word(self, word):

        if word in self.keywords:
            return "cuvant cheie"
        elif word in self.delimiters:
            return "delimitator"
        elif word in self.operators:
            return "operator"

        if re.match(r"[0-9]+$", word):
            return "numar"

        if re.match(r"[0-9]*\.{0,1}[0-9]+[fLd]{0,1}$", word):
            return "numar in virgula mobila"

        return "identificator"

    def get_next_word(self):
        for i in range(self.current_pointer, len(self.text)):

            if self.text[i] in self.string_delimiters:
                j = i + 1
                while not self.text[j] in self.string_delimiters:
                    j = j + 1
                full_word = self.text[i:(j+1)]
                token_type = 'constanta sir de caractere'
                token_length = len(full_word) - 2
                error = ""
                output = output = OutputObject(full_word, token_type, token_length, self.current_line, i, error)
                self.current_pointer = j +2
                return output

            if self.text[i] in DELIMITERS or self.text[i] in OPERATORS:

                if self.text[i] == '[' or self.text[i] == '(':
                    continue

                if self.text[i] == "=":
                    if self.text[i+1] == "=":
                        full_word = "=="
                        token_type = 'operator'
                        token_length = 2
                        error = ""
                        output = OutputObject(full_word, token_type, token_length, self.current_line, i, error)
                        self.current_pointer = i + 2
                        return output

                full_word = self.text[i]
                token_type = self.check_word(full_word)
                token_length = len(full_word)
                error = self.check_for_identifier(full_word, token_type)
                output = OutputObject(full_word, token_type, token_length, self.current_line, i, error)
                self.current_pointer = i+1

                return output

            if not self.text[i].isspace():
                j = i

                while not self.text[j].isspace() and j < len(self.text) - 1:
                    j = j + 1
                    if self.text[j] in DELIMITERS or self.text[j] in OPERATORS:
                        break

                if i == j:
                    full_word = self.text[i]
                    self.current_pointer = i+1
                else:
                    full_word = self.text[i:j]
                    self.current_pointer = j

                token_type = self.check_word(full_word)
                token_length = len(full_word)
                error = self.check_for_identifier(full_word, token_type)
                output = OutputObject(full_word, token_type, token_length, self.current_line, i, error)

                return output

            elif self.text[i] == '\n':
                self.current_line = self.current_line + 1

        return None

    def analyse(self):
        object = self.get_next_word()
        return object


def main():

    file_object = open(FILE_TITLE, 'r')
    text = file_object.read()
    analyzer = LexicalAnalyser(KEY_WORDS, DELIMITERS, STRING_DELIMITERS, OPERATORS, text)

    object = analyzer.analyse()
    print(object)

    while object is not None:
        object = analyzer.analyse()
        if object is None :
            break
        print(object)

main()




