from loguru import logger
import os
from core.config import load_config

cfg = load_config()

log_path = cfg["logging"]["filepath"]
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logger.add(log_path, rotation="1 MB", retention="10 days")
