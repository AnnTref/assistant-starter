from config.config import URL
import time
import httpx


def get_data(
    client: httpx.Client,
    service_name: str,
    url: str,
) -> None:
    print(f"Запрос '{service_name}': начало")
    response = client.get(url)
    response.raise_for_status()
    print(f"Запрос '{service_name}': завершен (статус {response.status_code}, "
          f"длина тела {len(response.text)} символов, "
          f"кодировка ответа {response.encoding})")


def main() -> None:
    with httpx.Client(timeout=10) as client:
        get_data(client, 'user-agent', URL['user-agent'])
        get_data(client, 'headers', URL['headers'])
        get_data(client, 'delay', URL['delay'])


start = time.perf_counter()
main()

timer = time.perf_counter() - start
print(f"{timer:.5f} seconds")