import gettext


def switch_locale(locale=None):
    locale_map = {
        'en': gettext.translation('messages', localedir='./translations', languages=['en']),
        'zh': gettext.translation('messages', localedir='./translations', languages=['zh'])
    }
<<<<<<< HEAD
    language = locale_map.get(locale, 'en')
=======
    language = locale_map.get(locale, locale_map['en'])
>>>>>>> 1166516ec8718379f74d4d76ffe18d0d52dd6146
    language.install()
