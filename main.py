import kivy
kivy.require('1.0.6')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty


class Picture(Scatter):
    source = StringProperty(None)


class PicturesApp(App):

    def build(self):

        # корень создается в pictures.kv
        root = self.root

        # получать любые файлы в директорию изображения
        curdir = dirname(__file__)
        for filename in glob(join(curdir, 'images', '*')):
            try:
                # Загрузка изображения
                picture = Picture(source=filename, rotation=randint(-30, 30))
                # Добавление основного поля
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

    def on_pause(self):
        return True


if __name__ == '__main__':
    PicturesApp().run()
