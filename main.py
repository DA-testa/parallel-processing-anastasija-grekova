# python3

from queue import Queue
import threading
import time

count = []
n = 0 #thread count 
#jobIndex = 0
activeThreads = 0
m = 0 #job count
data = [] #seconds per job
    
def jobTime(second, threadIndex, q):
#    global jobIndex
    global count
    q.put(0)
 #   global jobIndex
    #jobIndex += 1
    time.sleep(second)
    #print(threadIndex, count[threadIndex])
    count[threadIndex] += second

    
    
    if q.qsize() < m:
        #count[threadIndex] += second
        jobTime(data[q.qsize()], threadIndex, q)
        #t = threading.Thread(target=jobTime, args=(data[len(jobIndex)-1], threadIndex))
        #t.start()
        #print(threadIndex, " ", data[i])



def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    global m
    global n
    global data
    n, m = map(int, input().split())       # 2 5
    data = list(map(int, input().split())) # 1 2 3 4 5
    print(n, m)
    print(data)
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []
    #output = []
    global activeThreads
    global count
    queue = Queue()
    for i in range(0, n):
        #jobTime(data[i], i)
        activeThreads += 1
        count.append(0)
        t = threading.Thread(target=jobTime, args=(data[i], i,queue))
        t.start()
       # t.join()

        #print(i, " ", 0)

        
        

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    

    # TODO: create the function
    #result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
