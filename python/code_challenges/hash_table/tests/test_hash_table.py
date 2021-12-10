from hash_table import __version__
import pytest 
from hash_table.hash_table import Hash_table


@pytest.fixture
def testing():
    testing = Hash_table(100)
    testing.add("key","value")
    testing.add("yek","value2")
    return testing  


def test_version():
    assert __version__ == '0.1.0'

# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored

def test_adding_key_value(testing):
    assert testing.get("key") == "value"

# Successfully returns null for a key that does not exist in the hashtable

def test_getting_none(testing):
    assert not testing.get("yahia")

# Successfully handle a collision within the hashtable

def test_collision(testing):
    assert testing.get("key") != testing.get("yek")

# Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_bucket(testing):
    assert testing.get("yek") == "value2"

# Successfully hash a key to an in-range value

def test_hashing(testing):
    assert testing.hash("abcdABCD") < testing.size
