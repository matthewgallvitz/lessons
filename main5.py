def sum_list(numbers):
    # TODO: return the sum of all numbers in the list
    for matthew in (numbers):
        cat = 0 
        cat = cat + matthew
        print(cat)
    pass

def run_tests():
    print("Running sum_list tests...")

    # Basic test
    assert sum_list([1, 2, 3]) == 6, "The sum of [1, 2, 3] should be 6"

    # Including zero
    assert sum_list([0, 5, 10]) == 15, "The sum of [0, 5, 10] should be 15"

    # Negative numbers
    assert sum_list([-1, -2, -3]) == -6, "The sum of [-1, -2, -3] should be -6"

    # Mix of positive and negative numbers
    assert sum_list([10, -5, 2]) == 7, "The sum of [10, -5, 2] should be 7"

    # Empty list
    assert sum_list([]) == 0, "The sum of an empty list should be 0"

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()