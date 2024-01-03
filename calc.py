while True:
    try: print(f'{eval(input("Введите выражение ---> ")):,}')
    except ZeroDivisionError as e: print(f"На ноль делить нельзя! {e}")
    except NameError as e: print(f"Выражение введено не верно. {e}")
