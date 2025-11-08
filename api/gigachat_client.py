import os

from gigachat import GigaChatAsyncClient

client = GigaChatAsyncClient(credentials=os.getenv("GIGACHAT_AUTH_KEY"),
                             verify_ssl_certs=False)


async def get_gigachat_response_async(prompt: str) -> str:
    try:
        response = await client.achat(prompt)
        return response.choices[0].message.content
    except Exception as e:
        return f"!Ошибка GigaChat: {str(e)}"
