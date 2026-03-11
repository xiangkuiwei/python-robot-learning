# 字符串反转递归示例
def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print("字符串反转递归示例")
test_str = "hello"
print(f"'{test_str}' 反转后: '{reverse_string(test_str)}'")
test_str = "Python"
print(f"'{test_str}' 反转后: '{reverse_string(test_str)}'")

# 演示递归过程
def reverse_detail(s):
    if len(s) <= 1:
        print(f"返回's' ")
        return s
    else:
        print(f"reverse('{s}') = reverse('{s[1:]}') + '{s[0]}'")
        result = reverse_detail(s[1:])+s[0]
        print(f"结果: '{result}'")
        return result
print("\n 递归过程演示:")
reverse_detail("hello")