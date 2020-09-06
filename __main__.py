"""
This program prints "Hello World!". Printer and ink not included.
"""

import bs4, tempfile, time, os, urllib.request, webbrowser

PRINT_TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
        <title>PyConAU 2020 – A Rude Codeberg entry</title>
    </head>
    <body>
        <h1></h1>
        <div>
            <img src="https://2020.pycon.org.au/assets/build/Curlyboi.2ac78b14.svg"></img>
        </div>
        <script>
            window.print();
        </script>
    </body>
</html>
"""

class Printer:
    @staticmethod
    def print(text: str):
        # Populate the template.
        html = bs4.BeautifulSoup(PRINT_TEMPLATE)
        html.h1.append(text)

        # We'll need a file.
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html') as file:
            file.write(str(html))
            file.flush()

            # Let's open the file.
            url = 'file:{}'.format(urllib.request.pathname2url(os.path.abspath(file.name)))
            webbrowser.open(url)

            # We should hang around while the file is opened.
            time.sleep(10)

class Greeting:
    def __init__(self, prefix: str, entity: str) -> None:
        self.prefix = prefix
        self.entity = entity

    def __str__(self) -> str:
        return '{prefix} {entity}!'.format(prefix=self.prefix, entity=self.entity)

class World:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def greet(self, prefix: str) -> None:
        Printer.print(str(Greeting(prefix, str(self))))


if __name__ == '__main__':
    world = World(name='world')
    world.greet('Hello')
