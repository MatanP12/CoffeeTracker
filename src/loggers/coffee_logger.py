import logging
from pythonjsonlogger.json import JsonFormatter

json_formater = JsonFormatter('%(levelname)s : %(name)s : %(message)s : %(asctime)s', datefmt="%d-%m-%Y %H:%M:%S")

coffee_logger = logging.getLogger("coffee_creation")
coffee_logger.setLevel(logging.INFO)
coffee_handler= logging.FileHandler("./logs/coffee.log")
coffee_handler.setFormatter(json_formater)
coffee_logger.addHandler(coffee_handler)

program_logger = logging.getLogger()
file_handler = logging.FileHandler("logs/app.log")
stream_handler = logging.StreamHandler()
file_handler.setFormatter(json_formater)
program_logger.addHandler(file_handler)
# program_logger.addHandler(stream_handler)

# logging.basicConfig(
#     level=logging.INFO,  # Set the logging level
#     format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
#     handlers=[
#         file_handler,
#         stream_handler
#     ]
# )


