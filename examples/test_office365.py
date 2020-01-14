from ewsonprem_connector import EWSOnPremConnector

email_test = EWSOnPremConnector()
email_test.poll_now = True
email_test.config = {
    'url': 'https://outlook.office365.com/EWS/Exchange.asmx',
    'username': 'matt@testphantom.onmicrosoft.com',
    'password': 'a_password_goes_here',
    'poll_user': 'matt@testphantom.onmicrosoft.com',
    'auth_type': 'basic',
    'poll_folder': 'Inbox',
    'ingest_manner': 'latest first',
    'first_run_max_emails': '10',
    'max_containers': '10',
    'extract_attachments': True,
    'extract_urls': True,
    'extract_ips': True,
    'extract_domains': True,
    'extract_hashes': True,
    'add_body_to_header_artifacts': True,
    'use_impersonation': False
}
email_test.app_id = 'a73f6d32-c9d5-4fec-b024-43876700daa6'
email_test.initialize()

# test poll
email_test.action_identifier = 'on_poll'
email_test.handle_action({'container_count': 10})

# test get_email
email_test.action_identifier = 'get_email'
email_test.handle_action({'id': 'AAMkAGFmNTRhODA4LWIxMjQtNDJjYy05NDM2LWQ5MzY1MGFhMTkzYwBGAAAAAADRlY7ewL4xToKRDciQog5UBwBvUzMoUJx2S4nbgxzZWx2PAAAAAAEMAABvUzMoUJx2S4nbgxzZWx2PAAFEyUC4AAA='})