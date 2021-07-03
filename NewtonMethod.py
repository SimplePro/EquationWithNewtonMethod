from MathModule import Equation
import fractions

def regex_term(term, unknown_variable='x') -> str:
    term = term.replace(" ", '')

    if term[0] not in ['+', '-']: term = "+" + term

    if unknown_variable not in term:
        return term + unknown_variable + "^0"

    unknown_variable_index = term.index(unknown_variable)

    if term[unknown_variable_index+2:] == '':
        term += "^1"

    if term[:unknown_variable_index] in ['+', '-']:
        term = term.replace("+", "+1")
        term = term.replace("-", "-1")

    return term

def newton_method(terms = [], unknown_variable='x') -> tuple:
    terms = [regex_term(t) for t in terms]
    print(terms)
    equation = Equation(terms, unknown_variable)
    equation.to_derivative()

    result_list = [1]

    for i in range(10000):
        result_list.append(result_list[i] - (equation.calculate(result_list[i], mode="default") / equation.calculate(result_list[i], mode="derivative")))

        if result_list[i-1] == result_list[i]: break

    
    result_list[-1] = float(str(result_list[-1])[:16])
    fraction = fractions.Fraction(result_list[-1])

    return result_list[-1], str(fraction.numerator) + '/' + str(fraction.denominator)


if __name__ == '__main__':
    print(newton_method(terms = ["1x^4", "-4"]))