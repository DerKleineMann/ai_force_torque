# Ai Force Torque Control (See Notion)

## Thesis

### Links

[Overleaf LaTeX](https://www.overleaf.com/learn/latex/How_to_Write_a_Thesis_in_LaTeX_(Part_1)%3A_Basic_Structure)  
[Dissertation structure](https://gradcoach.com/dissertation-structure/)

### Plan

1. Title page
2. Acknowledgements
3. Abstract
4. Table of contents
5. Core chapters
    1. Introduction
        1. GreenBot AI project
        2. Core research question
        3. Use-cases & aims
    2. State of the art / literature review
        1. State of the art : AI
        2. State of the art : Peg-in-hole assembly using robots
        2. State of the art : Robot automation & AI
        3. Research basis (literature)
    3. Methodology
        1. Segmentation of processes
        2. Neural network base structure
        3. Optimization of hyperparameters
        4. Results review methodology (result metrics)
    4. Results
        1. Basic tests (before optimization)
        2. Advanced tests (optimization algorithms)
    5. Discussion
        1. Stress-testing results
        2. Generalization of piloting algorithm
        3. Precision of AI-based piloting
        4. Improvement ideas
    6. Conclusion
6. Reference list
7. Appendix

## Code

### File summary

- Environment check
- Data preparation
- Keras Tuner files
- Result visualization

### Data preparation

1. Import the data from the test zip folder
2. Transform the data to match the labels
3. Reshape data to the last XXXX points
4. Rename columns and select the rights ones (relevant ones)
5. Add the 'key' column
6. Merge every dataframe into one and save for later use

### Data visualization 

- 3D Vis of graphs
    - Average per joint per point
    - Amp per joint per point

### Folder pathing

- Data folder : datasets from robot
    - Packages : compressed datasets taken raw from KUKA Sunshine
    - Unzipped to import to dataframe
    - Deleted after saving the feather file


### Erfassungsbogen 

https://sci-intern.hm.edu/fk/forms/abschlussarbeiten.php?studgang=PAB


