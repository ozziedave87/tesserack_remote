#interperter line
#!/usr/bin/env python3



import rclpy #python lib for Ros2
from rclpy.node import Node

class oled_subscriberNode(Node):

    def __init__(self):
        super().__init__("oled_subscriber")
        self.oled_subscriber_ = self.create_subscription(oled, , self.oled_callback, 10)

    def oled_callback(self, msg: oled):
        self.get_logger().info("oled screen is on")

def main(args=None):
    rclpy.init(arsg=args)
    node = oled_subscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()