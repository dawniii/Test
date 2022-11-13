import numpy as np
from hmmlearn import hmm

# For this example, we will model the stages of a conversation,
# where each sentence is "generated" with an underlying topic, "cat" or "dog"
# 2个隐含状态
states = ["cat", "dog"]
# 生成一个字典{0: 'cat', 1: 'dog'}
id2topic = dict(zip(range(len(states)), states))
# we are more likely to talk about cats first
# 初始状态概率分布
start_probs = np.array([0.6, 0.4])

# For each topic, the probability of saying certain words can be modeled by
# a distribution over vocabulary associated with the categories
# 观测变量集合
vocabulary = ["tail", "fetch", "mouse", "food"]
# if the topic is "cat", we are more likely to talk about "mouse"
# if the topic is "dog", we are more likely to talk about "fetch"
# 观测序列的概率分布
#     tail  fetch   mouse   food
# cat
# dog
emission_probs = np.array([[0.25, 0.1, 0.4, 0.25],
                           [0.2, 0.5, 0.1, 0.2]])

# Also assume it's more likely to stay in a state than transition to the other
trans_mat = np.array([[0.8, 0.2], [0.2, 0.8]])


# Pretend that every sentence we speak only has a total of 5 words,
# i.e. we independently utter a word from the vocabulary 5 times per sentence
# we observe the following bag of words (BoW) for 8 sentences:
# 观测序列
observations = [["tail", "mouse", "mouse", "food", "mouse"],
        ["food", "mouse", "mouse", "food", "mouse"],
        ["tail", "mouse", "mouse", "tail", "mouse"],
        ["food", "mouse", "food", "food", "tail"],
        ["tail", "fetch", "mouse", "food", "tail"],
        ["tail", "fetch", "fetch", "food", "fetch"],
        ["fetch", "fetch", "fetch", "food", "tail"],
        ["food", "mouse", "food", "food", "tail"],
        ["tail", "mouse", "mouse", "tail", "mouse"],
        ["fetch", "fetch", "fetch", "fetch", "fetch"]]

# 将单词转换为数字
# {'tail': 0, 'fetch': 1, 'mouse': 2, 'food': 3}
vocab2id = dict(zip(vocabulary, range(len(vocabulary))))
def sentence2counts(sentence):
    ans = []
    for word, idx in vocab2id.items():
        count = sentence.count(word)
        ans.append(count)
    return ans

X = []
# 遍历每一个观测序列
# row统计的是每个观测序列中["tail", "fetch", "mouse", "food"]的个数。
for sentence in observations:
    row = sentence2counts(sentence)
    X.append(row)
# X是长为10的列表，每一个元素是一个长为4的列表。
data = np.array(X, dtype=int)

# pretend this is repeated, so we have more data to learn from:
lengths = [len(X)]*5
# sequences={ndarray:(50,4)}是一个可见序列。
sequences = np.tile(data, (5,1))


# 构建一个模型
model = hmm.MultinomialHMM(n_components=len(states),
        n_trials=len(observations[0]),
        n_iter=50,
        init_params='')
model.n_features = len(vocabulary)
model.startprob_ = start_probs
model.transmat_ = trans_mat
model.emissionprob_ = emission_probs
model.fit(sequences, lengths)
# 3.Decoding
# received：ndarray:(50,) 返回的是sequence序列的状态标签，即cat or dog
logprob, received = model.decode(sequences)

print("Topics discussed:")
print([id2topic[x] for x in received])

print("Learned emission probs:")
print(model.emissionprob_)

print("Learned transition matrix:")
print(model.transmat_)

# Try to reset and refit:
new_model = hmm.MultinomialHMM(n_components=len(states),
        n_trials=len(observations[0]),
        n_iter=50, init_params='ste')

new_model.fit(sequences, lengths)
logprob, received = new_model.decode(sequences)

print("\nNew Model")
print("Topics discussed:")
print([id2topic[x] for x in received])

print("Learned emission probs:")
print(new_model.emissionprob_)

print("Learned transition matrix:")
print(new_model.transmat_)
