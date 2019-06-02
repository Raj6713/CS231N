# This class will implement the nearest neighbor on the given data set
import numpy as np
import pandas as pd


class NearestNeighbour(object):
    def __init__(self, train_data, test_data):
        print("Init Enter")
        self.train_data = train_data
        self.test_data = test_data
        self.train_values = None
        self.train_labels = None
        self.test_values = None
        self.test_labels = None
        print("Init Exit.")

    def train(self):
        self.train_values = self.train_data[b'data']
        self.train_labels = self.train_data[b'labels']
        self.test_values = self.test_data[b'data']
        self.test_labels = self.test_data[b'labels']

    def predictor(self):
        predicted_values = []
        for i in range(len(self.test_values[:100])):
            distance = np.Inf
            index_values = None
            for j in range(len(self.train_values)):
                distance_1 = np.sum(np.abs(self.test_values[i]-self.train_values[j]))
                print(distance_1)
                if distance_1 <= distance:
                    distance = distance_1
                    index_values = j
            predicted_values.append((self.train_labels[index_values], self.test_labels[i]))
        return predicted_values


