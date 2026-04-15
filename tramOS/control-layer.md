# ⚡ Smarte Energie für Aachen: Der Control Layer

Der **Control Layer** ist das digitale Gehirn von tramAachen. Er sorgt dafür, dass Energie dort ist, wo sie gebraucht wird – von der Sonne direkt in die Straßenbahn oder zurück ins Stadtnetz (**V2G**).

---

## 🚦 Die Drei Säulen der Energie-Intelligenz

Wir nutzen Echtzeit-Daten (APIs), um kluge Entscheidungen für die Stadt zu treffen:

| Daten-Quelle | Was wir wissen | Warum das wichtig ist |
| :--- | :--- | :--- |
| ☀️ **Sonnen-API** | Wie viel Strom erzeugen unsere Haltestellen heute? | Wir laden Batterien, wenn die Sonne scheint. |
| 🚋 **Fahrplan-API** | Wann kommen die nächsten Bahnen an den Bushof? | Wir halten Energie bereit für das Anfahren der Bahnen. |
| 🔌 **Netz-Status** | Ist das Aachener Stromnetz (STAWAG) gerade belastet? | E-Autos spenden Strom, um das Netz stabil zu halten. |

---

## 🧠 Wie funktioniert die Entscheidung? (V2G Logic)

Für Nicht-Techniker lässt sich die Logik einfach zusammenfassen:

1.  **Sicherheit geht vor:** Dein E-Auto wird *immer* geladen, wenn der Akku fast leer ist (< 20%).
2.  **Gemeinwohl:** Wenn eine Straßenbahn gerade viel Energie zum Beschleunigen braucht (Peak), "leiht" sich das System kurzzeitig Energie von geparkten Autos.
3.  **Nachhaltigkeit:** Wir laden bevorzugt dann, wenn die Sonne in Aachen scheint oder viel Windstrom im Netz ist.

---

## 🛠️ Technische Basis (Für Experten)

Obwohl die Logik einfach klingt, läuft im Hintergrund modernste Technik:
*   **Engine:** Entwickelt mit **FastAPI** (Python) für blitzschnelle Reaktionen.
*   **Orchestrierung:** Läuft auf einem **K3s (Kubernetes)** Cluster – verteilt auf Raspberry Pi 5 für maximale Effizienz.
*   **GitOps:** Automatische Updates über **ArgoCD** direkt aus unserem Gitea-Repository.

---
*tramAachen – Wir bewegen die Kaiserstadt mit Köpfchen.*
