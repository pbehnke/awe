import os
import time
import webbrowser

from . import messages
from . import registry
from . import view
from . import webserver
from . import websocket


class Page(view.Element):

    def __init__(self, port=8080, ws_port=9000, width=None, style=None):
        super(Page, self).__init__(parent=None, element_id='', props=None, style=None)
        self._port = port
        self._style = self._set_default_style(style, width)
        self._registry = registry.Registry()
        self._message_handler = messages.MessageHandler(self._registry, self.dispatch)
        self._server = webserver.WebServer(self, port=port)
        self._ws_server = websocket.WebSocketServer(self._message_handler, port=ws_port)
        self._started = False
        self._version = 0

    def start(self, block=False, open_browser=True):
        self._message_handler.start()
        self._server.start()
        self._ws_server.start()
        self._started = True
        if open_browser:
            port = 3000 if os.environ.get('AWE_DEVELOP') else self._port
            webbrowser.open_new_tab('http://localhost:{}'.format(port))
        if block:
            self.block()

    def get_initial_state(self):
        return {
            'children': [t.get_view() for t in self.children],
            'variables': self._registry.get_variables(),
            'version': self._version,
            'style': self._style
        }

    def increase_version(self):
        self._version += 1

    def register(self, obj, obj_id=None):
        self._registry.register(obj, obj_id)

    def dispatch(self, action):
        self.increase_version()
        if not self._started:
            return
        action['version'] = self._version
        self._ws_server.dispatch_from_thread(action)

    @staticmethod
    def _set_default_style(style, width):
        style = style or {}
        defaults = {
            'width': width or 1200,
            'paddingTop': '6px',
            'paddingBottom': '6px'
        }
        for key, default in defaults.items():
            style.setdefault(key, default)
        return style

    @staticmethod
    def block():
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass