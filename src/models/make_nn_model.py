import paths
import os.path
import sklearn.neural_network
import sklearn.metrics
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_test_train_data


def make_nn_model(processed_file_path, split):
    X_train, X_test, y_train, y_test = src.models.get_test_train_data.zscaled_data(processed_file_path, split)

    nn_classifier = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(8, 8, 8, 8, 8, 8, 8, 8), max_iter=600)
    nn_classifier.fit(X_train, y_train)

    result = nn_classifier.predict(X_test)
    print("Classification report for classifier %s:\n\n%s\n"
          % (nn_classifier, sklearn.metrics.classification_report(y_test, result)))
    return result, y_test


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.PROCESSED_DATA_DIR, "qws2_processed.csv")
    make_nn_model(processed_file_path, split=0.4)
