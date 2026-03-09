# CLAUDE.md - 项目开发指南

## 项目概览

这是一个包含多个前端可视化项目的代码库，主要用于展示互动式 Web 效果。

## 目录结构

```
ai-coding/
├── .claude/                 # Claude 配置和任务文件
│   ├── settings.local.json
│   └── tasks/
│       └── requirements.md  # 圣诞树项目需求文档
├── get-started/             # 主要项目代码
│   ├── static/              # 静态 HTML 页面
│   │   ├── index.html       # 首页（待完善）
│   │   ├── visualization.html  # 粒子星云可视化
│   │   └── christmas-tree.html # 手势互动圣诞树
│   └── calculator.py        # FastAPI 后端服务
```

## 已实现项目

### 1. 粒子星云可视化 (visualization.html)

**技术栈**: Canvas 2D + 原生 JavaScript

**功能特性**:
- 300+ 粒子系统，支持鼠标/触摸互动
- 4 种互动模式：流动 (flow)、聚集 (swarm)、爆炸 (explode)、漩涡 (vortex)
- 5 种配色方案：星云、海洋、火焰、森林、日落
- 粒子间动态连接线效果
- FPS 性能监控
- 响应式画布尺寸

**关键类**: `Particle` - 粒子类，包含位置、速度、颜色、生命周期等属性

---

### 2. 手势互动圣诞树 (christmas-tree.html)

**技术栈**: Three.js r0.160 + MediaPipe Vision Tasks + Postprocessing

**功能特性**:
- 1500+ 3D 粒子组成圣诞树（盒子、球体、糖果棒形状）
- 2500 个背景尘埃粒子
- MediaPipe 手势识别：捏合、握拳、张开手掌
- 三种模式切换：
  - `TREE`: 螺旋圆锥树形
  - `SCATTER`: 粒子分散球体
  - `FOCUS`: 聚焦查看照片
- 照片上传功能（动态纹理贴图）
- 摄像头实时手势追踪控制场景旋转
- UnrealBloomPass 后处理光效

**核心类**: `ChristmasTree` - 主场景类，管理渲染器、相机、粒子系统、手势处理

**关键依赖**:
```javascript
three: "https://unpkg.com/three@0.160.0/build/three.module.js"
@mediapipe/tasks-vision: "https://unpkg.com/@mediapipe/tasks-vision@0.10.3"
```

---

### 3. FastAPI 后端 (calculator.py)

**端点**:
- `GET /` - 首页
- `GET /visualization.html` - 粒子可视化页面
- `POST /api/calc` - 计算器 API (a, b, op)

**运行方式**:
```bash
uvicorn calculator:app --reload
```

---

## 开发规范

### 代码风格
- HTML 页面使用语义化标签
- CSS 采用 BEM 命名风格
- JavaScript 使用 ES Module 语法
-  Three.js 场景使用类封装模式

### 性能优化
- 粒子数量根据屏幕尺寸动态调整
- 使用 `requestAnimationFrame` 渲染循环
- Canvas 绘制使用 `globalAlpha` 优化透明度
- Three.js 使用 `PMREMGenerator` 环境贴图

### 手势识别逻辑

| 手势 | 检测条件 | 触发模式 |
|------|----------|----------|
| 捏合 (Pinch) | 拇指与食指距离 < 0.05 | FOCUS 聚焦 |
| 握拳 (Fist) | 指尖到手腕平均距离 < 0.25 | TREE 树形 |
| 张开 (Open) | 指尖到手腕平均距离 > 0.4 | SCATTER 分散 |

---

## 待办事项

- [ ] 完善 `index.html` 首页内容
- [ ] 创建计算器前端页面
- [ ] 添加 `README.md` 项目说明文档
- [ ] 添加依赖管理文件

---

## 外部资源

### CDN 依赖
- Three.js: `https://unpkg.com/three@0.160.0/`
- MediaPipe: `https://unpkg.com/@mediapipe/tasks-vision@0.10.3/`
- Google Fonts: Cinzel 字体

### 模型资源
- Hand Landmarker: `https://storage.googleapis.com/mediapipe-models/hand_landmarker/...`
