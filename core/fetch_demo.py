from config.config import URL
import time
import asyncio
import httpx


async def async_get_data(
    client: httpx.AsyncClient,
    service_name: str,
    url: str,
) -> None:
    print(f"Запрос '{service_name}': начало")
    response = await client.get(url)
    response.raise_for_status()
    print(f"Запрос '{service_name}': завершен (статус {response.status_code}, "
          f"длина тела {len(response.text)} символов, "
          f"размер тела {len(response.content)} байт)")


async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        await asyncio.gather(
            async_get_data(client, 'user-agent', URL['user-agent']),
            async_get_data(client, 'headers', URL['headers']),
            async_get_data(client, 'delay', URL['delay']),
        )


start = time.perf_counter()
asyncio.run(main())

timer = time.perf_counter() - start
print(f"{timer:.5f} seconds")