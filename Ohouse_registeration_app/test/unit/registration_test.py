import jsonrpclib
from testtools import *
import unittest

CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/configuration/'
KEYS_PATH = os.path.dirname(os.path.realpath(__file__)) + '/keys/'

class TestRegApp(unittest.TestCase):

    def test_register_with_given_public_key(self):
        server_ip, server_port = get_server_conf('registration_app_config.json')
        server = jsonrpclib.Server('http://%s:%s' % (server_ip, server_port))
        first_name = 'TestFirstName1'
        last_name = 'TestLastName1'
        user_name = 'test_username1'
        email = 'test1@test.de'
        public_key_value = '-----BEGIN PUBLIC KEY-----\n'\
                           'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDeKDzrXDtK/n/9maxvNBDXBM3f\n'\
                           'Z4JE9dwZUTNUUrklbsrguQ3Nb6k10yw5Rqz+DKArHUmLY3gjfvC7AWeh6y+VIPdm\n'\
                           'z+HIQLexHRE2ru3gfcUPCfdCUhqFW5nh0h8+lyKvu/k/rTmidSrleyXiDM8p+NuL\n'\
                           'dwOthf/l3hrhoOPUMwIDAQAB\n'\
                           '-----END PUBLIC KEY-----'

        member, key, credentials = server.register_user(first_name,
                                                       last_name,
                                                       user_name,
                                                       email,
                                                       public_key_value)

        return 0 if credentials else 200

    def test_register_without_given_public_key(self):
        server_ip, server_port = get_server_conf('registration_app_config.json')
        server = jsonrpclib.Server('http://%s:%s' % (server_ip, server_port))
        first_name = 'TestFirstName2'
        last_name = 'TestLastName2'
        user_name = 'test_username2'
        email = 'test2@test.de'
        public_key_value, private_key_value = get_ssh_keys(first_name, last_name)

        member, key, credentials = server.register_user(first_name,
                                                       last_name,
                                                       user_name,
                                                       email,
                                                       public_key_value)

        return 0 if credentials else 200


if __name__ == '__main__':
    unittest.main(verbosity=0, exit=True)
