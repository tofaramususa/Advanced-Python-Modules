
def ft_filter(function, iterable):
    """filter elements based on function
    Args:
        function: function to apply on each item in iterable
        iterable: iterable to apply function on
    Returns:
        pass: iterator with items of iterable for which function(item) is True
    """
    if function is None or callable(function) is False:
        return (item for item in iterable if item)
    if hasattr(iterable, '__iter__') is False:
        raise TypeError(f"{type(iterable)} is not iterable") 
    return (item for item in iterable if function(item))

def run_test(test_name, function, iterable, test_number):
    """Run a test comparing built-in filter with ft_filter"""
    built_in_result = list(filter(function, iterable))
    custom_result = list(ft_filter(function, iterable))
    passed = built_in_result == custom_result
    
    print(f"Test {test_number}: {test_name}")
    print(f"Input: {iterable}")
    print(f"Expected: {built_in_result}")
    print(f"Got: {custom_result}")
    print(f"Status: {'PASS' if passed else 'FAIL'}")
    print()
    
    return passed

def main():
    tests_passed = 0
    total_tests = 10  # Updated number of tests
    
    # Test 1: Nested data structures
    complex_list = [(1, 'a'), [2, 'b'], (3, 'c'), [4, 'd']]
    tests_passed += run_test("Filter tuples only",
                           lambda x: isinstance(x, tuple),
                           complex_list,
                           1)
    
    # Test 2: Custom objects with truth value
    class CustomBool:
        def __init__(self, value):
            self.value = value
        def __bool__(self):
            return self.value
        def __repr__(self):
            return f"CustomBool({self.value})"
    
    custom_objects = [CustomBool(True), CustomBool(False), CustomBool(True)]
    tests_passed += run_test("Filter custom objects with __bool__",
                           None,
                           custom_objects,
                           2)
    
    # Test 3: Nested function filtering
    def is_valid_person(person):
        return (isinstance(person, dict) and 
                'age' in person and 
                'name' in person and 
                person['age'] >= 18 and 
                len(person['name']) > 2)
    
    people = [
        {'name': 'Bob', 'age': 20},
        {'name': 'A', 'age': 25},
        {'name': 'Charlie', 'age': 17},
        {'age': 19},
        {'name': 'David', 'age': 22}
    ]
    tests_passed += run_test("Complex dictionary filtering",
                           is_valid_person,
                           people,
                           3)
    
    # Test 4: Generator input
    def fibonacci_gen():
        a, b = 0, 1
        for _ in range(10):
            yield a
            a, b = b, a + b
    
    tests_passed += run_test("Filter generator input",
                           lambda x: x % 2 == 0,
                           fibonacci_gen(),
                           4)
    
    # Test 5: Empty sequences
    tests_passed += run_test("Filter empty sequence",
                           lambda x: True,
                           [],
                           5)
    
    # Test 6: Mixed types with None
    mixed_types = [0, "", False, None, [], {}, (), set(), "text", 123, [1, 2], {'a': 1}]
    tests_passed += run_test("Filter mixed types with None predicate",
                           None,
                           mixed_types,
                           6)
    
    # Test 7: Function that raises exceptions
    def safe_div(x):
        try:
            return 10 / x != 1
        except ZeroDivisionError:
            return False
    
    numbers_with_zero = [0, 1, 2, 5, 10, 0, 20]
    tests_passed += run_test("Filter with exception handling",
                           safe_div,
                           numbers_with_zero,
                           7)
    
    # Test 8: Unicode strings
    unicode_strings = ["", "hello", "世界", "", "🌍", "α β γ", ""]
    tests_passed += run_test("Filter unicode strings",
                           lambda s: len(s.strip()) > 0,
                           unicode_strings,
                           8)
    
    # Test 9: Nested iterables
    nested_data = [
        range(3),
        [],
        [1, 2, 3],
        (),
        set([1, 2]),
        {},
        {'a': 1}
    ]
    tests_passed += run_test("Filter non-empty iterables",
                           lambda x: len(tuple(x)) > 0,
                           nested_data,
                           9)
    
    # Test 10: Large numbers and edge cases
    edge_cases = [float('inf'), float('-inf'), float('nan'), -0.0, 0.0, 2**31-1, -(2**31)]
    tests_passed += run_test("Filter numerical edge cases",
                           lambda x: isinstance(x, (int, float)) and x > 0,
                           edge_cases,
                           10)
    
    # Print summary
    print("=" * 40)
    print(f"Final Results: {tests_passed}/{total_tests} tests passed")
    if tests_passed == total_tests:
        print("All tests passed successfully!")
    else:
        print(f"Failed {total_tests - tests_passed} test(s)")

if __name__ == "__main__":
    main()