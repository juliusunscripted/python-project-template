# %%
# !%load_ext autoreload
# !%autoreload 1

# !%aimport python_project_template.fun_module.hi

# %%

import structlog
import time
from python_project_template.fun_module import hi
from python_project_template.utils import structlog_utils

structlog_utils.configure_structlog()

log = structlog.stdlib.get_logger()

# %%

hi.huhu()

# %%
