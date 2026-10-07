from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["Real-Time Notifications"])

connections = {}

@router.websocket("/ws/notifications/{user_id}")
async def notification_socket(websocket: WebSocket, user_id: int):
    await websocket.accept()

    if user_id not in connections:
        connections[user_id] = []

    connections[user_id].append(websocket)

    try:
        while True:
            message = await websocket.receive_text()

            for connection in connections.get(user_id, []):
                await connection.send_json({
                    "type": "realtime",
                    "message": message
                })

    except WebSocketDisconnect:
        if user_id in connections and websocket in connections[user_id]:
            connections[user_id].remove(websocket)
