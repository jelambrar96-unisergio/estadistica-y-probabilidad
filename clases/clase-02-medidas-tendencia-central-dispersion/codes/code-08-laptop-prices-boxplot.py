import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("laptopPrice.csv")

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['brand'], y=df['Price'], color="skyblue")
plt.title("Laptop Brand Price Distribution")
plt.xlabel("Laptop Brand")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()

