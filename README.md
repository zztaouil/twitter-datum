```
accounts = [
    "fm6oaorg",
    "MmedHamdaoui",
    "osekguub6096Gwf",
    "habousmaroc",
    "MarocDiplo_AR",
    "nosraorg",
    "USAbilAraby",
    "AIPACofficial",
    "TuckerCarlson",
    "SecRubio",
    "WhiteHouse",
    "CUFI",
    "TheIRD",
    "StateDept",
    "USIPorg",
    "Franklin_Graham",
    "SpeakerJohnson",
    "GovMikeHuckabee",
    "RTErdogan",
    "DiyanetDijital",
    "Tika_Turkiye",
    "mfa_russia",
    "KremlinRussia_E",
    "patriarchia_ru",
    "mospat_ru",
    "ar_khamenei",
    "IRIMFA_EN",
    "netanyahu",
    "IsraelMFA",
    "IsraelinUSA",
    "EdyCohen",
    "IsraeliPM",
    "IDF",
    "itamarbengvir",
    "bezalelsm",
    "Pontifex_ar",
    "vaticannews_fr",
    "AlAzhar",
    "alimamaltayeb",
]

```

il faut extraire des données qui permettent de cartographier :

1.⁠ ⁠les nœuds = les comptes,
2.⁠ ⁠les liens = abonnements, mentions, Re-posts, réponses, citations,
3.⁠ ⁠les contenus = textes, hashtags, liens, médias,
4.⁠ ⁠la temporalité = quand et à quel rythme le discours circule,
5.⁠ ⁠l’impact = engagement, diffusion, centralité, polarisation.

---

### Premiere exploration

Elle a pour but de construire un proof of concept pour le graph

On va partir sur 10 tweets plus recent de nos target, extraire 50 reply et mapper le graph.
Les profils sont des noeuds les liens sont des reponses.

```
- get 10 tweet of an account
- for each tweet get 50 reply (skip RT tweet)
- save reply authors 
```

cette exploration a aboutit à une definition de scenario d'extraction.

scenario alpha extrait les tweets et réponses d'un compte target, checker le lien des réponses et les re-posts.


#### Notes
For large scale extraction.
- we have to study how rate limits works.
- how much do our workflows cost
- setup db to persist data and enrich it gradually
- Re explore the data extraction of one twitter account

25% pourcentage pour que la donées soit valide/representative

---

- most used words ; communication
- topic moddeling + co occurence ; theme 
- sentiment analysis ; impact


---

  1. الله                      771
  2. أمريكا                    582
  3. اليوم                     516
  4. الشعب                     501
  5. العالم                    494
  6. الإسلامية                 488
  7. إيران                     467
  8. الإسلامي                  391
  9. الإيراني                  373
 10. الصهيوني                  363
 11. الكيان                    351
 12. الإمام                    303
 13. العدو                     299
 14. لكن                       288
 15. يجب                       288
 16. فلسطين                    279
 17. المنطقة                   244
 18. الناس                     243
 19. البلاد                    242
 20. المقاومة                  230

[الشعب, إيران, الإيراني,الناس,البلاد]
[الله, الإسلامية, الإسلامي, الإمام]
[أمريكا, العالم, الصهيوني, العدو, فلسطين, المقاومة, المنطقة]