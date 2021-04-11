#ubuntu install gettext
sudo apt install gettext

locale -a

#mkdir
mkdir -p translations/zh_TW/LC_MESSAGES/
mkdir -p translations/en_US/LC_MESSAGES/

#make pot file
find . -iname "*.py" | xargs xgettext --from-code=utf-8 -o messages.pot
sed -i 's/charset=CHARSET/charset=UTF-8/g' messages.pot

#make po file
msginit --no-translator --input=messages.pot --locale=zh_TW.utf8 -o translations/zh_TW/LC_MESSAGES/messages.po
msginit --no-translator --input=messages.pot --locale=en_US.utf8 -o translations/en_US/LC_MESSAGES/messages.po

#make mo file
msgfmt translations/zh_TW/LC_MESSAGES/messages.po -o translations/zh_TW/LC_MESSAGES/messages.mo
msgfmt translations/en_US/LC_MESSAGES/messages.po -o translations/en_US/LC_MESSAGES/messages.mo
