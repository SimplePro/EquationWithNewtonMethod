from MathModule import Equation, regex_term
import fractions


def newton_method(terms = [], unknown_variable='x') -> tuple:
    terms = [regex_term(t) for t in terms]
    print(terms)
    equation = Equation(terms, unknown_variable)
    equation.to_derivative()

    result_list = []

    for i in range(1, 10000):
        a = equation.calculate(i, mode="default") - equation.calculate(i, mode="derivative")
        if a != 0:
            result_list.append(i)
            break

    for i in range(10000):
        result_list.append(result_list[i] - (equation.calculate(result_list[i], mode="default") / equation.calculate(result_list[i], mode="derivative")))

        if result_list[i-1] == result_list[i]: break

        # 이렇게 허근을 판단하는지는 이유는 NewtonMethodMemo 파일을 확인.
        elif i > 3 and abs(result_list[i-1] - result_list[i-2]) < abs(result_list[i-1] - result_list[i]): return "허근", "허근"
    
    result_list[-1] = float(str(result_list[-1])[:16])

    fraction = fractions.Fraction(result_list[-1])

    return result_list[-1], str(fraction.numerator) + '/' + str(fraction.denominator)


if __name__ == '__main__':
    print(newton_method(terms = ["x^4", "+x^3", "-x^2", "+4"]))