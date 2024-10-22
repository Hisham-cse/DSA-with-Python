n = int(input("Enter the number: "))
count = 0

# Handle negative numbers by taking the absolute value
# if n < 0:
#     n = -n

# if n == 0:
#     count = 1  # Edge case: '0' has one digit

# for i in range(100):  # Arbitrary large range
#     if n == 0:
#         break
#     n = n // 10
#     count += 1

# print(count)

while n>0:
    n=n//10
    count+=1
print(count)