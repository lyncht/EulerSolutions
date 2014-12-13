#Solution to problem 1 of Project Euler
#Tom Lynch

sumOfAnswers = 0
for i in range(0,1000):
    if i%3==0:
        sumOfAnswers += i
    elif i%5==0:
        sumOfAnswers += i
print "Sum=", sumOfAnswers
