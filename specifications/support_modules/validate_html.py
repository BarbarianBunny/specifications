import re


class ValidateHTML:

    @staticmethod
    def tag(string):
        regex = re.compile("<(\"[^\"]*\"|'[^']*'|[^'\">])*>")
        if str and re.match(regex, string):
            return True
        else:
            return False
