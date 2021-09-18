cmake_minimum_required(VERSION 3.5)
project(minimal_publisher)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(std_msgs REQUIRED)
find_package(minimal_interfaces REQUIRED)

include_directories(include)

add_executable(publisher_lambda_custom src/lambda_custom.cpp)
ament_target_dependencies(publisher_lambda_custom rclcpp std_msgs minimal_interfaces)

add_executable(publisher_lambda src/lambda.cpp)
ament_target_dependencies(publisher_lambda rclcpp std_msgs)

add_executable(publisher_member_function src/member_function.cpp)
ament_target_dependencies(publisher_member_function rclcpp std_msgs)

add_executable(publisher_not_composable src/not_composable.cpp)
ament_target_dependencies(publisher_not_composable rclcpp std_msgs)

add_library(talker_component SHARED src/talker_component.cpp)
target_compile_definitions(talker_component
  PRIVATE "MINIMAL_PUBLISHER_BUILDING_DLL")
ament_target_dependencies(talker_component rclcpp std_msgs rclcpp_components)
rclcpp_components_register_nodes(talker_component "minimal_publisher::Talker")
# To register multiple components in the same shared library, use multiple calls
# rclcpp_components_register_nodes(talker_component "composition::Talker2")

install(TARGETS
  talker_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

install(TARGETS
  publisher_lambda_custom
  publisher_lambda
  publisher_member_function
  publisher_not_composable
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
