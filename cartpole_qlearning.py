import gym
import time
import numpy as np

# create CartPole environment
env = gym.make('CartPole-v1')
np.random.seed(0)
env.seed(0)

# Define a Q-Learning Policy
class Policy_QLearning():
    def __init__(self, ):
        self.buckets = (3, 3, 6, 6)
        self.alpha = 0.5
        self.epsilon = 1.0
        self.gamma = 0.99
        self.current_state = None
        self.Q = np.zeros(self.buckets + (2,))

    def discretize(self, obs):
        lower_bounds = [-1, -0.5, -0.4, -1.0]
        upper_bounds = [1, 0.5, 0.4, 1.0]
        ratios = [(obs[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(obs))]
        new_obs = [int(round((self.buckets[i] - 1) * ratios[i])) for i in range(len(obs))]
        new_obs = [min(self.buckets[i] - 1, max(0, new_obs[i])) for i in range(len(obs))]
        return tuple(new_obs)

    def act(self, state, reward):
        new_state = self.discretize(state)
        if self.current_state is not None:
            self.update_q(self.current_state, self.action, reward, new_state, self.alpha)
        self.current_state = new_state
        # TODO: implement the action policy for Q-Learning
        self.action = 0
        return self.action

    def update_q(self, state_old, action, reward, state_new, alpha):
        # TODO: implement the update rule for Q-Learning
        pass

    def reset(self, state):
        print('Epsilon: %4.2f Q: [%4.2f - %4.2f - %4.2f]' % (self.epsilon, np.min(self.Q), np.mean(self.Q), np.max(self.Q)))
        self.epsilon = max(self.epsilon - 0.01, 0)
        self.current_state = None

policy = Policy_QLearning()
for episode in range(300):
    state = env.reset()
    score = 0
    start_time = time.time()
    max_timesteps = 500
    t = 0
    reward = 0
    policy.reset(state)
    while True:
        env.render()
        action = policy.act(state, reward)
        # execute one step of the simulation and obtain the next state and reward
        state, reward, done, info = env.step(action)
        #print("Step %3d: state %5.2f action %d reward %d" % (t, state[2], action, reward))
        time.sleep(0.05)
        t += 1
        score += reward
        if done or t >= max_timesteps:
            end_time = time.time()
            print("Episode %3d: cart pole survived for %4.2fs (score=%d)" % (episode, end_time - start_time, score))
            break
env.close()
