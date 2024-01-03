while True:
    try: print(f'{eval(input("Введите выражение ---> ")):,}'); break
    except ZeroDivisionError as e: print(f"На ноль делить нельзя! {e}"); continue
    except NameError as e: print(f"Выражение введено не верно. {e}"); continue
