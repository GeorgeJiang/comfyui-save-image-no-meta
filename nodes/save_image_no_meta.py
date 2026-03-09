# -*- coding: utf-8 -*-
"""
Save Image Without Metadata — MPS-safe, zero-dependency
"""

import os
import numpy as np
from PIL import Image
import folder_paths
import torch


class SaveImageNoMeta:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", {"tooltip": "The images to save."}),
                "filename_prefix": ("STRING", {"default": "ComfyUI_NoMeta", "tooltip": "Prefix for saved files."})
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "save_images"
    OUTPUT_NODE = True
    CATEGORY = "image"
    DESCRIPTION = "Saves images without embedding workflow or prompt metadata."
    SEARCH_ALIASES = ["save no meta", "clean save"]

    def save_images(self, images, filename_prefix="ComfyUI_NoMeta", prompt=None, extra_pnginfo=None):
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(
            filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0]
        )
        results = []

        for batch_number, image in enumerate(images):
            # Convert tensor to PIL Image
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            
            # ✅ KEY: Do NOT add any metadata
            metadata = None

            filename_with_batch_num = filename.replace("%batch_num%", str(batch_number))
            file = f"{filename_with_batch_num}_{counter:05}_.png"
            img.save(
                os.path.join(full_output_folder, file),
                pnginfo=metadata,
                compress_level=self.compress_level
            )
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            })
            counter += 1

        return {"ui": {"images": results}}

# At the bottom of save_image_no_meta.py
NODE_CLASS_MAPPINGS = {
    "💾 Save Image (No Meta)": SaveImageNoMeta,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "💾 Save Image (No Meta)": "💾 Save Image Without Metadata",
}