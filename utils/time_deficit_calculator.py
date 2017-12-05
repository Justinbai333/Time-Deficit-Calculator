
# -*- coding: utf-8 -*-
"""
Introduction: This is a program that counts the time deficit clocks would experience
due to special and general relativity. (Denoted by SR and GR)

It uses for loop to calculate midpoint Riemann sum of the desired integration. 

It can be used for two cases:
(i) Calculating the time deficit a clock on the earth would experience annually.
(ii) Calculating the time deficit a clock on a satellite 
orbiting around earth at certain fixed radius would experience annually.

All physics formulus used in this program are covered in PHYS 211, 214, 225 of UIUC physics curriculum.
Users of this program are assumed to own basic knowledge of classical mechanics and relativity.
Program is designed only for calculation use, not for the study of physics.

@author: Justin Bai(jinbai2), Brian Yang(brian-yang)

Note: all numbers are in SI units, ie (kg for mass, s for time, m for length)

"""

#------------------------------------------
# Below is the part for importing necessary libraries.
import numpy as np

#------------------------------------------
# Below is the preperation part before we do the integral. 
# Mainly inputing constants and do trivial calculations for basic values like mass or velocity.

# set up known constants (G refers to gravity constant, c for speed of light)
G = 6.674e-11
earth_mass = 5.972e24
earth_radius = 6.371e6
c = 299792458

# m is the mass of the satelitte we study.
# m is set to be one for convenience, in fact, mass of the satellite would cancel itself during calculation
m = 1

# T_earth is just one day, aka the time for earth to complete a full rotation
T_earth = 24*60*60

# omega_earth denotes the angular velocity of the earth
omega_earth = 2*np.pi/T_earth

# v_earth denotes the velocity of the earth
v_earth = omega_earth*earth_radius

# Special class to store the results of calculating the time deficit.
# Takes in a clock type parameter when initialized
class Clock:
        def __init__(self, clock_type):
                self.clock_type = clock_type
                self.results = []

        def add_time_deficit_results(self, special_rel, general_rel, special_general_rel):
                self.results.append(special_rel)
                self.results.append(general_rel)
                self.results.append(special_general_rel)

        def get_time_deficit_results(self):
                return self.results

def valid_satellite_radius(radius):
        try:
                radius = float(radius)
        except:
                return false

        return radius >= earth_radius

def calculate_time_deficit(choice, rmax = earth_radius):
        """
        PARAMETERS
        """

        # v_circle denotes the velocity of the satellite
        # here we can just use sqrt(G*m/r) since mass of satellite is negeligible compare to mass of the earth
        if choice == 2:
               v_satellite = np.sqrt(G * earth_mass / rmax)

        # here we set the initial coordinates for the clock on earth (or the satellite)
        # (i) use x = earth_radius for the earth if equatorial
        # (ii)use x=rmax for satellite if satellite
        if choice == 1:
                x = earth_radius
                y = 0
        elif choice == 2:
                x = rmax
                y = 0

        # t_max denote the time period in which time deficit takes place.
        # Here I choose t_max to be one day instead of 365 days, I will time a factor of 365 in the end.
        # This approximation is mainly for shrinking the running time of the program
        t_max = 24*60*60

        # we break a whole day into seconds to simulate integration 
        #(for a whole day, seconds are nearly infinitesimals)
        dt = 1

        # Define initial velocities for clocks
        # (i) use v_y = v_earth for the earth
        # (ii) use v_y = v_satellite for the satellite
        if choice == 1:
                v_x = 0
                v_y = v_earth
        elif choice == 2:
                v_x = 0
                v_y = v_satellite

        # following parameters are to be used in the for-loop but are unknown currently
        # so they are set to 0 just for initialization
        t = 0
        r = 0
        v = 0

        # let src, grc, sgrc denote the time deficit caused by SR, GR or both SR & GR.
        # t_xxx denotes total time deficit, dt_xxx denotes time deficit in one small period (namely one second) 
        t_src = 0
        dt_src = 0

        t_grc = 0
        dt_grc = 0

        t_sgrc = 0
        dt_sgrc = 0

        """
        CALCULATION
        """

        # create arrays to input total amount of change of time under correction by SR or GR or both.
        number_of_time_slices = int(t_max/dt)

        t_grc_array = np.empty(number_of_time_slices)
        t_src_array = np.empty(number_of_time_slices)
        t_sgrc_array = np.empty(number_of_time_slices)

        # create the for loop to complete the integral
        # this program use midpoint Riemann sums to approximate integration
        for i in range (0,number_of_time_slices):       

                F_x =m * (-G * earth_mass * x/(x ** 2 + y ** 2) ** (3 / 2))
                F_y =m * (-G * earth_mass * y/(x ** 2 + y ** 2) ** (3 / 2))

                x_midpoint = x + v_x*dt / 2
                y_midpoint = y + v_y*dt / 2

                v_xmidpoint = v_x + (F_x / m)*dt / 2
                v_ymidpoint = v_y + (F_y / m)*dt / 2

                F_xmidpoint = m * (-G * earth_mass * x_midpoint / (x_midpoint ** 2 + y_midpoint ** 2) ** (3 / 2))
                F_ymidpoint = m * (-G * earth_mass * y_midpoint / (x_midpoint ** 2 + y_midpoint ** 2) ** (3 / 2))

                dx = v_xmidpoint * dt
                dy = v_ymidpoint * dt

                dv_x = (F_xmidpoint / m) * dt
                dv_y = (F_ymidpoint / m) * dt

                x = x + dx
                y = y + dy

                r = np.sqrt(x**2 + y**2) 


                v_x = v_x + dv_x
                v_y = v_y + dv_y

                v = np.sqrt (v_x**2+v_y**2)

                dt_grc = dt-dt*np.sqrt(1-0.00887/r) 

                dt_src = dt - dt*np.sqrt(abs(1-v**2/c**2))

                dt_sgrc = dt - dt*np.sqrt(abs(1-v**2/c**2))*np.sqrt(1-0.00887/r)    

                t_grc = t_grc + dt_grc

                t_src = t_src + dt_src

                t_sgrc = t_sgrc + dt_sgrc

                t_grc_array[i] = t_grc  

                t_src_array[i] = t_src

                t_sgrc_array[i] = t_sgrc

        # Here I print out the desired values (Which would change correspondingly for different clocks)
        # I time every number by a factor of 365 since the for-loop only integrates through one day
        if choice == 1:
                clock_type = "equitorial clock"
        elif choice == 2:
                clock_type = "satellite clock"

        clock = Clock(clock_type)

        clock.add_time_deficit_results(t_src_array[number_of_time_slices-1]*365,
                                       t_grc_array[number_of_time_slices-1]*365,
                                       t_sgrc_array[number_of_time_slices-1]*36)

        print("Under special relativistic correction. " + clock_type +  " annual deficit is", 
              t_src_array[number_of_time_slices-1]*365)
        print("Under general relativistic correction. " + clock_type + " annual deficit is", 
              t_grc_array[number_of_time_slices-1]*365)
        print("Under special and general relativistic correction. " + clock_type + " annual deficit is", 
              t_sgrc_array[number_of_time_slices-1]*365)

        return clock
