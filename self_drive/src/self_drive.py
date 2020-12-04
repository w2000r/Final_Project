#!/home/pi/.pyenv/versions/rospy3/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher
        self.count = 30

    def lds_callback(self, scan):
        turtle_vel = Twist()	

        '''for i in range(30):
            if (scan.ranges[i] <= 0.25) or (scan.ranges[-i] <= 0.25):
                turtle_vel.linear.x = 0
                if (abs(scan.ranges[i] - scan.ranges[-i]) > 0.1 and scan.ranges[i] - scan.ranges[-i] > 0):
                    turtle_vel.angular.z = 1.8
                    self.publisher.publish(turtle_vel)
                    print("turn left")
                elif (abs(scan.ranges[-i] - scan.ranges[i]) > 0.1 and scan.ranges[i] - scan.ranges[-i] < 0):
                    turtle_vel.angular.z =-1.8
                    print("turn right")
                    self.publisher.publish(turtle_vel)
            else:
                print("go straight")
                turtle_vel.linear.x = 0.15
                turtle_vel.angular.z = 0
                self.publisher.publish(turtle_vel)'''
        '''for i in range(30):
            if (scan.ranges[i] <= 0.27) or (scan.ranges[-i] <= 0.27):
                turtle_vel.linear.x = 0
                if (scan.ranges[i] > scan.ranges[-i]):
                    print("right1")
                    turtle_vel.angular.z = 1
                    if (abs(scan.ranges[i] - scan.ranges[-i]) < 0.5):
                        turtle_vel.angular.z = 2
                        print("right")
                else:
                    print("left1")
                    turtle_vel.angular.z = -1
                    if (abs(scan.ranges[i] - scan.ranges[-i]) < 0.5):
                        turtle_vel.angular.z = -2
                        print("left")
            else:
                turtle_vel.linear.x = 0.15
                turtle_vel.angular.z = 0'''


        print("scan[0]:", scan.ranges[0])
        
        # 속도 출력
        self.publisher.publish(turtle_vel)


def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
