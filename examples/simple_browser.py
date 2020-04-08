import webview
import objc  # pylint: disable=unused-import # noqa F401
import pkg_resources.py2_warn  # pylint: disable=unused-import # noqa F401

"""
This example demonstrates how to create a webview window.
"""

if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window('Simple browser', 'https://pywebview.flowrl.com/hello')
    webview.start()
