gradePROJA = 7.5
gradePROG = 7.5
gradeMOD = 7.5

average = sum([gradePROJA, gradePROG, gradeMOD]) / 3
reward = (average * 30) * 3
overview = 'My grades (average of {}) accumulates a reward of {}'.format(average, reward)
print(overview)
