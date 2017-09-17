import ocr_try
from probCalculation import calc


# basic wrapper call that will take in the src of the image, scan, and calculate and return the relative score
def return_score(image):
    score = calc.score_calc((ocr_try.process_print(image)))
    return score