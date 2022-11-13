import numpy as np
"""
此代码只实现了概率计算问题和解码问题(viterbi算法)。
无学习问题。
"""
class HMM:
        def __init__(self, Ann, Bnm, Pi, O):
                self.A = np.array(Ann)
                self.B = np.array(Bnm)
                self.Pi = np.array(Pi)
                self.O = np.array(O)
                self.N = self.A.shape[0]
                self.M = self.B.shape[1]

        def viterbi(self):
                # input: O, lambda
                # output: I
                T = len(self.O)
                I = np.zeros(T, np.int) # 隐状态链
                delta = np.zeros((self.N, T)) # 概率计算矩阵
                psi = np.zeros((self.N, T), np.int) # 路径矩阵
                for i in range(self.N): # 计算delta[:, 0]
                        delta[i, 0] = self.Pi[i] * self.B[i, self.O[0]]
                        psi[i, 0] = 0
                for t in range(1, T): # 计算delta[:, 1:]
                        for i in range(self.N): # 对应t列
                                delta[i, t] = np.array( [delta[j,t-1] * self.A[j,i] for j in range(self.N)] ).max() * self.B[i,self.O[t]]
                                psi[i, t] = np.array([delta[j, t-1] * self.A[j, i] for j in range(self.N)]).argmax()
                I[T-1] = delta[:, T-1].argmax()
                print(delta); print(psi)
                for t in range(T-2, -1, -1):
                        I[t] = psi[I[t+1], t+1]
                return I

        def forward(self):
                # input: O, lambda
                # output: p
                T = len(self.O)
                alpha = np.zeros((self.N, T))
                for i in range(self.N):
                        alpha[i, 0] = self.Pi[i] * self.B[i, self.O[0]]
                for t in range(T-1):
                        for i in range(self.N): # 对应t+1列
                                s = 0.0
                                for j in range(self.N): # 对应t列
                                        s += alpha[j, t] * self.A[j, i]
                                alpha[i, t+1] = s * self.B[i, self.O[t+1]]
                p = alpha[:, -1].sum()
                return alpha, p

        def backward(self):
                T = len(self.O)
                beta = np.zeros((self.N, T))
                for i in range(self.N):
                        beta[i, T-1] = 1.0
                for t in range(T-2, -1, -1):
                        for i in range(self.N): # 对应t列
                                s = 0.0
                                for j in range(self.N): # 对应t+1列
                                        s += self.A[i, j] * self.B[j, self.O[t+1]] * beta[j, t+1]
                                beta[i, t] = s
                p = 0.0
                for i in range(self.N):
                        p += self.Pi[i] * self.B[i, self.O[0]] * beta[i, 0]
                return beta, p

def main():
        # 隐含状态转移概率分布(2个状态)
        transition_probability = [[0.7, 0.3], [0.4, 0.6]]
        # 观测序列概率分布(3个序列值)
        emission_probability = [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]]
        # 初始状态概率分布
        pi = [0.3, 0.7]
        # 观测序列
        obs_seq = [1, 0, 0, 0, 1]
        hmm = HMM(transition_probability, emission_probability, pi, obs_seq)
        I = hmm.viterbi(); print(I)
        alpha, p1 = hmm.forward(); print(alpha, p1)
        beta, p2 = hmm.backward(); print(beta, p2)

if __name__ == '__main__':
        main()