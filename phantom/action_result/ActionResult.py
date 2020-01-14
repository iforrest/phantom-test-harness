import pprint


class ActionResult():
    def __init__(self, param=None):
        self.param = param
        self.message = ''
        self.state = False
        self.data = []
        self.summary = {}
        self.logger = None
        self.pp = pprint.PrettyPrinter(indent=4)
        return

    def set_logger(self, logger):
        self.logger = logger

    def get_message(self):
        return self.message

    def set_status(self, state, message=None, error=None):
        self.state = state
        self.message = message
        self.logger.info('ActionResult.set_status() - State: {}; Message: {}; Exception: {}'.format(state, message, str(error)))
        return

    def add_data(self, data):
        self.data.append(data)
        self.logger.info('ActionResult.add_data() - Data (next line):\n{}'.format(self.pp.pformat(self.data)))
        return

    def update_summary(self, summary):
        self.summary = summary
        self.logger.info('ActionResult.update_summary() - Summary (next line):\n{}'.format(self.pp.pformat(summary)))
        return

    def set_summary(self, summary):
        self.update_summary(summary)
        return

    def get_status(self):
        return self.state
