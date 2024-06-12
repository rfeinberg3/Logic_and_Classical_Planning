
# Project 3: Logic and Classical Planning

## Introduction

In this project, we utilize simple Python functions to generate logical sentences describing Pacman physics (pacphysics) and employ a SAT solver, pycosat, to solve various logical inference tasks. These tasks include:
- **Planning**: Generating action sequences for Pacman to reach goal locations and eat all the dots.
- **Localization**: Determining Pacman's location on the map given a local sensor model.
- **Mapping**: Building the map from scratch.
- **SLAM**: Simultaneous localization and mapping.

The assignment includes an autograder to facilitate grading answers locally. Use the command:
```sh
python autograder.py
```

## Project Files

### Files to Edit
- `logicPlan.py`: Main file where logical agent code is implemented.

### Files to Review
- `logic.py`: Contains propositional logic code with utility functions.
- `logicAgents.py`: Defines logical planning problems for Pacman.
- `pycosat_test.py`: Tests pycosat module installation.
- `game.py`: Simulator code for Pacman world, particularly the `Grid` class.

### Files to Ignore
- `pacman.py`: Main file for running Pacman games.
- `logic_util.py`: Utility functions for `logic.py`.
- `util.py`: General utility functions.
- `logic_planTestClasses.py`: Project-specific autograding test classes.
- `graphicsDisplay.py`: Graphics for Pacman.
- `graphicsUtils.py`: Support for Pacman graphics.
- `textDisplay.py`: ASCII graphics for Pacman.
- `ghostAgents.py`: Agents controlling ghosts.
- `keyboardAgents.py`: Keyboard interface to control Pacman.
- `layout.py`: Code for reading and storing layout files.
- `autograder.py`: Project autograder.
- `testParser.py`: Parses autograder test and solution files.
- `testClasses.py`: General autograding test classes.

## Evaluation

Your code will be autograded for technical correctness. Adhere to function and class naming conventions to avoid autograder issues. Your implementation's correctness will ultimately determine your score. 

## Academic Integrity

Submit original work. We will use code similarity detection tools to identify plagiarism.

## Getting Help

Utilize course resources, including office hours, section, and discussion forums for support.

## Grade Weighting

The project score totals 100 points. Each section's score is multiplied by 4, with the last question offering 2 extra credit points.

## Tasks Overview

### Expr Class

- **sentence1()**: Represents a conjunction of three given sentences.
- **sentence2()**: Represents a conjunction of four given sentences.
- **sentence3()**: Creates symbols and an expression encoding three English sentences as propositional logic.
- **findModelCheck()**: Mimics `findModel` output.
- **entails(premise, conclusion)**: Determines if the premise entails the conclusion.
- **plTrueInverse(assignments, inverse_statement)**: Evaluates the inverse statement given assignments.

### Logic Workout

- **atLeastOne(literals)**: Returns an expression true if at least one literal is true.
- **atMostOne(literals)**: Returns an expression true if at most one literal is true.
- **exactlyOne(literals)**: Returns an expression true if exactly one literal is true.

### Pacphysics and Satisfiability

- **pacmanSuccessorAxiomSingle**: Defines conditions for Pacman’s location at time t.
- **pacphysicsAxioms**: Generates pacphysics axioms.
- **checkLocationSatisfiability**: Returns models proving Pacman's possible and impossible locations.

### Path Planning with Logic

- **positionLogicPlan(problem)**: Generates action sequences to reach the goal.

### Eating All the Food

- **foodLogicPlan(problem)**: Generates action sequences to eat all the food.

### Localization

- **localization(problem, agent)**: Yields possible locations at each timestep.

### Mapping

- **mapping(problem, agent)**: Yields map knowledge at each timestep.

### SLAM (Extra Credit)

- **slam(problem, agent)**: Yields map knowledge and possible locations at each timestep.

## Installation and Setup

To install the required `pycosat` module:
1. Activate your conda environment:
```sh
conda activate cap4621
```
2. Install pycosat:
```sh
pip install pycosat
```
or
```sh
conda install -c anaconda pycosat
```

Test installation:
```sh
python pycosat_test.py
```