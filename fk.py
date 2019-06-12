import numpy as np
import math

link1 = 1
link2 = 2
link3 = 3
theta1 = math.radians(int(input("Angle1:")))
theta2 = math.radians(int(input("Angle2:")))

#transform_matrix_0_1 = np.matrix([[math.cos(theta1), 0, math.sin(theta1), 0], [math.sin(theta1), 0, -math.cos(theta1), 0], [0, 1, 0, link1], [0, 0, 0, 1]])
#transform_matrix_1_2 = np.matrix([[math.cos(theta2), -math.sin(theta2), 0, link2*math.cos(theta2)], [math.sin(theta2), math.cos(theta2), 0, link2*math.sin(theta2)], [0, 0, 1, 0], [0, 0, 0, 1]])
#transform_matrix_2_3 = np.matrix([[math.cos(theta3), -math.sin(theta3), 0, link3*math.cos(theta3)], [math.sin(theta3), math.cos(theta3), 0, link3*math.sin(theta3)], [0, 0, 1, 0], [0, 0, 0, 1]])

x = (1.4*math.cos(theta1+math.pi)*math.cos(theta2))+(1.18*math.cos(theta1+math.pi))-(1.4*math.sin(theta1+math.pi)*math.sin(theta2))
y = 1.4*math.sin(theta1+math.pi)*math.cos(theta2)+1.4*math.cos(theta1+math.pi)*math.sin(theta2)+1.18*math.sin(theta1+math.pi)
z = 1
coordinates = (x, y, z)
print(coordinates)


