"""
@Author: yanzx
@Date: 2022/5/19 23:13
@Description: 
"""
import os

def get_project_path():
    """得到项目路径"""
    project_path = os.path.join(
        os.path.dirname(__file__), "."
    )
    return project_path
