import asyncio
from app.parser_service import ParserService

def main():
    service = ParserService()
    asyncio.run(service.run())

if __name__ == '__main__':
    main()