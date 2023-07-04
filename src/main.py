import webview
from backend.server import server
from backend.websocket import startWs, closeWs
from websockets.exceptions import ConnectionClosedError

def initWS(window):
    try:
        startWs(window.get_current_url().replace('/','').replace('region', '').split(':')[2]) # start the ws and pass the port of the server
        print("Successfully connected to websocket")
    except ConnectionClosedError as e:
        print("Connection closed: ", e)
        #TODO: Send user a page saying they closed valorant. Have a button on this page to restart websocket when they launch again.
    except Exception as e:
        print("Unknown error: ", e)
        raise e


window = webview.create_window('Agent Yoinker', server, height=768, width=1366)
webview.start(initWS, (window,)) # start the window along with startWs in a separate thread
closeWs()