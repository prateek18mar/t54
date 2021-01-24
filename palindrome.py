# Check string is palindrome or not

def palindrome(string):
    n = string
    m = n[::-1]
    if m == n:
        print("Palindrome {}".format(string))
    else:
        print("Not a palindrome string {}".format(string))


palindrome(string="nesttsen1")
