import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data

class ObstacleDetector(Node):

    def __init__(self):
        self.safe_dist_ = 1.5
        self.linear_speed = 0.4
        self.angular_speed = 2.5
        qos = QoSProfile(depth=10)
        super().__init__('obstacle_detector')
        self.subscriber_ = self.create_subscription(LaserScan, 'scan', self.callback, qos_profile=qos_profile_sensor_data)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', qos)

    def callback(self, msg):

        move = Twist()
        n = 10 # number of rays 
        # We took one ray per 20 degree
        # move.linear.x = 0.4
        # move.angular.z = 0.0
        segments = {
            'right': min(min(msg.ranges[0:2]), n),
            'front' : min(min(msg.ranges[3:5]), n),
            'left' : min(min(msg.ranges[6:9]), n),
        }

        if (segments['front'] > self.safe_dist_ and segments['left'] > self.safe_dist_ and segments['right'] > self.safe_dist_):
            move.linear.x = 0.4
            move.angular.z = 0.0
            self.get_logger().warn("No obstacles going freee")

        elif(segments['front'] < self.safe_dist_ and segments['left'] < self.safe_dist_ and segments['right'] < self.safe_dist_):
            move.linear.x = -self.linear_speed
            move.angular.z = self.angular_speed

        elif (segments['front'] < self.safe_dist_ and segments['left'] > self.safe_dist_ and segments['right'] > self.safe_dist_):
            move.linear.x = 0.0
            move.angular.z = self.angular_speed
        
        elif (segments['front'] > self.safe_dist_ and segments['left'] > self.safe_dist_ and segments['right'] < self.safe_dist_):
            move.linear.x = 0.0
            move.angular.z = self.angular_speed
        
        elif (segments['front'] > self.safe_dist_ and segments['left'] < self.safe_dist_ and segments['right'] > self.safe_dist_):
            move.linear.x = 0.0
            move.angular.z = -self.angular_speed

        elif (segments['front'] < self.safe_dist_ and segments['left'] > self.safe_dist_ and segments['right'] < self.safe_dist_):
            move.linear.x = 0.0
            move.angular.z = self.angular_speed
        
        elif (segments['front'] < self.safe_dist_ and segments['left'] < self.safe_dist_ and segments['right'] > self.safe_dist_):
            move.linear.x = 0.0
            move.angular.z = -self.angular_speed

        elif (segments['front'] > self.safe_dist_ and segments['left'] < self.safe_dist_ and segments['right'] <  self.safe_dist_):
            move.linear.x = self.linear_speed
            move.angular.z = 0.0

        else:
            self.get_logger().error("Unknown Case issued please check the environment!!!")
        self.publisher_.publish(move)


def main(args=None):

    rclpy.init(args=args)
    node = ObstacleDetector()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()