#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#  
from flask import g
from modele import *
from baza import *
from views import *
import os
from pathlib import Path

app.config.update(dict(
    SECRET_KEY='bardzotajnyklucz',
    TITLE='Czat'
))
# DATABASE=os.path.join(app.root_path, baza_nazwa)
@app.before_request
def before_request():
    g.db = baza
    g.db.connect(reuse_if_open=True)

@app.after_request
def after_request(response):
    g.db.close()
    return response

if __name__ == '__main__':
    sciezka_baza = os.path.abspath("./" + baza_nazwa)

    if not os.path.exists(sciezka_baza):
        Path(sciezka_baza).touch()

        db = baza
        db.connect(reuse_if_open=True)

        db.create_tables([Kategoria, Pytanie, Odpowiedz])

        dane = {
            Kategoria: 'kategorie',
            Pytanie: 'pytania',
            Odpowiedz: 'odpowiedzi',
        }

        dodaj_dane(dane)

        db.commit()
        db.close()

    app.run(debug=True)
    
    
