#!/usr/bin/env python
import rospy

from cr_week6_test.msg import *
from cr_week6_test.srv import *

def f_O(O):
	return 1.0/2.0 # since both object sizes have equal probability

def f_HA(HA):
	return 1.0/3.0 # since all actions have equal probability

def f_HE(HE):
	return 1.0/3.0 # since all expressions have equal probability

def f_RE(O, HA, HE, RE):
	#this function is to return probability values for object_size, human_action, human_expression based of each possible robot expression 
	if RE == '1':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.8 
			elif O == '2':
				return 1
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.8
			elif O == '2':
				return 1
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.6
			elif O == '2':
				return 0.8
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.1
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.2

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.7
			elif O == '2':
				return 0.8
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.8
			elif O == '2':
				return 0.9
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.6
			elif O == '2':
				return 0.7
	
	if RE == '2':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.1
			elif O == '2':
				return 0.1
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.3
			elif O == '2':
				return 0.2
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.1
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2
	if RE == '3':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 1.0
			elif O == '2':
				return 1.0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.9
			elif O == '2':
				return 0.8
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.8
			elif O == '2':
				return 0.6

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.1


def implement(data):
	O = str(data.object_size)
	HA = str(data.human_action)
	HE = str(data.human_expression)
	predictions = [1/3,1/3,1/3]
        # have to give corresponding values
	if O =='0' and HA == '0' and HE == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif O == '0' and HA == '0':
		# Have to work only with various HE values for each expressions and average out values for HA and O
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif O == '0' and HE == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif HA == '0' and HE == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif HE == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif HA == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
	elif O == '0':
		predictions[0] = 1/3
		predictions[1] = 1/3
		predictions[2] = 1/3
		
	return predict_robot_expressionResponse(predictions[0], predictions[1], predictions[2])


def robot_expression_prediction():
	rospy.init_node('robot_expression_prediction', anonymous=True)
	s = rospy.Service('predict_robot_expression', predict_robot_expression, implement)
	rospy.spin()

if __name__ == '__main__':
	try:
		robot_expression_prediction()
	except rospy.ROSInterruptException:
		pass
