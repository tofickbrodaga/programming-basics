def get_by_idx(lst: list) -> None:
    try:
        return lst[int(input())]
    except ValueError:
        print('Вы должны вводить числа')
    except IndexError:
        print(f'Индекс должен быть от 0 до {len(lst)-1}')

print()

def remove_common(fst: list, snd: list) -> list:
    return [value for value in fst + snd if value not in set(fst) & set(snd)]

def some_of_dicts(*args: dict[str, int|float]) -> dict:
    result = {}
    for arg in args:
        for key, value in arg.items():
            if key in result.keys():
                result[key] += value
            else:
                result[key] = value
    return result

print(some_of_dicts())

try:
    num = float(input())
except ValueError:
    print('Нужно вводить число')
except KeyboardInterrupt:
    print('Не смешно')
else:
    print(num ** 2)

def unions(first: dict, second: dict) -> dict:
    first.update(second)
    return first
print(unions({'two': 3}, {'two': 2}))