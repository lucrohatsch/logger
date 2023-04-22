import logging
from logger.enums import lavels
from datetime import datetime



class Logger():
    def __init__(self, lavel='debug'):
        self.lavel = lavels.get(lavel.lower())
        logging.basicConfig(level=self.lavel)
        msg = {
            "lavel":"info",
            "time": str(datetime.now()),
            "message": f"Starting logger in {lavel.upper} mode"
        }
        logging.info(msg)        


    def info(self, message:any):
        msg = self._format_message(message)
        logging.info(msg)

    def error(self, message):
        msg = self._format_message(message)
        logging.error(msg)

    def _format_message(self, message:any) -> dict:
        return {
            "lavel":f"{self.lavel}",
            "time": str(datetime.now()),
            "message": str(message)
        }

