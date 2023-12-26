#!/usr/bin/env python3
import subprocess
import os

rviz_config_prefix = subprocess.check_output(["ros2", "pkg", "prefix", "minibot_navigation2"]).decode().strip()
rviz_config_path = os.path.join(rviz_config_prefix, "share", "minibot_navigation2", "rviz", "nav2_view.rviz")
subprocess.run(["rviz2", "-d", rviz_config_path])
