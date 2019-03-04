import sys
import rclpy
from rclpy.qos import qos_profile_default

def main(args=None):
    if args is None:
        args = sys.argv

    rclpy.init(args=args)

    from std_msgs.msg import Float32
    # create a node called talker_float_py
    node = rclpy.create_node('talker_float_py')
    # create a publisher with the QoS default profile
    chatter_pub = node.create_publisher(msg_type=Float32, topic='chatter')
    # set to the msg variable the data type
    msg = Float32()
    # set the message
    i = 1
    msg.data = float(i)
    # print the published message
    print('Publishing: "{0}"'.format(msg.data))
    # publish the message
    chatter_pub.publish(msg)

if __name__ == '__main__':
    main()
