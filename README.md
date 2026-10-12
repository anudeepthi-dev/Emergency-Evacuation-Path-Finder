# 🚨 Emergency Evacuation Path Finder

## 📌 Project Overview

The **Emergency Evacuation Path Finder** is a web-based application that helps identify safe evacuation routes in a building during emergency situations. It uses Artificial Intelligence (AI) search algorithms to find paths from a starting location to a selected emergency exit while considering blocked paths and danger zones.

The application provides a simple, interactive interface where users can select their starting point, destination, and blocked routes to determine an available evacuation path.

This project demonstrates how AI search algorithms can be applied to pathfinding and emergency route planning.

## 🎯 Objectives

- Find available evacuation routes from a starting location to an emergency exit.
- Implement AI search algorithms for pathfinding.
- Identify alternative routes when certain paths are blocked.
- Compare different search algorithms based on their pathfinding behavior.
- Provide a user-friendly interface for visualizing evacuation routes.
- Demonstrate the application of Artificial Intelligence in emergency management.

## ✨ Features

- **Interactive Web Interface:** Built using Streamlit for easy interaction.
- **Multiple Search Algorithms:** Implements Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search.
- **Start and Destination Selection:** Allows users to choose their starting location and evacuation exit.
- **Blocked Path Management:** Enables users to mark paths as blocked to simulate obstacles or danger zones.
- **Alternative Route Finding:** Searches for another available route when the original path is blocked.
- **Path Cost Calculation:** Uses path costs to evaluate routes where supported by the selected algorithm.
- **Floor Plan Visualization:** Displays an illustrative sample building floor plan.
- **Route Results:** Presents the calculated evacuation path and relevant search results.
- **Emergency Simulation:** Allows users to explore different evacuation scenarios.

## 🧠 AI Search Algorithms

### 1. Breadth-First Search (BFS)

Breadth-First Search explores neighboring locations level by level. It finds a path with the minimum number of edges in an unweighted graph, provided a path exists.

### 2. Uniform Cost Search (UCS)

Uniform Cost Search expands the path with the lowest accumulated cost. It is useful for finding a minimum-cost route when movement costs differ and are non-negative.

### 3. A* Search

A* Search combines the accumulated path cost with a heuristic estimate of the remaining distance to the destination. With an appropriate admissible heuristic and non-negative edge costs, it can find an optimal path.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Visualization:** Matplotlib
- **AI Concepts:** Graph Search and Pathfinding
- **Algorithms:** BFS, UCS, A*
- **Version Control:** Git
- **Code Hosting:** GitHub
- **Deployment:** Streamlit Community Cloud

## 📂 Project Structure

```text
Emergency-Evacuation-Path-Finder/
│
├── app.py
├── algorithms.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── venv/                  # Local virtual environment (not committed)
```

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system
- pip package manager
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/anudeepthi-dev/Emergency-Evacuation-Path-Finder.git
```

Navigate to the project directory:

```bash
cd Emergency-Evacuation-Path-Finder
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser. If it does not open automatically, visit:

```text
http://localhost:8501
```

## 🚀 How to Use the Application

1. Open the Emergency Evacuation Path Finder application.
2. View the illustrative sample building floor plan.
3. Select a starting location.
4. Select the desired destination or emergency exit.
5. Choose the search algorithm.
6. Mark any paths that are blocked or unsafe.
7. Run the pathfinding process.
8. Review the resulting evacuation route and path cost, where available.
9. Change the blocked paths or destination to explore alternative routes.

## 📊 Expected Results

The application attempts to identify an available route between the selected starting location and destination.

Depending on the selected algorithm and building graph, the results may include:

- The calculated evacuation path.
- The selected search algorithm.
- The total path cost, where supported.
- A message indicating whether a route is available.
- An alternative route when the original route is blocked and another path exists.

If all possible routes are blocked, the application should indicate that no route is available.

## 🏢 Sample Building Environment

The application uses a sample building represented as a graph.

- **Nodes:** Rooms, hallways, corridors, entrances, and emergency exits.
- **Edges:** Connections between locations.
- **Edge Costs:** Movement costs associated with connections.
- **Blocked Edges:** Connections that cannot be used during an evacuation.

The floor plan is provided for illustrative purposes. The route calculations depend on the building graph and costs defined in the application code.

## 🌍 Applications

- Emergency evacuation planning in buildings.
- Route planning in offices, colleges, and public facilities.
- AI-based navigation systems.
- Pathfinding simulations involving obstacles.
- Educational demonstrations of graph search algorithms.

## ⚠️ Limitations

- The application uses a sample building graph rather than a live building map.
- Route results depend on the locations, connections, and costs defined in the code.
- The application does not automatically detect real fires, smoke, structural damage, or other hazards.
- It does not provide real-time emergency alerts or live sensor integration.
- The floor plan is illustrative and may not represent the exact graph used for calculations.

**Safety Disclaimer:** This project is an educational demonstration of AI-based pathfinding. It is not a certified life-safety system and should not be used as the sole basis for real-world emergency evacuation decisions. Always follow official emergency procedures and instructions from emergency personnel.

## 🔮 Future Enhancements

- Integrate real building floor plans.
- Add real-time hazard detection using sensors.
- Develop dynamic route updates when hazards change.
- Include multiple-floor building navigation.
- Add estimated evacuation times based on movement speeds.
- Introduce interactive floor plan editing.
- Compare algorithm performance using execution time and explored nodes.
- Integrate IoT-based emergency monitoring and alerts.

## 📌 Conclusion

The **Emergency Evacuation Path Finder** demonstrates how Artificial Intelligence search algorithms can support evacuation route planning in a simulated building environment. By implementing BFS, UCS, and A*, the project explores different approaches to finding paths while accounting for blocked connections and route costs.

The application combines Python, Streamlit, and Matplotlib to provide an interactive demonstration of AI-based pathfinding and its potential applications in emergency management.

## 📜 License

This project is intended for educational and demonstration purposes. A formal open-source license can be added if the project is to be distributed under specific licensing terms.
