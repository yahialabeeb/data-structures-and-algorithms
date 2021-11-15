import pytest
from stack_and_queue.animal_shelter import Animal_shelter

@pytest.fixture
def shelters():
    shelters = Animal_shelter()
    animal ="cat"
    dog = "dog"
    shelters.enqueue(animal)
    shelters.enqueue(dog)
    shelters.enqueue("cat")
    shelters.enqueue("dog")
    return shelters

def test_enqueuing(shelters):
    actual = shelters.__str__()
    excepted = "Front => cat <= dog <= cat <= dog <= Rear"
    assert actual == excepted

def test_dequeue_cat_only(shelters):
    shelters.dequeue("cat")
    shelters.dequeue("cat")
    actual = shelters.__str__()
    excepted = "Front => dog <= dog <= Rear"
    assert actual == excepted

def test_dequeue_dog_only(shelters):
    shelters.dequeue("dog")
    shelters.dequeue("dog")
    actual = shelters.__str__()
    excepted = "Front => cat <= cat <= Rear"
    assert actual == excepted

def test_dequeue_dog_more_than_exist(shelters):
    shelters.dequeue("dog")
    shelters.dequeue("dog")
    shelters.dequeue("dog")
    actual = shelters.__str__()
    excepted = "Front => cat <= Rear"
    assert actual == excepted