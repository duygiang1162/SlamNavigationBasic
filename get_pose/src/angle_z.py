from math import atan2, degrees

# Quaternion components for orientation around the Z-axis
z = 0.66
w = 0.74


# Function to convert quaternion to Euler angle in degrees around the Z-axis
def quaternion_to_euler_z(w, z):
    # Euler angle (yaw) calculation from quaternion components
    # Considering the robot is on a 2D plane, x and y components are assumed to be 0
    # This simplifies the yaw calculation as follows:
    yaw = atan2(2.0 * (w * z), 1.0 - 2.0 * (z * z))
    
    # Convert radians to degrees
    yaw_degrees = degrees(yaw)
    
    # Normalize the angle to the range [0, 360)
    # if yaw_degrees < 0:
    #     yaw_degrees += 360
    
    return yaw_degrees

# Calculate the rotation angle around the Z-axis
rotation_angle_z = quaternion_to_euler_z(w, z)
print(rotation_angle_z)
