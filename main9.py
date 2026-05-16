# --- Step 1: Define your functions below ---

def create_nested_list():
    """
    TODO:
    Return a list that contains TWO inner lists.
    Each inner list should contain at least two numbers.

    Example:
    [
        [1, 2],
        [3, 4]
    ]
    """
    return[
        [4,5],
        [6,7]
    ]



def get_first_inner_list(nested):
    """
    TODO:
    Return the first inner list from the nested list.
    """
    return (nested[0])


def get_first_element_of_second_list(nested):
    """
    TODO:
    
    Return the FIRST element of the SECOND inner list.
    """
    second_list = nested[1]
 
    return (second_list[0])


def add_inner_list(nested, new_list):
    """
    TODO:
    Add a new inner list to the nested list.
    Return the updated nested list.
    """

    nested.append(new_list)

    return nested


def flatten_once(nested):
    """
    TODO:
    Take a nested list (list of lists) and return a flat list
    containing all elements from the inner lists.

    Example:
    [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    play = []
    print(play)

    for inner_list in nested:
        print(inner_list)
        for numbers in inner_list:
            print(numbers)
            play.append(numbers)
    print(play)
    return play


def sum_nested(nested):
    """
    TODO:
    Return the total sum of ALL numbers inside ALL inner lists.

    Example:
    [[1, 2], [3, 4]] -> 10
    """
    guard = 0 
    print(guard)
    for inner_list in nested:
        for numbers in inner_list:
            guard = guard + numbers
    print(guard)
    return guard


# --- Tests ---
# --- You shouldn't have to change anything here! ---

def run_tests():
    print("Running nested array tests...\n")

    # 1️⃣ Create a nested list
    nested = create_nested_list()
    assert isinstance(nested, list), "Should return a list."
    assert len(nested) == 2, "Should contain exactly two inner lists."
    assert isinstance(nested[0], list), "First element should be a list."
    assert isinstance(nested[1], list), "Second element should be a list."

    # 2️⃣ Access first inner list
    first_inner = get_first_inner_list(nested)
    assert first_inner == nested[0], "Should return the first inner list."

    # 3️⃣ Access nested elements
    sample = [[10, 20], [30, 40]]
    assert get_first_element_of_second_list(sample) == 30, \
        "Should return the first element of the second list."

    # 4️⃣ Add a new inner list
    base = [[1, 2]]
    updated = add_inner_list(base[:], [3, 4])
    assert updated[-1] == [3, 4], "New inner list should be added at the end."
    assert len(updated) == 2, "Length should increase by 1."

    # 5️⃣ Flatten nested list
    flat = flatten_once([[1, 2], [3, 4]])
    assert flat == [1, 2, 3, 4], "Should flatten one level of nesting."

    # 6️⃣ Sum all elements
    total = sum_nested([[1, 2], [3, 4]])
    assert total == 10, "Should sum all elements in all inner lists."

    # Edge case: empty nested list
    assert sum_nested([]) == 0, "Sum of empty list should be 0."

    print("✅ All nested array tests passed!")


if __name__ == "__main__":
    run_tests()