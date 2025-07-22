# dash-react-scan-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-react-scan-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-react-scan-plugin.svg?color=dark-green)](https://pypi.org/project/dash-react-scan-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

简体中文 | [English](./README.md)

适用于[Dash](https://github.com/plotly/dash)应用的页面组件渲染性能监控插件，基于`Dash Hooks`+[react-scan](https://github.com/aidenybai/react-scan)实现，用于在当前`Dash`应用页面中添加额外的组件渲染性能监控功能，帮助开发者发现性能问题从而启发优化方向。

## 安装

```bash
pip install dash-react-scan-plugin
```

## 使用

```python
from dash import Dash

# 导入插件启用函数
from dash_react_scan_plugin import setup_react_scan_plugin

# 为当前应用启用插件
setup_react_scan_plugin()

app = Dash(__name__)

# 其他应用代码...
```

## 示例

执行示例应用，此示例演示了如何通过插件监控`Dash`应用程序中的组件渲染性能，该插件会自动将`react-scan`工具注入到当前`Dash`应用中，帮助开发者精准定位性能问题位置：

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## 参数说明

### `setup_react_scan_plugin()`

用于为当前`Dash`应用注入组件渲染监控工具。

| 参数         | 类型  | 默认值                                                                 | 描述                                                                                                                                                                                          |
| ------------ | ----- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `script_src` | `str` | `"https://cdn.jsdelivr.net/npm/react-scan@latest/dist/auto.global.js"` | 依赖的 react-scan 静态资源地址，常见的可用资源地址有：`https://unpkg.com/react-scan@latest/dist/auto.global.js`, `https://registry.npmmirror.com/react-scan/latest/files/dist/auto.global.js` |
