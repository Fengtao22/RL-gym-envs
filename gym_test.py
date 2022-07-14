import gym, time
import mujoco_py
import os

from gym import envs
all_envs = envs.registry.all()
env_ids = [env_spec.id for env_spec in all_envs]
#print(sorted(env_ids))

for env_name in env_ids: #sorted(env_ids):
    print('\nEnv: ', env_name)
    if 'Hand' in env_name:
        continue
    else:    
        env = gym.make(env_name) #"Zaxxon-v4" Taxi-v3  "MontezumaRevenge-v0" HalfCheetah-v2 LunarLander-v2
        observation = env.reset()

        #try:
        #    env.render()
        #except:
        #    continue
            
        '''
        for _ in range(5):
            env.render()
            #time.sleep(0.05)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            if done:
                observation = env.reset()
        '''        
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
