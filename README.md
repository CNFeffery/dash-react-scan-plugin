# dash-react-scan-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-react-scan-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-react-scan-plugin.svg?color=dark-green)](https://pypi.org/project/dash-react-scan-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A plugin to monitor the rendering performance of page components for Dash applications using Dash Hooks. This plugin integrates [react-scan](https://github.com/aidenybai/react-scan) to help you analyze and optimize your Dash application's performance.

## Installation

```bash
pip install dash-react-scan-plugin
```

## Usage

```python
from dash import Dash
# Import the react scan plugin
from dash_react_scan_plugin import setup_react_scan_plugin

# Enable the react scan plugin for the current app
setup_react_scan_plugin()

app = Dash(__name__)
# Rest of your app code...
```

## Example

Run the included example. This example demonstrates how to use react-scan to monitor component rendering performance in your Dash application. The plugin will automatically inject the `react-scan` tool into your application, allowing you to visualize and analyze component re-renders.

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## API Reference

### `setup_react_scan_plugin()`

This function sets up the react-scan plugin for your Dash application.

| Parameter    | Type  | Default                                                                | Description                                                                                                                                                                                    |
| ------------ | ----- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `script_src` | `str` | `"https://cdn.jsdelivr.net/npm/react-scan@latest/dist/auto.global.js"` | Source URL of the react-scan script. Alternative CDNs: `https://unpkg.com/react-scan@latest/dist/auto.global.js`, `https://registry.npmmirror.com/react-scan/latest/files/dist/auto.global.js` |
