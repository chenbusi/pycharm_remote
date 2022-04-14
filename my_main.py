import addition
import user_input


def my_main():
    a = user_input.user_input()
    b = user_input.user_input()
    result = addition.addition(a, b)
    print(result)


my_main()
