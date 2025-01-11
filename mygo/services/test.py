import os
import json

def generate_image_map(directory: str, output_file: str) -> None:
    """
    Generate a JSON file containing metadata for all images in a directory.

    Args:
        directory (str): Path to the directory containing the image files.
        output_file (str): Path to the output JSON file.
    """
    # 支持的图片扩展名
    supported_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

    # 获取目录下所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # 过滤图片文件
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in supported_extensions]

    # 构造 JSON 数据
    image_map = []
    for image_file in image_files:
        # 使用文件名（不包含扩展名）作为 `name` 和 `description`
        name = os.path.splitext(image_file)[0]
        image_map.append({
            "name": name,
            "file_name": image_file,
            "description": name
        })

    # 将数据写入 JSON 文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(image_map, f, ensure_ascii=False, indent=4)
    print(f"JSON file generated at: {output_file}")

# 使用示例
if __name__ == "__main__":
    # 输入图片目录路径和输出 JSON 文件路径
    image_directory = "./vv_image"  # 替换为你的图片目录路径
    output_json = "image_map.json"  # 替换为你希望生成的 JSON 文件路径

    # 生成 JSON 文件
    generate_image_map(image_directory, output_json)
