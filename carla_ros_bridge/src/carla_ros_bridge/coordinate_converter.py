#!/usr/bin/env python
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3
import numpy as np
import tf


def convert_pose(pose):
    """
    convert pose between left and right-hand coordinate system
    :param pose: pose to be converted
    :return: converted pose
    """
    data = Pose()
    data.position = convert_vector3(pose.position)
    data.orientation = convert_quaternion(pose.orientation)
    return data


def convert_vector3(pt):
    """
    convert vector3 between left and right-hand coordinate system
    :param pt: point to be converted
    :return: converted point
    """
    return Vector3(pt.x, -pt.y, pt.z)


def convert_point(pt):
    """
    convert point between left and right-hand coordinate system
    :param pt: point to be converted
    :return: converted point
    """
    return Point(pt.x, -pt.y, pt.z)


def convert_quaternion(q):
    """
    convert quaternion between left and right-hand coordinate system
    :param q: quaternion to be converted
    :return: converted quaternion
    """

    euler = tf.transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])
    euler = (euler[0], euler[1], -euler[2])
    return Quaternion(*tf.transformations.quaternion_from_euler(*euler))


def convert_euler(euler):
    """
    convert euler angles between left and right-hand coordinate system
    :param euler: euler angles to be converted
    :return: converted euler angles
    """
    return Vector3(euler.x, euler.y, -euler.z)
