import launch
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch import LaunchDescription
import os

def generate_launch_description():

    talker_component_node = ComposableNodeContainer(
        node_namespace='',
        node_name='minimal_container',
        package='rclcpp_components',
        # node_executable='component_container_mt', # this struggles to maintain timer rates!!!!!!!!!!
        node_executable='component_container', # this maintains the rates fine
        composable_node_descriptions=[
            ComposableNode(
                package="minimal_publisher",
                node_plugin='minimal_publisher::Talker',
                node_name='talker_component'),
        ],
        output='screen',
    )

    return LaunchDescription([
        talker_component_node
        ]
    )