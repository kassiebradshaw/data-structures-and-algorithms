import pytest
# from ..code_challenges.insertion_sort.insertion_sort import insertion_sort
from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_happy_path():
    list = [8,4,23,42,16,15]
    actual = insertion_sort(list)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_insertion_sort_expected_failure():
    list = []
    actual = insertion_sort(list)
    expected = 'List must not be empty. List must have more than 1 value to sort.'
    assert actual == expected

def test_small_list():
    list = [99, 1]
    actual = insertion_sort(list)
    expected = [1,99]
    assert actual == expected

def test_list_with_one_item():
    list = [5]
    actual = insertion_sort(list)
    expected = 'List must not be empty. List must have more than 1 value to sort.'
    assert actual == expected

def test_list_with_multiples():
    list = [5,5,5,4,3,2,4,3,2,1]
    actual = insertion_sort(list)
    expected = [1,2,2,3,3,4,4,5,5,5]
    assert actual == expected

