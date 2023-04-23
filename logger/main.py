import logging
from logger.enums import lavels
from datetime import datetime
import sys
import json
import inspect


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
        msg = self._format_message(message, "INFO")
        logging.info(json.dumps(msg))

    def error(self, message):
        msg = self._format_message(message, "ERROR")
        logging.error(json.dumps(msg))
    
    def warning(self, message):
        msg = self._format_message(message, "WARNING")
        logging.warning(msg)

    def metrics(self, name, value):
        msg = self._format_metric(name, value)
        logging.info(json.dumps(msg))

    def _format_message(self, message:any, lavel: str) -> dict:
        trace_file = inspect.stack()[2].filename 
        trace_line = inspect.stack()[2].lineno
        return {
            "lavel":lavel,
            "trace":f"{trace_file} line {trace_line}",
            "message": str(message)
        }

    def _format_metric(self, name, value) -> dict:
        return {
            "lavel":f"{self.lavel}",
            "time": str(datetime.now()),
            name: value  
        }
