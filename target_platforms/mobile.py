from . import base
import os

class Mobile(base.Base):
    index_content = '''<!DOCTYPE html>
<html>
<head>
  <link href="https://cdn.jsdelivr.net/npm/vuesax/dist/vuesax.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
</head>
<body>
  <div id="app">
    <vs-button vs-type="filled">Welcome to Raptor!</vs-button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuesax/dist/vuesax.umd.js"></script>
  <script>
    new Vue({
        el: '#app'
    })
  </script>
</body>
</html>   
'''

    def __init__(self, name):
        self.name = name
        self.folders = ['mobile']
        self.files = {
            '/mobile/index.html': self.index_content,
            }

    def create(self):
        for folder in self.folders:
            os.mkdir(folder)
            print('created "{folder}" folder.')
        
        for file in self.files:
            f = open(file, 'x')
            f.write()
            print(f'created "{file}" file.')