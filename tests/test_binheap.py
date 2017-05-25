"""Testing binary Heap."""

import pytest


@pytest.fixture
def empty_heap():
    """Fixture for empty_heap."""
    from src.binheap import Binheap
    bh = Binheap()
    return bh


@pytest.fixture
def heap():
    """Fixture for a heap."""
    from src.binheap import Binheap
    bh = Binheap([10, 4, 2, 6, 13, 72, 1, 49])
    return bh


def test_push_val_to_head(empty_heap):
    """Test push first val adds to the head."""
    empty_heap.push(3)
    assert empty_heap.container == [None, 3]


def test_push_val(empty_heap):
    """Test push second val adds to the tree."""
    empty_heap.push(3)
    empty_heap.push(2)
    assert empty_heap.container == [None, 3, 2]


def test_push_val_large(empty_heap):
    """Test push val for larger number."""
    empty_heap.push(3)
    empty_heap.push(2)
    empty_heap.push(1)
    empty_heap.push(16)
    assert empty_heap.container == [None, 16, 3, 1, 2]


def test_push_on_empty(empty_heap):
    """Test push on an empty list."""
    empty_heap.push(1)
    assert empty_heap.container == [None, 1]


def test_initialize_iterable(heap):
    """Test heap can be initialized with iterable."""
    assert heap.container == [None, 72, 49, 13, 10, 6, 2, 1, 4]


def test_display(heap):
    """Test the display method."""
    tree = '    72 \n  49 13 \n 10 6 2 1 \n4 \n'
    print(heap.display())
    print(tree)
    assert heap.display() == tree