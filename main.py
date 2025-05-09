import ast

def multiply_by_ten(number_str):
    try:
        number = ast.literal_eval(number_str)
        if not isinstance(number, (int, float)):
            raise ValueError("Введенные данные должны быть числом")
        return number * 10
    except (ValueError, SyntaxError) as e:
        raise ValueError(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    user_input = input("Введите число: ")
    try:
        result = multiply_by_ten(user_input)
        print(f"{user_input} * 10 = {result}")
    except ValueError as e:
        print(e)