age = 16

if age <= 18:
    print("oh you are a baby yet")
elif age >= 18 and age < 60:
    print("you are an adult")
else: #it could be "elif age >= 60"
    print("you are already a fossil. lol")


# ------------------------------------------------------------------------------------------------

schoolGrades = [9, 10, 9]

def calculateAverage(schoolGrades):
    sum = 0
    for element in schoolGrades:
        sum += element
    return sum / len(schoolGrades)

average = calculateAverage(schoolGrades)


if average >= 7:
    print(f"congragulations! you were approved. Your average was {average}")
    if average >= 7 and average < 8:
        print("your average was good")
    elif average >= 8:
        print("you are amazing!")
else:
    print(f"you were not approved. Your average was {average}")

