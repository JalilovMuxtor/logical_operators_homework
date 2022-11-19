def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """ 
    a
    z1=a%10
    z2=a//10
    return z1==z2
print(main(33))
