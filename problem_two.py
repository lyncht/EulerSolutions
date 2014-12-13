#Solution to problem 2 of Project Euler
#Tom Lynch

twoBefore = 1
oneBefore = 2
term = 0
sumOfTerms = 2
while term <= 4000000:
    term = oneBefore+twoBefore
    if term%2 ==0:
        sumOfTerms += term
    twoBefore = oneBefore
    oneBefore = term

print "Sum is", sumOfTerms 
    
