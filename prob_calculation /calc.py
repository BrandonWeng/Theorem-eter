import constants as const

print("hi")
data = ['set','subspace','asdasf','vector','rank']

def score_calc(data):
    score = 0
    for word in data:
        if word in const.frequency_weights:
            score = score + const.frequency_weights[word]
    print(score)
    return score


# with open ("defBody6text", 'rb') as loadText:
#     text = pickle.load(loadText);
#     print("test:")
#     print(text)

score_calc(data)




