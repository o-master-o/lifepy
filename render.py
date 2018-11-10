import pprint as pp


class Renderer(object):

    def __init__(self, rendering_method):
        self._RENDERING_METHODS = {'list_renderer': self.list_renderer,
                                   'text_renderer': self._text_renderer}
        self._method = self._RENDERING_METHODS.get(rendering_method)

    def draw_world(self, map_):
        self._method(map_)

    def list_renderer(self, map_):
        pp.pprint(map_)

    def _text_renderer(self, map_):
        pass