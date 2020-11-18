from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer



class my_model():
    def fit(self, X, y):
        # do not exceed 29 mins
        self.preprocessor = TfidfVectorizer(stop_words='english', norm='l2', use_idf=False, smooth_idf=False)
        XX = self.preprocessor.fit_transform(X["description"])
        self.clf = SGDClassifier(class_weight="balanced")
        self.clf.fit(XX, y)
        return

    def predict(self, X):
        # remember to apply the same preprocessing in fit() on test data before making predictions
        XX = self.preprocessor.transform(X["description"])
        predictions = self.clf.predict(XX)
        return predictions









