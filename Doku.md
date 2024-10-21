# Projektdokumentation: Smarthome Steuerung

## Projektbeteiligte

| Name    | Aufgabe                              | Beteiligung (%) |
|---------|--------------------------------------|-----------------|
| Joshua  | Hardwareaufbau                       | 33%             |
| Maik    | Softwareentwicklung (GUI, Logik)     | 33%             |
| Lars    | Softwareentwicklung (GUI, Logik)     | 33%             |

---

## Inhaltsverzeichnis

1. [Projektauftrag](#projektauftrag)
2. [Einleitung](#einleitung)
3. [Projektverlauf](#projektverlauf)
    - [Hardware](#hardware)
    - [Software](#software)
4. [Projektplanung](#projektplanung)
    - [Ablaufplanung](#ablaufplanung)
    - [Aufgabenverteilung](#aufgabenverteilung)
5. [Abschlussbericht](#abschlussbericht)
    - [Ergebnisse](#ergebnisse)
    - [Reflexion](#reflexion)
6. [Literatur- und Materialverzeichnis](#literatur-und-materialverzeichnis)

---

## Projektauftrag

Der Auftrag bestand darin, eine Smarthome-Steuerung zu entwickeln. Ziel des Projekts war es, mithilfe eines **Raspberry Pi 5**, eines **Raspberry Pi Touch Displays**, eines **BME280 Sensors** und **LEDs** eine Steuerung zu realisieren, die über eine GUI auf einem Flask Webserver bedienbar ist. Die Steuerung sollte es ermöglichen, Umweltdaten zu erfassen und Ausgaben über das Webinterface zu visualisieren sowie LEDs zu steuern.

---

## Einleitung

In der heutigen Zeit sind Smarthome-Lösungen aus vielen Haushalten nicht mehr wegzudenken. Ziel unseres Projekts war es, eine einfache, aber funktionsfähige Steuerung zu realisieren, die es ermöglicht, verschiedene Umgebungsparameter wie Temperatur, Luftfeuchtigkeit und Druck zu erfassen sowie einfache Steuerungsaufgaben, wie die Ansteuerung von LEDs, zu übernehmen.

Das Projekt wurde in zwei Phasen durchgeführt:
- **Phase 1 (17.07 - 24.07):** Hardware-Aufbau und grundlegende Softwareentwicklung.
- **Phase 2 (02.10):** Weiterentwicklung und finale Abstimmung der Software sowie Tests.

---

## Projektverlauf

### Hardware

Die Hardware-Komponenten wurden von **Joshua** zusammengebaut. Die verwendeten Bauteile waren:

- **Raspberry Pi 5**: Zentraler Controller für die Smarthome Steuerung.
- **Raspberry Pi Touch Display**: Interface für direkte Eingaben.
- **BME280 Sensor**: Sensor für die Erfassung von Temperatur, Luftfeuchtigkeit und Luftdruck.
- **LEDs**: Zur Anzeige und Kontrolle über die Webschnittstelle.

Der Zusammenbau der Hardware dauerte etwa zwei Arbeitstage. Alle Komponenten wurden erfolgreich miteinander verbunden, und die Kommunikation zwischen dem Raspberry Pi und dem BME280 Sensor über I²C funktionierte einwandfrei.

### Software

Die Softwareentwicklung wurde von **Maik** und **Lars** durchgeführt. Es wurde eine GUI entwickelt, die auf einem Flask Webserver läuft. Die GUI ermöglicht:

- **Sensor-Datenanzeige**: Die aktuellen Werte des BME280 Sensors werden auf der Webseite angezeigt.
- **LED-Steuerung**: Über die Weboberfläche können die LEDs ein- und ausgeschaltet werden.

Die Software besteht aus folgenden Hauptkomponenten:
- **Flask Webserver**: Der Webserver bildet die Grundlage für die GUI.
- **Python-Skript** zur Steuerung des BME280 Sensors.
- **HTML/CSS** für die Benutzeroberfläche.

---

## Projektplanung

### Ablaufplanung

Zur Planung des Projekts wurde ein **Gantt-Diagramm** verwendet, um die zeitliche Abfolge der einzelnen Aufgaben darzustellen. Das Diagramm zeigt den geplanten und tatsächlichen Fortschritt des Projekts.

```plaintext
| Aufgabe                 | Startdatum | Enddatum   | Dauer |
|-------------------------|------------|------------|-------|
| Hardwareaufbau           | 17.07.2023 | 19.07.2023 | 2 Tage|
| Software: Flask Webserver| 20.07.2023 | 24.07.2023 | 5 Tage|
| Tests und Debugging      | 02.10.2023 | 02.10.2023 | 1 Tag |
