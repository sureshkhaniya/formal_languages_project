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


'''---------------------------------------------------------------------------------------------------------------------------------------'''
def kleene_closure_generator(base_language, max_length):
    """
    Generate all strings in L* (Kleene closure) up to max_length
    
    Args:
        base_language (list): List of strings representing the base language
        max_length (int): Maximum length of generated strings
    
    Returns:
        set: Set of all strings in L* with length <= max_length
    """
    # Start with the empty string (always part of Kleene closure)
    result = {""}

    # Keep building new strings by concatenating
    # until we reach the maximum length
    changed = True
    while changed:  
        changed = False
        new_strings = set()

        # Try to extend each string we already have
        for s in result:
            for word in base_language:
                new_str = s + word
                # Only keep if length is within max_length
                if len(new_str) <= max_length and new_str not in result:
                    new_strings.add(new_str)

        # If we found any new strings, add them to result
        if new_strings:
            result.update(new_strings)
            changed = True

    return result

def main():
    # ---------------- Test Cases ----------------
    
    # Example 1
    result = kleene_closure_generator(["a"], 3)
    expected = {"", "a", "aa", "aaa"}
    assert result == expected, f"Test 1 failed: got {result}"

    # Example 2
    result2 = kleene_closure_generator(["ab"], 4)
    assert "" in result2, "Test 2 failed: missing empty string"
    assert "ab" in result2, "Test 2 failed: missing 'ab'"
    assert "abab" in result2, "Test 2 failed: missing 'abab'"

    print("All tests passed!")

main()

