import pytest
import os

"""
A função "str_to_bool()" aceita uma cadeia de caracteres como entrada e, dependendo de seu conteúdo, retorna um valor True ou False
"""
def str_to_bool(string):
    if string.lower() in ["yes", "y", "1"]:
        return True
    elif string.lower() in ["no", "n", "0"]:
        return False

# teste de valor verdadeiro
@pytest.mark.parametrize("string", ["Y", "y", "1", "YES"])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True

# teste de valor falso
@pytest.mark.parametrize("string", ["N", "n", "0", "NO"])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False


# Essa classe de teste cria um arquivo
class TestFile:

    def setup(self):
        with open("/tmp/done", "w") as _f:
            _f.write("1")

    def teardown(self):
        try:
            os.remove("/tmp/done")
        except OSError:
            pass

    def test_done_file(self):
        with open("/tmp/done") as _f:
            contents = _f.read()
        assert contents == "1"


# Crie um acessório que use o acessório pytest tmpdir()
@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath

    return write


class TestFile:

    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"
