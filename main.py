from kivmob import KivMob, TestIds

from kivy.app import App
from kivy.uix.label import Label

class BannerTest(App):
    """ Displays a banner ad at top of the screen.
    """

    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        return Label(text='Banner Ad Demo')

if __name__ == "__main__":
    BannerTest().run()
