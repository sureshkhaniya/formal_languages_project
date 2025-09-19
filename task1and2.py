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
    # Test Task 1: Language L membership
    assert is_in_language_L("ab") == True
    assert is_in_language_L("aabb") == True
    assert is_in_language_L("aaabbb") == True
    assert is_in_language_L("aabbb") == False
    assert is_in_language_L("aba") == False
    assert is_in_language_L("") == False
    assert is_in_language_L("a") == False
    assert is_in_language_L("b") == False

print("All tests passed!")
test_assignment()


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

def main_kleene_closure():
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
    assert len([s for s in result2 if len(s) <= 4]) >= 3

    print("All tests passed!")

main_kleene_closure()

# Function to generate the nth string of the language M
def generate_recursive_language_M(n):
    # Base case: if n is 0, just return "x"
    if n == 0:
        return "x"
    else:
        # Recursive case: put "y" in front and "z" at the end
        return "y" + generate_recursive_language_M(n - 1) + "z"
    
# Main function to test
def main_recursive():
    # Test cases
    assert generate_recursive_language_M(0) == "x"
    assert generate_recursive_language_M(1) == "yxz"
    assert generate_recursive_language_M(2) == "yyxzz"
    assert generate_recursive_language_M(3) == "yyyxzzz"

    # If all asserts pass, print this message
    print("All tests passed!")


# Run the program
main_recursive()

def regex_match(pattern, string):
    """
    Very simple regex matcher for beginners.
    Supports: concatenation, | (union), * (Kleene star).
    """

    # If the pattern is empty, the string must also be empty
    if pattern == "":
        return string == ""

    # -------- Handle union (|) --------
    if "|" in pattern:
        # Split the pattern into two parts around |
        left, right = pattern.split("|", 1)
        return regex_match(left, string) or regex_match(right, string)

    # -------- Handle star (*) --------
    if len(pattern) >= 2 and pattern[1] == "*":
        char = pattern[0]
        # Case 1: use zero times -> skip "a*" and try rest
        if regex_match(pattern[2:], string):
            return True
        # Case 2: if string starts with char, consume one and stay in pattern
        if string != "" and string[0] == char:
            return regex_match(pattern, string[1:])
        return False

    # -------- Handle single character / concatenation --------
    if string != "" and pattern[0] == string[0]:
        return regex_match(pattern[1:], string[1:])

    return False


# ----------------- Tests -----------------
def main_regex():
   
    assert regex_match("a*", "") == True
    assert regex_match("a*", "aaa") == True
    assert regex_match("a*b", "aaab") == True
    assert regex_match("a|b", "a") == True
    assert regex_match("a|b", "c") == False
    assert regex_match("ab", "ab") == True
    assert regex_match("ab", "a") == False
    print("All tests passed successfully!")

main_regex()



