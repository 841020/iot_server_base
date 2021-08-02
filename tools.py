import gettext


def switch_locale(locale=None):
    locale_map = {
        'en': gettext.translation('messages', localedir='./translations', languages=['en']),
        'zh': gettext.translation('messages', localedir='./translations', languages=['zh'])
    }
    language = locale_map.get(locale, 'en')
    language.install()
