from probCalculation import constants as const


#takes in an array of strings and will return the relative score
def score_calc(data):
    score1 = 0
    score2 = 0
    for word in data:
        if word in const.frequency_weights:
            score1 = score1 + const.frequency_weights[word]
        if word in const.keyterm_weights:
            score2 = score2 + const.keyterm_weights[word]
    score = score1 * const.c1_weight + score2 * const.c2_weight
    return score




