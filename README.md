## Passionfruit: Solutions for SmartGrid
Door: Max Hoogeveen, Stefan Marijnissen en Leo Zinn

## De case
Deze case draait om het optimaliseren van een Smart Grid voor groene energie in woonwijken. Huizen met zonnepanelen zijn verbonden aan batterijen via kabels, waarbij kostenbesparingen en efficiëntie centraal staan. De opdracht gaat van individuele kabelverbindingen naar gedeelde kabels. De uitdaging omvat het vinden van optimale configuraties van kabels. De output wordt gemaakt aan de hand van een uniform format, waarin de kosten en verbindingen van het Smart Grid worden weergegeven. De case biedt een diepgaande blik op het ontwerpen en optimaliseren van het Smart Grid probleem voor duurzame energieopwekking.

## De aanpak per algoritme
- Met Random pakken wij een random huis en random batterij en koppelen we die. Als aan het einde van het algoritme er geen geldige oplossing staat, runt het algoritme opnieuw tot er wel een geldige oplossing aanwezig is.

- Met Random Greedy pakken wij een random huis en verbinden wij deze greedy aan een batterij, waar greedy betekent dat we de dichtbijzijndste batterij pakken. Als deze batterij al een max capaciteit heeft, zoeken we de volgende dichtstbijzijndste batterij etc. Als er aan het einde van de algoritme geen oplossing aanwezig is, runt het algoritme opnieuw tot er een gevonden is.

- Met Greedy kijken we naar kleinste afstand tussen een huis in het grid en een batterij en deze twee koppelen we aan elkaar. Vervolgens word er gekeken naar de volgende kleinste manhatten afstand tussen een huis en een batterij en worden ze gekoppeld. Dit word gedaan voor elk huis in het district. Greedy geeft echter geen valide oplossingen.


- Hillclimber: een opgeloste staat van het probleem wordt gebruikt als begin staat. Vervolgens kiest het algoritme random twee verschillende batterijen, en van deze twee verschillende batterijen random twee huizen. De connectie tussen batterij 1 en huis 1 en batterij 2 en huis 2 worden verwisseld. Vervolgens word gekeken of deze wissel zorgt voor minder kosten. Zo ja, dan wordt de district geüpdated door deze verbinding met elkaar te wisselen. 5000 iteraties.

- Simulated annealing: werkt hetzelfde als hillclimber, maar maakt gebruik van temperatuur en cooling factor om een kans te creëren dat een verslechtering ook wordt geaccepteerd. De eerste 5000 iteraties is de temperatuur 0, waardoor het hetzelfde functioneert als hillclimber. De volgende 5000 iteraties werken met een functie om verslechteringen te accepteren.

- Heuristic hill: maakt gebruik van hetzelfde idee als hillclimber, maar selecteert steeds de slechtste verbinding om aan te passen. Als heuristiek wordt gebruikt de lengte kabels in eerste instantie en de lengte van de kabels na het verwisselen. Dit algoritme gebruikt dus geen calculate_own_costs() of calculate_shared_costs() en is daarom sneller. Een queue wordt gebruikt zodat niet steeds hetzelfde huis met elkaar wordt gewisseld.

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
visualisation -> gridcables -> plot1.png of plot2.png of plot3.png (dit hangt ervanaf welk district je hebt gerund. Als je district 1 runt zit hij in plot1 etc.)

## Experiment
Open experiment_scripts.py en daarin staat hoe we bij de uitkomsten zijn gekomen van het experiment.

## Opmerkingen
Advanced opdracht 5, 6 en een genetisch algoritme staan ook in de algorithms. Voor opdracht 5 zijn er 2 mogelijkheden gemaakt voor het plaatsen van de batterijen. 
- Random allocatie van de batterijen. 
- Plaatsing bij het huis met de meeste huizen in een straal. Met een algoritme om te voorkomen dat batterijen op een klutje komen.

Verder zijn deze 2 niet geimplementeerd met welk algoritme dan ook.

Voor opdracht 6 is er een base case waarbij random batterijen worden geselecteerd totdat er genoeg capaciteit is. Deze is dus nog totaal niet geoptimaliseerd. Het genetisch algoritme is ook werkend, maar doordat het vrij lastig is om betere childs te krijgen dan parents in dit probleem werkt het tot nu toe nog niet zoals wij willen.

## Presentatie
Op de grafieken van de resultaten zie je algoritmes uit onze main die 1000 keer zijn gerund. Deze kunnen herrund worden. Hiervoor moet je naar experiment_scripts.py (zelfde directory als main) gaan en de code die je wil runnen uitcommenten. De resultaten van het runnen van die experimenten vind je in het mapje presentation. Hier zie je allemaal csv files waarbij de naam weergeeft wat erin staat. Om de grafieken te maken kan je bar-chart.py en graph_distribution.py runnen. In theoretical_optimum.py word het theoretisch optimum berekend en deze word gebruikt voor de verdelingsgrafieken.