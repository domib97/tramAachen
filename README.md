# tramAachen

<table>
	<th><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/ASEAG_1006.JPG/1200px-ASEAG_1006.JPG" alt="" border=1  width=750></img>
	</th>
	<th><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Aachen-Elisenbrunnen-1910.jpg/440px-Aachen-Elisenbrunnen-1910.jpg" alt="" border=1 width=900 		</img>
	</th>
</table>

### Aktuelle Probleme & Herausforderungen

| Energiesektor | Verkehrssektor |
| :--- | :--- |
| Energiewende: zentral -> dezentral | Reduzierung des CO²-Ausstoßes |
| Energieverbraucher -> Prosumer (Produzent & Konsument) | Individualverkehr -> ÖPNV (höhere Skalierbarkeit) |

Die Heilbadstadt Aachen (lat. Aquae Granni) hatte bis zum Jahr 1974 eines der besten [Straßenbahn-Netze](https://de.m.wikipedia.org/wiki/Stra%C3%9Fenbahn_Aachen) Deutschlands. Heutzutage ist die historische High-Tech-Stadt nur noch über das im [Vergleich](https://www.vcd.org/themen/klimafreundliche-mobilitaet/verkehrsmittel-im-vergleich/) relativ **umweltschädliche** Diesel-Bus-System mit all seinen Nachteilen von Verspätungen durch Stau im **Individualverkehr**, kaum vorhandener Barrierefreiheit und unzureichendem Komfort erreichbar. Der alleinige Umstieg auf E-Busse löst weder die **Kapazitätsprobleme** noch den Gummireifen-Verschleiß (**Mikroplastik-Verschmutzung**) oder den damit einhergehenden großen Energieverlust.

Der international beschlossene Umstieg von einer **zentral-fossilen** zu einer **dezentral-erneuerbaren** Energieerzeugung führt jedoch **sektorenübergreifend** zu Problemen. Wie bewerkstelligt man an bewölkten und windstillen Tagen den Güter- und Personentransport innerhalb der Stadt? Wie kann eine Stadt durch intelligente Energieverteilung das Stromnetz auch bei Lastspitzen stabil halten? Wie werden die benötigten **dezentralen Energiespeicher** integriert?

Viele Aachener Initiativen sind an dem Vorhaben gescheitert, das S-Bahn-System mit dem deutlich besseren Wirkungsgrad erneut einzuführen, wie zuletzt die ["Campusbahn"](https://de.wikipedia.org/wiki/Campusbahn).
Außerdem geht aus einem erst vor kurzem an einem Bürgerentscheid gescheiterten Bahn-Projekt in [Wiesbaden](https://de.wikipedia.org/wiki/Citybahn_Wiesbaden) hervor, dass es mehr Bedarf als für eine simple altmodische Tram gibt.

Das Projekt "tramAachen" soll nun diese branchenübergreifenden Probleme angehen und ein **städtisches "Smart-Grid"** in ein elektrifiziertes ÖPNV-Netz wie einer S-Bahn oder eines O-Busses implementieren. Dabei dient eine **Haltestelle als Energiespeicher** für die lokalen Produzenten und Verbraucher (Prosumer) des grünen Stroms. Diese lokalen Speicher sind durch die dezentrale Netzstruktur miteinander verbunden. Ein E-Auto an den Park&Ride-Stellen außerhalb der Stadt könnte seine Akku-Kapazität dem Netz zur Verfügung stellen. Auf Wunsch wird das E-Auto kostengünstig nur in den wolkenlosen Stunden des Tages geladen, also nur wenn ein Überschuss an Photovoltaik-Strom vorhanden ist. Während den nächtlichen Sturmböen lädt sich die tramBattery mit dem Überschuss an Windenergie für den nächsten Tag auf.
Diese entwickelte Technologie ließe sich relativ einfach in EU-Städte mit **elektrifizierter ÖPNV-Infrastruktur** implementieren.

| Energiesektor | + | Verkehrssektor | = | tramAachen |

* **Energiesektor + Verkehrssektor = "tramAachen"**: Die Verbindung einer [Straßenbahn](https://de.m.wikipedia.org/wiki/Stra%C3%9Fenbahn_Stra%C3%9Fburg), die das allgemeine Stadtbild verbessert, mit einem ["Smart-Grid"](https://www.eon.de/de/eonerleben/smart-grid-so-funktioniert-das-intelligente-stromnetz.html), um die städtischen Erzeuger und Verbraucher von erneuerbaren Energien mit einem Pufferspeicher zu verknüpfen.

* **"tramLogistic"**: Der innerstädtische Transport von [Gütern](https://www.avg.info/unternehmen/presse/pressemitteilungen/meldungen/entwicklung-einer-guetertram-neues-verbundprojekt-logiktram.html) und Waren könnte damit emissionsfrei werden.

* **"tramAI"**: Relativ einfache Umsetzung eines voll-autonomen Triebwagens: [Siemens Mobility](https://www.mobility.siemens.com/global/de/portfolio/schiene/fahrzeuge/strassenbahnen/autonome-strassenbahn.html).

* **Transparent**: Um eine bürgernahe Entwicklung zu gewährleisten, wird das Projekt [open-source](https://github.com/readme/featured/nasa-ingenuity-helicopter).

* **Prototyp**: Die vier Regionalbahnhöfe in Aachen (Rothe Erde - HBF - Schanz - West) eignen sich für ein Proof-of-Concept dieser Akku-Stadtbahn.

### Projektstruktur

- **[tramGrid](./tramGrid)**: Konzepte und Ressourcen zum intelligenten Stromnetz.
- **[tramLine](./tramLine)**: Linienführung und Netzausbaupläne.
- **[tramLogistic](./tramLogistic)**: Konzepte für den Gütertransport per Tram.
- **[tramOS](./tramOS)**: Softwarekomponenten und Steuerung (tramAI, tramApp, etc.).
- **[tramSimulation](./tramSimulation)**: Simulationsprogramme und wissenschaftliche Grundlagen.
- **[tramWaggon](./tramWaggon)**: Spezifikationen der Fahrzeuge und Komponenten (tramBattery, tramSolar).
- **[tramVision](./tramVision)**: Langfristige Visionen und Ziele des Projekts.
- **[tramPictures](./tramPictures)**: Bildmaterial und Visualisierungen.
- **[tramPartner&Sponsor](./tramPartner&Sponsor)**: Informationen zu Kooperationen.

Kontakt-Email: dominik.boehm@alumni.fh-aachen.de
