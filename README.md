# RL-gym-envs
This repo provides a simple guideline for creating the Atari and MuJoCo gym env for RL training


## Python version == 3.8

* install packages
> pip install Box2D
> 
> pip install atari-py
> 
> pip install gym==0.15.7
> 
> python -m atari_py.import_roms atari_bins  #### This is to copy the bins directly to your virtualenv
> 
> mkdir -p ~/.mujoco && cp -a mujoco210/ ~/.mujoco

* add path to .bashrc 
> export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/```usr name (replace) ```/.mujoco/mujoco210/bin
> 
> export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia 
> 
> export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so 

* install mujoco
> pip install -U 'mujoco-py<2.2,>=2.1'

#### In  case there are any bugs with respect to missing Glew or patchelf
> sudo apt-get install libglew-dev
> 
> sudo apt-get install patchelf
