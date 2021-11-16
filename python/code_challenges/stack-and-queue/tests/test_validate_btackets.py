import pytest
from stack_and_queue.validating_brackets import validate_brackets

def test_given_example():
    input = ["{}","{}(){}","()[[Extra Characters]]","(){}[[]]","{}{Code}[Fellows](())","[({}]","(](","{(})"]
    excepted = [True, True, True, True, True, False, False, False] 
    actual = []
    for i in range(len(input)):
        actual.append(validate_brackets(input[i]))
    assert actual == excepted
## edge cases due to my code 

def test_empty_str():
    with pytest.raises(Exception) as excinfo:
        validate_brackets("")
    assert "Empty String" == str(excinfo.value)

def test_start_with_close_brackets():
    actual = validate_brackets("}{")
    assert not actual

def test_brackets_still_open():
    actual =  validate_brackets("({}")
    assert not actual 

def test_open_close():
    actual =  validate_brackets("()({}){}[]")
    assert actual