import pytest
from stack_and_queue.pseudo_queue import Pseudo_queue

@pytest.fixture
def pseudo():
    queue = Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    
    queue.enqueue(3)
    return queue

def test_malti_enqueue(pseudo):
    expexted = "Rear <= 3 <= 2 <= 1 <= Front"
    actual = pseudo.__str__()
    assert actual == expexted

def test_multi_dequeue(pseudo):
    pseudo.dequeue()
    pseudo.dequeue()
    expexted = "Rear <= 3 <= Front"
    actual = pseudo.__str__()
    assert actual == expexted

def test_dequeue_empty():
    check_queue = Pseudo_queue()
    with pytest.raises(Exception) as excinfo:
        check_queue.dequeue()
    assert "Empty" == str(excinfo.value)

def test_alternate_enqueue_dequeue(pseudo):
    pseudo.dequeue()
    pseudo.enqueue(4)
    expexted = "Rear <= 4 <= 3 <= 2 <= Front"
    actual = pseudo.__str__()
    assert actual == expexted