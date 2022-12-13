
# 12Dec2022

#############################
# ###### IMPORTS ####### #

import numpy as np

#############################


class ForceFunction:

    """
    Inputs:
        -vector which describes ball's rotation,
        -current velocity vector describing balls motion

        -rho: ------- density of fluid in which ball is moving in
        -drag_coeff:  drag coefficient that is particular to the ball
        we are using (getting this from resources online for the balls)
        -area: ------ cross-sectional area of the ball

        -mass: mass of ball
        -acceleration_due_to_gravity: the acceleration the ball feels
        at its particular altitude on earth
    """

    def __init__(self, rotational_vector, velocity, rho, drag_coeff, area,
                 mass, acceleration_due_to_gravity):
        self.rotational_vector = rotational_vector
        self.velocity = velocity
        self.rho = rho
        self.drag_coeff = drag_coeff
        self.area = area
        self.mass = mass
        self.acceleration_due_to_gravity = acceleration_due_to_gravity

    def drag_force(self, ):
        """
        Outputs:
            -Vector which encapsulates the drag the ball feels
        """

        velocity_mag = np.sqrt(np.dot(self.velocity, self.velocity))
        velocity_unit_vector = self.velocity/velocity_mag
        velocity_squared = np.dot(self.velocity, self.velocity)

        drag_beginning = (1.0/2.0) * self.rho * self.drag_coeff * self.area

        drag_force = - drag_beginning * velocity_squared * velocity_unit_vector


        return drag_force

    def magnus_force(self):
        """
        Outputs:
            - magnus force vector which the ball feels on its travels
        """
        factor = 4.1*10**(-4)
        magnus_force = self.mass*factor*\
        np.cross(self.rotational_vector, self.velocity)

        return magnus_force

    def gravitational_force(self):
        """
        Ouputs:
            -vector which only has a z-component as thats the only way gravity acts
            in this scenario
        """
        gravity = self.mass * self.acceleration_due_to_gravity

        gravitational_force = np.array([0, 0, gravity])

        return gravitational_force


    def total_acceleration(self):
        """
        Output:
            -Vector which sums all the acceleration contributions
            from each force
        """

        a_d = self.drag_force()/self.mass
        a_m = self.magnus_force()/self.mass
        a_g = self.gravitational_force()/self.mass

        return (a_g+a_m+a_d)




