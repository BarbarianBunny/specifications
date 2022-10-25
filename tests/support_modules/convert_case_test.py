from specifications.support_modules.convert_case import ConvertCase


class PascalToKebab:

    def given_pascal(self):
        return ConvertCase.pascal_to_kebab("PascalCase") == "pascal-case"

    def given_undesired_html_chars(self):
        return ConvertCase.pascal_to_kebab("Pascal{}[]|\/^~`&?-_ :Case") == "pascal-case"


class PascalToTitle:

    def given_pascal(self):
        return ConvertCase.pascal_to_title("PascalCase") == "Pascal Case"

    def given_undesired_html_chars(self):
        return ConvertCase.pascal_to_title("Pascal{}[]|\/^~`&?-_ :Case") == "Pascal Case"