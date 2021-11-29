# This program showcases the concept of machine learning
# Date: 29NOV21
# CSC221 M7Pro – kNearest
# Name: Taylor J. Brown

"""
    TO RUN THIS PROGRAM
    ______________________________________________________________________
    - Launch Anaconda Prompt
    - Navigate to the file location where you extracted this program
    - Use "cd *file path*"
    - Copy and paste this command "ipython M7Pro_kNearest_TaylorBrown.py"
    - Press enter and the program will run
"""
"""
    This program follows the book from pages 599-615
    ______________________________________________________________________
    ADDED CONTENT
    -------------
    - Prints the data array on the index 13 image
    - Prints the first 24 images in digits.images
    - Prints the predicted and expected values 
    - Prints the confusion matrix
    - Prints the classification report
    - Opens new window and plots a heatmap of the confusion matrix 
"""

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.DESCR)
digits.target[::100]
digits.data.shape
digits.target.shape
digits.images[13]
digits.data[13]
print("Data array of image in index position 13:\n",digits.images[13],"\n") # - Prints the data array on the index 13 image
digits.images[22]
digits.target[22]
import matplotlib.pyplot as plt
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
index = 0
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
    index += 1
    print("Image:", index, "\n", image, "\n") # - Prints the first 24 images in digits.images
  
plt.tight_layout()
axes = plt.subplot()
image = plt.imshow(digits.images[22], cmap=plt.cm.gray_r)
xticks = axes.set_xticks([])
xticks = axes.set_yticks([])
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11)
X_train.shape
X_test.shape
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=X_train, y=y_train)
predicted = knn.predict(X=X_test)
expected = y_test
print("Predicted: ",predicted[:20],"\n") # - Prints the predicted and expected values 
print("Expected:  ",expected[:20],"\n")  # - Prints the predicted and expected values 
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
wrong
print(f'Accuracy: {(len(expected) - len(wrong)) / len(expected):.2%}',"\n")
wrong = []
for p, e in zip(predicted, expected):
    if p != e:
        wrong.append((p, e))
        
wrong
print(f'Score:    {knn.score(X_test, y_test):.2%}',"\n")
from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print("Confusion matrix:\n", confusion, "\n") # - Prints the confusion matrix
from sklearn.metrics import classification_report
names = [str(digit) for digit in digits.target_names]
print("Report:\n",classification_report(expected, predicted, target_names=names)) # - Prints the classification report
import pandas as pd
confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
import seaborn as sns
axes = sns.heatmap(confusion_df, annot=True, cmap='nipy_spectral_r')

import matplotlib.pyplot as plt
plt.show() # - Opens new window and plots a heatmap of the confusion matrix