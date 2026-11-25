# Loudspeaker acoustics projects: PRONTO and PCE

Two IMT Atlantique engineering projects on loudspeaker design: Python analysis scripts, simulation exports and CAD files.

## PRONTO: tuning a 10-inch bass-reflex subwoofer (first year, 2025)

Team: Mathéo Cail, Raphaël Hierso-Iglesias, Ismaël Lahriri, Martin Leducq.

Design and build of a 10-inch passive bass-reflex subwoofer for home cinema or studio use. The requirements set an effective response between 50 and 150 Hz and a maximum sound pressure level above 120 dB at 1 m. A key step is sizing the port (the vent), whose length sets the tuning frequency of the enclosure.

The Python scripts process sound pressure level (SPL) curves for several port geometries:

- for each geometry (two cylindrical ports, four cylindrical ports), they plot SPL against frequency for four port lengths;
- they find the frequency of the SPL peak for each length, fit a least-squares line linking port length to that frequency, and deduce the length that tunes the enclosure to 50 Hz;
- they then compare the chosen designs, and the two-cylinder port against a rectangular port.

**Result:** a 50 Hz tuning needs a port length of about **266 mm** with two cylindrical ports, or **90 mm** with four.

```bash
pip install numpy matplotlib
python pronto/2_cylindres/Traitement_2_cylindres.py
```

Each script reads the data files stored in its own folder.

## PCE: driver and enclosure simulation in COMSOL (second year, 2025)

- Lumped-parameter loudspeaker models in COMSOL Multiphysics 6.3, built from the drivers' Thiele–Small parameters (moving mass, suspension compliance, force factor, voice coil resistance and inductance), for 6HX150 and 8HX200 drivers.
- Comparison of a simple-disk diaphragm with the real diaphragm shape.
- Parametric sweeps of the enclosure's internal dimensions and volume, with their effect on the SPL at 1 m (`pce/results/`, `pce/volumes.txt`).
- Coaxial driver parameters and enclosure CAD (SolidWorks part, with STEP, STL and Parasolid exports).

The COMSOL model files (`.mph`, from 100 MB to about 1 GB) are not included: they exceed GitHub's file size limit.

## Structure

```
pronto/
├── 2_cylindres/    SPL data and script, two cylindrical ports
├── 4_cylindres/    SPL data and script, four cylindrical ports
├── li/             SPL data and script, the chosen port lengths
├── comparaison/    SPL data and script, two-cylinder vs rectangular port
└── Pronto_suivi_projet-3.pdf   project brief and requirements (French)
pce/
├── cad/            driver CAD files (STEP)
├── coax/           coaxial driver parameters and enclosure CAD
├── essai_comsol/   first COMSOL test (lumped loudspeaker driver)
├── results/        exported SPL results
├── 6HX150_parameters.txt
└── volumes.txt
```

## Tech

Python (NumPy, Matplotlib), COMSOL Multiphysics, SolidWorks.
