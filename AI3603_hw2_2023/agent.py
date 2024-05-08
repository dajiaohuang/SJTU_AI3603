# -*- coding:utf-8 -*-
import math, os, time, sys
import numpy as np
import gym
##### START CODING HERE #####
# This code block is optional. You can import other libraries or define your utility functions if necessary.

##### END CODING HERE #####

# ------------------------------------------------------------------------------------------- #

class SarsaAgent(object):
    ##### START CODING HERE #####
    def __init__(self, all_actions):
        """initialize the agent. Maybe more function inputs are needed."""
        self.all_actions = all_actions
        self.epsilon = 1.0
        self.gamma = 0.95
        self.lr = 0.1
        self.q = np.zeros([12,4,4])

    def choose_action(self, observation):
        x = observation % 12
        y = int((observation - x) / 12)
        """choose action with epsilon-greedy algorithm."""
        if np.random.uniform() < self.epsilon: 
            action = np.random.choice(self.all_actions)
        else:
            action = np.argmax(self.q[x][y])
            #print(action)
        return action
    
    def learn(self,r,observation,action,observation_n,action_n):
        """learn from experience"""
        x = observation % 12
        y = int((observation - x) / 12)
        x_n = observation_n % 12
        y_n = int((observation_n - x_n) / 12)
        self.q[x][y][action] += self.lr * (r + self.gamma * self.q[x_n][y_n][action_n] - self.q[x][y][action])
        return True
    
    def epsilon_decay(self, episode):
        if episode < 200:
            self.epsilon = 1 - 0.0015 * episode
        elif episode < 400:
            self.epsilon = 0.5 - 0.0005 * episode
        else:
            self.epsilon = 0.1 - 0.0001 * episode
    ##### END CODING HERE #####


class QLearningAgent(object):
    ##### START CODING HERE #####
    def __init__(self, all_actions):
        """initialize the agent. Maybe more function inputs are needed."""
        self.all_actions = all_actions
        self.epsilon = 1.0
        self.gamma = 0.95
        self.lr = 0.1
        self.q = np.zeros([12,4,4])

    def choose_action(self, observation):
        x = observation % 12
        y = int((observation - x) / 12)
        """choose action with epsilon-greedy algorithm."""
        if np.random.random() < self.epsilon: 
            action = np.random.choice(self.all_actions)
        else:
            action =  np.argmax(self.q[x][y])
    
        return action
    
    def learn(self,r,observation,action,observation_n):
        """learn from experience"""
        x = observation % 12
        y = int((observation - x) / 12)
        x_n = observation_n % 12
        y_n = int((observation_n - x_n) / 12)
        self.q[x][y][action] += self.lr * (r + self.gamma * np.max(self.q[x_n][y_n]) - self.q[x][y][action])
        return False

    def epsilon_decay(self, episode):
        if episode < 200:
            self.epsilon = 1 - 0.0015 * episode
        elif episode < 400:
            self.epsilon = 0.5 - 0.0005 * episode
        else:
            self.epsilon = 0.1 - 0.0001 * episode
    ##### END CODING HERE #####
