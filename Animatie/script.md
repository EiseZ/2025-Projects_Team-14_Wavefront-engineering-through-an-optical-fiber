# Script animatie
1. opstelling uitleggen:
- we beginnen met een foto van de opstelling die fade naar een diagram van de opstelling
- zoom in op de optical fiber, manim animatie van hoe dit werkt + uitleg modes, en plaatje speckle pattern
- zoom in op de slm, manim animatie van hoe dit werkt + uitleg concept wavefront shaping, noem ook iets over de applicatie

- stukje over het algoritme, hoe dat werkt, met plaatje uit paper, en mogelijk nog een manim animatie

- Nu een doorloop van de hele opstelling:
- begin met lensen, met een plaatje over hoe een 4f system werkt
- vertel dat de polarisatie nodig is voor een goede werking van de slm
- leg kort uit hoe de beamsplitter
- uitleg over hoe het oculair het licht in en uit de fiber foccused
- de camera laten zien en speckel pattern veranderd als de phases worden aangepast (dus het vinden van een focal spot).

2. Onderzoek uitleggen.
- heel kort praten over wat we gedaan hebben
- resultaten animeren met manim (plots ect....), over resultaten praten en een conclusie geven.
- afsluiten.

## Voice-over tekst
Hier zie je een foto van onze optelling, aan de hand van deze optelling gaan ik je uitleggen wat wij in ons project hebben gedaan.

De glasvezelkabel, een van de centrale delen van de opstellig, bestaat uit twee lagen. Het licht kan op verschillende manieren door de vezel propageren, deze manieren noemen we de modes. Tijdens dit procces wordt het licht op een schijnbaar willekeurige manier verdeelt, waardoor de optelling van alle modes door interferentie een spikkelpatroon vormt - die kun je hier zien.

We zouden graag willen dat dit licht zich op een punt focussed, zodat we deze opstelling kunnen gebruiken als microscoop.

Hiervoor kunnen we een spacial light modulator gebruiken. Wanneer de laser op de pixels van dit scherm valt kan de SLM de phase van het licht per pixel aanpassen. Dit werkt door middel van kristallen die door een voltage toe te passen kunnen worden gedraaid, waardoor de padlengte van het licht veranderd. We kunnen nu per mode in de fiber de phase aanpassen, waardoor door interferentie ook het uitgaande patroon veranderdt.

Door de pixels op de SLM aan te passen kunnen we bijvoorbeeld het licht op een punt focussen. Het algoritme dat wij hebben gebruikt deelt de SLM op in delen, segmenten genaamt. Voor elk segment veranderen we de phase. Daarna kiezen we de phase die ons het dichtste bij de gewenste patroon brengt - in ons geval is dat de phase waarbij het licht op het focuspunt het felst is. Aan het einde kun je dan de SLM instellen het alle correcte phases, en verschijnt het patroon wat je zocht.


In ons onderzoek hebben we eerst geprobeert een focus punt te krijgen. Nadat dit gelukt is hebben we onderzocht hoe het aantal segmenten en aantal phases invloed heeft op de duur van het algoritme en de kwaliteit van het focus punt. De kwaliteit van het focus punt meten we door te kijken hoe veel procent van het licht dat door de fiber schijnt daadwerkelijk op het focus punt beland. Uiteindelijk hebben wij, na het testen van waarden tussen de 100 en 1100 segmenten en 2 tot 5 fasen, een maximaal resultaat van XXX project bereikt nadat het algoritme XXX seconden heeft gedraaid.

In ons onderzoek hebben we de verhouding genomen tussen deze twee factoren, om te kijken welke instellingen het meest efficient zijn. Deze verhouding blijkt volgens onze resultaten het beste te zijn bij XXX segmenten en XXX fasen. Al hangt je keuze van je parameters die je nodig hebt sterk af van je applicatie.
