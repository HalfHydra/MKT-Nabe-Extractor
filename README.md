# MKT-Nabe-Extractor
This python script was made in order to simplify the process of extracting data from the Mario Kart Tour game. It uses UnityPy as the way to decompile and iterate through the different assets inside each of the unity asset bundles. A json of all the assets that were already seen is kept inside the "SeenAssets.json" file in order to output a separate folder of only what was added in the newest dataset compared to the previous. A sample copy of this has been included in the repository for the assets downloaded to my game.

The script takes as input the "Nabe" folder from the game which contains all of the assets that were needed to be downloaded locally for that version of the game. 

The files of type "Sprite" and "Texture2D" are what is outputted by this script, and based on filenames, can be sorted to what they are. 

Using another file as input which can be dumped from the game the runtime whenever possible, a way to rename the files for the "b" folder is also supported, taking as input "AllBAssetNames.json". A sample has been provided in the repository for the assets downloaded to my game.

The assets include all new item icons, course icons, badges, audio, as well as localization string files, audio banks, and so much more. 
