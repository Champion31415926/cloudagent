# CS426FZ Assignment Question 2

## Task 1：石块立方体（3 marks）

立方体表面使用石头纹理，正面放上缩写 **CPY**。下图同时包含渲染结果、UV Editor 和 Shader Editor。

![Task 1：渲染视图、UV Editor 与 Shader Editor](images/task1.png)

## Task 2：海滩上的石子（3 marks）

用 UV Sphere 做成石子，并用 Noise Texture、Color Ramp、Fresnel 和 Bump 生成石头材质。地面使用 Shadow Catcher。`spiaggia_di_mondello` HDRI 只用于照明，最终画面中不显示海滩照片。

![Task 2：Layout 中的最终渲染](images/task2.png)

## Task 3：球体着色器（4 marks）

按实验给出的节点连接球体：近处使用 Glossy BSDF，远处使用 Diffuse BSDF，切换由 View Z Depth 经过 Greater Than 控制。

在此基础上做了两处改动：

- 颜色改为粉色。
- Greater Than 的阈值从 10.600 改为 20。

View Z Depth 小于 20 时，Greater Than 输出 0，Mix Shader 使用上方的 Glossy BSDF，球体呈粉色光泽。深度大于 20 时输出 1，改为使用下方的 Diffuse BSDF。阈值从 10.600 提高到 20 后，光泽区域延伸得更远，漫反射从更远的位置才开始。

![Task 3：着色器节点](images/task3-shader.png)

![Task 3：渲染结果](images/task3-render.png)
