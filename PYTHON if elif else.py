# Using if, elif, and else in Functions:
# 1:

def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

result = classify_number(7)
print("7 is", result)  # Output: "7 is Positive"

result = classify_number(-2)
print("-2 is", result)  # Output: "-2 is Negative"

result = classify_number(0)
print("0 is", result)  # Output: "0 is Zero"

# 2:

def grade_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test cases
score1 = 95
score2 = 78
score3 = 62

grade1 = grade_score(score1)
grade2 = grade_score(score2)
grade3 = grade_score(score3)

print(f"Score: {score1}, Grade: {grade1}")  # Output: Score: 95, Grade: A
print(f"Score: {score2}, Grade: {grade2}")  # Output: Score: 78, Grade: C
print(f"Score: {score3}, Grade: {grade3}")  # Output: Score: 62, Grade: D
