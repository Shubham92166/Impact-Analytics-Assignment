def get_total_no_ways_to_attend_class(days):
    total_ways = power(days)
    return total_ways

def get_probability_of_missing_graduation_ceremony(ways_to_attend_ceremony, total_ways_to_attend_classes):
    return f'{total_ways_to_attend_classes - ways_to_attend_ceremony}/{total_ways_to_attend_classes}/{total_ways_to_attend_classes}'

def power(days):
    '''calculates 2^days'''
    def binexp(base, power):
        if power == 0:
            return 1
        val = binexp(base, power//2)
        ans = (val*val)
        if power % 2 == 0:
            return ans
        else:
            return (ans*base)
    
    return binexp(2, days)

    