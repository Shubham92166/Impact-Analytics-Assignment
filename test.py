import utils, approach_1, approach_2, approach_3, approach_4

def test_approach_1():
    print("Testing approach 1")
    assert approach_1.get_ans_approach_1(5, 3) == "(3/32)/32", "It should be 3/32/32 for test case 1"
    print("Test Case 1 passed")
    assert approach_1.get_ans_approach_1(10, 3) == "(251/1024)/1024", "It should be 251/1024/1024 for test case 2"
    print("Test Case 2 passed")

def test_approach_2():
    print("Testing approach 2")
    assert approach_2.get_ans_approach_2(5, 3) == "(3/32)/32", "It should be 3/32/32 for test case 1"
    print("Test Case 1 passed")
    assert approach_2.get_ans_approach_2(10, 3) == "(251/1024)/1024", "It should be 251/1024/1024 for test case 2"
    print("Test Case 2 passed")

def test_approach_3():
    print("Testing approach 3")
    assert approach_3.get_ans_approach_3(5, 3) == "(3/32)/32", "It should be 3/32/32 for test case 1"
    print("Test Case 1 passed")
    assert approach_3.get_ans_approach_3(10, 3) == "(251/1024)/1024", "It should be 251/1024/1024 for test case 2"
    print("Test Case 2 passed")
    
def test_approach_4():
    print("Testing approach 4")
    assert approach_4.get_ans_approach_4(5, 3) == "(3/32)/32", "It should be 3/32/32 for test case 1"
    print("Test Case 1 passed")
    assert approach_4.get_ans_approach_4(10, 3) == "(251/1024)/1024", "It should be 251/1024/1024 for test case 2"
    print("Test Case 2 passed")

def test_util_pow():
    print("Testing power function")
    assert utils.power(5) == 32, "Test Case 1 passed"
    print("Test Case 1 passed")
    assert utils.power(10) == 1024, "Test Case 2 passed"
    print("Test Case 2 passed")

def test_util_total_ways_attend_class():
    print("Testing total ways to attend classes")
    utils.get_total_no_ways_to_attend_class(5) == 29, "It should be 29"
    print("Test Case 1 passed")
    utils.get_total_no_ways_to_attend_class(10) == 1024, "it should be 1024"
    print("Test Case 2 passed")

def test_probability_of_missing_graduation_ceremony():
    print("Testing probability of missing graduation ceremony")
    utils.get_probability_of_missing_graduation_ceremony(29, 32) == "(3/32)/32", "It should be (3/32)/32"
    print("Test Case 1 passed")
    utils.get_probability_of_missing_graduation_ceremony(773, 1024) == "(251/1024)/1024", "It should be (251/1024)/1024"
    print("Test Case 2 passed")


def run_test_cases():
    test_approach_1()
    test_approach_2()
    test_approach_3()
    test_approach_4()
    test_probability_of_missing_graduation_ceremony()
    test_util_total_ways_attend_class()
    test_util_pow()
    print("All test cases passed")

if __name__ == "__main__":
    run_test_cases()






