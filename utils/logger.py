import logging

class LoggerUtils:
    def __init__(self):
         
        self.log = logging.basicConfig(
            filename="app.log",
            filemode="w",  # Overwrites the file each run; use 'a' to append
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    def 
    logging.debug("Diagnosing structural steps.")
    logging.info("System operational sequence cleared.")
    logging.warning("Memory usage exceeds reference index.")
