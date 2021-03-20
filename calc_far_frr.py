import frAPI
import numpy as np


def get_FAR(op_analysis): # False Acceptance Rate
  x = []
  y = []

  if op_analysis == 1:
    score_spoof = np.loadtxt('score_spoof.txt', dtype=str)
  else:
    score_spoof = frAPI.get_similarity_score('face_match_spoof.txt')

  for limiar in list(range(-100, 0)):
    tt_false_positives = 0

    for result in score_spoof:
      if float(result) > limiar:
         tt_false_positives += 1

    x.append(limiar)
    y.append(tt_false_positives / len(score_spoof))

  return x, y

def get_FRR(op_analysis): #False Rejection Rate -> FRR = FNR x (FN / (TP + FN))
  x = []
  y = []

  if op_analysis == 1:
    score_life = np.loadtxt('score_life.txt', dtype=str)
  else:
    score_life = frAPI.get_similarity_score('face_match_life.txt')

  tt_score = len(score_life)

  for limiar in list(range(0, 100)):
    tt_false_negative = 0

    for result in score_life:
      if float(result) < limiar:
        tt_false_negative += 1
    
    tt_positives = tt_score - tt_false_negative
    false_negative_rate = tt_false_negative / tt_score

    frr = false_negative_rate * tt_false_negative / (tt_positives + tt_false_negative)

    x.append(limiar)
    y.append(frr)

  return x, y



