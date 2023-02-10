from utils import get_total_no_ways_to_attend_class, get_probability_of_missing_graduation_ceremony

def get_ways_to_attend_graduation_ceremony(days, absent_days_left, max_consecutive_absent_allowed):
    if days == 0:
        return 1
    
    missed_ways = 0
    if absent_days_left > 0:
        missed_ways = get_ways_to_attend_graduation_ceremony(days-1, absent_days_left-1, max_consecutive_absent_allowed)

    no_missed_ways = get_ways_to_attend_graduation_ceremony(days-1, max_consecutive_absent_allowed, max_consecutive_absent_allowed)
    
    return missed_ways + no_missed_ways

def get_ans_approach_1(days, allowed_absent_days):
    ways_to_attend_graduation_days = get_ways_to_attend_graduation_ceremony(days, allowed_absent_days, allowed_absent_days)
    total_no_ways_to_attend_class = get_total_no_ways_to_attend_class(days)
    return get_probability_of_missing_graduation_ceremony(ways_to_attend_graduation_days, total_no_ways_to_attend_class)
    


