import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data

class CollisionAvoider(Node):

    def __init__(self):

        qos = QoSProfile(depth=10)

        super().__init__('collision_detector')

        self.subscriber_ = self.create_subscription(LaserScan, 'scan', self.callback, qos_profile=qos_profile_sensor_data)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', qos)
        # self.timer_ = self.create_timer(0.01, self.callback)

    def callback(self, msg):
        move = Twist()
        
        dist_obstacle = min(msg.ranges)
        safe_dist = 0.8
        if (dist_obstacle > safe_dist):
            move.linear.x = 0.3
            move.angular.z = 0.0
        else:
            move.linear.x = 0.0
            move.angular.z = 3.5 #change this to control the avoidance speed
            self.get_logger().info("Obstacles are detected nearby. Changing course!!!")
        
        # else:
        #     move.linear.x = 0.0
        #     move.angular.z = 3.5
        # if msg.ranges[0] < 0.7:
        #     if msg.ranges[90] <= msg.ranges[270]:
        #         move.linear.x = 0.0
        #         move.angular.z = -3.5
        #         self.get_logger().info('Obstacle detected changing the course!!!')
            
        #     elif msg.ranges[90] > msg.ranges[270]:
        #         move.linear.x = 0.0
        #         move.angular.z = 3.5
        # else:
        #     move.linear.x = 0.5
        #     move.angular.z = 0.0
        self.publisher_.publish(move)


def main(args=None):

    rclpy.init(args=args)
    node = CollisionAvoider()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
