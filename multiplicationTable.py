numberHorizon = int(input())
numberVertical = int(input())
for i in range(1, numberHorizon+1):
    for j in range(1, numberVertical + 1):
        print(i*j, end='\t')
    print()
