import gettext


def switch_locale(locale=None):
    locale_map = {
        'en_US': gettext.translation('messages', localedir='./translations', languages=['en_US']),
        'zh_TW': gettext.translation('messages', localedir='./translations', languages=['zh_TW'])
    }
    language = locale_map.get(locale, 'en_US')
    language.install()
