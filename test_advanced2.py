import pytest
import os

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
