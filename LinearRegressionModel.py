https://colab.research.google.com/drive/1Y8QTu553UgQ4P8pDphysTrgZt99sMe3m?usp=sharing


from sklearn.metrics import roc_auc_score
predictions = linear.predict(X_test)
roc_auc_scores = []
for i in range(len(target_columns)):
    roc_auc_scores.append(roc_auc_score(y_test.iloc[:, i], predictions[:, i]))
avg_roc_auc = sum(roc_auc_scores) / len(roc_auc_scores)

print("Average ROC AUC:", avg_roc_auc)
