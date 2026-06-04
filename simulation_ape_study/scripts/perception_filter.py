#!/usr/bin/env python
import rospy
import random


#from cr_week6_test.srv import *
from cr_week6_test.msg import human_info
from cr_week6_test.msg import object_info
from cr_week6_test.msg import perceived_info

class Callback:
	def __init__(self, perceived_info):
		self.id = 0
		self.object_size = 0
		self.human_action = 0
		self.human_expression = 0
		self.perceived_info = perceived_info
	def callback1(self, data):
		#function that return the data(msg) from the object info publisher
		rospy.loginfo(rospy.get_caller_id() + "\n object info heard %s", data) #print info
		
		# Storing the published id and object size
		self.id = data.id
		self.object_size = data.object_size

	def callback2(self, data):
		#function that return the data(msg) from the human info publisher
		rospy.loginfo(rospy.get_caller_id() + "\n human info heard %s", data) #print info
		
		# Storing the published human action and human expression
		self.human_action = data.human_action
		self.human_expression = data.human_expression
		
		# Randomly filter the information
		self.filter_info()
		
		# Publish the data
		self.publish_new_data(perceived_info)
		
	def filter_info(self):
		# Function to check whether the random filter is equal to the following conditions
		choice = random.randint(1,8) #int(np.random.uniform(1,8))
		
		# Changing object size, human action and human expression to 0 if conditions met
		if choice == 1 :
			self.object_size = 0
		elif choice == 2 :
			self.human_action = 0
		elif choice == 3 :
			self.human_expression = 0
		elif choice == 4 :
			self.object_size = 0
			self.human_action = 0
		elif choice == 5 :
			self.object_size = 0
			self.human_expression = 0
		elif choice == 6 :
			self.human_action = 0
			self.human_expression = 0
		elif choice == 7 :
			self.object_size = 0
			self.human_action = 0
			self.human_expression = 0
		elif choice == 8 :
			#no change
			pass

	def publish_new_data(self, perceived_info):
		# initialising new topic
		# pub3 is publishing to the perceived_info topic using perceived_info as message type
		pub3 = rospy.Publisher('perceived_info', perceived_info, queue_size=0)
		
		# Creaing msg for the perceived_info
		obj3 = perceived_info()
		
		# Updating parameters - perceived_info
		obj3.id = self.id
		obj3.object_size = self.object_size
		obj3.human_action = self.human_action
		obj3.human_expression = self.human_expression 
		
		# Publishing the id and object size to the perceived_info topic
		pub3.publish(obj3)
		print(obj3)
		rospy.loginfo(obj3)
		
def perception_filter():
	# initialising new topic
	rospy.init_node('perception_filter', anonymous=True)
	
	obj = Callback(perceived_info)
	
	# subscribing to object_info and humna_info
	rospy.Subscriber("object_info", object_info, obj.callback1) 
	rospy.Subscriber("human_info", human_info, obj.callback2)
	rospy.spin()
	
if __name__ == '__main__':
	perception_filter() #calling the subscriber node function
