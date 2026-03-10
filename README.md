# ComfyUI Save Image Without Metadata

A custom node that saves images **without embedding your workflow, prompt, or model info** in PNG files.

Perfect for:
- Sharing clean images publicly
- Reducing file size
- Privacy protection

## 📦 Installation

<!-- 
### Method 1: ComfyUI Manager (Recommended)
1. In ComfyUI, open **Manager → Install Custom Nodes**
2. Search for `comfyui-save-image-no-meta`
3. Click **Install**
-->

### Method 1: Download ZIP (No Git Required)
1. Go to [GitHub Releases](https://github.com/GeorgeJiang/comfyui-save-image-no-meta/releases) or click **[Code → Download ZIP](https://github.com/GeorgeJiang/comfyui-save-image-no-meta/archive/refs/heads/main.zip)**
2. Extract the ZIP file → you'll get a folder named `comfyui-save-image-no-meta-main`
3. Rename it to **`comfyui-save-image-no-meta`** (remove the `-main` suffix)
4. Move this folder into your ComfyUI's `custom_nodes` directory:
```
ComfyUI/
└── custom_nodes/
    └── comfyui-save-image-no-meta/  ← your folder here
```
5. Restart ComfyUI

### Method 2: Git Clone (For Developers)
```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/GeorgeJiang/comfyui-save-image-no-meta.git
```

## 🧩 Usage

1. Add the node **"💾 Save Image Without Metadata"** from the **image** category  
2. Connect your image output  
3. Saved images will have **no hidden metadata**

> 🔍 **Tip**: Compare with the original "Save Image" node — this one produces smaller, cleaner files!

## 🛡️ Features

- ✅ Removes all ComfyUI metadata (workflow, prompts, seeds, models, etc.)
- ✅ Same filename format as built-in "Save Image"
- ✅ Zero dependencies — uses only standard ComfyUI modules
- ✅ Works on CPU, CUDA, and MPS (Apple Silicon)

---
Made by [George Jiang](https://github.com/GeorgeJiang) · MIT License