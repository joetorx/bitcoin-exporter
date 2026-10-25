# Copyright (c) 2025 Joel Torres
# Distributed under the MIT License. See the accompanying file LICENSE.

import os
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

def create(logger_name):

    logging_level = logging.INFO

    log_file = f"{logger_name.split('.')[1]}.log"
    log_dir = Path(".").parent / "logs"
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)
    logger_format = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s - %(message)s")

    file_handler = RotatingFileHandler(Path.joinpath(log_dir, log_file), maxBytes=10000000, backupCount=3)
    file_handler.setFormatter(logger_format)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logger_format)
    logger.addHandler(console_handler)

    return logger
