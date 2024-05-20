# tpsDig-Data-Processing
This repository contains the code used to process data exported from tpsDig for MorphJ input.

### [Open OFFICIAL tpsDIG Data Cleanup.py](docs/Open-OFFICIAL-tpsDIG-Data-Cleanup.py)
The purpose of this code is to reformat the data created when landmarking images in tpsDig2 (Rohlf 2004) into the correct 'tps format' for MorphoJ (Klingenberg 2011) processing. The program can be ran in the command line, Python IDLE, or similar interface.

> [!IMPORTANT]
> Based on how your image files are named, this code to extract the specimen number may not work for you. The program gets the name of the image file by separating the string based on the image naming style, which was created by the ZEISS Smartzoom5 program and imaging system. In this case, all the images had underscores in the file name to distinguish certain data (i.e., magnification and specimen number). The program may need further tweaks depending on the initial image file names used in your project. 

Complete the following steps in order to run the code properly:
1. Use tpsDig2 software to annotate landmarks on images.
2. Download and open [Open OFFICIAL tpsDIG Data Cleanup.py](Open-OFFICIAL-tpsDIG-Data-Cleanup.py)
3. Follow the "TO DO" instructions within the file to use on your computer (e.g., rewriting file directories/names)
4. Run the program and follow on-screen instructions.

#### References
* Klingenberg, C. P. 2011. MorphoJ: an integrated software package for geometric morphometrics. Molecular Ecology Resources 11: 353-357.
* Rohlf, F. J. 2004. tpsDig, digitize landmarks and outlines, version 2.0. Department of Ecology and Evolution, State University of New York at Stony Brook
