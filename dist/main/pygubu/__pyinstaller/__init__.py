from typing import List
import os


def get_hook_dirs() -> List[str]:
    return [os.path.dirname(__file__)]
