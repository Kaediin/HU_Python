
beginTafel = 1
eindTafel = 10

# forloop i die 11x (10+1) draait maar op index 1 begint (dus in theorie 10 keer)
for i in range(beginTafel, eindTafel+1):

    # forloop die hetzelfde doet maar 10x een forloop dit voor elke loop in i. Zo krijg je dus per i-iteration 10x een
    # j iteration
    for j in range(beginTafel, eindTafel+1):
        print('{} x {} = {}'.format(i, j, (i*j)))