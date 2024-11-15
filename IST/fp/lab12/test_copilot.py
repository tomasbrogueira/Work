#organize a string alphabetically but capital letteres come first
def alphabetize(string):
    lower = []
    upper = []
    for letter in string:
        if letter.isupper():
            upper.append(letter)
        else:
            lower.append(letter)
    return "".join(sorted(lower) + sorted(upper))

def calculator(input):
    #split input into list of numbers and operators
    input = input.split()
    #initialize result to the first number
    result = int(input[0])
    #loop through the rest of the list
    for i in range(1, len(input), 2):
        #if the operator is +, add the next number to the result
        if input[i] == "+":
            result += int(input[i+1])
        #if the operator is -, subtract the next number from the result
        elif input[i] == "-":
            result -= int(input[i+1])
        #if the operator is *, multiply the next number by the result
        elif input[i] == "*":
            result *= int(input[i+1])
        #if the operator is /, divide the result by the next number
        elif input[i] == "/":
            result /= int(input[i+1])
    return result

