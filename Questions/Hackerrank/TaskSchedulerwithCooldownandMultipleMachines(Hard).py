"""
Task Scheduler with Cooldown and Multiple Machines
--------------------------------------------------

Problem:
    We are given:
        - tasks: a list where each number represents a task type
        - m: number of machines (each machine runs 1 task per time unit)
        - k: cooldown (a machine cannot run the SAME task type again
          until k time units have passed)

Goal:
    Compute the minimum number of time units required to finish all tasks.

Key Ideas:
    1. Capacity Limit:
        With m machines, we can complete at most m tasks per time unit.
        So even with no cooldown, we need at least:
            total_tasks / m  time units (rounded up)

    2. Cooldown Limit:
        Some task types appear many times.
        Even if we spread them across machines, the busiest machine
        (the one that receives the most copies of that task type)
        determines how long cooldown forces us to wait.

        Example:
            If a task type appears 5 times and we have 2 machines,
            one machine must run that type at least 3 times.
            If cooldown = k, that machine needs:
                (3 runs with k gaps between them)
                total time = (3 - 1) * k + 1

        We compute this for each task type and take the maximum.

Final Answer:
    The real minimum time must satisfy BOTH limits:
        - the capacity limit
        - the cooldown limit
    So the answer is the maximum of these two values.

Time Complexity:
    O(n), where n = number of tasks

Space Complexity:
    O(t), where t = number of unique task types
"""
def calculateMinimumTimeUnits(tasks, m, k):
    n = len(tasks)
    if n==0 or m <= 0:
        return 0
    capacity_time = (n+m-1)//m
    
    freq = Counter(tasks)
    max_time = 0
    for count in freq.values():
        per_machine_capacity = (count + m -1 )//m
        if per_machine_capacity > 0:
            type_time = (per_machine_capacity - 1) * k + 1 
            if type_time > max_time:
                max_time = type_time
    return max(capacity_time , max_time)
