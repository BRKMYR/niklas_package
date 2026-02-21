# niklas_package

A ROS/KnowRob package for semantic object recognition and knowledge-based reasoning on the iCub humanoid robot platform. The system combines visual object classification (via GURLS machine learning) with an OWL ontology and Prolog knowledge base to identify household objects by their material, shape, and affordance properties -- and to learn new objects at runtime.

## Historical Context

This project was developed circa 2016 as a student/research project, likely at the Technical University of Munich (TUM), under the supervision of Karinne Ramirez-Amaro. It integrates the KnowRob knowledge processing framework with the iCub robot ecosystem to explore how a robot can semantically reason about everyday objects. The work sits at the intersection of knowledge representation, ontological reasoning, and robotic perception: the robot observes objects through its vision system, classifies their physical attributes, and then queries a Prolog-backed ontology to determine what the object is and what it can be used for.

## How It Works

1. The iCub robot's vision pipeline (GURLS classifier) produces four outputs over YARP ports: the detected object name, its material type, its shape type, and its affordance (intended use).
2. A C++ ROS node receives these classifications and constructs Prolog queries against the KnowRob knowledge base.
3. The Prolog layer queries an OWL ontology (`icubworld.owl`) that defines household objects and their properties.
4. If the object is recognized, the system returns the matching ontology class. If not, it prompts the operator to provide corrections and learns the new object by asserting facts into the knowledge base and exporting a new OWL class file.

## Repository Structure

### Prolog Files (`prolog/`)

- **`init.pl`** -- Entry point for the Prolog knowledge base. Registers KnowRob dependencies (`knowrob_map_tools`, `knowrob_map_data`, `knowrob_actions`, `knowrob_objects`), loads the Semantic Web and OWL libraries, parses the OWL ontology files, registers the `niklasComputables` and `icubworld` namespaces, and consults the utility and definition modules.

- **`niklasComputable_utils.pl`** -- Core Prolog module defining custom computable predicates:
  - `detectObject/4` -- Queries objects by material, shape, and affordance properties.
  - `check_MaterialType/2`, `check_ShapeType/2`, `check_AffordanceType/2` -- Check whether an object has a specific material, shape, or affordance type via OWL reasoning.
  - `comp_onTopTable/2` -- Spatial reasoning computable that determines whether an object is positioned on top of a table by comparing Z coordinates from the semantic map.
  - `comp_newInstance/2` and `create_instance_from_class/3` -- Create new OWL instances of a given class and assert them into the RDF triple store.

- **`missing_definitions.pl`** -- Asserts object attribute knowledge that cannot be inferred from the OWL ontology alone (due to open-world vs. closed-world semantics). Defines predicates for object categories such as `CleaningDevice`, `CleaningPersonal` (Soap), `CleaningTool` (Sponge), `CleaningSubstance` (detergents, sprayers), `FoodVessel`, `DrinkingVessel` (Cup), and `EatingVessel` (Plate), each asserting the appropriate material, shape, and usage properties.

- **`missing_definitions_ORIGINAL.pl`** -- The original, simpler version of the definitions file where attributes were asserted per individual object (Cup, Plate, Soap, etc.) rather than per object category. Retained for reference.

- **`TEST_QUERIES`** -- A plain-text reference file with example Prolog queries and ROS launch commands for testing the system interactively via `rosprolog`.

### OWL Ontologies (`owl/`)

- **`objects_affordances_attributes.owl`** -- The main ontology defining the domain model. Contains:
  - **Object properties**: `hasObjectMaterialType`, `hasObjectShapeType`, `hasObjectUsedFor`
  - **Attribute classes**: Materials (`Ceramic`, `Plastic`, `Clear`, `Wet`), Shapes (`Round`, `Long`, `Rectangular`), Affordances (`CleaningEvent`, `DrinkingEvent`, `EatingEvent`)
  - **Object classes**: `Cup`, `Plate`, `Soap`, `Sponge`, `Sprayer`, `DishwashingSoap`, `LaundryDetergent` -- each with OWL restrictions linking them to their material, shape, and affordance
  - **Individuals**: Pre-instantiated objects (e.g., `Cup_1`, `Plate_1`, `Sponge_1`) and attribute instances

