# Konzept: Control Layer

Dieses Dokument beschreibt das erste Konzept für die Steuerungsebene (Control Layer) von tramAachen. Die Orchestrierung erfolgt mittels K3s (Kubernetes).

## K3s-Manifeste & FastAPI
Einführung von K3s-Manifesten zum Starten eines zentralen Steuerungsdienstes auf Basis von **FastAPI**. Dieser Dienst bildet das Rückgrat für die intelligente Energieverteilung und Verkehrssteuerung.

## Kernfunktionen
1. **Wetterdaten-API-Anbindung**: Vorhersage der Photovoltaik-Erzeugung an den Haltestellen basierend auf aktuellen Wetterprognosen, um die Pufferkapazitäten optimal zu nutzen.
2. **GTFS-Anbindung (Fahrplandaten)**: Integration von GTFS-Daten zur Berechnung der zu erwartenden Lastspitzen an den Hubs. Dies ermöglicht eine vorausschauende Laststeuerung.
3. **V2G-Logik (Vehicle-to-Grid)**: Ein intelligenter Algorithmus zur Entscheidungsfindung: "Wird das E-Auto im Park&Ride-Parkhaus geladen oder wird die Energie aktuell in der Oberleitung für den Fahrbetrieb benötigt?"
