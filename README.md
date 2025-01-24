# ros2_minimal_project

ros2 humble版本基础工程，编译使用

```bash
colcon build
```

注意：

强烈不建议采用ROS1方式去写ROS2节点程序，如例程中`not_composable`，会导致无法更好利用ROS2特征，出现传输效率低等问题