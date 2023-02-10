#augmentaiton for test set
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model

# Create an instance of the ImageDataGenerator class
data_gen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.11,
    height_shift_range=0.11,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)
data_gen.fit(X_test)
image_batch, mask_batch = next(data_gen.flow(X_test, y_test, batch_size=32, seed=123))

Roc curve

from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
prediction = model.predict(image_batch)
prediction = prediction.reshape(-1)

mask_batch = mask_batch.astype(int)
mask_batch = mask_batch.reshape(-1)
# Set the range of thresholds
thresholds = np.arange(0, 1.01, 0.01)

# Initialize lists to store the false positive rate (FPR) and true positive rate (TPR) at each threshold
roc_point= []

# Iterate over the thresholds
for threshold in thresholds:
    # Compute the FPR and TPR at the current threshold
    fpr, tpr, _= roc_curve(mask_batch, prediction > threshold)
    
    # Store the FPR and TPR
    roc_point.append([tpr[1],fpr[1]])
# plot the ROC 
import pandas as pd
# Plot the ROC curves
pivot = pd.DataFrame (roc_point, columns = ["x", "y"])
pivot["threshold"] = thresholds
plt.plot (pivot.y, pivot.x)
# Add labels and a title
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.title("ROC curves")

#calculating the AUC (Area under curve)
from sklearn.metrics import auc

# Compute the area under the curve (AUC)
roc_points_sorted = sorted(roc_point2, key=lambda x: x[1])
auc_value = auc([x[1] for x in roc_points_sorted], [x[0] for x in roc_points_sorted])
