#ubuntu install gettext<br>
<code>sudo apt install gettext</code>

locale -a

#mkdir<br>
<code>mkdir -p translations/zh_TW/LC_MESSAGES/</code><br>
<code>mkdir -p translations/en_US/LC_MESSAGES/</code>

#make pot file<br>
<code>find . -iname "*.py" | xargs xgettext --from-code=utf-8 -o messages.pot</code><br>
<code>sed -i 's/charset=CHARSET/charset=UTF-8/g' messages.pot</code>

#make po file<br>
<code>msginit --no-translator --input=messages.pot --locale=zh_TW.utf8 -o translations/zh_TW/LC_MESSAGES/messages.po</code><br>
<code>msginit --no-translator --input=messages.pot --locale=en_US.utf8 -o translations/en_US/LC_MESSAGES/messages.po</code>

#make mo file<br>
<code>msgfmt translations/zh_TW/LC_MESSAGES/messages.po -o translations/zh_TW/LC_MESSAGES/messages.mo</code><br>
<code>msgfmt translations/en_US/LC_MESSAGES/messages.po -o translations/en_US/LC_MESSAGES/messages.mo</code>
