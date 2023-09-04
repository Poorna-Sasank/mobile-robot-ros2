import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class VelPublisher(Node):

    def __init__(self):
         
        qos = QoSProfile(depth=10)

        super().__init__('vel_pub')
        self.vel_publisher_ = self.create_publisher(Twist, 'cmd_vel', qos)
        self.timer_ = self.create_timer(0.5, self.velocity_publisher_callback)
        self.get_logger().info('Velocity publisher node has started!!!')

    def velocity_publisher_callback(self):
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.vel_publisher_.publish(msg)

def main(args=None):

    rclpy.init(args=args)
    node = VelPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()