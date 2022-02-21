import gym
import math
import time

# create CartPole environment
env = gym.make('CartPole-v1')
env.env.theta_threshold_radians = math.pi / 2
state = env.reset()

# parameters for scoring
score = 0
done = False
start_time = time.time()
max_timesteps = 200
t = 0

# parameters for PID controller
Kp, Ki, Kd = 1, 0.1, 5
desired_angle = 0
integral = 0
prev_error = 0

while True:
    env.render()
    if done or t >= max_timesteps:
        continue

    # TODO: determine action according to PID control rule
    pole_angle = state[2]
    error = pole_angle - desired_angle
    action = 0

    # execute one step of the simulation and obtain the next state and reward
    state, reward, done, info = env.step(action)
    print("Step %3d: state %5.2f action %d reward %d" % (t, state[2], action, reward))
    time.sleep(0.05)
    t += 1
    score += reward
    if done or t >= max_timesteps:
        end_time = time.time()
        print("Game Over: cart pole survived for %4.2fs (score=%d)" % (end_time - start_time, score))
env.close()
