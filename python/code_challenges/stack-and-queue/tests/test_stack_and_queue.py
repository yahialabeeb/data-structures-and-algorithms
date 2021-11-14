from inspect import stack
from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack, Queue, Node
import pytest
def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def stack_create():
    new_stack = Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    return new_stack

# Can successfully push onto a stack
def test_stack_one_push():
    new_stack = Stack()
    new_stack.push(1)
    excepted = "Top -> 1"
    actual = new_stack.__str__()
    assert actual == excepted
# Can successfully push multiple values onto a stack
def test_stack_multiple_push(stack_create):
    excepted = "Top -> 3 -> 2 -> 1"
    actual = stack_create.__str__()
    assert actual == excepted

# Can successfully pop off the stack
def test_stack_one_pop(stack_create):
    stack_create.pop()
    excepted = "Top -> 2 -> 1"
    actual = stack_create.__str__()
    assert actual == excepted

# Can successfully empty a stack after multiple pops
def test_stack_multiple_pop(stack_create):
    stack_create.pop()
    stack_create.pop()
    stack_create.pop()
    excepted = "Empty"
    actual = stack_create.__str__()
    assert actual == excepted
# Can successfully peek the next item on the stack
def test_stack_peek(stack_create):
    actual = stack_create.peek()
    excepted = 3
    assert actual == excepted


# Can successfully instantiate an empty stack
def test_empty_stack():
    new_stack = Stack()
    excepted = "Empty"
    actual = new_stack.__str__()
    assert actual == excepted

# Calling pop or peek on empty stack raises exception
def test_peek_empty_stack_raises_exception():
  check_stack = Stack()
  with pytest.raises(Exception) as excinfo:
    check_stack.peek()
  assert "Empty" == str(excinfo.value)

@pytest.fixture
def queue_creating():
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    return new_queue

# Can successfully enqueue into a queue
def test_queue_one_enqueue():
    new_queue = Queue()
    new_queue.enqueue(1)
    excepted = "Front => 1 <= Rear"
    actual = new_queue.__str__()
    assert actual == excepted


# Can successfully enqueue multiple values into a queue
def test_queue_multi_enqueue(queue_creating):
    excepted = "Front => 1 <= 2 <= 3 <= Rear"
    actual = queue_creating.__str__()
    assert actual == excepted

# Can successfully dequeue out of a queue the expected value
def test_queue_one_dequeue(queue_creating):
    queue_creating.dequeue()
    excepted = "Front => 2 <= 3 <= Rear"
    actual = queue_creating.__str__()
    assert actual == excepted

# Can successfully empty a queue after multiple dequeues
def test_queue_multiple_dequeue(queue_creating):
    queue_creating.dequeue()
    queue_creating.dequeue()
    queue_creating.dequeue()
    excepted = "Empty"
    actual = queue_creating.__str__()
    assert actual == excepted

# Can successfully peek into a queue, seeing the expected value
def test_queue_peek(queue_creating):
    excepted = 1
    actual =queue_creating.peek()
    assert actual == excepted



# Can successfully instantiate an empty queue
def test_empty_queue():
    new_queue = Queue()
    excepted = "Empty"
    actual = new_queue.__str__()
    assert actual == excepted

# Calling dequeue or peek on empty queue raises exception
def test_peek_empty_queue_raises_exception():
  check_queue = Queue()
  with pytest.raises(Exception) as excinfo:
    check_queue.peek()
  assert "empty queue" == str(excinfo.value)