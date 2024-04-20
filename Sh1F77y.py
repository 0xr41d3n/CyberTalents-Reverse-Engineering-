cipher="ReenYbkV'('&)"
i=2
for letter in cipher:
    plain=chr(ord(letter)+i)
    i=i+1
    print(plain,end=" ")
