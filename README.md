# Ape Gaze Prediction : A Bayesian ROS Simulation of False Belief Understanding

This project implements a Bayseian Network using ROS (Robot Operating System) to simulate predictins inspired by the research paper "Great Apes anticipate that other individuals will act according to false beliefs" (Krupenye et al., 2016). The system models how oberved inputs (object_size, human_action, human_expression) influence the probability of robot expressions, analogus to predicting the object the ape's gaze went to first based on the species and experimental condition. This project was develoiped as part of the coursework for Cognitive Robotics.

## Orignal Research Summary

The paper ‘Great Apes anticipate that other individuals will act according to false beliefs’ studied whether Greater Apes have the ability to understand False Beliefs. The study concluded that they did have the ability. Previously, it was believed that the Great Apes and other mammals were in fact incapable understanding such cognitive ability and theorised that this is what makes human cognitive ability greater. The research was thorough; it used two different experimental setups and measures to avoid various other factors including learned behaviour to emulate how false beliefs are tested in young toddlers and babies.

❗False Beliefs are defined as the mental beliefs or assertions which are inaccurate or deviate from reality in some way.

### The Experiment

<img width="456" height="642" alt="image" src="https://github.com/user-attachments/assets/b8f90a74-0349-47f5-8f62-d7a0fb0c843a">


The study tracked the eyes of the Great Apes (Bonobo, Chimpanzee, Orangutan) to see whether the ape would look at the target, a distractor or not look at all. Only the first looks were considered. The apes were subjected to two different experiments and 2 different false beliefs to avoid learned and coincidental behaviours affecting the study.

### Study Data
The following proability data were extracted from the study (Krupenye et al., 2016):

**Species Prior Probabilities**

| Species    | Count | Probability |
| ---------- | ----- | ----------- |
| Bonobo     | 8     | 8/29        |
| Chimpanzee | 14    | 14/29       |
| Orangutan  | 7     | 7/29        |

**Experiment Prior Probabilities**

P(Exp 1) = P(Exp 2) = 1/2

**Overall Gaze Probabilities**

|  Gaze       | Probabilities |
|  --------   | ------------- |
|  Target     | 31/58         |
|  Distractor | 11/58         |
|  No Look    | 16/58         |

**Gaze Probabilities per Experiment (Marginal over species)**

| Gaze       | Exp 1 | Exp 2 |
| ---------- | ----- | ----- |
| Target     | 15/29 | 16/29 |
| Distractor | 6/29  | 5/29  |
| No Look    | 8/29  | 8/29  |

**Conditional Probabilities P(Gaze | Ape, Experiment)**

| Species    | Experiment | Target | Distractor | No Look |
| ---------- | ---------- | ------ | ---------- | ------- |
| Bonobo     | Exp 1      | 7/8    | 1/8        | 0       |
| Bonobo     | Exp 2      | 3/8    | 4/8        | 1/8     |
| Chimpanzee | Exp 1      | 7/14   | 5/14       | 2/14    |
| Chimpanzee | Exp 2      | 8/14   | 1/14       | 5/14    |
| Orangutan  | Exp 1      | 1/7    | 0          | 6/7     |
| Orangutan  | Exp 2      | 5/7    | 0          | 2/7     |

These conditional probabilities are the core of the Bayesian Network Model.

## Bayesian Network Model

The joint probability distribution over Ape species, Experiment number, and Gaze outcome is given by:

****P(Ape, Experiment, Gaze) = P(Gaze|Ape,Experiment)* P(Ape)*P(Experiment)****

This factorization assumes that the Ape and Experiment are independent (the prior probability of each species and does not depend on which experiment is performed). The gaze outcome depends conditionally on both the apes species and the experiment number.

## ROS Implementation Mapping

The orignal study variables are mapped to the ROS system as follows:
|  Study Variables   | ROS Variable                                                                    |
|  ---------------   | ------------------------------------------------------------------------------- |
|  Ape Species       | Not directly used. Instead, inputs: object_size, human_action, human_expression |
|  Experiment Number | Perception filter status (whether inputs are set to zero)                       |
|  Gaze Outcome      | Robot expression (probability of each expression)                               |

