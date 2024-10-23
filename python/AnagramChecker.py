def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if are_anagrams(str1, str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
