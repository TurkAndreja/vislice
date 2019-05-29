% import model
% rebase ("base.tpl", title = "Vislice")

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <h2>{{igra.pravilni_del_gesla()}}</h2>

  Nepravilne črke : {{igra.nepravilni_ugibi()}}

  % preostali_poskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1
  Število preostalih poskusov: {{preostali_poskusi}}   <!--spremenljivke v htmlju pišeš v dvakrat zavitih oklepajih, za % pa je python koda in lahko definiraš spremenljivke. Ker je to template, moraš zaključit z end, da ve, kdaj nehati  -->
  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">
 


% if poskus == model.ZMAGA:
    <h2> ZMAGA! </h2>

      <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
      </form>


%elif poskus == model.PORAZ:
    <h2> Poraz! </h2>
    Pravilno geslo je {{igra.geslo}}.

      <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
      </form>


%else:
  <form action="/igra/" method="post">
    Črka: <input type = "text" name = "crka">
    <button type="submit">Pošlji ugib!</button>
  </form>

% end 
