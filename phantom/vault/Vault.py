import hashlib
import uuid


class Vault():
    TEMP_PATH = None
    VAULT_PATHS = {}

    def __init__(self):
        return

    @classmethod
    def add_attachment(clas, file_location, container_id, file_name=None, metadata=None):
        sha1_hash = None
        with open(file_location, 'r') as vault_file:
            vault_data = vault_file.read()
            sha1_data = hashlib.sha1(vault_data)
            sha1_hash = sha1_data.hexdigest()             

        return {
            'container': container_id,
            'message': 'success',
            'file_name': (file_name or str(uuid.uuid4())),
            'succeeded': True,
            'hash': sha1_hash
        }

    @classmethod
    def create_attachment(cls, file_contents, container_id, file_name=None, metadata=None):
        vault_data = file_contents
        sha1_data = hashlib.sha1(vault_data)
        sha1_hash = sha1_data.hexdigest()

        return {
            'container': container_id,
            'message': 'success',
            'file_name': (file_name or str(uuid.uuid4())),
            'succeeded': True,
            'hash': sha1_hash
        }

    @classmethod
    def get_vault_tmp_dir(cls):
        return '/Users/iforrest/Documents/Dev/vault_tmp'

    @classmethod
    def get_file_path(cls, vault_id):
        return Vault.VAULT_PATHS.get(vault_id)

    # TODO: Implement this
    @classmethod
    def get_file_info(cls, vault_id=None, file_name=None, container_id=None):
        return {}
