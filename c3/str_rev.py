def reverse(text):
    a = ""
    for j in range(len(text)):
        a = a + text[len(text) - j - 1]
    return a


print(reverse("Python@#$%"))