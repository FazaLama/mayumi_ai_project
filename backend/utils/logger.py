import logging
import os
from datetime import datetime


class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        filename = datetime.now().strftime("%Y-%m-%d") + ".log"

        path = os.path.join("logs", filename)

        self.logger = logging.getLogger("Mayumi")

        if not self.logger.handlers:

            self.logger.setLevel(logging.INFO)

            handler = logging.FileHandler(
                path,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "[%(asctime)s] %(message)s",
                datefmt="%H:%M:%S"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    def info(self, text):

        self.logger.info(text)