#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('Your grade is an A. Woo Hoo!')
else:
    if score >= 80:
        print('Your grade is a B. Not bad!')
    else:
        if score >= 70:
            print('Your grade is a C. Fine.')
        else:
            if score >= 60:
                print('Your grade is a D. You need to improve.')
            else:
                print('Your grade is an F. See me ASAP.')