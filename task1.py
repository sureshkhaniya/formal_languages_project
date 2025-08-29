def is_in_language_L(string):
    count_a = 0
    count_b = 0
    seen_b = False   # flag to check if we've started counting b's

    for ch in string:
        if ch == "a":
            if seen_b:  
                return False
            count_a += 1
        elif ch == "b":
            seen_b = True
            count_b += 1
        else: 
            return False

    # At least one 'a' and 'b', and equal counts
    if count_a > 0 and count_b > 0 and count_a == count_b:
        return True
    else:
        return False


def test_assignment():
    # Test Task 1: Language L membership
    assert is_in_language_L("ab") == True
    assert is_in_language_L("aabb") == True
    assert is_in_language_L("aaabbb") == True
    assert is_in_language_L("aabbb") == False
    assert is_in_language_L("aba") == False
    assert is_in_language_L("") == False
    assert is_in_language_L("a") == False
    assert is_in_language_L("b") == False
test_assignment()
print("All tests passed!")
