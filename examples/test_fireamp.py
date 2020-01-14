from fireamp_connector import FireAMPConnector

amp_test = FireAMPConnector()
amp_test.config = {
    'api_client_id': 'client_id',
    'api_key': 'api_key'
}
param = {'url': 'http://www.google.com'}
amp_test.action_identifier = 'hunt_url'
amp_test.handle_action(param)

amp_test.action_identifier = 'test_asset_connectivity'
amp_test.handle_action({})
