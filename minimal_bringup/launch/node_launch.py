from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='minimal_publisher',
            node_namespace='minimal',
            node_executable='publisher_lambda',
            node_name='publisher'
        ),
        Node(
            package='minimal_subscriber',
            node_namespace='minimal',
            node_executable='subscriber_lambda',
            node_name='subscriber'
        )
    ])