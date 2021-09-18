from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # start a publisher_lambda in the minimal namespace
    minimal_publisher_node = Node(
        package='minimal_publisher',
        node_namespace='minimal',
        node_executable='publisher_lambda',
        node_name='publisher'
    )

    minimal_subscriber_node = Node(
        package='minimal_subscriber',
        node_namespace='minimal',
        node_executable='subscriber_lambda',
        node_name='subscriber'
    )

    return LaunchDescription([
        minimal_publisher_node,
        minimal_subscriber_node
    ])
