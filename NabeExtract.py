import os
import json

from pathlib import Path
from shutil import copyfile, move

import UnityPy

# inputted json of seen assets from the previous tours to be modified and saved as output
seen_assets = {}
# copy of the seen assets json which does not include anything added from the current intake
prior_assets = {}

def unpack_all_assets(source_folder: str, destination_folder: str):
    Path("Output\\Sprite").mkdir(parents=True, exist_ok=True)
    Path("Output\\Texture2D").mkdir(parents=True, exist_ok=True)

    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            try:
                # generate file_path
                file_path = os.path.join(root, file_name)
                # load that file via UnityPy.load
                env = UnityPy.load(file_path)

                # iterate over internal objects
                for obj in env.objects:
                    # process specific object types
                    if obj.type.name in ["Sprite"]:
                        # parse the object data
                        data = obj.read()

                        # create destination path
                        dest = os.path.join(os.path.join(os.path.join(cwd, "Output"), "Sprite"), data.name)

                        # make sure that the extension is correct
                        # you probably only want to do so with images/textures
                        dest, ext = os.path.splitext(dest)
                        dest = dest + ".png"

                        img = data.image
                        img.save(dest)

                        if data.name not in seen_assets:
                            seen_assets['Sprite'].append(data.name)

                    if obj.type.name in ["Texture2D"]:
                        # parse the object data
                        data = obj.read()

                        # create destination path
                        dest = os.path.join(os.path.join(os.path.join(cwd, "Output"), "Texture2D"), data.name)

                        # make sure that the extension is correct
                        # you probably only want to do so with images/textures
                        dest, ext = os.path.splitext(dest)
                        dest = dest + ".png"

                        img = data.image
                        img.save(dest)

                        if data.name not in seen_assets:
                            seen_assets['Texture2D'].append(data.name)

            except Exception as e:
                print(f"Exeception on {file_name}")
                print(e)

def generate_new_images():
    Path("Output\\Sprite (New)").mkdir(parents=True, exist_ok=True)
    Path("Output\\Texture2D (New)").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)").mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(os.path.join(os.path.join(cwd, "Output"), "Sprite")):
        for i in files:
            if i[0:-4] not in prior_assets['Sprite']:
                copyfile(os.path.join(root, i), os.path.join(cwd, "Output\\Sprite (New)\\" + i))
                copyfile(os.path.join(root, i), os.path.join(cwd, "Output\\Sprite (Sorted)\\" + i))

    for root, dirs, files in os.walk(os.path.join(os.path.join(cwd, "Output"), "Texture2D")):
        for i in files:
            if i[0:-4] not in prior_assets['Texture2D']:
                copyfile(os.path.join(root, i), os.path.join(cwd, "Output\\Texture2D (New)\\" + i))


def sort_output():
    Path("Output\\Sprite (Sorted)\\Badges").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\Banner").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\Cups").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\CourseIcons").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\FaceEntry").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\Machine").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\UpperBody").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\WholeBody").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\Wing").mkdir(parents=True, exist_ok=True)
    Path("Output\\Sprite (Sorted)\\Others").mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(os.path.join(os.path.join(cwd, "Output"), "Sprite (Sorted)")):
        for i in files:
            found = False

            if "banner" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Banner\\" + i))
                found = True

            if "Cup.png" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Cups\\" + i))
                found = True

            if "WholeBody.png" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\WholeBody\\" + i))
                found = True

            if "UpperBody.png" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\UpperBody\\" + i))
                found = True

            if "FaceEntry.png" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\FaceEntry\\" + i))
                found = True

            if "_Large.png" in i and "Machine" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Machine\\" + i))
                found = True

            if "_Large.png" in i and "Wing" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Wing\\" + i))
                found = True

            if "pb0" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Badges\\" + i))
                found = True

            if "_main_" in i or "_sub.png" in i or "_BG" in i:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\CourseIcons\\" + i))
                found = True

            if found is False:
                move(os.path.join(root, i), os.path.join(
                    cwd, "Output\\Sprite (Sorted)\\Others\\" + i))

def b_renamer():
    asset_json = {}

    with open('AllBAssetNames.json') as f:
        contents = f.read()
        asset_json = json.loads(contents)
    
    for root, dirs, files in os.walk(os.path.join(os.path.join(cwd, "Input"),"b")):
        for filename in files:
            with open(os.path.join(root, filename), 'r', errors="ignore") as f:
                try:
                    rename =  "Output/Renamed/" + asset_json[filename]
                except KeyError:
                    rename = "Output/Renamed/Unknown/" + filename
                except:
                    print("An exception occurred")
                pathrename = rename[0:rename.rfind('/')]
                pathrerename = pathrename.replace('/', '\\')
                Path(pathrename).mkdir(parents=True, exist_ok=True)
                old_path =  os.path.join(os.path.dirname(os.path.dirname(root)), pathrerename)
                new_path = rename[rename.rfind('/')+1:]
                if new_path not in seen_assets['b']:
                    seen_assets['b'].append(new_path)
                if "_msbt.bytes" in new_path:
                    new_path = new_path.replace("_msbt.bytes",".msbt")
                
                if ".pck" in new_path:
                    new_path = new_path.replace(".pck","")

                copyfile(os.path.join(root, filename), os.path.join(old_path, new_path))

    Path("Output\\Renamed\\Audio (New)").mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(os.path.join(os.path.join(os.path.join(cwd, "Output"), "Renamed"), "Audio")):
        for i in files:
            if i + ".pck" not in prior_assets['b']:
                copyfile(os.path.join(root, i), os.path.join(os.path.dirname(os.path.dirname(root)), "Audio (New)\\" + i))

### Perform ###
# get current working directory
cwd = os.getcwd()
# create output folder
Path("Output").mkdir(parents=True, exist_ok=True)
# open and store the seen assets json twice
with open('SeenAssets.json') as f:
    contents = f.read()
    seen_assets = json.loads(contents)
    prior_assets = json.loads(contents)
# run the unpacker and store the output
unpack_all_assets(os.path.join(cwd, "Input"), os.path.join(cwd, "Output"))
# compare the output with the seen assets json to get just the new images from the prior dump
generate_new_images()
# sort files based on their name into folders to be used in my github repo
sort_output()
# rename all 'b' folder files to their proper names and with proper pathing
b_renamer()
# save the json back with the new entries from this dump
print('Done, saving JSON')
with open('SeenAssets.json', 'w') as outfile:
    json.dump(seen_assets, outfile, indent=4)
