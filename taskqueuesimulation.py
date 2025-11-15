from collections import deque

def getTaskOrder(time , m):
    q = deque() #make a double ended queue

    result = []

    for i , t  in enumerate(time , start=1): #gives job number and time for it (1,time[1])
        q.append((i,t))

    while q:
        task , remtime = q.popleft()
        remtime -= m

        if remtime <= 0: #if the task is completed
            result.append(task) 
        else: #if the task is not completed
            q.append((task , remtime))  

    return result

m = int(input("Enter Time Slice:"))
n = int(input("Enter Number of Tasks:"))
print("Enter List of time requred for each task")
time= []
while n:
    num = input()
    time.append(num)
print(getTaskOrder(time,m))
