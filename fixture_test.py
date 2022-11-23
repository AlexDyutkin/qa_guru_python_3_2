import pytest

@pytest.fixture() # декоратор
def open_brouser():
    assert False # Эта проверка упала в фикстуре

def test_body (open_brouser): # передать в аргумент open_brouser для запуска теста
    pass
