from fractions import Fraction
import math

EPS = 1e-3

def pred(coefficients, x):
    return sum([coefficients[i] * x**i for i in range(len(coefficients))])

def differentiate(coefficients):
    differential_coefficients = []
    
    for i in range(1, len(coefficients)):
        differential_coefficients.append(
            i * coefficients[i]
        ) 

    if differential_coefficients == []:
        differential_coefficients = [0]


    return differential_coefficients


def optimize(coefficients, init_x):

    max_iter = 1000

    solution_x = init_x
    differential_coefficients = differentiate(coefficients)
    # print(f"OPTIMIZE equation: {print_coefficients(coefficients)}, differential: {print_coefficients(differential_coefficients)}")
    # print(init_x)

    for i in range(max_iter):
        solution_x -= (pred(coefficients, solution_x) / pred(differential_coefficients, solution_x))
        # print(i, solution_x)

        if math.isclose(pred(coefficients, solution_x), 0, abs_tol=1e-16):
            # print(i)
            return solution_x

    return None


def print_coefficients(coefficients):
    s = [f"({str(coefficients[i])}x^{i})" for i in range(len(coefficients)-1, -1, -1)]
    return " + ".join(s)


def solve(coefficients):
    if len(coefficients) == 2: return [-coefficients[0]/coefficients[1]]
    differential_coefficients = differentiate(coefficients)
    # print(f"equation: {print_coefficients(coefficients)}, differential: {print_coefficients(differential_coefficients)}")

    alphas = solve(differential_coefficients)
    if alphas == None: alphas = [0]

    solutions = []

    left_solution = optimize(coefficients, alphas[0]-EPS)
    if left_solution is not None:
        solutions.append(left_solution)

    for i in range(len(alphas)-1):
        solution_x = optimize(coefficients, (alphas[i]+alphas[i+1])/2)
        if solution_x is not None:
            solutions.append(solution_x)

    right_solution = optimize(coefficients, alphas[-1]+EPS)
    if right_solution is not None:
        solutions.append(right_solution)

    if len(solutions) == 0: return None
    return sorted(solutions)


if __name__ == '__main__':
    n_degree = int(input("enter a number of the polynomial's degree: "))
    coefficients = []

    for i in range(n_degree, 0, -1):
        coefficients.append(
            float(input(f"enter a coefficient of x^{i}: "))
        )

    coefficients.append(
        float(input("enter a constant: "))
    )

    coefficients = coefficients[::-1]

    solutions = solve(coefficients=coefficients)
    preprocessed_solutions = []

    for i in range(len(solutions)):
        frac_sol = Fraction(solutions[i]).limit_denominator()
        str_sol = f"{frac_sol.numerator}/{frac_sol.denominator}"

        if frac_sol.denominator == 1:
            if str(frac_sol.numerator) not in preprocessed_solutions:
                preprocessed_solutions.append(
                    str(frac_sol.numerator)
                )

        elif str_sol not in preprocessed_solutions:
            preprocessed_solutions.append(str_sol)

    print("solutions:", preprocessed_solutions)
