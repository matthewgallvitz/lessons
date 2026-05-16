# Your code should go here!

def create_person_dict():
    """
    TODO: Return a dictionary with the keys:
      - "first_name"
      - "last_name"
    Each value should be a non-empty string.
    """
    person = {"first_name":"matthew"}
    person["last_name" ] = "Gallvitz"
    #print(person)
    return person


def add_middle_name(person):
    """
    TODO: Take a dictionary that contains 'first_name' and 'last_name'.
    Return a NEW dictionary with an added key:
      - "middle_name": <non-empty string>
    """
    person["middle_name" ] = "john"
   
    return person


def get_value_by_key(d, key):
    """
    TODO: Return the value stored in the dictionary for the given key.
    If the key does not exist, return None.
    """
    if(key not in d):
        return None
    
    return d[key]



def update_value(d, key, new_value):
    """
    TODO: Update the dictionary so that `key` now maps to `new_value`.
    Return the updated dictionary.
    """

    
    d[key] = new_value
    print (d[key])
    return d


def remove_key(d, key):
    """
    TODO: Remove the given key from the dictionary if it exists.
    Return the updated dictionary.
    """
    pass

# You should not have to change any code below here!

def run_tests():
    print("Running dictionary tests...\n")

    # 1️⃣ Test: create_person_dict()
    person = create_person_dict()
    assert isinstance(person, dict), "create_person_dict() must return a dictionary."

    assert "first_name" in person, "Dictionary must have a 'first_name' key."
    assert "last_name" in person, "Dictionary must have a 'last_name' key."

    assert isinstance(person["first_name"], str) and person["first_name"].strip() != "", \
        "'first_name' must be a non-empty string."

    assert isinstance(person["last_name"], str) and person["last_name"].strip() != "", \
        "'last_name' must be a non-empty string."

    # 2️⃣ Test: add_middle_name()
    updated = add_middle_name(create_person_dict())
    assert "middle_name" in updated, "Dictionary must contain new key 'middle_name'."
    assert isinstance(updated["middle_name"], str) and updated["middle_name"].strip() != "", \
        "'middle_name' must be a non-empty string."

    # 3️⃣ Test: get_value_by_key()
    sample = {"a": 1, "b": 2}
    assert get_value_by_key(sample, "a") == 1, "Should return value for an existing key."
    assert get_value_by_key(sample, "missing") is None, "Should return None if key doesn't exist."

    # 4️⃣ Test: update_value()
    updated_dict = update_value({"x": 10}, "x", 99)
    assert updated_dict["x"] == 99, "update_value() should modify existing keys."

    new_key_dict = update_value({"a": 1}, "b", 2)
    assert new_key_dict["b"] == 2, "update_value() should add new key if it doesn't exist."

    # 5️⃣ Test: remove_key()
    removed = remove_key({"first": 1, "second": 2}, "first")
    assert "first" not in removed, "remove_key() should remove the key if it exists."

    removed_noop = remove_key({"only": 5}, "missing")
    assert removed_noop == {"only": 5}, "Removing a missing key should not change the dictionary."

    print("✅ All dictionary tests passed!")

if __name__ == "__main__":
    run_tests()
