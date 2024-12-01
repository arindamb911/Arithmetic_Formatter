def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error if problems to many"

    top_row = []
    middle_row = []
    bottom_row = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operator, num2 = parts

        if operator not in ['+','-']:
            return "Error: Operator must be '+', '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: number must only contain digits."
        if len(num1) > 4 or len(num2) >4:
            return "Error: Number cannot be more than four digits."
        if operator == '+':
            result = str(int(num1) + int(num2))
        elif operator == "-":
            result = str(int(num1) - int(num2))
        
        width = max(len(num1), len(num2)) + 2

        top_row.append(num1.rjust(width))
        middle_row.append(operator + ' ' + num2.rjust(width - 2))
        bottom_row.append('-' * width)

        if show_answers:
            answers.append(result.rjust(width))
        
    arranged_problems = '    '.join(top_row) + '\n' + '    '.join(middle_row) + '\n' + '    '.join(bottom_row) 

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems






    


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')