# MC-AI-BUILD

[English](README.md) | 简体中文

本项目基于 OpenAI 的 [Point-E](https://openai.com/research/point-e) 模型。玩家可以通过文本描述或图片来生成Minecraft建筑。

## 项目结构
```
├── images          # 用于存放图片
├── pcs             # 用于存放生成的点云，避免重复生成
|   ├── image
|   └── text
├── point-e         # Point-E模型
├── build.py        # 程序入口
├── color.py        # 方块颜色
├── image2point.py  # 图片转点云
├── text2point.py   # 文本转点云
└── ...
```

## 环境准备
1. 下载、构建、运行Minecraft服务端，可参考<https://www.spigotmc.org/wiki/spigot-installation>。
2. 安装 [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) 插件。

![](https://file.moluuser.com/img/202308052327994.png)

## 运行程序
`build.py` 中的 `SIZE` 变量为生成建筑的大小。

### 由图片生成
1. 将图片放入 `images` 文件夹中。
2. 修改 `build.py` 中的 `IMAGE_PATH` 变量为图片路径。
3. 运行 `build.py`。

即可在Minecraft中当前人物附近生成对应的建筑。

![](https://file.moluuser.com/img/202308052333507.png)

![](https://file.moluuser.com/img/202308052336193.png)

### 由文本生成
1. 修改 `build.py` 中的 `PROMPT` 变量。
2. 运行 `build.py`。
