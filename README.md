# 🚨 Emergency Evacuation Path Finder

## 📌 Project Overview

Emergency Evacuation Path Finder is an AI-based system designed to find a safe and shortest route for people during emergencies such as fires, earthquakes, floods, or other disasters.

The system represents a building or area as a graph, where locations are treated as nodes and paths are treated as edges. Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search can be used to identify an appropriate evacuation route.

The system considers blocked paths, obstacles, danger zones, and available emergency exits while calculating the route. It helps users quickly identify a safe path from their current location to a suitable emergency exit.

The main objective of this project is to reduce evacuation time, avoid dangerous areas, and improve safety during emergency situations.

The proposed system can be useful in places such as schools, colleges, hospitals, offices, shopping malls, airports, and other large buildings.

---

## 🎯 Objectives

- Find a suitable evacuation route during emergency situations.
- Reduce the time required to reach an emergency exit.
- Avoid dangerous areas and blocked paths.
- Apply AI search techniques for emergency route planning.
- Compare different path-finding algorithms.
- Display the evacuation route visually.
- Help users identify an available emergency exit.
- Provide the total path cost of the selected route.

---

## 🤖 AI Algorithms Used

### 1. Breadth-First Search (BFS)

Breadth-First Search explores the building graph level by level. It finds a route with the minimum number of connections between the starting location and the selected emergency exit.

### 2. Uniform Cost Search (UCS)

Uniform Cost Search considers the cost associated with each path and searches for a route with the lowest total path cost.

### 3. A* Search

A* Search combines the actual path cost with a heuristic estimate to efficiently search for an appropriate route toward the selected emergency exit.

---

## ⚙️ How the System Works

The building is represented as a graph.

- Nodes represent locations such as rooms, halls, corridors, entrances, and exits.
- Edges represent paths connecting different locations.
- Path costs represent the cost of moving between locations.
- Danger zones represent areas that should be avoided.
- Blocked paths represent routes that cannot be used.
- Emergency exits represent possible evacuation destinations.

The user selects a starting location, emergency exit, AI algorithm, danger zone, and blocked path.

The selected search algorithm searches the building graph while considering the selected blocked paths and danger zones.

The resulting evacuation route is displayed on a building map along with the total path cost and number of locations in the route.

---

## ✨ Features

- 🚨 Emergency evacuation route finding
- 🗺️ Building map visualization
- 🤖 Breadth-First Search (BFS)
- 🤖 Uniform Cost Search (UCS)
- 🤖 A* Search
- ⚠️ Danger-zone selection
- 🚧 Blocked-path selection
- 🚪 Multiple emergency exits
- 🛣️ Recommended evacuation route
- 💰 Total path-cost calculation
- 📍 Number of locations in the selected route
- ❌ No-route detection

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Matplotlib
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search
- Git
- GitHub

---

## 📂 Project Structure

Emergency-Evacuation-Path-Finder/
│
├── app.py
├── algorithms.py
├── requirements.txt
├── README.md
└── venv/

### File Description

| File | Description |
|------|-------------|
| app.py | Main Streamlit application and user interface |
| algorithms.py | Contains BFS, UCS, and A* search algorithms |
| requirements.txt | Contains the required Python packages |
| README.md | Project documentation |
| venv/ | Python virtual environment |

---

## 📋 Requirements

The project requires the following Python packages:

streamlit
matplotlib

Python built-in modules such as collections and heapq are used in the project and do not need to be installed separately.

---

## ⚙️ Installation

### Step 1: Clone the Repository

git clone <YOUR-GITHUB-REPOSITORY-URL>

### Step 2: Open the Project Folder

cd Emergency-Evacuation-Path-Finder

### Step 3: Create a Virtual Environment

python -m venv venv

### Step 4: Activate the Virtual Environment

For Windows:

venv\Scripts\activate

### Step 5: Install Required Packages

pip install -r requirements.txt

---

## ▶️ Running the Application

After activating the virtual environment, run:

streamlit run app.py

The application will open in a web browser.

---

## 🧭 How to Use the Application

