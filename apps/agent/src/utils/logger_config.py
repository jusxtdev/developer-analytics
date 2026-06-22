import logging

def setup_logging():
    logging.basicConfig(
        filename='log.txt',
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
