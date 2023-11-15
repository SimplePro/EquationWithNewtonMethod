from fractions import Fraction
import math
import sys

EPS = 1
betas = (0.5, 0.999)
lr = 0.002

class SGD:

    def __init__(self, coefficients, differential_coefficients):
        self.coefficients = coefficients
        self.differential_coefficients = differential_coefficients
    
    def optimize(self, init_x):
        solution_x = init_x
        print(init_x)

        for i in range(10000):
            solution_x -= lr * pred(self.differential_coefficients, solution_x) * pred(self.coefficients, solution_x)
            print(solution_x)

            if math.isclose(pred(self.coefficients, solution_x), 0, abs_tol=1e-4):
                return solution_x

        return None

def pred(coefficients, x):
    res = sum([coefficients[i] * x**i for i in range(len(coefficients))])
    # print(res)
    return res

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
    # return SGD(coefficients, differential_coefficients).optimize(init_x)
    # print(f"OPTIMIZE equation: {print_coefficients(coefficients)}, differential: {print_coefficients(differential_coefficients)}")
    # print(init_x)

    for i in range(max_iter):
        solution_x -= (pred(coefficients, solution_x) / pred(differential_coefficients, solution_x))
        # print(i, solution_x)

        if math.isclose(pred(coefficients, solution_x), 0, abs_tol=1e-8):
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
    # print(alphas)

    solutions = []

    # optim = SGD(coefficients, differential_coefficients)

    # left_solution = optim.optimize(alphas[0]-EPS)
    left_solution = optimize(coefficients, alphas[0] - EPS)
    if left_solution is not None:
        solutions.append(left_solution)

    for i in range(len(alphas)-1):
        # solution_x = optim.optimize((alphas[i]+alphas[i+1])/2)
        solution_x = optimize(coefficients, (alphas[i]+alphas[i+1])/2)
        # print(solution_x)
        if solution_x is not None:
            solutions.append(solution_x)

    # right_solution = optim.optimize(alphas[-1]+EPS)
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

    # (x-1/2)^3 * (x+3/4)^2 * (x-4)
    coefficients = [1, -4, -15/16, 125/32, -25/64, -129/128, 9/32]
    coefficients = coefficients[::-1]

    solutions = solve(coefficients=coefficients)
    preprocessed_solutions = []

    if solutions is None:
        print("there's no solution")
        sys.exit(0)

    for i in range(len(solutions)):
        frac_sol = Fraction(round(solutions[i], 2)).limit_denominator()
        str_sol = f"{frac_sol.numerator}/{frac_sol.denominator}"

        if frac_sol.denominator == 1:
            if str(frac_sol.numerator) not in preprocessed_solutions:
                preprocessed_solutions.append(
                    str(frac_sol.numerator)
                )

        elif str_sol not in preprocessed_solutions:
            preprocessed_solutions.append(str_sol)

    print("solutions:", preprocessed_solutions)
