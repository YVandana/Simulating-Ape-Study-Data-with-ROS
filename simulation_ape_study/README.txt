Y VANDANA; Cognitive Robotics (ROBOTICS IV)
COURSEWORK-1
CR_WEEK6_TEST
Impleneting Bayesian Networks through ROS
PKG: cr_week6_test
MSG: object_info, human_info, perceived_info, robot_info
SRV: predict_robot_expression
launch: group 4 python nodes to be presented in the GUI:- Generator, Filter, Controller, Predictor
Python Nodes: Generator, Filter, Controller, Predictor
Interaction Generator: Using random generator creates values for Id, object_size, human_action and human_expression.
Perception Filter: Using a Random generator results in setting input values that are object_size, human_expression and human_action as 0.
Robot Controler: Calls Msg Perceived Info and Function from Robot Expression Predictor to calculate the probability of each robot expression
Robot Expression Predictor: Uses Bayes theorem and the CPT Table to result in values (I couldn't really perform the formula from scratch and the baysian network wasn't running so I was not able to use query but I have used 2 functions one to call probability of each input and also fucntion for indivdual conditional probabilities)

How to RUN:
1. Run source /opt/ros/noetic/setup.bash
2. Go to Catkin directory
3. Run catkin_make (you may have to use catkin_make clean before using this)
4. Run soruce ./deve/setup.bash
5. Go to cr_week6_test directory roscd cr_week6_test
6. roslaunch cr_week6_test human_robot_interaction.launch should run and display all the nodes.
7. If it doesn't run you might have to change permissions on the .py files with chmod +x filename.py (It should Run)
8. To check graph open new shell run source /opt/ros/noetic/setup.bash
9. Go to catkin_ws and run source ./devel/setup.bash
10. run rqt_graph (All active nodes can be run to check the working of the msgs)
11. Opening new shells for each topic you have to run 8 and 9 again
12. run rostopic echo /object_info
13. run rostopic echo /human_info
14. run rostopic echo /perceived_info
15. run rostopic echo /robot_info
16. Warning: The video doesn't show ropstopic as for some reason even with me using sourcing bash files it still shows not published hence I have also presented the plot so it is seen that the msgs are active.
