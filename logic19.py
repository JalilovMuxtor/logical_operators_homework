def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x%10==x//10 or x%10==(x//10)%10
    return x%10==x//10 or x%10==(x//10)%10
print(main(11))