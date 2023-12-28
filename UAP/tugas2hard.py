string = 'radar'

# Buat fungsi disini
def ispalindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

ispalindrome(string)

result= ispalindrome(string)

print(result)

