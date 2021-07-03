class Equation:
    def __init__(self, terms = [], unknown_variable = "x") -> None:
        self.terms = terms
        self.derivative_terms = []
        self.unknown_variable = unknown_variable


    # 항을 추가하는 메소드
    def add_term(self, term: str) -> None:
        self.terms.append(term)


    # 항 하나를 미분하는 메소드
    @staticmethod
    def to_derivative_term(unknown_variable, term: str) -> str:
        coefficient = 0
        quotient = 0

        # if unknown_variable not in term: return '0'  # 상수항이라면 0 리턴

        
        unknown_variable_index = term.index(unknown_variable)
        
        # if term[unknown_variable_index+2:] == '': return term[:unknown_variable_index]  # 일차식이라면 계수만 리턴
        # else:
        coefficient = int(term[:unknown_variable_index])
        quotient = int(term[unknown_variable_index+2:])

        if quotient == 0: return '0'
        if quotient == 1: return str(coefficient)

        return str(coefficient * quotient) + unknown_variable + "^" + str(quotient - 1)


    # 항들을 미분하는 메소드
    def to_derivative(self) -> None:
        for term in self.terms:
            self.derivative_terms.append(self.to_derivative_term(self.unknown_variable, term))
    

    # 매개변수 x 에 대한 식의 값을 구하는 메소드
    def calculate(self, x, mode="default") -> int:

        terms = []

        if mode == "default": terms = self.terms
        elif mode == "derivative": terms = self.derivative_terms
        
        result = 0

        for term in terms:
            if self.unknown_variable not in term:
                result += int(term)
                continue  # 상수면 그냥 계산
            
            unknown_variable_index = term.index(self.unknown_variable)
            
            if term[unknown_variable_index+2:] == '': result += int(int(term[:unknown_variable_index]) * x)

            else:
                coefficient = int(term[:unknown_variable_index])
                quotient = int(term[unknown_variable_index+2:])

                result += coefficient * (x ** quotient)

        return result


if __name__ == '__main__':
    equation = Equation()
    equation.add_term("-12x^3")
    equation.add_term("12x^2")
    equation.add_term("-3x")
    equation.add_term("-14")

    equation.to_derivative()
    print(equation.derivative_terms)

    print(equation.calculate(3, mode="derivative"))