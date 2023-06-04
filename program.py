import time
from millercheck import my_miller_rabin
from p_polard import pollards_rho
from brill import brillhart_morris
from casual_trial_div import trial_division

def factorize(n):
    result = []

    steps = [
        ("Просте число", my_miller_rabin, None),
        ("Пробні ділення", trial_division, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        ("ρ-Поларда", pollards_rho, None),
        ("Брiлхарта-Моррiсона", brillhart_morris, None)
    ]

    for step_name, step_method, step_values in steps:
        start_time = time.time()
        if step_values:
            for val in step_values:
                if n % val == 0:
                    end_time = time.time()
                    print_result(n, step_name, val, end_time - start_time)
                    n //= val
                    result.append(val)
                    break
        elif step_method(n):
            if step_name == "Просте число":
                return helper(n, step_name, start_time, result)
            factor = step_method(n)
            end_time = time.time()
            print_result(n, step_name, factor, end_time - start_time)
            n //= factor
            result.append(factor)
        elif step_name == "Брiлхарта-Моррiсона":
            print("Не можу знайти канонічний розклад числа :(")
            return result
    simple_start_time = time.time()
    return helper(n, "Просте число", simple_start_time, result)

def helper(n, arg1, simple_start_time, result):
    end_time = time.time()
    print_result(n, arg1, n, end_time - simple_start_time)
    result.append(n)
    return result

def print_result(n, step_name, val, time_taken):
    print(f"Знайдено: {val} - методом {step_name}. [time = {time_taken} sec]")

if __name__ == "__main__":
    number_to_factorize = int(input("Введіть число дільники якого треба знайти: ")) 
    factors = factorize(number_to_factorize)
    print(f"Знайдено дільники {number_to_factorize}, це - {factors}")