## Repository Structure

```bash
CR_WEEK6_TEST/
├── src/
│   ├── generator.py          # Generates random input values (ID, object size, human action, human expression)
│   ├── filter.py             # Perception filter: sets some inputs to zero based on random process
│   ├── controller.py         # Calls predictor service and calculates robot expression probabilities
│   └── predictor.py          # Implements Bayes theorem and conditional probability tables
├── msg/
│   ├── object_info.msg
│   ├── human_info.msg
│   ├── perceived_info.msg
│   └── robot_info.msg
├── srv/
│   └── predict_robot_expression.srv
├── launch/
│   └── cr_week6_test.launch  # Launches all four nodes together
├── package.xml
└── CMakeLists.txt
```

## Dependencies

- ROS (tested on Noetic)
- Python 3
- rospy
- random (standard libary)
- numpy (optional, for probability calculations)

## Running the Simulation

1. Clone the repository into your ROS workspace src folder:
```bash
cd ~/catkin_ws
```

2. Build Package

```bash
catkin_make
source devel/setup.bash
```
3. Running the Simulation

```bash
roslaunch cr_week6_test cr_week6_test.launch

# or alternatively

rosrun cr_week6_test generator.py
rosrun cr_week6_test filter.py
rosrun cr_week6_test controller.py
rosrun cr_week6_test predictor.py

```

## Nodes Description

### Generator

Generates random values for:
- ID (identifier)
- object_size
- human_action
- human_expression

These values are published as **object_info** and **human_info** messages.

### Perception Filter

Simulates imperfect perception by randomly setting some input values (object_size, human_expression, human_action) to zero. This mirrors the controlled experimental conditions in the orignal ape study where certain cues were hidden to test false belief understanding. This filter acts as the "experiment" variable in the Bayesian network: when values are set to zero, it represents a different experimental condition.

### Robot Controller

Subscribes to filtered perception messages and calls the **predict_robot_expression** service from the predictor node. It then calculates the probability of each possible robot expression. In the orignal study, this would correspond to computing P(gaze | Ape, Experiment) based on observed data.

### Robot Expression Predictor

Implements a Bayesian network using:
- Prior probabilities for each input variable.
- Conditional probability table (CPT) for robot expressions given input states.
- Bayes theorem to compute posterior probabilites

The predictor attempts to compute:

**P(Robot_Expression | Object_Size, Human_Action, Human_Expression) = P(Object_Size, Human_Action, Human_Expression | Robot_Expression) * P(Robot_Expression) / P(Data)**

Due to the implementation constraints, the full Bayesian Query couldn't be executed. Two helper functions:

- One to calculate indivdual input probabilities
- One to compute conditional probabilities for each expression

## Expected Output

<img width="813" height="693" alt="image" src="https://github.com/user-attachments/assets/4732dfe8-4e5b-44ef-91cb-4384e24dfe4d" />


When running the simulation, teh controller node displays probabilities for each robot expression (e.g., p_target, p_distractor, p_nolook) analogous to the gaze probabilities in the orignal study. For a given species (mapped through inputs) and experiment number (filter sstate), the probabilities approximate the values via the conditional probability table.

## Acknowledgements

This work is based on the research paper:
Krupenye, C., Kano, F., Hirata, S., Call, J. and Tomasello, M., 2016. Great apes anticipate that other individuals will act according to false beliefs. Science, 354(6308), pp.110-114.

Coursework Assignment for Cognitive Robotics Module (QMUL-EECS Lorenzo Jamone)

## References 

- Krupenye, C., Kano, F., Hirata, S., Call, J. & Tomasello, M. (2016). Great apes anticipate that other individuals will act according to false beliefs. Science, 354(6308), 110-114.

- Bian, L. & Baillargeon, R. (2021). False Beliefs. Encyclopedia of Evolutionary Psychological Science, pp.2922-2934.
