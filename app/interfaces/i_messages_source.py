class IMessageSource:

    async def next_message() -> str:
        raise NotImplementedError