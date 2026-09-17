# AI 时代的算力鸿沟 —— 汇报要点整理

> 来源：`C:\Users\lenovo\Desktop\扫描全能王 2026-9-17 16.14.pdf`（10 页扫描件，纯图片无文字层，经 `render_pdf.py` 渲染后逐页识读整理）
> 说明：以下为对幻灯片内容的转述与归纳，非逐字转录；模糊或存疑处已标注。

---

## 一、整体脉络

一条主线贯穿全套幻灯片：

**AI 算力需求指数级增长 → 芯片算力供给跟不上（缺口 >10⁵）→ 从封装、互连、存储、器件、EDA 多层面提出"创新"对策。**

- 技术供给轴：摩尔定律（尺寸微缩）→ 先进封装（HBM/HBF）→ 片上互连 / 光互连
- 模型需求轴：卷积神经网络 → 深度网络 → Transformer → 世界模型

---

## 二、逐页要点

### 第 1 页 · AI 时代的算力鸿沟

- 图表横轴为年份（2000–2026），纵轴为算力（FLOPS，对数刻度）。
- 模型侧算力增速明显快于芯片侧，图中以红色箭头标出 **"算力缺口 >10⁵"**。
- 芯片技术演进带：摩尔定律（尺寸微缩）→ 先进封装（HBM/HBF）→ 片上互连 / 光互连。
- 模型演进带：卷积神经网络 → 深度网络 → Transformer → 世界模型。
- 结论句：
  - "AI 算力 scaling 的速度远低于模型 scaling"
  - "多模态融合的物理 AI、世界模型成为端侧 AI 芯片算力和能效的最大挑战"
- 数据来源：Stanford AI Index 2026；Nature 637, 801 (2025)。

### 第 2 页 · 创新 1：以时延缩微替代几何缩微，全层级时延分解

- 范式转移：从"几何微缩"转向"时延缩微"。
- 性能瓶颈已不再是晶体管本身，而是**电路级互连时延**。
- 时延分解公式：

  `τ_total = τ_transistor + τ_circuit + τ_chip + τ_system`

- 各层级占比（约）：

  | 层级 | 名称 | 说明 | 占比 |
  |---|---|---|---|
  | τ₁ | 晶体管层 Transistor | 本征延迟，新型结构/低 k 材料压至 ps 级 | ≈ 2% |
  | τ₂ | 电路层 Circuit | 互连 RC 寄生延迟（当前最大来源），逻辑折叠/拓扑优化压至 ns 级 | ≈ 80% |
  | τ₃ | 芯片层 Chip | 计算 + 存储访问延迟，3D 堆叠/Chiplet 压至 µs 级 | ≈ 12% |
  | τ₄ | 系统层 System | 多芯片/整机互联、协议同步，时间折叠调度压至 ms 级 | ≈ 6% |

### 第 3 页 · 创新 3：wafer → vifer（vertically integrated wafer）

- 关键词：**跨层拆分与设计**、**E2E 时延分析寻优求解**。
- 3D 堆叠分层示意（自上而下）：

  | 层 | 组成 | 作用 |
  |---|---|---|
  | 顶层 | I/O 接口层 / 电源分配层 | 对外通信与供电管理 |
  | 中间层 | 核心逻辑层（CPU / GPU / AI 计算单元） | 主算力实体 |
  | 下层 | 片上存储层（SRAM / 高速缓存） | 低延迟数据缓冲 |
  | 底层 | HBM 集成存储层 | 大容量数据带宽 |

- 强调：**每一层均为有效激活电路，并非无源堆叠结构。**

### 第 4 页 · 创新 5：PDN 与散热

四大痛点（围绕 3DI 结构剖面图）：

1. **功耗大、功耗密度高** —— 1000W，热点重叠。
2. **传导热阻大** —— 散热路径受限，热阻增加。
3. **多层堆叠、内部温升高** —— HBM 多层、高密、高吞吐。
4. **热串扰** —— 结温极限。

### 第 5 页 · 创新 7：Panel level FO

- 面板级扇出封装（Panel Level Fan-Out）。
- 参数（左侧示意图）：

  | 参数 | 值 |
  |---|---|
  | Die Width | 70 mm |
  | Die Height | 70 mm |
  | Horizontal Spacing | 120 mm |
  | Vertical Spacing | 120 mm |
  | Wafer Diameter | 300 mm |
  | Edge Clearance | 5 mm |
  | Notch Height | 10 mm |

