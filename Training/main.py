import pandas as pd
import numpy as np
from helper_functions import unpickle
from nearest_neighbor import NearestNeighbour
data_location = './data/'
if __name__ == '__main__':
    train_1 = unpickle(data_location+'data_batch_1')
    print(train_1[b'data'][0], train_1[b'labels'][0])
    predict_values = unpickle(data_location+'test_batch')
    print(predict_values[b'data'][0], predict_values[b'labels'][0])
    nn = NearestNeighbour(train_1, predict_values)
    nn.train()
    values = nn.predictor()
    accuracy = 0
    for val in values:
        if val[0] == val[1]:
            accuracy = accuracy + 1
    print(accuracy/len(values))

