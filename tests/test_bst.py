"""Test binary search tree implementation."""

import pytest


@pytest.fixture
def test_bsts():
    """Fixture for bst."""
    from src.bst import Bst
    empty = Bst()
    one = Bst([5])
    three = Bst([5, 3, 7])
    balance = Bst([5, 3, 2, 1, 9, 7, 8])
    leftheavy = Bst([5, 3, 2, 1])
    rightheavy = Bst([5, 6, 7, 8, 9, 10])
    return empty, one, three, balance, leftheavy, rightheavy


def test_insert_sets_root(test_bsts):
    """Test first insert updates root."""
    test_bsts[0].insert(5)
    assert test_bsts[0].root.val == 5


def test_insert_updates_pointers(test_bsts):
    """Test insert updates pointers."""
    test_bsts[1].insert(3)
    assert test_bsts[1].root.left.val == 3
    assert test_bsts[1].root.left.parent == test_bsts[1].root


def test_insert_smallest_left(test_bsts):
    """Test insert the smallest to the left."""
    test_bsts[1].insert(3)
    assert test_bsts[1].root.left.val < test_bsts[1].root.val


def test_insert_largest_right(test_bsts):
    """Test insert the largest to the right."""
    test_bsts[1].insert(7)
    assert test_bsts[1].root.right.val > test_bsts[1].root.val


def test_insert_increases_size(test_bsts):
    """Test insert increases size."""
    test_bsts[0].insert(4)
    assert test_bsts[0].size() == 1


def test_contains_method(test_bsts):
    """Test contains on number that exists."""
    assert test_bsts[2].contains(5)
    assert test_bsts[2].contains(3)
    assert test_bsts[2].contains(7)


def test_contains_method_no_val(test_bsts):
    """Test contains that doesnt exist."""
    assert not test_bsts[4].contains(10)

# def test_depth_method(test_bsts):
#     """Test depth method."""
#     assert test_bsts[2].depth() == 2
