from utils import get_total_no_ways_to_attend_class, get_probability_of_missing_graduation_ceremony

'''Using 1D array as a cache to store the calculated results'''
def get_ways_to_attend_graduation_ceremony(days, max_consecutive_absent_allowed):
    prev_day = [1]*(max_consecutive_absent_allowed+1)
    
    for day in range(1, days+1):
        cur_day = [0]*(max_consecutive_absent_allowed+1)
        cur_day[0] = 1
        for days_left in range(max_consecutive_absent_allowed+1):
            missed_ways = 0
            
            if days_left > 0:
                missed_ways = prev_day[days_left-1]
  
            no_missed_ways = prev_day[max_consecutive_absent_allowed]
            
            cur_day[days_left] =  missed_ways + no_missed_ways
        prev_day = cur_day
     
    return cur_day[max_consecutive_absent_allowed]

def get_ans_approach_4(days, allowed_absent_days):
    ways_to_attend_graduation_days = get_ways_to_attend_graduation_ceremony(days, allowed_absent_days)
    total_no_ways_to_attend_class = get_total_no_ways_to_attend_class(days)
    return get_probability_of_missing_graduation_ceremony(ways_to_attend_graduation_days, total_no_ways_to_attend_class)
    
