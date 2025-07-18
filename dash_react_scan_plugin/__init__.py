import re
from dash import hooks


def setup_react_scan_plugin(
    script_src: str = "https://cdn.jsdelivr.net/npm/react-scan@latest/dist/auto.global.js",
):
    """Setup the react scan plugin

    Args:
        script_src (str, optional): The source link of the origin react-scan script, other commonly used options include public CDN sources such as https://unpkg.com/react-scan@latest/dist/auto.global.js and https://registry.npmmirror.com/react-scan/latest/files/dist/auto.global.js. Defaults to "https://cdn.jsdelivr.net/npm/react-scan@latest/dist/auto.global.js".
    """

    @hooks.index()
    def add_react_scan_js(app_index: str):
        # Extract the first line of the footer part
        match = re.findall("[ ]+<footer>", app_index)

        if match:
            # Add the react-scan script
            app_index = app_index.replace(
                match[0],
                match[0]
                + '\n<script crossOrigin="anonymous" src="__SCRIPT_SRC__" ></script>'.replace(
                    "__SCRIPT_SRC__", script_src
                ),
            )

        return app_index
