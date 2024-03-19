a1 = int(input())
b1 = int(input())

a2 = int(input())
b2 = int(input())

# if (a1 < a2 and b1 < b2 and b1 < a1 ) and (a2 < a1 and b2 < b1 and b2 < a1):
#     print("пустое множество")
# elif a1 < a2 and b2 < b1:
#     print(a2, b2)
# elif a1 < a2 and b1 < b2:
#     print(a2, b1)
# elif a2 < a1 and b2 < b1:
#     print(a1, b2)

if (b1 == a2):
    print(b1)
elif (b2 == a1):
    print(b2)
elif (b1 < a2 or b2 < a1):
    print("пустое множество")
else:
    print(max(a1, a2), min(b1, b2))