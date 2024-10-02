# a = [1, 1, 2]
#
# for i in range(len(a)-1):
#     count = 0
#     for j in range(1, len(a)):
#         if a[i] == a[j]:
#             if j >= i:
#                 count += 1
#
#     print(count)


# a = [0, 1, 0, 1, 0]
# count = 0
# for i in range(len(a)-1):
#     for j in range(1, len(a)):
#         if a[i] == a[j]:
#             if i != j:
#                 count += 1
# print(count)


a = [1, 2, 2, 2, 1]

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            if j != i:
                count += 1
    if count % 2 == 0:
        break
print(a[i])

