from drivers.singleton import MetaSingleton
import vk_api
import logging


class VKConnect(metaclass=MetaSingleton):
    vk = None
    session = None

    def connect(self, context=None):
        if context is None and self.vk is None:
            return None
        if self.vk is None:
            logging.debug('Initialize VKConnect driver')
            self.session = vk_api.VkApi(token=context['config'].get('settings', 'access_token'))
            #self.vk = self.session.get_api()
            #logging.debug(self.vk.users.get())
        return self.session
