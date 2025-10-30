# bridge.py
import asyncio
import websockets
import json

ESP_IP   = "192.168.1.112"   # ← YOUR ESP IP
ESP_PORT = 8080

COMMANDS = {
    (1, True):  bytes.fromhex("A0 01 01 A2"),
    (1, False): bytes.fromhex("A0 01 00 A1"),
    (2, True):  bytes.fromhex("A0 02 01 A3"),
    (2, False): bytes.fromhex("A0 02 00 A2"),
    (3, True):  bytes.fromhex("A0 03 01 A4"),
    (3, False): bytes.fromhex("A0 03 00 A3"),
    (4, True):  bytes.fromhex("A0 04 01 A5"),
    (4, False): bytes.fromhex("A0 04 00 A4"),
}

async def tcp_client(websocket):
    try:
        reader, writer = await asyncio.open_connection(ESP_IP, ESP_PORT)
        print(f"TCP CONNECTED to {ESP_IP}:{ESP_PORT}")
    except Exception as e:
        print(f"TCP FAILED: {e}")
        await websocket.close()
        return

    async def ws_to_tcp():
        async for msg in websocket:
            try:
                data = json.loads(msg)
                relay = int(data["relay"])
                on = bool(data["on"])
                cmd = COMMANDS.get((relay, on))
                if not cmd:
                    await websocket.send(json.dumps({"error": "bad cmd"}))
                    continue
                writer.write(cmd)
                await writer.drain()
                print(f"Sent: {cmd.hex().upper()} → R{relay} {'ON' if on else 'OFF'}")
            except Exception as e:
                print(f"WS Error: {e}")

    async def tcp_to_ws():
        try:
            while True:
                data = await reader.read(100)
                if not data: break
                print(f"ESP → {data.hex()}")
        except: pass

    await asyncio.gather(ws_to_tcp(), tcp_to_ws())
    writer.close()
    await writer.wait_closed()

async def main():
    async with websockets.serve(tcp_client, "0.0.0.0", 8765):
        print("WebSocket → TCP Bridge RUNNING on ws://127.0.0.1:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())