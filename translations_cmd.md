[可以使用 Babel 幫助掃描檔案 但是不要加入 requirement.txt](https://github.com/twtrubiks/Flask-Babel-example)
<<<<<<< HEAD

1.在虛擬環境裝 pybabel[非 docker requirement]
2.add babel.cfg
3.pybabel extract -F babel.cfg -o messages.pot . #.pot init
4.pybabel init -i messages.pot -d translations -l zh # mkdir zh & .po init
5.pybabel init -i messages.pot -d translations -l en # mkdir en & .po init
6.pybabel compile -d translations # init .mo
7.pybabel extract -F babel.cfg -o messages.pot . #update .pot
8.pybabel update -i messages.pot -d translations # update .po
9.pybabel compile -d translations # update .mo
=======
1.install Babel
2.create babel.cfg
3.pybabel extract -F babel.cfg -o messages.pot .
4.pybabel init -i messages.pot -d translations -l zh # mkdir zh and init zh .po  
5.pybabel compile -d translations # .po to .mo
6.pybabel extract -F babel.cfg -o messages.pot . #scan folder
7.pybabel update -i messages.pot -d translations #update .po
8.pybabel compile -d translations # .po to .mo
>>>>>>> 1166516ec8718379f74d4d76ffe18d0d52dd6146

#ubuntu install gettext<br>
<code>sudo apt install gettext</code>

locale -a

#mkdir<br>
<code>mkdir -p translations/zh_TW/LC_MESSAGES/</code><br>
<code>mkdir -p translations/en_US/LC_MESSAGES/</code>

#make pot file<br>
<code>find . -iname "\*.py" | xargs xgettext --from-code=utf-8 -o messages.pot</code><br>
<code>sed -i 's/charset=CHARSET/charset=UTF-8/g' messages.pot</code>

#make po file<br>
<code>msginit --no-translator --input=messages.pot --locale=zh_TW.utf8 -o translations/zh_TW/LC_MESSAGES/messages.po</code><br>
<code>msginit --no-translator --input=messages.pot --locale=en_US.utf8 -o translations/en_US/LC_MESSAGES/messages.po</code>

#make mo file<br>
<code>msgfmt translations/zh_TW/LC_MESSAGES/messages.po -o translations/zh_TW/LC_MESSAGES/messages.mo</code><br>
<code>msgfmt translations/en_US/LC_MESSAGES/messages.po -o translations/en_US/LC_MESSAGES/messages.mo</code>
