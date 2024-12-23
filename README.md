# 📝 Aplikacja do Zarządzania Zadaniami (To-Do List)

## **📜 Opis projektu**
Aplikacja To-Do List umożliwia zarządzanie codziennymi zadaniami. Pozwala na dodawanie, edytowanie, oznaczanie zadań jako wykonane oraz ich usuwanie. Dane są zapisywane w pliku JSON, dzięki czemu lista zadań jest dostępna po ponownym uruchomieniu programu. Graficzny interfejs użytkownika został zbudowany za pomocą biblioteki **Tkinter**.

---

## **🎮 Funkcjonalności**
- **➕ Dodawanie zadań:**
  - Tytuł, opis, termin realizacji i opcjonalny priorytet.
- **📋 Wyświetlanie listy zadań:**
  - Zadania pokazane w przejrzystym formacie z informacją o statusie.
- **✅ Oznaczanie jako wykonane:**
  - Zmiana statusu zadania na „wykonane”.
- **🗑️ Usuwanie zadań:**
  - Możliwość trwałego usunięcia wybranego zadania.
- **💾 Zapisywanie i wczytywanie:**
  - Dane przechowywane w pliku `zadania.json` są automatycznie wczytywane przy starcie aplikacji.
- **⭐ Priorytety:**
  - Przypisanie zadaniom priorytetów (wysoki, średni, niski).
- **🔎 Filtrowanie i sortowanie:**
  - Filtrowanie zadań według terminu lub priorytetu.
- **🔔 Powiadomienia:**
  - Informowanie użytkownika o zbliżających się terminach.

---

## **🛠️ Technologie**
- **Python 3.8+**
- **Tkinter** – biblioteka do tworzenia graficznego interfejsu użytkownika.
- **JSON** – do zapisywania i wczytywania listy zadań.

---

## **📋 Wymagania**
- Python 3.8 lub nowszy.
- Edytor kodu lub IDE (np. PyCharm, VS Code).
- Opcjonalnie: Wirtualne środowisko Python (`venv`).

---

## **📦 Instalacja**
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/uzytkownik/to-do-list-app.git
   cd to-do-list-app
