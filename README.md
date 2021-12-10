# atsproxy

## Descrizione

è un proxy verso rentman che implementa la politica CORS.

questo permette di fare chiamate alle api di rentman (api.rentman.net) da un'altro sito (tipo ats.rentmanapp.com).

in questo modo si può implementare una webapp per gestire rentman.

## Installazione

1) creare una app su heroku e copiarci dentro questa repository
2) nelle variabili globali di heroku aggiungere una variabile con nome:"BEARER", e valore:_TOKEN_DI_RENTMAN_
3) dalla webapp fare uyna qualunque chiamata come si farebbe a api.rentman.net, ma sostituendo l'url iniziale Es. appname.herokuapp.com/contacts?distance[lte]=300
