from utils import get_total_no_ways_to_attend_class, get_probability_of_missing_graduation_ceremony

'''Using 2D array as a cache to store the calculated results'''
def get_ways_to_attend_graduation_ceremony(days, absent_days_left, max_consecutive_absent_allowed, cache):
    if days == 0:
        cache[days][absent_days_left] = 1
        return cache[days][absent_days_left]
    
    if cache[days][absent_days_left] != -1:
        return cache[days][absent_days_left]

    missed_ways = 0
    if absent_days_left > 0:
        missed_ways = get_ways_to_attend_graduation_ceremony(days-1, absent_days_left-1, max_consecutive_absent_allowed, cache)

    no_missed_ways = get_ways_to_attend_graduation_ceremony(days-1, max_consecutive_absent_allowed, max_consecutive_absent_allowed, cache)
    
    cache[days][absent_days_left] = missed_ways + no_missed_ways
    return cache[days][absent_days_left] 

def get_ans_approach_2(days, allowed_absent_days):
    cache = [[-1]*(allowed_absent_days+1) for day in range(days+1)]
    ways_to_attend_graduation_days = get_ways_to_attend_graduation_ceremony(days, allowed_absent_days, allowed_absent_days, cache)
    total_no_ways_to_attend_class = get_total_no_ways_to_attend_class(days)
    return get_probability_of_missing_graduation_ceremony(ways_to_attend_graduation_days, total_no_ways_to_attend_class)
