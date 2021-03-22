import matplotlib.pyplot as plt
import calc_far_frr


def normalize(array):
  normalized_array = []

  for index in range(len(array)):
    result = (array[index] - min(array)) / (max(array) - min(array))
    normalized_array.append(result)

  return normalized_array

def generate(op_graphic, op_analysis):
  if op_graphic == 1:
    x1, y1 = calc_far_frr.get_FAR(op_analysis)
    plt.plot(x1, y1)
    plt.title('False Acceptance Rate')
    plt.xlabel('limiar (%)')
    plt.ylabel('taxa de falsa de aceitação (%)')
  elif op_graphic == 2:
    x2, y2 = calc_far_frr.get_FRR(op_analysis)
    plt.plot(x2, y2)
    plt.title('False Rejection Rate')
    plt.xlabel('limiar (%)')
    plt.ylabel('taxa de falsa de rejeição (%)')
  else:
    x1, y1 = calc_far_frr.get_FRR(op_analysis)
    x2, y2 = calc_far_frr.get_FAR(op_analysis)
    plt.plot(normalize(x1), normalize(y1))
    plt.plot(normalize(x2), normalize(y2))
    plt.grid(True)
    
  plt.show()
