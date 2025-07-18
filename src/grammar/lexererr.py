class LexerError(Exception):
    def __str__(self):
        return self.message


class ErrorToken(LexerError):
    def __init__(self, s):
        self.message = "Error Token " + s


class UncloseString(LexerError):
    def __init__(self, s):
        self.message = "Unclosed String: " + s


class IllegalEscape(LexerError):
    def __init__(self, s):
        self.message = "Illegal Escape In String: " + s
