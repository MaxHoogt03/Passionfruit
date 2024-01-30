# Passionfruits Sollutions for Smartgrid
Door: Max Hoogeveen, Stefan Marijnissen en Leo Zinn
## HoofdProgramma: main.py
Om een bepaald algoritme te runnen ga je naar main.py. In main.py kan je de volgende algoritmen runnen: 

1. Random 
2. Random to greedy
3. Random to hillclimber
4. Random to simulated annealing
5. Random to heuristic hill.
   
Waarbij hillclimber 5000 keer word gerund, Simulated annealing 10000 keer en heuristic hill 150 keer.

Bij het runnen van main.py gebeurd er het volgende:

1. Er verschijnt een prompt waarbij je een getal kan kiezen. Dit getal representeerd het algoritme die je wil runnen.

2. Vervolgens word er gevraagd op welk district je het zou willen runnen. Hier kan je weer een getal invullen (1-3)

3. Na het district gekozen te hebben kan je kiezen of je een gereformeerde district wil. Gereformeerd betekend dat de huizen die naar dezelfde batterij gaan, aan elkaar worden aangesloten mits dit voordeliger is.

4. Afhankelijk wat je bij 3 hebt gekozen kan je eventueel ook nog geprompt worden of je de shared costs of own costs wil zien. Own costs zijn de kosten waarbij je ervanuit gaat dat elke huis zijn eigen kabels heeft naar de batterij en Shared costs haalt dubbel getelde kabels die naar dezelfde batterij gaan van de kosten af omdat deze al "shared" zijn dus aangesloten.  
## Experiment
Open experiment_scripts.py en daarin staat hoe we bij de uitkomsten zijn gekomen van het experiment.
