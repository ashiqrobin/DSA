import pytest
from stack import Stack
from balance_bracket import is_paran_balance
from decimal_to_binary import  convert
from reverse_string import reverse_str

@pytest.mark.stack
def test_stack_push():
    s = Stack()
    s.push("A")
    assert s.get_stack() == ['A']

@pytest.mark.stack
def test_stack_pop():
    s = Stack()
    s.push("B")
    s.push("A")
    s.pop()
    assert s.get_stack() == ['B']

@pytest.mark.balance
@pytest.mark.parametrize("bracket, result",[("({})",True),("({[",False),("{()}", True)])
def test_bracket_balance(bracket, result):
    assert is_paran_balance(bracket) == result


@pytest.mark.binary
@pytest.mark.parametrize("value, result",[(243,11110011),(830,1100111110)])
def test_decimal_binary(value, result):
    assert convert(value) == result


@pytest.mark.reverse
@pytest.mark.parametrize("value, result",[("243","342"),("ABC","CBA")])
def test_reverse_string(value, result):
    assert reverse_str(value) == result

    


    
    