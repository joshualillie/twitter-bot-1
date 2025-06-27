if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        records.append([name, score])
    records.sort(key = lambda x: x[1])
    scores.sort()
    
    lowest = records.pop(0)[1]
    runner_up = False
    runner_up_score = 100

    for x in range(len(records)):
        if runner_up and records[x][1] > runner_up_score:
            exit()
        else:
            runner_up = True
            runner_up_score = records[x][1]
            print(runner_up_score)
