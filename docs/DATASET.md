# Dataset Documentation

## Dataset Name
WM-811K / Silicon Wafer Defect Dataset

## Dataset Source
Local Archive (`archive.zip`)

## Dataset File Structure
The raw dataset was extracted and verified. The contents are as follows:
```
data/
└── raw/
    └── LSWMD.pkl
```

The primary file is `LSWMD.pkl`, which is a pandas DataFrame stored in pickle format containing the wafer map data and associated metadata.

## Wafer Map Representation
- Wafer maps are typically represented as 2D arrays (matrices).
- Each cell in the matrix corresponds to a die on the wafer.
- Typical values represent:
  - Background / non-wafer area
  - Normal / passing die
  - Defective die

## Target / Label Information
The dataset typically includes labels for different defect patterns (e.g., Center, Donut, Edge-Loc, Edge-Ring, Loc, Random, Scratch, Near-full).

## Relevant Attributes
Based on typical structures of the WM-811K dataset:
- `waferMap`: The 2D array representation of the wafer.
- `dieSize`: The number of dies on the wafer.
- `lotName`: Identifier for the lot.
- `waferIndex`: Identifier for the wafer within the lot.
- `failureType`: The target label representing the defect pattern.
- `trianTestLabel`: Indicates if the sample is intended for training or testing.
