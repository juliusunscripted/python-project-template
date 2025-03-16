# run this python file in vscode via the play button on the top right (in case python extension is installed)
# or use the following command (be sure .venv is actived (should be activated automatically))
# python -m python_project_template.scripts.dev_01_simple_script
import structlog
import time
from python_project_template.fun_module import hi
from python_project_template.utils import structlog_utils

structlog_utils.configure_structlog()

log = structlog.stdlib.get_logger()


def main():

    log.info("press ctrl + c to stop the script")
    for i in range(100):
        log.info("hi", i=i)
        # the following command run a method from the improted hi module ;)
        hi.huhu()
        time.sleep(1.5)


if __name__ == "__main__":
    main()
