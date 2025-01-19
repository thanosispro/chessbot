def opponent(cp, previous_cp, best_cp):
    diff1 = cp - previous_cp
    diff2 = cp-best_cp
    print(diff1, diff2)
    
    value = ''  # Default value
    
    # Condition checks
    if diff2 > 500:
        value = 'You Missed'
    elif abs(diff2)<4:
        value = 'best move'
    elif abs(diff2)<10 and diff1 > 300:
        value = 'brilliant'
    elif diff1 > 150 and abs(diff2)<10:
        value = 'great move'
    elif diff1 > 50 and abs(diff2)<10:
        value = 'nice move'
   
    elif diff1 >= 0:
        value = 'good'
    elif abs(diff2) > 300:
        value = 'blunder'
    elif abs(diff2) >100 and diff1 < -100:
        value = 'worst move'
    elif abs(diff2) > 50:
        value = 'mistake'
    elif abs(diff2) >10 and diff1<-10:
        value = 'inaccuracy'
    elif diff1 < 0:
        value = 'not Good'
    
    # If no condition is met, assign a default value
    if value == '':
        value = 'neutral'  # Or any default value you prefer
    
    return value
