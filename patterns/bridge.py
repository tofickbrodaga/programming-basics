# Bridge
# data /--|--|--\ way of processing
# Page (web-page)
# content: str
# TextRenderer

from abc import ABC, abstractstaticmethod
from typing import Optional


class TextRenderer(ABC):
    @abstractstaticmethod
    def render(text: str) -> str:
        pass

class TitleRenderer(TextRenderer):
    @staticmethod
    def render(text: str) -> str:
        return text.title()

class UpperRenderer(TextRenderer):
    @staticmethod
    def render(text: str) -> str:
        return text.upper()

class Page:
    def __init__(self, content: str, renderer: Optional[TextRenderer] = None) -> None:
        self.content, self.renderer = content, renderer
    
    def show_content(self) -> None:
        print(self.renderer.render(self.content) if self.renderer else self.content)

main_page = Page('home page', TitleRenderer)
news_page = Page('news', UpperRenderer)
[page.show_content() for page in (main_page, news_page)]