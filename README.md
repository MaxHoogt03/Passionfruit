## Passionfruit: Solutions for SmartGrid
Door: Max Hoogeveen, Stefan Marijnissen en Leo Zinn

## De case
Deze case draait om het optimaliseren van een Smart Grid voor groene energie in woonwijken. Huizen met zonnepanelen zijn verbonden aan batterijen via kabels, waarbij kostenbesparingen en efficiëntie centraal staan. De opdracht gaat van individuele kabelverbindingen naar gedeelde kabels. De uitdaging omvat het vinden van optimale configuraties van kabels. De output wordt gemaakt aan de hand van een uniform format, waarin de kosten en verbindingen van het Smart Grid worden weergegeven. De case biedt een diepgaande blik op het ontwerpen en optimaliseren van het Smart Grid probleem voor duurzame energieopwekking.

## De aanpak per algoritme

## HoofdProgramma: main.py
Om een bepaald algoritme te runnen ga je naar main.py. In main.py kan je de volgende algoritmen runnen: 

1. Random 
2. Random to greedy
3. Random to hillclimber
4. Random to simulated annealing
5. Random to heuristic hill.
   
Waarbij hillclimber 5000 keer iteraties heeft, Simulated annealing 10000 en heuristic hill 150.

Bij het runnen van main.py gebeurd er het volgende:

1. Er verschijnt een prompt waarbij je een getal kan kiezen. Dit getal representeerd het algoritme die je wil runnen.

2. Vervolgens word er gevraagd op welk district je het zou willen runnen. Hier kan je weer een getal invullen (1-3)

3. Na het district gekozen te hebben kan je kiezen of je een gereformeerde district wil. Gereformeerd betekend dat de huizen die naar dezelfde batterij gaan, aan elkaar worden aangesloten mits dit voordeliger is.

4. Afhankelijk wat je bij 3 hebt gekozen kan je eventueel ook nog geprompt worden of je de shared costs of own costs wil zien. Own costs zijn de kosten waarbij je ervanuit gaat dat elke huis zijn eigen kabels heeft naar de batterij en Shared costs haalt dubbel getelde kabels die naar dezelfde batterij gaan van de kosten af omdat deze al "shared" zijn dus aangesloten.

In de command line word er een uitkomst geprint. Als je reformed hebt gekozen bij stap 3 kan de waarde van Shared cost verschillen van de laatste iteratie in de commandline. Dit komt omdat het reformeren bij de laatste iteratie word uitgevoerd. Het herleggen van de kabels geeft dan een ander resultaat.

De plot voor de laatste iteratie van het gerunde algortime is te vinden in: <br> 
visualisation -> gridcables -> plot1.png

## Experiment
Open experiment_scripts.py en daarin staat hoe we bij de uitkomsten zijn gekomen van het experiment.

## Opmerkingen
Advanced opdracht 5, 6 en een genetisch algoritme staan ook in de algorithms. Voor opdracht 5 zijn er 2 mogelijkheden gemaakt voor het plaatsen van de batterijen. 
- Random allocatie van de batterijen. 
- Plaatsing bij het huis met de meeste huizen in een straal. Met een algoritme om te voorkomen dat batterijen op een klutje komen.

Verder zijn deze 2 verder niet geimplementeerd met welk algoritme dan ook.

Voor opdracht 6 is er een base case waarbij random batterijen worden geselecteerd totdat er genoeg capaciteit is. Deze is dus nog totaal niet geoptimaliseerd. Het genetisch algoritme is ook werkend, maar doordat het vrij lastig is om betere childs te krijgen dan parents in dit probleem werkt het tot nu toe nog niet zoals wij willen.

## Presentatie
Op de grafieken van de resultaten zie je algoritmes uit onze main die 1000 keer zijn gerund. Deze kunnen herrund worden. Hiervoor moet je naar experiment_scripts.py (zelfde directory als main) gaan en de code die je wil runnen uitcommenten. De resultaten van het runnen van die experimenten vind je in het mapje presentation. Hier zie je allemaal csv files waarbij de naam weergeeft wat erin staat. Om de grafieken te maken kan je bar-chart.py en graph_distribution.py runnen. In theoretical_optimum.py word het theoretisch optimum berekend en deze word gebruikt voor de verdelingsgrafieken.