from collections import deque

def timeToBuyTickets(tickets, k):
    queue = deque()
    time = 0
    for person , number_of_tickets in enumerate(tickets):
        queue.append((person,number_of_tickets))
    
    while queue:
        person , number_of_tickets = queue.popleft()
        number_of_tickets -= 1
        time+=1
        if person == k and number_of_tickets == 0:
            return time
        if number_of_tickets > 0:
            queue.append((person , number_of_tickets))


tickets = [2, 3, 2]
k = 2
print(timeToBuyTickets(tickets, k))
