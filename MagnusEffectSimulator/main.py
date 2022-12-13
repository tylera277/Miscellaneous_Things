
# 12Dec2022

#

#############################
# ###### IMPORTS ####### #

import numpy as np
import matplotlib.pyplot as plt

from forces_function import ForceFunction

#############################


#############################
# User Inputs (metric units)
velocity_magnitude = 40
velocity_theta = 0
velocity_phi = 0
#       (omega: 100rpm ~= 10rad/s)
fastball = np.array([0, -157, 0])
vertical_curveball = np.array([0, 157, 0])
slider = np.array([0, -157, 157])

rotational_vector = slider

# Drag force constants
area = np.pi*0.036322**2
drag_coefficient = 0.3411
density_of_air = 1.225

# Gravitational force constants
acceleration_due_to_gravity = -10
mass = 0.145

time = 0.0
dt = 0.01

v_m = velocity_magnitude
v_t = np.radians(velocity_theta)
v_p = np.radians(velocity_phi)
#############################


#############################
# Calculation section
position = np.array([0.0, -0.3, 1.33])

velocity = np.array([v_m * np.cos(v_t) * np.sin((np.pi/2)-v_p),
                     v_m * np.sin(v_t) * np.sin((np.pi/2)-v_p),
                     v_m * np.cos((np.pi/2)-v_p)])

# Storage arrays for plotting later
x_position = []
y_position = []
z_position = []



while time < 0.5:


    # Runge-kutta things
    k_1  = ForceFunction(rotational_vector=rotational_vector,
                       velocity=velocity,
                       rho=density_of_air,
                       drag_coeff=drag_coefficient,
                       area=area,
                       mass=mass,
                       acceleration_due_to_gravity=acceleration_due_to_gravity
                       ).total_acceleration()

    k_2 = ForceFunction(rotational_vector=rotational_vector,
                       velocity=velocity+(dt*(k_1/2)),
                       rho=density_of_air,
                       drag_coeff=drag_coefficient,
                       area=area,
                       mass=mass,
                       acceleration_due_to_gravity=acceleration_due_to_gravity
                       ).total_acceleration()

    k_3 = ForceFunction(rotational_vector=rotational_vector,
                        velocity=velocity + (dt * (k_2 / 2)),
                        rho=density_of_air,
                        drag_coeff=drag_coefficient,
                        area=area,
                        mass=mass,
                        acceleration_due_to_gravity=acceleration_due_to_gravity
                        ).total_acceleration()

    k_4 = ForceFunction(rotational_vector=rotational_vector,
                       velocity=velocity+(dt*k_3),
                       rho=density_of_air,
                       drag_coeff=drag_coefficient,
                       area=area,
                       mass=mass,
                       acceleration_due_to_gravity=acceleration_due_to_gravity
                       ).total_acceleration()

    change_in_velocity = ((1.0/6.0)*(k_1 + 2*k_2 + 2*k_3 + k_4)*dt)


    position += (velocity * dt)

    velocity += change_in_velocity

    x_position.append(position[0])
    y_position.append(position[1])
    z_position.append(position[2])

    time += dt


plt.plot(y_position, z_position)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()
#############################

