"""
MIT License

Copyright (c) 2021 codebyte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import websocket


class WebsocketClient:

    def __init__(self):
        self.api_url = "https://api.hiven.io/v1"
        self.ws_url = "wss://swarm-dev.hiven.io/socket?encoding=json&compression=text_json"

        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

    def open_connection(self):
        """Starts the WebSocket connection"""

        self.ws.run_forever()

    def on_open(ws):
        """Function triggered when a WebSocket connection is opened"""

        pass

    def on_message(ws, message):
        """Function triggered when a message is received from the WebSocket connection"""

        pass

    def on_error(ws, error):
        """Function triggered when there is an error in the WebSocket connection"""

        pass

    def on_close(ws):
        """Function triggered when the WebSocket connection is closed"""

        pass
