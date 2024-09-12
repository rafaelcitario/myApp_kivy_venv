from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.tools.coverage import Coverage

class LoginScreen(GridLayout):



  def callback(self, instance):
    if self.linkField.text == 'Cole o Link do Youtube aqui':
      instance.text = 'BAIXAR MP3'

    instance.disabled = True
    instance.text = 'BAIXANDO...'
    instance.background_color = '#f0f0f0'
    instance.color = '#000000'

  def enableDownloadButton(self, instance, value):
    if self.downloadButton.disabled == True:
      instance.text = 'Cole o Link do Youtube aqui'
      self.downloadButton.disabled = False
      self.downloadButton.text = 'BAIXAR MP3'
      self.downloadButton.background_color = '#c7eeaa'
      self.downloadButton.color = '#ffffff'

    instance.text = ''

  def __init__(self, **kwargs):
    super(LoginScreen, self).__init__(**kwargs)

    self.cols = 1
    self.padding = 10
    self.spacing = 10
    self.width = 480
    self.height = 850

    self.canvas.add(Color(1, 1, 1, 1))

    self.imageBackground = Image(
      size = (480, 853),
      pos = (0, 0),
      source='./images/image.png',
      fit_mode = "cover",
    )

    self.linkField = TextInput(
        text = 'cole o link do Youtube aqui',
        multiline=False,
        size_hint=(1, .1),
        padding_y = (10, 10),
        font_size = "20sp",
        on_touch_down = self.enableDownloadButton
        )


    self.downloadButton = Button(
        text='Baixar MP3',
        size_hint=(1, .09),
        color = "#ffffff",
        background_color = "#c7eeaa",
        on_press = self.callback
      )


    Widget.bind(self.downloadButton)
    Widget.bind(self.linkField)
    self.add_widget(self.imageBackground)
    self.add_widget(self.linkField)
    self.add_widget(self.downloadButton)



class DownloadMP3FromYoutube(App):
  def build(self):
    return LoginScreen()

if __name__ == '__main__':
  DownloadMP3FromYoutube().run()
