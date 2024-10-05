from app.message import Message

class IMessageParser:

    def parse_message(data: str) -> Message:
        pass