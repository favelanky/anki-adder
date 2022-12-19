import json

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0",
           "Content-Type": "application/json; charset=UTF-8"
           }


class ReversoContextAPI():
    """
    Class for Reverso Context API (https://context.reverso.net/)

    Reference:
        https://github.com/demian-wolf/pyreverso
    Attributes:
        supported_langs
        source_text
        target_text
        source_lang
        target_lang
        total_pages
    Methods:
        get_translations()
        get_examples()
        swap_langs()
    """

    def __init__(self,
                 source_lang='en',
                 target_lang='ru') -> None:
        self._sentence = None
        self._source_lang = source_lang
        self._target_lang = target_lang
        self._supported_langs = self.__get_supported_langs()

    @staticmethod
    def __get_supported_langs() -> dict:
        """
        Copied code

        Returns:
            {'source_lang' : tuple, 'target_lang': tuple}
        """
        supported_langs = {}

        response = requests.get("https://context.reverso.net/translation/",
                                headers=HEADERS)

        soup = BeautifulSoup(response.content, features="lxml")

        src_selector = soup.find("div", id="src-selector")
        trg_selector = soup.find("div", id="trg-selector")

        for selector, attribute in ((src_selector, "source_lang"),
                                    (trg_selector, "target_lang")):
            dd_spans = selector.find(class_="drop-down").find_all("span")
            langs = [span.get("data-value") for span in dd_spans]
            langs = [lang for lang in langs
                     if isinstance(lang, str) and len(lang) == 2]

            supported_langs[attribute] = tuple(langs)

        return supported_langs

    @property
    def sentence(self):
        return self._sentence

    @property
    def source_lang(self):
        return self._source_lang

    @property
    def target_lang(self):
        return self._target_lang

    @sentence.setter
    def sentence(self, value):
        self._sentence = value

    @source_lang.setter
    def source_lang(self, value):
        self._source_lang = value

    @target_lang.setter
    def target_lang(self, value):
        self._target_lang = value

    def get_synonyms(self) -> [str, ]:
        """Give list of synonyms"""
        url = f"https://synonyms.reverso.net/synonym/{self._source_lang}/{self.sentence}"
        soup = self.response(url)
        synonyms = soup.find_all(class_="synonym relevant")
        return [synonym.text for synonym in synonyms]

    def get_translation(self) -> ([str, ], [str, ]):
        """Returns tuple: translations array and example"""
        assert self._source_lang == 'en' and self._target_lang == 'ru', "unsupported languages"

        url = f'https://context.reverso.net/translation/english-russian/{self.sentence}'
        soup = self.response(url)
        translation = soup.find_all(class_="display-term")
        examples = soup.find_all(class_="src ltr")
        return [tr.text for tr in translation], [ex.text[13:-2] for ex in examples]

    def response(self, url) -> BeautifulSoup:
        """Returns html page"""
        response = requests.get(url=url, headers=HEADERS)
        return BeautifulSoup(response.text, "html.parser")


var = ReversoContextAPI(source_lang="en", target_lang="ru")
var.sentence = "leeched"
print(var.get_synonyms())
print(var.get_translation())
