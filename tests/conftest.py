import pytest

class User :

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self) :
        self.name = "Anat"
        self.second_name = "Dym"

    def remove(self) :
        self.name = ""
        self.second_name = ""

    

@pytest.fixture
def user() :
    user = User()
    user.create()

    yield user

    user.remove

