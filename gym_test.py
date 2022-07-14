import gym, time
import mujoco_py
import os




env = gym.make("CartPole-v0") #"Zaxxon-v4" Taxi-v3  "MontezumaRevenge-v0" HalfCheetah-v2 LunarLander-v2
observation = env.reset()

for _ in range(1000):
    env.render()
    #time.sleep(0.05)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()
env.close()

'''
mj_path = mujoco_py.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)

print(sim.data.qpos)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

sim.step()
print(sim.data.qpos)
'''