1. Open the Emergency Evacuation Path Finder application.
2. Select the Starting Location.
3. Select the required Emergency Exit.
4. Select an AI search algorithm:
   - BFS
   - UCS
   - A*
5. Select a Danger Zone, if required.
6. Select a Blocked Path, if required.
7. Click Find Safe Path.
8. View the building map.
9. View the recommended evacuation route.
10. Check the total path cost.
11. Check the number of locations in the route.

---

## 🏢 Building Graph

The current building contains the following locations:

Entrance
Hall
Room A
Room B
Corridor
Exit 1
Exit 2

The connections between these locations are used by the search algorithms to calculate evacuation routes.

---

## 🧪 Example

Suppose the user selects:

Starting Location: Entrance
Emergency Exit: Exit 1
Algorithm: A*
Danger Zone: None
Blocked Path: None

The system can identify a route such as:

Entrance → Hall → Corridor → Exit 1

The route is then highlighted on the building map.

---

## ⚠️ Danger Zone Handling

The application allows the user to select a danger zone.

For example:

Danger Zone: Corridor

The system prevents normal movement through the danger-zone connections and attempts to find another available route.

If the selected starting location itself is the danger zone, the system allows movement out of that location so that the user can escape the dangerous area.

---

## 🚧 Blocked Path Handling

The application also allows the user to select a blocked path.

Example:

Blocked Path: Hall → Corridor

The selected path is treated as unavailable, and the search algorithm attempts to find another route to the emergency exit.

---

## 🔍 Search Algorithm Comparison

| Algorithm | Main Approach | Purpose |
|-----------|----------------|---------|
| BFS | Level-by-level search | Finds a route with minimum number of connections |
| UCS | Cost-based search | Finds a minimum-cost route |
| A* | Cost + heuristic | Efficiently searches toward the goal |

---

## 📊 Output

After clicking Find Safe Path, the application displays:

- 🗺️ Building Map
- 🛣️ Recommended Safe Route
- ⚠️ Danger Zone Information
- 🚧 Blocked Path Information
- 💰 Total Path Cost
- 📍 Number of Locations in the Route

If no available route exists, the application displays:

No safe evacuation route is available.

The user can then try another emergency exit or modify the danger zone or blocked path.

---

## 🔄 System Workflow

User
↓
Select Starting Location
↓
Select Emergency Exit
↓
Select AI Algorithm
↓
Select Danger Zone / Blocked Path
↓
Build/Use Graph
↓
Run BFS / UCS / A*
↓
Find Available Route
↓
Display Building Map
↓
Display Evacuation Result

---

## 🌍 Applications

The proposed Emergency Evacuation Path Finder can be useful in:

- Schools
- Colleges
- Hospitals
- Offices
- Shopping Malls
- Airports
- Large Buildings
- Public Facilities

The system provides an approach for assisting people in identifying an available evacuation route during emergency situations.

---

## 🎯 Expected Outcome

The Emergency Evacuation Path Finder provides a simple and effective approach to emergency route planning using AI search techniques.

The system helps identify suitable evacuation paths while considering blocked paths and danger zones. By applying BFS, UCS, and A* search algorithms, the system demonstrates how AI-based path-finding techniques can be applied to emergency evacuation planning.

The main expected outcomes are:

- Faster identification of evacuation routes.
- Avoidance of selected dangerous areas.
- Avoidance of blocked paths.
- Visualization of the selected evacuation route.
- Comparison of different AI search techniques.
- Improved understanding of AI-based emergency route planning.

---

## 🚀 Future Enhancements

The project can be further enhanced by integrating:

- Real-time fire and smoke sensors.
- Dynamic building maps.
- Real-time emergency information.
- Multiple simultaneous danger zones.
- IoT-based emergency monitoring.
- Voice-based evacuation instructions.
- Mobile application support.
- Real-time route updates.
- GPS-based location tracking.

---

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes.

The Emergency Evacuation Path Finder is an AI-based prototype and should not be considered a replacement for certified emergency evacuation systems, professional safety planning, or real-world emergency response procedures.