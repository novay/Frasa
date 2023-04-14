import os
import pickle
from frasa.deteksi.gender.classify import NBClassifier

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path) + '/data/'
filename = dir_path + 'frasa-gender.pickle'

def model_gender():    
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
    
    except FileNotFoundError:
        model = NBClassifier()
        model.train_and_test()

        with open(filename, 'wb') as file:
            pickle.dump(model, file)
            
    return model

def probabilitas(nama):
    return model_gender().get_probability(nama)