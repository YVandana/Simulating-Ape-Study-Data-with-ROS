#!/usr/bin/env python
import rospy

from cr_week6_test.msg import perceived_info
from cr_week6_test.msg import robot_info
from cr_week6_test.srv import predict_robot_expression, predict_robot_expressionResponse


# Callback for the perceived_info topic
def callback(data):
	try:
		predict = rospy.ServiceProxy('predict_robot_expression', predict_robot_expression)        
		# Initilaising new publishing nodes
		# pub4 node is publishing to the robot_info topic using robot_info as message type
		pub4 = rospy.Publisher('robot_info', robot_info, queue_size=0)
		#pub2 = rospy.Publisher('human_info_generator', human_info, queue_size=0)
		
		# Creating msg of the robot_info
		obj4 = robot_info()
		sol = predict(data.object_size, data.human_action, data.human_expression)
		
		obj4.id = data.id
		obj4.p_happy = sol.p_happy
		obj4.p_sad = sol.p_sad
		obj4.p_neutral = sol.p_neutral
		
		rospy.loginfo(obj4)
		print(obj4)
		pub4.publish(obj4)
		
	except rospy.ServiceException as e:
		print("Service call failed: %s"%e)

def robot_controller():
	# initialising new topic
	rospy.init_node('robot_controller', anonymous = True)
	# initialising new node subscribing to perceived info
	
	rospy.Subscriber("perceived_info", perceived_info, callback)
	print("Ready to Predict Robot Expression")
	rospy.spin()


if __name__ == "__main__":
	robot_controller()
