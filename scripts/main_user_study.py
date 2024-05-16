"""
Authors: Giovanni Franzese 
Email: g.franzese@tudelft.nl
Cognitive Robotics, TU Delft
This code is part of TERI (TEaching Robots Interactively) project
"""
#%%
import matplotlib
from SIMPLe_bimanual.dual_panda import DualPanda
import time

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#%%
if __name__ == '__main__':
    BiManualTeaching=DualPanda()
    #ILoSA.connect_ROS()
    time.sleep(1)
    BiManualTeaching.Panda_left.home_gripper()
    BiManualTeaching.Panda_right.home_gripper()
    time.sleep(1)

#%% KINESTHETIC TEACHING# %%
BiManualTeaching.Kinesthetic_Demonstration_BiManual()
# %%
BiManualTeaching.Panda_left.home()
BiManualTeaching.Panda_right.home()
#%%
BiManualTeaching.save()
# %%
BiManualTeaching.load()
# %%e
BiManualTeaching.Panda_right.go_to_start()
BiManualTeaching.Panda_left.go_to_start()
#%%    
BiManualTeaching.execute_dual()
# %%
BiManualTeaching.correction_execute_dual()
# %%
BiManualTeaching.enable_correction = False
# %%
BiManualTeaching.Kinesthetic_Demonstration_BiManual()
#%%
BiManualTeaching.go_to_start()
#%%
BiManualTeaching.execute_dual()