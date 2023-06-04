from millercheck import my_miller_rabin
from math import e, exp, log, sqrt, floor
from sympy import legendre_symbol
from math import gcd
import math
from copy import deepcopy
from functools import reduce


def brillhart_morris(n: int) -> int or None:
    if my_miller_rabin(n):
        return n
    factor_base = [-1, 2]
    calc_l = round(pow(math.exp(pow(math.log(n, e) * math.log(math.log(n, e), e), 0.5)), 1 / math.sqrt(2)))
    factor_base.extend(
        i
        for i in range(3, calc_l)
        if my_miller_rabin(i) and legendre_symbol(n % i, i) == 1
    )
    incrementor = 0

    while True:
        step1 = [0, 1]
        step2 = [0, 1]
        sqrt_n = round(pow(n, 0.5), 3)
        val_1 = 1
        res_1 = int(sqrt_n) + incrementor
        uni_1 = res_1
        step_idx = 2
        s_n_number = 1
        b_smooth_numbers = {}
    
        if sqrt_n.is_integer():
            return int(sqrt_n)

        if incrementor > 1000:
            return None
        
        while True:
            next_step = (res_1 * step1[-1] + step1[-2]) % n
            step1.append(next_step)
            step_tmp = pow(step1[-1], 2, n)
            if step_tmp > n // 2:
                step_tmp = step_tmp - n
            tmp_b_s2_count = step2.count(step_tmp)
            if tmp_b_s2_count > 20:
                incrementor = incrementor + 1
            else:
                step2.append(step_tmp)
            
            bin_vector = [int(step_tmp < 0)] * len(factor_base)
                    
            num = abs(step_tmp)
            counter = 0
            
            for unpack_tmp, factor in enumerate(factor_base[1:], start=1):
                while num % factor == 0:
                    counter += 1
                    num //= factor
            
                bin_vector.append(counter % 2)
                counter = 0
        
            if num == 1 and set(bin_vector) != {0}:
                b_smooth_numbers[step_idx] = bin_vector

            val_2 = (n - pow(uni_1, 2)) / val_1
            uni_2 = floor((sqrt_n + uni_1) / val_2)
            uni_1, val_1, res_1 = uni_2 * val_2 - uni_1, val_2, uni_2
            step_idx += 1

            if len(b_smooth_numbers) > s_n_number:
                smooth_matrix = deepcopy(list(b_smooth_numbers.values()))
                height, width = len(smooth_matrix), len(smooth_matrix[0])
                det_value = [0] * height
            #gauss elemination part
                for j in range(width):
                    for i, val in enumerate(row[j] for row in smooth_matrix):
                        if val:
                            smooth_matrix = [[(smooth_matrix[h][k] + ([row[j] for row in smooth_matrix])[h]) % 2 if k != j and smooth_matrix[i][k] else row[k] for k in range(width)] for h, row in enumerate(smooth_matrix)]
                            det_value[i] = 1
                            break
            #//

                if any(det_value):
                    zero_row = [(smooth_matrix[i], i) for i in range(height) if not det_value[i]]
                else:
                    return None

                for zero_row_loop, zero_row_idx in zero_row:
                    solution = [j for i in [i for i in range(len(zero_row_loop)) if zero_row_loop[i]] for j in range(height) if smooth_matrix[j][i] == zero_row_loop[i] and det_value[j]]
                    solution.insert(0, zero_row_idx)
                    x, y = reduce(lambda acc, curr: (acc[0] * step1[curr], acc[1] * step2[curr]), [list(b_smooth_numbers.keys())[index] for index in solution], (1, 1))
                    y, x = int(sqrt(y) % n), x % n
                    gcd_1, gcd_2 = gcd(x - y, n), gcd(x + y, n)
                    if 1 < gcd_1 < n and 1 < gcd_2 < n: return gcd_1
                s_n_number += 5