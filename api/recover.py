if diff2 > 250:
        value = 'You Missed'
    elif abs(diff2)<4:
        value = 'best move'
    elif abs(diff2) == 0 and diff1 > 300:
        value = 'brilliant'
    elif diff1 > 150:
        value = 'great move'
    elif diff1 > 50:
        value = 'nice move'
    elif diff1 > 20:
        value = 'best move'
    elif diff1 >= 0:
        value = 'good'
    elif diff1 < -300:
        value = 'blunder'
    elif diff1 < -150:
        value = 'worst move'
    elif diff1 < -50:
        value = 'mistake'
    elif diff1 < -5:
        value = 'inaccuracy'
    elif diff1 < 0:
        value = 'not Good'