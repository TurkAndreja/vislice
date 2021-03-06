import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'u:\\Programiranje\\SSH\\vislice\\views')
    #tole je pomoč, če ti niti index.tpl niti celotno pot ne prepozna pri returnu pri bottle. get
    #greš na google bottle template not found in stack overthrow in ti tam pokaže tole zgoraj, da skopiraš sem samo do views, spodaj pa napišeš samo ime te določene mape
    #to bo delalo samo na tem računalniku, ker tu taka pot
    #doma, če tole začasno rešitev zakomentiraš in imaš index v vislicah in samo index.tpl spodaj pri return napišeš, bi moralo delati

# vislice = model.Vislice()
# id_testne_igre = vislice.nova_igra()
# vislice.ugibaj(id_testne_igre, "A")

SKRIVNOST = "pssst, moja skrivnost"
DATOTEKA_S_STANJEM = 'u:\\Programiranje\\SSH\\vislice\\stanje.json'
DATOTEKA_Z_BESEDAMI = 'u:\\Programiranje\\SSH\\vislice\\besede.txt'
vislice = model.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_Z_BESEDAMI)

@bottle.get("/")
def index():
    return bottle.template("index.tpl") #najprej te vrže na to stran in ko klikneš nova igra tu te vrne na drugo stran - tole spodaj bottle.get

@bottle.get("/igra")
def testna_igra():
    return bottle.template("igra.tpl", igra = vislice.igre[id_testne_igre][0], id_igre = id_testne_igre, poskus = vislice.igre[id_testne_igre][1])

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret = SKRIVNOST, path = "/")
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret = SKRIVNOST)
    return bottle.template("igra.tpl", igra = vislice.igre[id_igre][0], id_igre = id_igre, poskus = vislice.igre[id_igre][1])

@bottle.post("/igra/")
def ugibaj():
    #igra = vislice.igre[id_igre][0] ne rabim
    id_igre = bottle.request.get_cookie("id_igre", secret = SKRIVNOST)
    crka_za_ugib = bottle.request.forms.getunicode("crka") #tole crko potem pokličeš v igra.tpl, zato mora bti isto napisana; za šumnike
    vislice.ugibaj(id_igre, crka_za_ugib)
    bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture, root = "u:\\Programiranje\\SSH\\vislice\\img") #tu načeloma dovolj samo "img", tole spet samo na tem računalniku dela in namesto views moraš napisati img

bottle.run(reloader=True, debug=True)