US Supreme Court Voting Behavior TensorFlow Predictions
========================================================

Description
----------------------

* The application is written python and uses the TensorFlow api to train an algorithm that predicts the outcome of court cases.
* Data is collected from `The Supreme Court Datase <http://scdb.wustl.edu/about.php?s=3>`_
* The predicted outcomes of the cases proved to be correct about 80% of the time when tested against historical data.  
* Thus it appears that justices vote according to personal preferences towards political issue areas. 


How to Improve
-------------------

* Import this data into :ref:`The US Supreme Court Metadata Graph<metadatagraph>`.
* Train the algorithm to correlate outcome with as many other variables as possible.
  
Case Centric Training Features
-------------------------------

* issue
* issueArea
* naturalCourt
* petitioner
* petitionerState
* respondent
* jurisdiction
* adminAction
* adminActionState
* threeJudgeFdc
* caseOrigin
* caseOriginState
* respondentState
* caseSource
* caseSourceState
* lawType
* lawSupp

Justice Centric Training Features
----------------------------------

* justice
* issue
* issueArea
* lawType
* direction
* petitioner
* naturalCourt
* petitionerState
* respondent
* respondentState
* jurisdiction
* caseOrigin
* caseOriginState
* caseSource
* caseSourceState
* certReason
* lawSupp

Links
------
* `Github <https://github.com/justin-napolitano/Supreme-Court-Predictions>`_
* `The Supreme Court Datase <http://scdb.wustl.edu/about.php?s=3>`_
* `Sphinx Documentation <https://court-behavior.io/ml/ml-abstract.html>`_


Case Centric Code
------------------

.. code-block:: python

    #supremeCourtPrediction.py
  #a program that uses the segal and spaeth dataset to predict the outcomes of cases


  import pandas as pd

  import tensorflow as tf

  import math

  import seaborn as sns
  import matplotlib.pyplot as plt

  import shap
  shap.initjs()

  import os 
  import csv
  import datetime

  from tensorflow import feature_column
  from tensorflow.keras import layers
  from sklearn.model_selection import train_test_split

  from itertools import permutations 

  import matplotlib.pyplot as plt


  def get_environmental_variables():
      cwd = os.getcwd()
      log_dir = os.path.join(cwd,"logs/fit/") + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
      return cwd, log_dir

  def load_data(cwd):
      data_path = os.path.join(cwd,'data','citation.csv') 
      drop_path = os.path.join(cwd,'data','features','drop','drop.txt')
      #print(path)
      dataframe = pd.read_csv(data_path,encoding= 'unicode_escape')
      #print(dataframe.head())
      
      with open(drop_path) as fp:
          for cnt, line in enumerate(fp):
              #print("Dropping {} from dataframe".format(line))
              line = line.strip('\n')
              line = line.strip('\t')
              line = line.strip("'")

              dataframe.drop(line,axis=1,inplace=True)
      
      dataframe.fillna(0, inplace=True)
      print(dataframe)
      #dataframe.issue = dataframe.astype({'issue': 'str'})
      #dataframe[issue] = dataframe[issue].astype(str)
      #print(dataframe)
      #print(dataframe.head())
      return dataframe

  def split_datframe(dataframe):
      train, test = train_test_split(dataframe, test_size=0.2)
      train, val = train_test_split(train, test_size=0.2)
      print(len(train), 'train examples')
      print(len(val), 'validation examples')
      print(len(test), 'test examples')
      return train, test, val

      # A utility method to create a tf.data dataset from a Pandas Dataframe
  def df_to_dataset(dataframe, shuffle=True, batch_size=32):
      dataframe = dataframe.copy()
      labels = dataframe.pop('declarationUncon')
      ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
      if shuffle:
          ds = ds.shuffle(buffer_size=len(dataframe))
      ds = ds.batch(batch_size)
      print(ds)
      return ds

  def get_input_pipeline(train, test, val, batch_size=32, shuffle=True):
      train_ds = df_to_dataset(train, batch_size=batch_size)
      val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
      test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)
      return train_ds, val_ds, test_ds

  def get_feature_layer(cwd): #select the columns for analysis from dataset
      feature_path = os.path.join(cwd,'data','features','use','features.txt')
      dict_path = os.path.join(cwd,'data','features','use')
      feature_columns = []
      
      #embedded columns
      with open(feature_path) as fp:
          for cnt, line in enumerate(fp):
              #print("Adding {} to features".format(line))
              line = line.strip('\n')
              line = line.strip('\t')
              line = line.strip("'")

              print(cnt)   
              print(line)

              indicator = feature_column.numeric_column(line)
              
              #feature_column.categorical_column_with_vocabulary_file(
              #            key = line, vocabulary_file = os.path.join(dict_path,"{}.txt".format(line)), default_value=0)

              print(indicator)
              feature_columns.append(indicator)


              #feature_columns.append(feature_column.embedding_column(indicator, dimension=8))

      
      crossed_feature = feature_column.crossed_column(['issue', 'issueArea', 'naturalCourt'], hash_bucket_size=1000)
      crossed_feature = feature_column.indicator_column(crossed_feature)
      feature_columns.append(crossed_feature)


      crossed_feature = feature_column.crossed_column(['issue', 'naturalCourt'], hash_bucket_size=1000)
      crossed_feature = feature_column.indicator_column(crossed_feature)
      feature_columns.append(crossed_feature)

      crossed_feature = feature_column.crossed_column(['issueArea', 'naturalCourt'],hash_bucket_size=1000)
      crossed_feature = feature_column.indicator_column(crossed_feature)
      feature_columns.append(crossed_feature)
      
     # court_buckets = feature_column.bucketized_column(naturalCourt, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])

      #print(feature_columns)
      feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
      #for item in feature_columns:
      #    print(item)
      #    print("\n")

      return feature_layer
       
      #crossed cols


      #categorical_columns 
  def understand_input_pipeline(train_ds):
      for feature_batch, label_batch in train_ds.take(1):
          print('Every feature:', list(feature_batch.keys()))
          #print('A batch of ages:', feature_batch['age'])
          print('A batch of targets:', label_batch )

  def create_model(log_dir,feature_layer, train_ds, val_ds, epochs = 5):
      
      model = tf.keras.Sequential([
          feature_layer,
          layers.Dense(128, activation='relu'),
          layers.Dense(128, activation='relu'),
          layers.Dense(1)
      ])

      model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy', 'mae'])

      history = model.fit(train_ds,
              validation_data=val_ds,
              epochs=epochs)

      loss, accuracy,mae = model.evaluate(test_ds)
      print("Accuracy", accuracy)
      print(model.summary())
      return model,history

  def plot_history(history):

      hist = pd.DataFrame(history.history)
      print(hist)
      hist['epoch'] = history.epoch

      plt.figure()
      plt.xlabel('Epoch')
      plt.ylabel('Mean Absolute Error')
      plt.plot(hist['epoch'], hist['mae'],
              label='Train Error')
      plt.plot(hist['epoch'], hist['val_mae'],
              label = 'Val Error')
      plt.legend()
  def explain_kernal(df_train,model,train_ds):
      
      # KernelExplainer is a general approach that can work with any ML framework
      # Its inputs are the predictions and training data

      # Summarize the training set to accelerate analysis
      df_train_summary = shap.kmeans(df_train.values, 25)

      # Instantiate an explainer with the model predictions and training data summary
      explainer = shap.KernelExplainer(model.predict, df_train)

  # Extract Shapley values from the explainer
      #shap_values = explainer.shap_values(df_train.values)
  if __name__ == "__main__":
      cwd, log_dir = get_environmental_variables()
      #print(cwd)
      df = load_data(cwd)
      train,test,val = split_datframe(df)
      dataset = df_to_dataset(df)
      train_ds, val_ds, test_ds = get_input_pipeline(train,test,val,32)
      understand_input_pipeline(train_ds)
      feature_layer = get_feature_layer(cwd)
      model, model_history = create_model(log_dir,feature_layer, train_ds, val_ds)
      plot_history(model_history)
      #print(model.predict(train_ds))
      #print(model.predict)
      explain_kernal(df,model,train_ds)