- **`niklasComputables.owl`** -- Defines KnowRob computable properties and classes that bind Prolog predicates to OWL reasoning. Registers `comp_onTopTable` as a property computable and `comp_newInstance` as a class computable.

- **`catalog-v001.xml`** -- XML catalog file mapping ontology URIs to local OWL files for the OWL parser.

### C++ Source (`src/`)

- **`computablesCpp.cpp`** -- The main ROS/YARP bridge node. Initializes a `json_prolog` connection to KnowRob, sets up YARP buffered ports to receive object classifications from the GURLS vision pipeline (`/GURLS_object_out`, `/GURLS_material_out`, `/GURLS_shape_out`, `/GURLS_affordance_out`), constructs and executes Prolog queries to identify objects, and implements an interactive learning loop: when no matching object is found, the operator can provide corrections and the system asserts the new knowledge into the ontology and exports it as an OWL file.

### SWIG Bindings (`src/`)

- **`icub.py`**, **`yarp.py`**, **`_icub.so`**, **`_yarp.so`** -- Auto-generated SWIG Python bindings for the iCub and YARP libraries. These provide Python-level access to iCub's Cartesian and Gaze controllers and the YARP middleware layer. They are generated artifacts, not hand-written code.

### Launch Files (`launch/`)

- **`niklas_computables_cpp.launch`** -- ROS launch file that starts the `json_prolog` node with the `niklas_package` knowledge base and parses the main OWL ontology on startup.

### Build Configuration

- **`CMakeLists.txt`** -- Catkin/CMake build file. Declares dependencies on `json_prolog`, `knowrob_actions`, `knowrob_map_data`, `knowrob_map_tools`, `roscpp`, `rospy`, `std_msgs`, YARP, and rosjava packages. Builds the `computablesCpp_node` executable.

- **`package.xml`** -- ROS package manifest declaring build and runtime dependencies.

## Dependencies

- **ROS** (Robot Operating System) -- tested with ROS Indigo/Jade era distributions
- **KnowRob** -- knowledge processing framework for robots (packages: `knowrob_common`, `knowrob_actions`, `knowrob_map_data`, `knowrob_map_tools`, `knowrob_objects`)
- **SWI-Prolog** -- used by KnowRob for semantic reasoning (with `semweb`, `owl`, and `rdfs_computable` libraries)
- **json_prolog** -- ROS package providing a JSON-based Prolog query interface
- **YARP** (Yet Another Robot Platform) -- middleware for iCub robot communication
- **iCub software** -- libraries and SWIG bindings for the iCub humanoid robot
- **GURLS** -- machine learning library used for visual object classification (external to this package)
- **catkin** -- ROS build system

## Usage

Start the knowledge base and Prolog reasoning engine:

```bash
roslaunch niklas_package niklas_computables_cpp.launch
```

Run the C++ bridge node (requires GURLS vision pipeline to be active on YARP ports):

```bash
rosrun niklas_package computablesCpp_node
```

For interactive Prolog queries:

```bash
rosrun rosprolog rosprolog niklas_package
```

Example queries within the Prolog shell:

```prolog
% Initialize object definitions
definitions:setDefinitions(A,B,C,D,E,F,G,H,I).

% Create a new instance of Cup
create_instance_from_class('http://www.semanticweb.org/niklas/ontologies/2016/3/icubworld.owl#Cup', 1, X).

% Query object properties
owl_has(A, icubworld:'hasObjectMaterialType', icubworld:'Ceramic').

% Find all objects with specific attributes
owl_has(A, icubworld:'hasObjectMaterialType', icubworld:'Ceramic'),
owl_has(A, icubworld:'hasObjectShapeType', icubworld:'Round'),
owl_has(A, icubworld:'hasObjectUsedFor', icubworld:'EatingEvent').
```

## License

The Prolog initialization code is licensed under the GNU General Public License v3 (GPLv3), as noted in `init.pl`. The OWL ontology `objects_affordances_attributes.owl` includes content derived from KnowRob (TUM) and OpenCyc, licensed under Creative Commons Attribution 3.0.
