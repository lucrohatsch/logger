import logging
from logger.enums import lavels
from datetime import datetime
import sys



class Logger():
    def __init__(self, lavel='debug'):
        self.lavel = lavels.get(lavel.lower())
        logging.basicConfig(level=self.lavel, format='%(message)s', stream=sys.stdout)
        
        msg = {
            "lavel":"info",
            "time": str(datetime.now()),
            "message": f"Starting logger in {lavel.upper()} mode"
        }
        logging.info(msg)        


    def info(self, message:any):
        msg = self._format_message(message)
        logging.info(msg)

    def error(self, message):
        msg = self._format_message(message)
        logging.error(msg)
    
    def warning(self, message):
        msg = self._format_message(message)
        logging.warning(msg)

    def metrics(self, name, value):
        msg = self._format_metric(name, value)
        logging.info(msg)

    def _format_message(self, message:any) -> dict:
        return {
            "lavel":f"{self.lavel}",
            "time": str(datetime.now()),
            "message": str(message)
        }

    def _format_metric(self, name, value) -> dict:
        return {
            "lavel":f"{self.lavel}",
            "time": str(datetime.now()),
            "metric": {
                name: value 
            } 
        }
