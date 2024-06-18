# __init__.py
from .FrameSkipping import FrameSkipping
from .FrameTruncating import FrameTruncating
from .MaskFrameSkipping import MaskFrameSkipping
from .MaskGenerator import MaskGenerator
from .IntOperationsNode import IntOperationsNode
from .FrameSelector import FrameSelector
from .MaskSelector import MaskSelector

NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping,
    "FrameTruncating": FrameTruncating,  # 添加新的组件到节点类映射
    "MaskFrameSkipping": MaskFrameSkipping,
    "MaskGenerator": MaskGenerator,
    "IntOperationsNode": IntOperationsNode,
    "FrameSelector": FrameSelector,
    "MaskSelector": MaskSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping",
    "FrameTruncating": "Frame Truncating",
    "MaskFrameSkipping": "Mask Frame Skipping",  # 添加新的组件到节点显示名称映射
    "MaskGenerator": "Mask Generator",
    "IntOperationsNode": "Int Operations",
    "FrameSelector": "Frame Selector",
    "MaskSelector": "Mask Selector",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
