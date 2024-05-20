# tpsDig-Data-Processing
This repository contains the code used to process data exported from tpsDig for MorphJ input.
___
### [Open OFFICIAL tpsDIG Data Cleanup.py](OFFICIAL-tpsDIG-Data-Cleanup.py)
The purpose of this code is to reformat the data created when landmarking images in tpsDig2 (Rohlf 2004) into the correct 'tps format' for MorphoJ (Klingenberg 2011) processing. The simple program can be ran in the command line, Python Shell, or similar interface.

> [!IMPORTANT]
> Based on how your image files are named, this code to extract the specimen number may not work for you. The program gets the name of the image file by separating the string based on the image naming style, which was created by the ZEISS Smartzoom5 program and imaging system. In this case, all the images had underscores in the file name to distinguish certain data (i.e., magnification and specimen number). The program may need further tweaks depending on the initial image file names used in your project.


#### Required data/software
* Text editor such as Notepad, Python IDLE, or VS Code.
* Interface to run the code such as Python Shell or command line.
* File with a list of Unique Identifier Codes (UICs) that corresponds to each specimen and its data.
  * E.g., a UIC may contain species, sex, and specimen ID# and appear as 'FAWM0054', where FAW = fall armyworm (species), M = male (sex), and 0054 = ID#54.
  * This file should be named "OFFICIAL-UICs-CleanedData.txt"; otherwise, the name in [Open OFFICIAL tpsDIG Data Cleanup.py](OFFICIAL-tpsDIG-Data-Cleanup.py) should be modified.
* File with annotated landmark data from tpsDig2 (Rohlf 2004).

#### Complete the following steps in order to run the code properly:
1. Use tpsDig2 software to annotate landmarks on images.
2. Download and open [Open OFFICIAL tpsDIG Data Cleanup.py](OFFICIAL-tpsDIG-Data-Cleanup.py)
3. Follow the "TO DO" instructions within the file to use on your computer (e.g., rewriting file directories/names)
4. Run the program and follow on-screen instructions.

#### References
* Klingenberg, C. P. 2011. MorphoJ: an integrated software package for geometric morphometrics. Molecular Ecology Resources 11: 353-357.
* Rohlf, F. J. 2004. tpsDig, digitize landmarks and outlines, version 2.0. Department of Ecology and Evolution, State University of New York at Stony Brook.
