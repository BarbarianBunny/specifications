import re


class ConvertCase:

    @classmethod
    def kebab_case(cls, text):
        return re.sub(r"[-_ :&?/\"|]+", "-", text.lower())

    @classmethod
    def remove_kebab(cls, text):
        return re.sub(r"-+", " ", text)

    @classmethod
    def pascal_to_kebab(cls, text):
        return ''.join(['-' + char.lower() if char.isupper() else char for char in text]).lstrip('{}[]|\/^~`&?-_ :')

    @classmethod
    def pascal_to_title(cls, text):
        return ''.join([' ' + char.upper() if char.isupper() else char for char in text]).lstrip('{}[]|\/^~`&?-_ :')
