'''

1) __init__ function
2) step function
3) reset function

'''
import rospy
from std_srvs.srv import Empty
from gazebo_msgs.srv import GetLinkState
from package1.msg import Num
import numpy as np
import time
import sys



class ArmEnv():

	def __init__(self, target):
		print('__init__5')
		self.net_reward = 0
		self.episode_no = 0
		self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
		self.pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
		self.get_end_effector_pos = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)
		self.reset_simulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
		self.target = target
		self.angle1 = 0.0
		self.angle2 = 0.0


	def step(self, action):
		print('step')
		self.unpause_sim()
		self.set_action(action)
		# self.pause_sim()
		time.sleep(2)
		obs = self.get_obs()
		done = self.is_done(obs)
		reward = self.calc_reward(obs, done)
		self.net_reward += reward
		info = {'episode_no:':self.episode_no, 'observation:':obs, 'curr_reward':reward, 'net_reward':self.net_reward, 'is_done':done}
		return obs, reward, done, info

	def reset(self):
		print('reset')
		self.reset_sim()
		self.update_episode() #update episode no and set net reward to zero
		obs = self.get_obs()
		return obs

	def close(self, reason):
		# rospy.signal_shutdown(reason)
		sys.exit()

	def unpause_sim(self):
		print('unpausing sim')
		self.unpause()

	def pause_sim(self):
		print('pausing sim')
		self.pause()

	def set_action(self, action):
		print('setting action:', action)
		self.pause_sim()
		self.publisher(action)
		self.unpause_sim()

	def get_obs(self):
		end_effector_pos = self.get_end_effector_pos(link_name='2links_plugin_2::link_0_0', reference_frame='2links_plugin_2::link')
		x = end_effector_pos.link_state.pose.position.x
		y = end_effector_pos.link_state.pose.position.y
		return (x, y)

	def is_done(self, observation):
		tolerance = 0.1
		x_min = self.target[0]-tolerance
		x_max = self.target[0]+tolerance
		y_min = self.target[1]-tolerance
		y_max = self.target[1]+tolerance
		print(x_min, x_max, y_min, y_max)
		if (observation[0]>x_min and observation[0]<x_max):
			if (observation[1]>y_min and observation[1]<y_max):
				return True
			else:
				return False

		else:
			return False

	def calc_reward(self, observation, done):
		distance = self.dist(observation, self.target)
		reward = -distance
		if done == True:
			reward += 1
		return reward


	def dist(self, observation, target):
		return np.sqrt((target[0]-observation[0])**2 + (target[1]-observation[1])**2)

	def reset_sim(self):
		print('reset')
		self.pause_sim()
		self.reset_simulation()
		self.publisher((0.0, 0.0))
		self.unpause_sim()
		time.sleep(2)

	def update_episode(self):
		self.episode_no +=1
		self.net_reward = 0

	def publisher(self, angles):
		pub = rospy.Publisher('/2links_plugin_2/vel_cmd', Num, queue_size=1, latch=True)
		rospy.init_node('set_angle', anonymous=True, disable_signals=True)
		msg = Num()
		msg.angle1 = angles[0]
		msg.angle2 = angles[1]
		pub.publish(msg)
		time.sleep(1)



		



