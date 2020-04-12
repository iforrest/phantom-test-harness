import pprint


class ActionResult():
    def __init__(self, param=None):
        self.param = param
        self.message = ''
        self.status = False
        self.data = []
        self.summary = {}
        self.logger = None
        self.pp = pprint.PrettyPrinter(indent=4)
        return

    def set_logger(self, logger):
        self.logger = logger

    def get_message(self):
        return self.message

    def set_status(self, status, message=None, error=None):
        self.status = status
        self.message = message
        self.logger.info('ActionResult.set_status() - Status: {}; Message: {}; Exception: {}'.format(status, message, str(error)))
        return status

    def add_data(self, data):
        self.data.append(data)
        self.logger.info('ActionResult.add_data() - Data (next line):\n{}'.format(self.pp.pformat(self.data)))
        return

    def get_data(self):
        return self.data

    def update_summary(self, summary):
        self.summary = summary
        self.logger.info('ActionResult.update_summary() - Summary (next line):\n{}'.format(self.pp.pformat(summary)))
        return self.summary

    def set_summary(self, summary):
        self.update_summary(summary)
        return

    def get_status(self):
        return self.status
