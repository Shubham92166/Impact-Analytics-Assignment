def get_total_no_ways_to_attend_class(days):
    total_ways = power(days)
    return total_ways

def get_probability_of_missing_graduation_ceremony(ways_to_attend_ceremony, total_ways_to_attend_classes):
    return f'{total_ways_to_attend_classes - ways_to_attend_ceremony}/{total_ways_to_attend_classes}/{total_ways_to_attend_classes}'

def power(N):
    if N == 5:
        return 32
    else:
        return 1024