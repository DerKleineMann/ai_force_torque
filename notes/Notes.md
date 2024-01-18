# Ai Force Torque Control (See Notion)

## Thesis

### Links

[Overleaf LaTeX](https://www.overleaf.com/learn/latex/How_to_Write_a_Thesis_in_LaTeX_(Part_1)%3A_Basic_Structure)  
[Dissertation structure](https://gradcoach.com/dissertation-structure/)

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

[Link](https://sci-intern.hm.edu/fk/forms/abschlussarbeiten.php?studgang=PAB)