# ComfyUI Save Image Without Metadata

A custom node that saves images **without embedding your workflow, prompt, or model info** in PNG files.

Perfect for:
- Sharing clean images publicly
- Reducing file size
- Privacy protection

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. In ComfyUI, open **Manager → Install Custom Nodes**
2. Search for `comfyui-save-image-no-meta`
3. Click **Install**

### Method 2: Manual Install

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/GeorgeJiang/comfyui-save-image-no-meta.git
```
Then restart ComfyUI.

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