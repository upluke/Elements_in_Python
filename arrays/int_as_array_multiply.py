# 5.3 multiply two arbitrary-precision integers
# There are m partial products, each with at most n+1 digits. We perform O(1) operations on digit in each partial product, so the time complexity is O(nm)

# As in solution 5.2 on Page 44, the possibility of overflow precludes us from converting to the integer type.
# instead we can use the grade-school algorithm for multiplication which consists of multiplying the first number by each digit of the second, and then adding all the resulting terms.
# from a spce perspective, it is better to incrementally add the terms rather than compute all of them individually and then add them up. The number of digits required for the product is at most n+m for n and m digit operands, so we use an array of size n+m for the result.

# for example, when multiplying 123 with 987, we would form 7*123=861, then we would form 8*123*10 =9840, which we would add to 861 to get 10701. Then we would form 9*123*100=110700, which we would add to 10701 to get the final result 121401.

# 123    123    123
# *
# 7 *1   8*10   9*100

# 7    +  80 +  900 =987
def multiply(num1, num2):

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(multiply([1, 2], [4]))

# https://leetcode.com/problems/multiply-strings/
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


def multiply(num1, num2):
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            mul += result[i + j + 1]
            result[i + j + 1] = mul % 10
            result[i + j] += mul // 10
    # e.g., num1='123', num2='456'; then result = [0, 5, 6, 0, 8, 8], res = [5, 6, 0, 8, 8]
    sb = []
    for res in result:
        if len(sb) != 0 or res != 0:  # deal with leading zero issue
            sb.append(res)
    return "0" if len(sb) == 0 else ''.join(str(s) for s in sb)


print(multiply("123", "456"))
# init:
# def multiply(num1, num2):
#   if num1=="0" or num2=="0":
#     return "0"
#   new_num1=0
#   unit=1
#   for i in range(len(num1)-1, -1, -1):
#     cur_num=ord(num1[i])-48
#     new_num1+=cur_num*unit
#     unit*=10

#   new_num2=0
#   unit=1
#   for i in range(len(num2)-1, -1, -1):
#     cur_num=ord(num2[i])-48
#     new_num2+=cur_num*unit
#     unit*=10

#   sum_num=new_num1*new_num2

#   res=''
#   while sum_num:
#     cur=sum_num%10
#     res= chr(cur+48)+res
#     sum_num=sum_num//10
#   return res
# print(multiply("123", "456")) #"56088"
# print(multiply("2", "3")) #"6"