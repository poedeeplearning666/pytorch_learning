import torch
from torch import nn

# hyper parameters
in_dim = 1
n_hidden_1 = 1
n_hidden_2 = 1
out_dim = 1
"""
module 和 childern区别
module 是深度优先遍历打印出网络结构,而 children是只打印出网络的子结构,不再管子结构的下一结构
"""
# class Net(nn.Module):
#     def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
#         super().__init__()
#
#         self.layer = nn.Sequential(
#             nn.Linear(in_dim, n_hidden_1),
#             nn.ReLU(True)
#         )
#         self.layer2 = nn.Sequential(
#             nn.Linear(n_hidden_1, n_hidden_2),
#             nn.ReLU(True),
#         )
#         self.layer3 = nn.Linear(n_hidden_2, out_dim)
#
#         print("children")
#         for i, module in enumerate(self.children()):
#             print(i, module)
#
#         print("modules")
#         for i, module in enumerate(self.modules()):
#             print(i, module)
#
#     def forward(self, x):
#         x = self.layer1(x)
#         x = self.layer2(x)
#         x = self.layer3(x)
#         return x
#
#
# model = Net(in_dim, n_hidden_1, n_hidden_2, out_dim)

"""
embedding vector
"""
# import numpy as np
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch.autograd import Variable
#
# word_to_ix = {'hello': 1, 'world': 2}
# embeds = nn.Embedding(7, 5, padding_idx=0)
# hello_idx = torch.LongTensor([word_to_ix['hello']])
# hello_idx = hello_idx
# hello_embed = embeds(hello_idx)
# print(hello_embed)
#
# inputs = torch.randint(1, 7, (3, 3))
# print(embeds(inputs).shape)
# print(embeds(inputs))

"""
torch.mm  矩阵乘法
torch.bmm 三维矩阵乘法，第一维是batchsize
torch.matmul 广播乘法
torch.mul 对位相乘
"""
import torch

a = torch.tensor([[1, 2], [2, 3]])
b = torch.tensor([[2, 3], [2, 3]])
c = torch.mul(a, b)
print(c)

d = torch.mm(a, b)
print(d)

e = torch.matmul(a, b)
print(e)
