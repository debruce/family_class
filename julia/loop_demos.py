
for i in range(4):
    print("statement1", i)
    for j in range(3):
        s=f"    i={i} j={j}"
        print(s)
    print("statement2", i)
print("statement after for loop")

# w = 10

# while w > 0:
#     print("while statement1", w)
#     print("while statement2", w)
#     w -= 2
# print("statement after while loop")

# for i in range(20):
#     comparison_value = (i == 10) * 100
#     print(f"comparison_value={comparison_value}")
#     if comparison_value:
#         print('hurray!')
#     else:
#         print(i)
