# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name = "Name"):
    return f"Hello, {name}!"

# Task 3: Calculator 
def calc(num1, num2, operator= "multiply"):
    try:
        if operator == "multiply":
            return num1 * num2
        if operator == "add":
            return num1 + num2
        if operator == "subtract":
            return num1 - num2
        if operator == "divide":
            return num1 / num2
        if operator == "modulo":
            return num1 % num2 
        if operator == "int_divide":
            return num1 // num2
        if operator == "power":
            return num1 **num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        if type == "str":
            return str(value)
        if type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

# Task 5: Grading System, using *args 
def grade(*args):
    try:
        avg = sum(args)/ len(args)
        if avg >=90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        if avg < 60:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    for i in range(count):
        return string * count

# Task 7: Student Scores, Using **kwargs
def student_scores(postional, **kwargs):
    if postional == "best":
        best_student = ""
        highest_grade = 0
        for key, value in kwargs.items():
            if value > highest_grade:
                highest_grade = value
                best_student = key
        return best_student 

    if postional == "mean":
        return sum(kwargs.values()) / len(kwargs.keys())

# Task 8: Titleize, with String and List Operations
def titleize(a_string):
    lower_words = ["a","on","an","the","of","and","is","in"]
    words = a_string.split()
    result = []
    for i, word in enumerate(words):
        if i ==0 or i == len(words) -1 or word not in lower_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)

print(titleize("war and peace"))

# Task 9: Hangman, with more String Operations
def hangman(secret,guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result= result + letter
        else:
            result = result + "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels = "aeiou"
    new_words = []

    for word in sentence.split():
        i=0
        while i < len(word) and word[i] not in vowels:
            if word[i:i + 2] =="qu":
                i +=2
            else:
                i += 1
        new_words.append(word[i:] + word[:i] + "ay")
    return " ".join(new_words)
