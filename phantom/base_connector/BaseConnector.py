import os
import logging
import pprint
import sys
import phantom.app as phantom
import json


class BaseConnector(object):
    def __init__(self):
        # asset configuration settings
        self.config = {}

        # other asset settings
        self.asset_id = '1abc234'

        # app settings
        self.app_id = '1abc1234'
        self.app_json_file_loc = None

        # log settings
        self.log_path = 'debug_log.log'
        self.log_to_console = True
        self._setup_logger()

        # current container settings
        self.container_id = 1
        # the following is an example
        self.container_info = {
            '1': {'container_info_would_go_here': True},
            '2': {'container_info_would_go_here': True}
        }
        # used when saving containers
        self.starting_container_id = 2

        # artifact settings
        self.starting_artifact_id = 1

        # product information settings
        self.product_install_id = '1234'
        self.product_version = '4.5.15370'

        # state settings
        self.state_file_location = 'state_file'

        # polling settings
        self.poll_now = False

        # baseurl
        self.base_url = 'https://127.0.0.1'

        # internal trackers
        self.message = ''
        self.progress_message = ''
        self.state = None
        self.status = None
        self.action_results = []
        self.pp = pprint.PrettyPrinter(indent=4)
        self.action_identifier = ''

        return

    def _setup_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(name)s %(levelname)s %(message)s',
            filename=(self.log_path or 'debug_log.log'),
            filemode='a'
        )
        self.logger = logging.getLogger(__name__)

        # Add console output if configured
        if self.log_to_console:
            console = logging.StreamHandler(sys.stdout)
            console.setLevel(logging.INFO)
            console.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
            self.logger.addHandler(console)

    def _config_parser_to_dict(self, config_parser):
        return {s: dict(config_parser.items(s)) for s in config_parser.sections()}

    def get_config(self):
        return self.config

    def get_phantom_base_url(self):
        return self.base_url

    def get_container_id(self):
        return self.container_id

    def get_container_info(self, container_id=None):
        if not container_id:
            container_id = self.container_id
        return True, self.container_info[container_id], '200'

    def get_product_installation_id(self):
        return self.product_install_id

    def get_product_version(self):
        return self.product_version

    def load_state(self):
        with open(self.state_file_location, 'r+') as state_file:
            self.state = json.loads(state_file.read() or '{}')
        self.logger.info('load_state() - State: {}'.format(self.pp.pformat(self.state)))
        return self.state

    def get_state(self):
        return self.state

    def save_state(self, state=None):
        self.state = (state or self.state)
        with open(self.state_file_location, 'w+') as state_file:
            state_file.write(json.dumps(self.state))
        self.logger.info('save_state() - State: {}'.format(self.pp.pformat(self.state)))
        return

    def save_artifact(self, artifact):
        artifact_id = self.starting_artifact_id
        self.starting_artifact_id += 1
        return (phantom.APP_SUCCESS, 'Artifact saved', artifact_id)

    def save_artifacts(self, artifacts):
        return_val = []
        for artifact in artifacts:
            return_val.append([phantom.APP_SUCCESS, 'Artifact saved', self.starting_artifact_id])
            self.starting_artifact_id += 1

        return return_val

    def save_container(self, container):
        container_id = self.container_artifact_id
        self.starting_container_id += 1
        return (phantom.APP_SUCCESS, 'Container saved', container_id)

    def save_containers(self, containers):
        return_val = []
        for container in containers:
            return_val.append([phantom.APP_SUCCESS, 'Container saved', self.starting_container_id])
            self.starting_container_id += 1

        return return_val

    def debug_print(self, message, dump_obj=None):
        self.logger.debug('BaseConnector.debug_print - Message: {}; Object (next line):\n{}'.format(message, (self.pp.pformat(dump_obj) if dump_obj else '')))
        return

    def set_status(self, status, message=None, error=None):
        self.status = status
        self.message = message
        self.logger.info('BaseConnector.set_status - State: {}; Message: {}; Exception: {}'.format(status, message, str(error)))
        return status

    def append_to_message(self, message):
        self.message += message
        self.logger.info('BaseConnector.append_to_message - Message: {}'.format(message))
        return

    def set_status_save_progress(self, status, message):
        self.status = status
        self.progress_message = message
        self.logger.info('BaseConnector.set_status_save_progress - Status: {}, Message: {}'.format(status, message))
        return self.status

    def send_progress(self, message):
        self.progress_message = message
        self.logger.info('BaseConnector.send_progress - Progress: {}'.format(message))
        return

    def save_progress(self, message, more=None):
        self.progress_message = message
        self.logger.info('BaseConnector.save_progress - Progress: {}; More: {}'.format(message, more))
        return

    def add_action_result(self, action_result):
        action_result.set_logger(self.logger)
        self.action_results.append(action_result)
        return action_result

    def get_status(self):
        return self.status

    def get_status_message(self):
        return self.message

    def get_action_identifier(self):
        return self.action_identifier

    def is_poll_now(self):
        return self.poll_now
    
    def get_app_id(self):
        return self.app_id

    def get_asset_id(self):
        return self.asset_id
        
    def set_validator(self, type=None, validation_function=None):
        # TODO: Make this do something. For now, it does nothing
        return None