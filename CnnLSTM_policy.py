import torch
import gym

class CnnLSTM_policy:
    
    def __init__(
        self,
        observation_space: gym.spaces.Space,
        action_space: gym.spaces.Space,
    ):
        policy_net = torch.nn.Sequential(

