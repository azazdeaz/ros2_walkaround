import sys

import rclpy

from rclpy.qos import qos_profile_default

def chatter_callback(msg):
    print('I heard: [%s]' % msg.data)
    detect_intent_texts('walkaround-6b68f', '1', [msg.data], 'en')

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))


def main(args=None):
    if args is None:
        args = sys.argv

    rclpy.init(args=args)

    from std_msgs.msg import String

    node = rclpy.create_node('listener_float_py')

    sub = node.create_subscription(
        msg_type=String, topic='chatter', callback=chatter_callback, qos_profile=qos_profile_default)
    assert sub  # prevent unused warning

    print('Listening...')

    while rclpy.ok():
        rclpy.spin_once(node)


if __name__ == '__main__':
    main()
