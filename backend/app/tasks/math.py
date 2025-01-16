import random

def generate_math_problem():
    num1 = random.randint(1, 5)  # Generating numbers between 1 and 5
    num2 = random.randint(1, 5)  # Generating numbers between 1 and 5
    answer = num1 + num2
    if answer > 10:  # If the answer exceeds 10, adjust the numbers
        return generate_math_problem()
    problem = f"{num1} + {num2}"
    return {'problem': problem, 'answer': answer}
