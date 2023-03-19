# python3

import threading
import time
    
def threadJob(sleepTime) :
    time.sleep(sleepTime)

def jobTime(threadArray):
    count = 0
    for i in range(0, len(threadArray)):
        threadJob(threadArray[i])
        count += threadArray[i]

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    mas = [[] for i in range(n)]

    for i in range(0, n):
        mas[i].append(data[i])
        print(i, 0)

    for i in range(n, m):
        smallestThread = 0
        countInThread = 9999
        for j in range(0, n):
            totals = 0
            for k in range(0, len(mas[j])):
                totals += mas[j][k]
            if (totals < countInThread):
                countInThread = totals
                smallestThread = j
        mas[smallestThread].append(data[i])
        print(smallestThread, countInThread)

    ta = []

    for i in range(0, n):
        ta.append(threading.Thread(target=jobTime, args=(mas[i])))

    for i in range(0, len(ta)):
        ta[i].start()

if __name__ == "__main__":
    main()
