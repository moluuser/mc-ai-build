# MC-AI-BUILD

[English](README.md) | [简体中文](README.zh-CN.md)

This project is based on OpenAI's [Point-E](https://openai.com/research/point-e) model. Players can generate Minecraft buildings through text descriptions or images.

## Project structure
```
├── images          # Used to store images
├── pcs             # Used to store generated point clouds to avoid repeated generation
|   ├── image
|   └── text
├── point-e         # Point-E model
├── build.py        # Program entry
├── color.py        # Block color
├── image2point.py  # Image to point cloud
├── text2point.py   # Text to point cloud
└── ...
```

## Environment preparation
1. Download, build, and run the Minecraft server, refer to <https://www.spigotmc.org/wiki/spigot-installation>.
2. Install the [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) plugin.

![](https://file.moluuser.com/img/202308052327994.png)

## Run the program
The `SIZE` variable in `build.py` is the size of the generated building.

### Generated from image
1. Put the image in the `images` folder.
2. Modify the `IMAGE_PATH` variable in `build.py` to the image path.
3. Run `build.py`.

The corresponding building will be generated near the current character in Minecraft.

![](https://file.moluuser.com/img/202308052333507.png)

![](https://file.moluuser.com/img/202308052336193.png)

### Generated from text
1. Modify the `PROMPT` variable in `build.py`.
2. Run `build.py`.
