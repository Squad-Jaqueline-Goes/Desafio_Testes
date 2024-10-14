import pytest
from desafio2 import admin_command

class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
    
    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"

    def test_empty_command(self):
        result = admin_command([], sudo=True)
        assert result == ["sudo"]

    def test_no_sudo_empty_command(self):
        result = admin_command([], sudo=False)
        assert result == []

    def test_complex_command(self):
        command = ["curl", "-I", "http://example.com"]
        result = admin_command(command, sudo=True)
        assert result == ["sudo"] + command

    def test_complex_command_no_sudo(self):
        command = ["curl", "-I", "http://example.com/"]
        result = admin_command(command, sudo=False)
        assert result == command

    def test_invalid_command(self):
        with pytest.raises(TypeError) as error:
            admin_command(123, sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'int'>"

    def test_empty_string_command(self):
        with pytest.raises(TypeError) as error:
            admin_command("", sudo=True)
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"
