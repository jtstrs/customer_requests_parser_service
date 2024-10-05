from app.interfaces.i_service import IService
from app.interfaces.i_messages_source import IMessageSource

class ParserService(IService):
    def __init__(self, message_source: IMessageSource) -> None:
        self.msg_source = message_source

    async def run(self):
        self.msg_source.next_message()