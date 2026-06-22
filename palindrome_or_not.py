'''Check Weather Palindrome or Not'''
def IsPalindrome(text):
    if len(text)<=1:
        return True
    elif text[0]==text[-1]:
        return IsPalindrome(text[1:-1])
    else:
        return False

word=input("Enter a Word: ")
print(IsPalindrome(word))