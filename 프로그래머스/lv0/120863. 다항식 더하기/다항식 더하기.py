def solution(polynomial):
    answer = ''
    tmp_polynomial_list = list(polynomial.split('+'))
    polynomial_list_x = []
    polynomial_list_num = []
    for tmp_polynomial in tmp_polynomial_list:
        polynomial = tmp_polynomial.strip()
        if polynomial[-1] == 'x':
            if len(polynomial) == 1:
                polynomial_list_x.append(1)
            else:
                polynomial_list_x.append(int(polynomial[:-1]))
        else:
            polynomial_list_num.append(int(polynomial))
    sum_x = sum(polynomial_list_x)
    sum_num = sum(polynomial_list_num)
    if sum_x == 0:
        return f'{sum_num}'
    elif sum_num == 0:
        if sum_x == 1:
            return 'x'
        else:
            return f'{sum_x}x'
    else:
        if sum_x == 1:
            return f'x + {sum_num}'
        else:
            return f'{sum_x}x + {sum_num}'
   