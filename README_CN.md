# 全球大学名单数据库 (Global Universities List)

一个包含全球大学标准化**中英文**名称的综合数据库。

[English Version](README.md)

## 项目目标
本项目致力于整合全球高等教育机构的完整名单。对于每一所大学，我们提供：
- **_id**: 合并列表中的唯一标识符。
- **中文名称**: 官方简体中文名称。
- **英文名称**: 标准国际名称（已针对 CSV 兼容性进行清洗）。
- **国家**: 院校所属国家。

## 数据结构
项目按地区/国家文件夹组织：

- `world_universities.csv`: 所有大学的汇总主表。
- `China/`: 包含中国大陆、香港、澳门和台湾的记录。缺失的英文名已通过 AI 翻译补全。
- `Japan/`: 日本院校数据，译自日语原名。
- `Poland/`: 波兰院校数据，译自波兰语原名。
- `Egypt/`: 埃及院校数据。

## 功能特性与自动化
- **AI 驱动翻译**: 使用 **Gemini 2.0 Flash**，主要基于原始语言名称（波兰语、日语等）提供官方国际英文名，并参考中文语境。
- **增量更新**: 脚本会自动跟踪现有记录，避免重复 API 调用，节省成本及时间。
- **数据清洗**: 
    - 自动剥离名称首尾的包裹双引号。
    - 将名称内部的双引号替换为单引号。
    - 将英文名中的逗号替换为空格，确保 CSV 格式在不使用转义符的情况下依然整洁。
- **主表汇总**: 汇总脚本自动聚合各地区的 CSV，并生成唯一 ID。

## 汇总生成
运行以下命令更新全局汇总文件：
```bash
python generate_summary.py
```

## 当前进度
- [x] **中国**: 3000 条记录（含港澳台）。
- [x] **日本**: 959 条记录（译自日语）。
- [x] **波兰**: 88 条记录（译自波兰语）。
- [x] **埃及**: 28 条记录。
- [ ] **美国**: 计划中。
- [ ] **欧洲**: 计划中。

## 技术栈
- **Python 3**: 核心处理语言。
- **Pandas**: 数据处理与 CSV 管理。
- **Gemini 2.0 Flash**: 学术级翻译与实体映射。
- **Requests / Curl**: 官方 API 交互。
- **python-dotenv**: 安全的环境变量管理。

## 环境配置
1. **API Key**: 在根目录创建 `.env` 文件：
   ```env
   GEMINI_API_KEY=your_key_here
   ```
2. **安装依赖**:
   ```bash
   pip install pandas google-generativeai python-dotenv requests
   ```
3. **运行更新脚本**:
   ```bash
   python Poland/update_poland_universities.py
   python Japan/update_japan_universities.py
   ```

## 存储格式
- 编码格式: `UTF-8 with BOM` 以适配 Excel。
- 标准化列名 (`_id`, `chinese_name`, `english_name`, `country`)。
