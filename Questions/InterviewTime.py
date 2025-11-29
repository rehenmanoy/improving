# ---------------------------------------------------------
#  Interview Time – Faulty Watch Simulation (IBM Coding Round)
# ---------------------------------------------------------
#
#  PROBLEM:
#  A candidate sets his watch correctly in the morning, but the watch
#  is faulty and gains a few seconds every 5 minutes. The candidate
#  reaches the interview venue by following this faulty time, and is
#  informed that he arrived 'X' minutes early.
#
#  Given:
#      1. timeSetAt  – Time when the watch was set correctly (HHMM format)
#      2. secondsGainedEveryFiveMinute – Gain of the watch every 5 minutes
#      3. minutesEarly – How many minutes early the candidate reached
#
#  TASK:
#      Compute the ACTUAL time (24-hour format, HHMM) when the candidate
#      reached the venue.
#
# ---------------------------------------------------------
#  KEY LOGIC:
#
#  • The faulty watch gains G seconds every 5 minutes.
#  • Gain per minute = G / 5 seconds
#  • Gain per hour  = (G / 5) minutes
#
#  Example:
#      G = 5 seconds gained every 5 minutes
#      Gain per hour = 5/5 = 1 minute/hour
#
#  • If the candidate reaches 'minutesEarly' minutes early,
#    the faulty watch must gain that many minutes ahead.
#
#  • Therefore:
#        hours_needed = minutesEarly / (gain_per_hour)
#
#  • Convert hours_needed → TOTAL minutes, add to the original time,
#    and adjust for overflow:
#        - Convert overflow minutes to hours
#        - Wrap around hours using modulo 24
#
# ---------------------------------------------------------
#  VALIDATION:
#  • timeSetAt must be exactly 4 digits (HHMM)
#  • HH must be in [0–23], MM must be in [0–59]
#  • seconds gained must be positive
#
# ---------------------------------------------------------
#  TIME COMPLEXITY:
#      O(1) – Pure mathematical calculation + time formatting
#
# ---------------------------------------------------------
#  OUTPUT FORMAT:
#      Print the final time in strict 24-hour format (HHMM),
#      always 4 digits, with leading zeros if needed.
#
# ---------------------------------------------------------
#  CODE:

def interviewTime(timeSetAt, secondsGainedEveryFiveMinute, minutesEarly):

    # Validate format: exactly 4 digits
    if len(timeSetAt) != 4 or not timeSetAt.isdigit():
        print("Invalid input")
        return
    
    hh = int(timeSetAt[:2])
    mm = int(timeSetAt[2:])

    # Validate time range
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        print("Invalid input")
        return
    
    G = secondsGainedEveryFiveMinute

    # Validate positive gain
    if G <= 0:
        print("Invalid input")
        return

    # Gain per hour in minutes
    hourly_gain = G / 5   # minutes gained per hour

    # Real hours needed to gain 'minutesEarly'
    hours_needed = minutesEarly / hourly_gain
    total_minutes = int(hours_needed * 60)

    # Add to original time
    hh += total_minutes // 60
    mm += total_minutes % 60

    # Fix overflow
    hh += mm // 60
    mm = mm % 60
    hh = hh % 24

    # Print valid 24-hour format
    print(f"{hh:02d}{mm:02d}")


# TEST CASE
timeSetAt = "0600"
secondsGainedEveryFiveMinute = 5
minutesEarly = 10

interviewTime(timeSetAt, secondsGainedEveryFiveMinute, minutesEarly)
