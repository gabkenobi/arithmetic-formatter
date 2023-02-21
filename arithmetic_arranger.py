import re

def arithmetic_arranger(problems, should_show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_terms = []
    bottom_terms = []
    separators = []
    answers = []

    for p in problems:
        if not re.match('[0-9]+\\s*[\\+\\-]\\s*[0-9]+', p):
            if '/' in p or '*' in p:
                return "Error: Operator must be '+' or '-'."

        if '+' in p:
            first, second = p.split('+')
            op = '+'
        elif '-' in p:
            first, second = p.split('-')
            op = '-'

        first = first.strip()
        second = second.strip()

        if not (1 <= len(first) <= 4 and 1 <= len(second) <= 4):
            return 'Error: Numbers cannot be more than four digits.'
        elif not (first.isdigit() and second.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if op == '+':
            answer = str(int(first) + int(second))
        elif op == '-':
            answer = str(int(first) - int(second))

        longest = max([len(first), len(second)])

        first = '{: >{i}}'.format(first, i=longest+2)
        second = op + '{: >{i}}'.format(second, i=longest+1)
        separator = '-' * (longest+2)
        answer = '{: >{i}}'.format(answer, i=longest+2)

        top_terms.append(first)
        bottom_terms.append(second)
        separators.append(separator)
        answers.append(answer)

    top_line, bottom_line, separator_line, answer_line = ['    '.join(line) for line in (top_terms, bottom_terms, separators, answers)]
    arranged_problems = '\n'.join([top_line, bottom_line, separator_line])

    if should_show_answers:
        arranged_problems += '\n' + answer_line

    return arranged_problems