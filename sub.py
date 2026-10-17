def subtraction(positive, *negative):
    #('positive: ',positive,'negative: ',negative)
    for i in negative:
        positive = positive - i
    answer = positive
    print('answer: ',answer)

subtraction(20,9,4,5)