Justice Centric Code
--------------------

.. code-block:: python

    #supremeCourtPrediction.py
  #a program that uses the segal and spaeth dataset to predict the outcomes of cases


  import pandas as pd

  import tensorflow as tf

  import math

  import seaborn as sns
  import matplotlib.pyplot as plt

  import shap
  shap.initjs()

  import os 
  import csv
  import datetime

  from tensorflow import feature_column
  from tensorflow.keras import layers
  from sklearn.model_selection import train_test_split

  from itertools import permutations
  from itertools import combinations_with_replacement

  import matplotlib.pyplot as plt


  def get_environmental_variables():
      cwd = os.getcwd()
      log_dir = os.path.join(cwd,"logs/fit/") + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
      return cwd, log_dir

  def load_data(cwd):
      data_path = os.path.join(cwd,'data','justice.csv') 
      drop_path = os.path.join(cwd,'data','features','drop','drop.txt')
      target_path = os.path.join(cwd,'data','features','targets.txt')
      print(data_path)
      dataframe = pd.read_csv(data_path,encoding= 'unicode_escape')
      #print(dataframe.head())
      
      with open(drop_path) as fp:
          for cnt, line in enumerate(fp):
              #print("Dropping {} from dataframe".format(line))
              line = line.strip('\n')
              line = line.strip('\t')
              line = line.strip("'")

              dataframe.drop(line,axis=1,inplace=True)
      
      dataframe.fillna(0, inplace=True)
      print(dataframe)
      #dataframe.issue = dataframe.astype({'issue': 'str'})
      #dataframe[issue] = dataframe[issue].astype(str)
      #print(dataframe)
      #print(dataframe.head())
      return dataframe

  def split_datframe(dataframe):
      train, test = train_test_split(dataframe, test_size=0.2)
      train, val = train_test_split(train, test_size=0.2)
      print(len(train), 'train examples')
      print(len(val), 'validation examples')
      print(len(test), 'test examples')
      return train, test, val

      # A utility method to create a tf.data dataset from a Pandas Dataframe
  def df_to_dataset(dataframe, shuffle=True, batch_size=32):
      dataframe = dataframe.copy()
      labels = dataframe.pop('vote')
      ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
      if shuffle:
          ds = ds.shuffle(buffer_size=len(dataframe))
      ds = ds.batch(batch_size)
      print(ds)
      return ds

  def get_input_pipeline(train, test, val, batch_size=32, shuffle=True):
      train_ds = df_to_dataset(train, batch_size=batch_size)
      val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
      test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)
      return train_ds, val_ds, test_ds

  def get_feature_layer(cwd): #select the columns for analysis from dataset
      feature_path = os.path.join(cwd,'data','features','use','features.txt')
      dict_path = os.path.join(cwd,'data','features','use')
      feature_columns = []
      feature_list = []
      #embedded columns
      with open(feature_path) as fp:
          for cnt, line in enumerate(fp):
              #print("Adding {} to features".format(line))
              line = line.strip('\n')
              line = line.strip('\t')
              line = line.strip("'")

              print(cnt)   
              print(line)
              feature_list.append(line)

              indicator = feature_column.numeric_column(line)
              
              #feature_column.categorical_column_with_vocabulary_file(
              #            key = line, vocabulary_file = os.path.join(dict_path,"{}.txt".format(line)), default_value=0)

              print(indicator)
              feature_columns.append(indicator)


              #feature_columns.append(feature_column.embedding_column(indicator, dimension=8))

      feature_comb = combinations_with_replacement(feature_list, 2) 
      lst = list(feature_comb)
      limit = len(feature_list)
      print(limit)
      j = 0
      k = limit - 1
      lookup = []
      for i in range(limit):
          lookup.append(i+j)
          j = j + k
          k = k - 1 


      for i in range(len(lst)):
          if i in lookup:
              continue
          else:
              one, two = lst[i]
              crossed_feature = feature_column.crossed_column([one, two], hash_bucket_size=1000)
              crossed_feature = feature_column.indicator_column(crossed_feature)
              feature_columns.append(crossed_feature)

      """
      crossed_feature = feature_column.crossed_column(['issue', 'naturalCourt'], hash_bucket_size=1000)
      crossed_feature = feature_column.indicator_column(crossed_feature)
      feature_columns.append(crossed_feature)

      crossed_feature = feature_column.crossed_column(['issueArea', 'naturalCourt'],hash_bucket_size=1000)
      crossed_feature = feature_column.indicator_column(crossed_feature)
      feature_columns.append(crossed_feature)
      """
     # court_buckets = feature_column.bucketized_column(naturalCourt, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])

      #print(feature_columns)
      feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
      #for item in feature_columns:
      #    print(item)
      #    print("\n")

      return feature_layer
       
      #crossed cols


      #categorical_columns 
  def understand_input_pipeline(train_ds):
      for feature_batch, label_batch in train_ds.take(1):
          print('Every feature:', list(feature_batch.keys()))
          #print('A batch of ages:', feature_batch['age'])
          print('A batch of targets:', label_batch )

  def create_model(log_dir,feature_layer, train_ds, val_ds, epochs = 8):
      
      model = tf.keras.Sequential([
          feature_layer,
          layers.Dense(128, activation='relu'),
          layers.Dense(128, activation='relu'),
          layers.Dense(1)
      ])

      model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy', 'mae'])

      history = model.fit(train_ds,
              validation_data=val_ds,
              epochs=epochs)

      loss, accuracy,mae = model.evaluate(test_ds)
      print("Accuracy", accuracy)
      print(model.summary())
      return model,history

  def plot_history(history):

      hist = pd.DataFrame(history.history)
      print(hist)
      hist['epoch'] = history.epoch

      plt.figure()
      plt.xlabel('Epoch')
      plt.ylabel('Mean Absolute Error')
      plt.plot(hist['epoch'], hist['mae'],
              label='Train Error')
      plt.plot(hist['epoch'], hist['val_mae'],
              label = 'Val Error')
      plt.legend()

  def explain_kernal(model,train_ds):
      model.predict(train_ds)
      # KernelExplainer is a general approach that can work with any ML framework
      # Its inputs are the predictions and training data

      # Summarize the training set to accelerate analysis
      df_train_summary = shap.kmeans(train_ds.values, 25)
      #print(df_train_summary)
      #model.predict(df_train_summary)
      # Instantiate an explainer with the model predictions and training data summary
      explainer = shap.KernelExplainer(model.predict, train_ds)

  # Extract Shapley values from the explainer
      #shap_values = explainer.shap_values(df_train.values)
  if __name__ == "__main__":
      cwd, log_dir = get_environmental_variables()
      print(cwd)
      df = load_data(cwd)
      train,test,val = split_datframe(df)
      dataset = df_to_dataset(df)
      train_ds, val_ds, test_ds = get_input_pipeline(train,test,val,32)
      understand_input_pipeline(train_ds)
      feature_layer = get_feature_layer(cwd)
      model, model_history = create_model(log_dir,feature_layer, train_ds, val_ds)
      #plot_history(model_history)
      #print(model.predict(train_ds))
      #print(model.predict)
      #explain_kernal(model,train_ds)
