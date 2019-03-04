import sys

import rclpy

from rclpy.qos import qos_profile_default


def chatter_callback(msg):
    print('I heard: [%s]' % msg.data)


def main(args=None):
    if args is None:
        args = sys.argv

    rclpy.init(args=args)

    from std_msgs.msg import Float32

    node = rclpy.create_node('listener_float_py')

    sub = node.create_subscription(
        msg_type=Float32, topic='chatter', callback=chatter_callback, qos_profile=qos_profile_default)
    assert sub  # prevent unused warning

    while rclpy.ok():
        rclpy.spin_once(node)


if __name__ == '__main__':
    main()
