sigmoid_values = 1 / (1 + np.exp(-z_values))

plt.figure(figsize=(8, 4))
plt.plot(z_values, sigmoid_values)
plt.axhline(0.5, linestyle="--")
plt.scatter([z], [prediction], s=100)
plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("sigmoid(z)")
plt.text(z, prediction, f"  ({z:.2f}, {prediction:.2f})")
plt.show()

# ------------------------------------------------------------
# STEP 9 : Final Decision
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("STEP 9 : FINAL SENTIMENT DECISION")
print("=" * 70)

print("Decision rule:")
print("Prediction >= 0.5  -> Positive")
print("Prediction <  0.5  -> Negative")

if prediction >= 0.5:
    sentiment = "Positive"
    sentiment_value = 1
else:
    sentiment = "Negative"
    sentiment_value = 0

print("\nPrediction value :", prediction)
print("Final Sentiment  :", sentiment)
print("Sentiment Value  :", sentiment_value)

# ------------------------------------------------------------
# STEP 10 : Complete Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("COMPLETE FLOW SUMMARY")
print("=" * 70)

print(f"""
Input Sentence:
{sentence}

Token Sequence:
{tokens}

Embedding Matrix:
{X}

Final Hidden State:
{h_final}

Dense Score:
z = {z:.4f}

Sigmoid Output:
prediction = {prediction:.4f}

Final Output:
{sentiment} Sentiment
""")

plt.figure(figsize=(10, 7))
plt.title("Complete RNN Sentiment Flow")

summary = f"""
Input:
food was not good

Tokenization:
{tokens}

Embedding:
Each token is replaced by its vector

RNN:
h_t = tanh(Wx.x_t + Wh.h_previous + b)

Final Hidden State:
[{h_final[0]:.2f}, {h_final[1]:.2f}, {h_final[2]:.2f}]

Dense:
z = Wy.h_final + by
z = {z:.2f}

Sigmoid:
prediction = {prediction:.2f}

Decision:
{sentiment} Sentiment
"""

plt.text(0.05, 0.5, summary, fontsize=12, va="center")
plt.axis("off")
plt.show()


