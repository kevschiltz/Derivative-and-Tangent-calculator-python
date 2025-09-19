#does the base derivative calculations
def derivative_calc(constant, exponent):
    #if c = 0 then we need to add instead of multiplying because 0 * any number = 0
    if constant == 0:
        c = exponent + constant
    else:
        c = exponent * constant
    #minus the exponent by one
    n = exponent - 1
    #returning the x-nomial
    if (c <= -1 or c > 1) and n == 1:
        return (f"{c}x")
    elif (c <= -1 or c > 1) and n == 0:
        return (f"{c}")
    elif (c <= -1 or c > 1) and n > 1:
        return (f"{c}x^{n}")
    else:
        return 0


def derivative_calc_values(constant, exponent):
    #if c = 0 then we need to add instead of multiplying because 0 * any number = 0
    if constant == 0:
        c = exponent + constant
    else:
        c = exponent * constant
    #minus the exponent by one
    n = exponent - 1

    return c, n




def single_derivative_calc(constant,exponent):
    print(derivative_calc(constant,exponent))

#single_derivative_calc(1,2)

def binomial_derivative_calc(constant_one,exponent_one,constant_two,exponent_two):
    #if i was to input 4,3,6,2 for the parameter, then the binomial will be 4X^3+6X^2

    if constant_two < 0:
        print(f"Your equation is: {constant_one}X^{exponent_one}{constant_two}X^{exponent_two}")
    else:
        print(f"Your equation is: {constant_one}X^{exponent_one}+{constant_two}X^{exponent_two}")
    c_one= constant_one
    c_two= constant_two
    ex_one= exponent_one
    ex_two= exponent_two

    first_half = derivative_calc(c_one,ex_one)
    second_half = derivative_calc(c_two, ex_two)

    if c_two < 0:
        print(f"Derivative: {first_half}{second_half}")
    else:
        print(f"Derivative: {first_half}+{second_half}")

#binomial_derivative_calc(4,3,2,2)

def trinomial_derivative_calc(constant_one,exponent_one,constant_two,exponent_two, constant_three, exponent_three):
    if constant_two < 0 and constant_three < 0:
        if exponent_three == 0 or exponent_three == 1:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}{constant_two}X^{exponent_two}{constant_three}X")
        else:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}{constant_two}X^{exponent_two}{constant_three}X^{exponent_three}")
    elif constant_two < 0 and constant_three > 0:
        if exponent_three == 0 or exponent_three == 1:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}{constant_two}X^{exponent_two}+{constant_three}X")
        else:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}{constant_two}X^{exponent_two}+{constant_three}X^{exponent_three}")
    elif constant_two > 0 and constant_three < 0:
        if exponent_three == 0 or exponent_three == 1:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}+{constant_two}X^{exponent_two}{constant_three}X")
        else:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}+{constant_two}X^{exponent_two}{constant_three}X^{exponent_three}")
    else:
        if exponent_three == 0 or exponent_three == 1:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}+{constant_two}X^{exponent_two}+{constant_three}X")

        else:
            print(f"Your trinomial equation is: {constant_one}X^{exponent_one}+{constant_two}X^{exponent_two}+{constant_three}X^{exponent_three}")

    c_one= constant_one
    c_two= constant_two
    c_three = constant_three
    ex_one= exponent_one
    ex_two= exponent_two
    ex_three= exponent_three



    first_half = derivative_calc(c_one, ex_one)
    second_half = derivative_calc(c_two, ex_two)
    third_half = derivative_calc(c_three, ex_three)
    print("-----------------------------------------")

    if c_two < 0 and c_three < 0:
        if third_half != 0:
            print(f"Derivative: {first_half}{second_half}{third_half}")
        else:
            print(f"Derivative: {first_half}{second_half}")
    elif c_two < 0 and c_three > 0:
        if third_half != 0:
            print(f"Derivative: {first_half}{second_half}+{third_half}")
        else:
            print(f"Derivative: {first_half}{second_half}")
    elif c_two > 0 and c_three < 0:
        if third_half != 0:
            print(f"Derivative: {first_half}+{second_half}{third_half}")
        else:
            print(f"Derivative: {first_half}+{second_half}")
    elif c_two > 0 and c_three > 0:
        if third_half != 0:
            print(f"Derivative: {first_half}+{second_half}+{third_half}")
        else:
            print(f"Derivative: {first_half}+{second_half}")

    c_one = derivative_calc_values(constant_one, exponent_one)[0]
    ex_one = derivative_calc_values(constant_one, exponent_one)[1]
    c_two = derivative_calc_values(constant_two, exponent_two)[0]
    ex_two = derivative_calc_values(constant_two, exponent_two)[1]
    c_three = derivative_calc_values(constant_three, exponent_three)[0]
    ex_three = derivative_calc_values(constant_three, exponent_three)[1]

    print("-----------------------------------------")
    x_value = int(input("Whats the x value? "))
    print("-----------------------------------------")
    y_value = int(input("Whats the y value? "))
    print("-----------------------------------------")
    m = ((x_value ** ex_one) * c_one) + ((x_value ** ex_two) * c_two)+((x_value ** ex_three) * c_three)
    b = (m * -x_value) + y_value
    if b > 0:
        equation = f"y = {int(m)}X + {int(b)}"
        print(f"The tangent line at ({x_value},{y_value}) is: {equation}")
    else:
        equation = f"y = {int(m)}X{int(b)}"
        print(f"The tangent line at ({x_value},{y_value}) is: {equation}")


trinomial_derivative_calc(4,3,-2,3,5,0)















