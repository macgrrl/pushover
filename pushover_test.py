from pushover_complete import PushoverAPI
from PushoverConfig import PushoverConfig

pc = PushoverConfig()
pc.read()

papi = PushoverAPI(pc.app_key)
papi.send_message(pc.user_key, 'This is a test', title='Pythonista')