- 右侧面板示意：**6R 面板，尺寸 510 mm × 515 mm**。

### 第 6 页 · 创新 8：高密度高带宽存储

- HBM 架构概览；对比两种键合方式：**ubump / Microbump** 与 **Hybrid bonding**。
- 演进数据表（HBM2 → HBM4e）：

  | 指标 | HBM2 2018 | HBM2e 2020 | HBM3 2022 | HBM3e 2024 | HBM4 2026 | HBM4e 2028 |
  |---|---|---|---|---|---|---|
  | 最大堆叠 die 数 | 4 | 8 | 12 | 12 | 16 | 20 |
  | 带宽 (Tbps) | 2.4 | 3.6 | 6.4 | 8 | 12.8 | 16 |
  | 最大容量 (GB) | 8 | 16 | 24 | 36 | 48 | 80 |

- 标注：Hybrid bonding 下 Chip 厚度可 **<25 µm**（图中另见 `≥25µm` / `<15µm` 等对比标注）。

### 第 7 页 · 创新 9：光互联

光互联五代演进：

| 代际 | 名称 |
|---|---|
| Gen I | Pluggable Optics（可插拔光模块） |
| Gen II | On-board Optics（板上光学） |
| Gen III | 2.5D Co-packaged Optics（2.5D 共封装光学） |
| Gen IV | 3D Co-packaged Optics（3D 共封装光学） |
| Gen V | 3D Co-packaged Optics with Integrated Laser（集成激光器的 3D 共封装） |

### 第 8 页 · 创新 11：数模融合 + 存算融合

- 应用方向：手机、AR 眼镜、手表、耳机、机器狗、汽车、机器人等。
- 技术条目：
  - MEMS、微信号采集、ECG/PPG 信号处理架构、超低功耗
  - TOF、超声器件及阵列、MEMS、异质感知材料
  - 波导技术、IOT 模拟电路、信道算法、对消校正算法
  - 高性能时钟分发、高速/超高速、异质异构
- 三大指标：**Power（功耗）/ BW（带宽）/ Latency（时延）**。

### 第 9 页 · 创新 12：AI-based 一体化 3D EDA

- 方向标签：AI4EDA、AI4chip。
- 主题：EDA 的创新与颠覆 —— **伪 3D vs 真 3D**。
- 左侧为"电磁光力热分析"多物理场仿真流程；右侧为一体化 3D 设计/分析框架示意。

### 第 10 页 · 创新 15：后摩尔

- 器件架构展望（PPA vs Device Architecture）：
  - 主流路线：**FinFET → Nanosheet → CFET**
  - Beyond Si（超越硅）：
    - **2D TMD**（WS₂、MoS₂、WSe₂ 等）
    - **CNT / Carbon Nanotube**（碳纳米管）

---

## 三、术语速查

| 缩写 | 全称 | 中文 |
|---|---|---|
| HBM | High Bandwidth Memory | 高带宽存储器 |
| HBF | High Bandwidth Flash（存疑，按上下文推断） | 高带宽闪存 |
| PDN | Power Delivery Network | 供电网络 |
| 3DI | 3D Integration | 三维集成 |
| FO | Fan-Out | 扇出封装 |
| vifer | vertically integrated wafer | 垂直整合晶圆 |
| CFET | Complementary FET | 互补场效应晶体管 |
| TMD | Transition Metal Dichalcogenide | 过渡金属硫族化合物 |
| CNT | Carbon Nanotube | 碳纳米管 |
| E2E | End-to-End | 端到端 |
| PPA | Power, Performance, Area | 功耗、性能、面积 |

---

## 四、整理者备注

1. **编号为奇数**（1、3、5、7、8、9、11、12、15），疑似从一套"15 个创新点"中**抽取的重点页**；2、4、6、10、13、14 未出现，若需完整材料可向讲者补要。
2. 第 1 页仅引两条文献（Stanford AI Index 2026、Nature 637,801(2025)），若做读书报告，建议为每页关键结论补充可核查出处。
3. 部分小字（第 6、9 页）在扫描件中较模糊，已尽力识读，标注"存疑"处请以原件为准。
