# --- Step 1: Define your functions below ---
# Each function works with Python lists (which behave like arrays in other languages).

def create_empty_list():
    # TODO: Return a new empty list
    a = []
    return a 

def create_list_with_three_elements():
    # TODO: Return a new list with three numbers of your choice
    a = [1,2,3]
    return a

def get_first_element(mylist):
    # TODO: Return the first element of the list
    return mylist[0]

def add_element(mylist, value):
    # TODO: Add 'value' to the end of the list and return the updated list
    mynewlist = []
    for number in (mylist):
        mynewlist.append(number)
    mynewlist.append(value)
    print(mynewlist)
    return mynewlist

def get_length(mylist):
    # TODO: Return how many elements are in the list
    return len(mylist)

# --- Step 2: Tests ---
# These tests will help verify understanding of how arrays/lists work.

def run_tests():
    print("Running array tests...")

    # 1 Creating a list
    my_list = create_empty_list()
    assert isinstance(my_list, list), "make_list() should return a list"
    assert len(my_list) == 0, "Your list should contain exactly three elements"

    my_second_list = create_list_with_three_elements()
    assert isinstance(my_second_list, list), "make_list() should return a list"
    assert len(my_second_list) == 3, "Your list should contain exactly three elements"

    # 2 Accessing elements
    accessing_elements = [3,2,1]
    assert get_first_element(accessing_elements) == accessing_elements[0], "get_first_element() should return the first item in the list"

    # 3 Adding an element
    list_with_an_element_to_add = [3,2,1]
    element_to_add = 10
    extended = add_element(list_with_an_element_to_add, element_to_add) # use a copy of the list
    assert extended[-1] == element_to_add, "add_element() should add the new value to the end"
    print(len(extended))
    print(len(list_with_an_element_to_add))
    assert len(extended) == len(list_with_an_element_to_add) + 1, "List length should increase by 1"

    # 4 Getting list length
    assert get_length([1, 2, 3]) == 3, "get_length() should return the number of elements in the list"
    assert get_length([]) == 0, "get_length() should return 0 for an empty list"

    print("✅ All list tests passed!")

if __name__ == "__main__":
    run_tests()