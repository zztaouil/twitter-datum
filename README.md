```
TARGETS = [
    "fm6oaorg",
    "Saudi_Moia",
    "diyanet_en",
    "h_bennajeh",
    "Ali_AlQaradaghi",
    "realDonaldTrump",
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


25% pourcentage pour que la donées soit valide

---

- most used words ; communication
- topic moddeling + co occurence ; theme
- sentiment analysis ; impact