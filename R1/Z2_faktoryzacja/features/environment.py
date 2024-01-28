from behave.model import Scenario
from behave import use_fixture


def before_all(context):
	# -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
	userdata = context.config.userdata
	continue_after_failed = userdata.getbool("runner.continue_after_failed_step", False)
	Scenario.continue_after_failed_step = continue_after_failed