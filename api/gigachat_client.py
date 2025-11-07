# from gigachat import GigaChat
from gigachat import GigaChatAsyncClient
from asgiref.sync import sync_to_async
import os


# Установите переменную окружения: export GIGACHAT_CREDENTIALS="<ваш_токен>"
client = GigaChatAsyncClient(credentials=os.getenv("GIGACHAT_AUTH_KEY"),
                             verify_ssl_certs=False)

async def get_gigachat_response_async(prompt: str) -> str:
    try:
        response = await client.achat(prompt)
        return response.choices[0].message.content
    except Exception as e:
        return f"!Ошибка GigaChat: {str(e)}"

# get_gigachat_response_async = sync_to_async(get_gigachat_response)