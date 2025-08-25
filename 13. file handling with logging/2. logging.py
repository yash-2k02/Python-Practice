import logging

logging.basicConfig(
    filename='files/mylogfile.log',
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    filemode='a'
)

logging.debug("Debugging issue")
logging.info("Starting process")
logging.warning("Low disk space")
logging.error("An error occurred")
logging.critical("System failure")
