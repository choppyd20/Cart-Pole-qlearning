import gym
import math
import time
from pyglet.window import key

# create CartPole environment
env = gym.make('CartPole-v1')
env.env.theta_threshold_radians = math.pi / 2
state = env.reset()
env.render()
action = 0
def key_press(k, mod):
    global action
    if k==key.LEFT:  action = 0  # Push cart to the left
    if k==key.RIGHT: action = 1  # Push cart to the right
env.viewer.window.on_key_press = key_press

while True:
    env.reset()
    t = 0
    score = 0
    start_time = time.time()
    max_timesteps = 200
    while True:
        env.render()
        # execute one step of the simulation and obtain the next state and reward
        state, reward, done, info = env.step(action)
        print("Step %3d: state %5.2f action %d reward %d" % (t, state[2], action, reward))
        time.sleep(0.1)
        t += 1
        score += reward
        if done or t >= max_timesteps:
            end_time = time.time()
            print("Game Over: cart pole survived for %4.2fs (score=%d)" % (end_time - start_time, score))
            break
env.close()
