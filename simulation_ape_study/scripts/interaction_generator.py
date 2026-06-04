#!/usr/bin/env python

import rospy
import random

from cr_week6_test.msg import object_info
from cr_week6_test.msg import human_info

def interaction_generator():
	# initialising new topic
	pub1 = rospy.Publisher('object_info', object_info, queue_size=0)
	pub2 = rospy.Publisher('human_info', human_info, queue_size=0)
	    
	# initialising new node
	rospy.init_node('interaction_generator', anonymous=True)
	rate = rospy.Rate(0.10) #  1/10 Hz for Once every 10 seconds
	
	msg1 = object_info()
	msg2 = human_info()
	id=1
    
	while not rospy.is_shutdown():
	        # generate random numbers
	        msg1.id = id
	        msg2.id = id
        
	        #the random.randint function gives a number between [a,b] a and b including a and b
        
	        #msg1.id = random.randint(1, 100,1) #curtailing number of ids generated to 100
	        msg1.object_size = random.randint(1, 2) # Object Size 1=Small or 2=Big 
	        msg2.human_action = random.randint(1, 3) # Human Action 1= looking at the robots face 2= looking at the coloured toy 3= looking away
	        msg2.human_expression = random.randint(1, 3) # Human Expression 1= Happy 2= Sad 3= Neutral
	        #msg2.id = msg1.id
        
	        rospy.loginfo(msg1)
	        rospy.loginfo(msg2)
        
	        pub1.publish(msg1)
	        pub2.publish(msg2)
        
	        #print(msg1)
	        #print(msg2)
	        rate.sleep()
	        
	        id += 1

if __name__ == '__main__':
	try:
		interaction_generator()
	except rospy.ROSInterruptException:
		pass
