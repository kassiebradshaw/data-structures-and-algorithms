import pytest
from code_challenges.merge_sort.merge_sort import merge_sort, merge

def test_merge_sort_happy_path():
    list = [8,4,23,42,16,15]
    actual = merge_sort(list)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_merge_sort_expected_failure():
    list = []
    actual = merge_sort(list)
    expected = "List must not be empty. List must have more than 1 item."
    assert actual == expected

def test_small_list():
    list = [99, 1]
    actual = merge_sort(list)
    expected = [1,99]
    assert actual == expected

def test_list_with_one_item():
    list = [5]
    actual = merge_sort(list)
    expected = "List must not be empty. List must have more than 1 item."
    assert actual == expected

def test_list_with_multiples():
    list = [5,5,5,4,3,2,4,3,2,1]
    actual = merge_sort(list)
    expected = [1,2,2,3,3,4,4,5,5,5]
    assert actual == expected

