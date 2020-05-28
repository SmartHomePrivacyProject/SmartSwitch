import sys
sys.path.append('/home/haipeng/Documents/dl_attack')
sys.path.append('/home/carl')
from keras.models import Sequential, load_model
import numpy as np
import selfUtils as su
import csv
import pandas as pd


def permutation(X, y_test, step,dim,model_path):

    model = load_model(model_path)
    col_num = X.shape[1]
   # iterations = int(400/step)
    iterations = int(dim)-step
    results=[]
    for i in range(iterations):
       # feature_set=[j for j in range(i*step, (i+1)*step)]
        feature_set=[j for j in range(i, i+step)]
        X_p = X.copy()
        #col = X.iloc[:,feature_set].sample(frac=1)
        col = X.iloc[:,feature_set]
        col = col.sample(frac=1,axis=1)
        # X_p[str(i+1)] = list(col)
        X_p.iloc[:,feature_set] = (col).values
        X_test = np.expand_dims(X_p, axis=2)
        score, acc = model.evaluate(X_test, y_test, batch_size=100)
        print(f"Model Performance: {score, acc} at feature {feature_set}")
        r = [feature_set, acc]
        results.append(r)
    #with open('/home/liuhao/lhp/Documents/permuatation_' + str(step) + '.csv','w') as w:
     #   writer = csv.writer(w)
      #  writer.writerow()
    df = pd.DataFrame(results)
    df.to_csv('/home/haipeng/Documents/permutation_results/KB/'+path+'_permutation_'+str(step)+'.csv',index=False)

def main(step,dim):
    selected_col = [i for i in range(1, 401)]
    data_path = sys.argv[3]
    model_path = sys.argv[4]
    X_train, y_train, X_test, y_test, num_classes = su.load_data('/home/haipeng/Documents/dataset/Video_dataset/KB/video_bin_'+path+'_kb.csv', dim)
    permutation(X_test, y_test, step, dim, model_path)
   # X_train, y_train, X_test, y_test, num_classes = su.shuffle_and_load('/home/liuhao/lhp/Documents/dataset/Alexa_dataset/generic_class.csv', selected_col)
   # model_path = '/home/liuhao/lhp/Documents/models/cnn.h5'
   # model = load_model(model_path)
   # X_test = np.expand_dims(X_test, axis=2)
   # score, acc = model.evaluate(X_test, y_test, batch_size=100)
   # print(f"Model Performance: {score, acc} at feature {feature_set}")


if __name__ == '__main__': 
    step = sys.argv[1]
    dim =int(sys.argv[2])
    main(int(step),dim)

