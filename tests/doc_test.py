from specifications.doc import Doc


class Init:

    def given_filename(self):
        assert Doc("test-file.pdf").filename == "test-file.pdf"


class Name:

    def given_filename(self):
        assert Doc("test-file.pdf").name() == "test-file"

    def given_filename_with_caps(self):
        assert Doc("Test-File.pdf").name() == "Test-File"


class Title:

    def given_filename(self):
        assert Doc("test-file.pdf").title() == "test file"

    def given_filename_with_caps(self):
        assert Doc("Test-File.pdf").title() == "Test File"


class Extension:

    def given_filename(self):
        assert Doc("test-file.pdf").extension() == "pdf"
