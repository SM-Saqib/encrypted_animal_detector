from channels.routing import route
from animal_detector_app.consumers import ws_connect,ws_disconnect

channel_routing = [
    route('websocket.connect',ws_connect),
    route('websocket.disconnect',ws_disconnect),
    
]