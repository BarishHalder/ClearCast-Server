import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print("Client connected:", websocket.remote_address)
    try:
        async for message in websocket:
            # Broadcast to all clients except sender
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except:
        pass
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 10000):
        await asyncio.Future()  # keep alive

if __name__ == "__main__":
    asyncio.run(main())