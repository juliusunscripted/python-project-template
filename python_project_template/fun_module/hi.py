import structlog

log = structlog.stdlib.get_logger()


def huhu():
    log.info("huhu")
