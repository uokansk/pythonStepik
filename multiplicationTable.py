numberHorizon = int(input())
numberVertical = int(input())
for i in range(1, numberHorizon+1):
    for j in range(1, numberVertical + 1):
        if i <= j:
            print(i*j, end='\t')
    print()
    print(i+1, end='\t'*i)
