from app.message import Message
from app.interfaces.i_messages_source import IMessageSource

class IMessageParser:

    async def parse_message(source: str) -> Message:
        raise NotImplementedError