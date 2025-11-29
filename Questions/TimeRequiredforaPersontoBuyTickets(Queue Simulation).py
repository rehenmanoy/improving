# ---------------------------------------------------------
#  Time Required for Kth Person to Buy Tickets
#  Queue Simulation (IBM-Style Greedy + Simulation Problem)
# ---------------------------------------------------------
#
#  PROBLEM:
#  You are standing in a ticket queue where each person wants
#  a certain number of tickets. Every second:
#      - The person at the front buys exactly 1 ticket.
#      - If they still need more tickets, they move to the back.
#      - If they finish, they leave the queue.
#
#  Given:
#      tickets[i] = number of tickets person i needs
#      k = your position (0-indexed)
#
#  TASK:
#      Return the total number of seconds it takes for the
#      person at index k to finish buying all tickets.
#
# ---------------------------------------------------------
#  APPROACH: QUEUE SIMULATION
#
#  We simulate the queue using collections.deque().
#  Each step:
#      - Pop the front person
#      - Decrease their ticket count by 1
#      - Increase time by 1 (each ticket takes 1 second)
#      - If this person is 'k' and has now finished → return time
#      - If they still need more tickets → re-add them to queue
#
#  This mimics a round-robin scheduling system, identical to
#  CPU scheduling or service queues.
#
# ---------------------------------------------------------
#  WHY GREEDY?
#  The system always greedily serves the front of the queue.
#  No rearranging of order is allowed.
#
# ---------------------------------------------------------
#  TIME COMPLEXITY:
#      O(total tickets)    (each ticket purchase = 1 operation)
#
#  SPACE COMPLEXITY:
#      O(n)                (queue storing all people)
#
# ---------------------------------------------------------
#  CODE:

from collections import deque

def timeToBuyTickets(tickets, k):
    queue = deque()
    time = 0

    # store person index + their current ticket count
    for person, ticket_count in enumerate(tickets):
        queue.append((person, ticket_count))
    
    while queue:
        person, ticket_count = queue.popleft()

        # person buys 1 ticket
        ticket_count -= 1
        time += 1

        # If THIS is the target person and they just finished → return time
        if person == k and ticket_count == 0:
            return time
        
        # still needs more tickets → back to queue
        if ticket_count > 0:
            queue.append((person, ticket_count))


tickets = [2, 3, 2]
k = 2
print(timeToBuyTickets(tickets, k))  # Output: 6
