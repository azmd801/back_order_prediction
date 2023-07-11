import logging 
import os
from datetime import datetime

import logging
import os
from datetime import datetime

logs_dir = os.path.join(os.getcwd(), "logs","app_logs")
os.makedirs(logs_dir, exist_ok=True)

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(logs_dir, log_file)

# Logger for app logs
logs_logger = logging.getLogger("logs")
logs_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

logs_logger.addHandler(file_handler)

# Logger for AI assistant logs

ai_assistant_logs_dir = os.path.join(os.getcwd(), "logs","ai_assistant_logs")
os.makedirs(ai_assistant_logs_dir, exist_ok=True)

ai_assistant_logger = logging.getLogger("ai_assistant_log")
ai_assistant_logger.setLevel(logging.DEBUG)

ai_log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_ai.log"
ai_log_file_path = os.path.join(ai_assistant_logs_dir, ai_log_file)

ai_file_handler = logging.FileHandler(ai_log_file_path)
ai_file_handler.setLevel(logging.DEBUG)
ai_file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

ai_assistant_logger.addHandler(ai_file_handler)


