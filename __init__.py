# -*- coding: utf-8 -*-
"""
ComfyUI Save Image Without Metadata — MPS-safe, zero-dependency plugin
Author: Hongzhi Jiang
Purpose: Save Image Without Metadata
"""

import os
import sys

# Add current plugin directory to Python path so we can import nodes/
plugin_dir = os.path.dirname(__file__)
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)

# Safely import node definitions
try:
    from .nodes.save_image_no_meta import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except Exception as e:
     # Print error but don't crash ComfyUI
    print(f"[comfyui-save-image-no-meta] ❌ Failed to load nodes: {e}")
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

# ComfyUI requires these two variables to register custom nodes
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]