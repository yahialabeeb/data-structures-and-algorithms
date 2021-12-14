import pytest 
from hash_table.hash_table import Hash_table
from hash_table.left_join import left_joins

@pytest.fixture
def testing():
    hash1 = Hash_table(100)
    hash1.add("diligent", "employed")   
    hash1.add("fond", "enamored")	 	
    hash1.add("guide", "usher")	 	
    hash1.add("outfit", "garb")	 	
    hash1.add("wrath","anger")
    hash2 = Hash_table(100) 	
    hash2.add('diligent', 'idle') 
    hash2.add('fond', 'averse')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')
    hash2.add('wrath', 'delight')
    return hash1, hash2


def test_leftjoin(testing):
    assert left_joins(testing[0],testing[1]) == [
        ['diligent', 'employed', 'idle'], 
        ['outfit', 'garb', None], 
        ['wrath', 'anger', 'delight'], 
        ['fond', 'enamored', 'averse'], 
        ['guide', 'usher', 'follow']
        ]