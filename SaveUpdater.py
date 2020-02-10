import json;
import os;

#oldSave = 'GameSlot1.sav_pyromancer.bak';
oldSave = os.listdir('./old')[0];
newSave = os.listdir('./new')[0];

#Load both savegames
with open('./old/' + oldSave, encoding="utf8") as oldF:
    oldData = json.load(oldF);
with open('./new/' + newSave, encoding="utf8") as newF:
    newData = json.load(newF);
#Save the wipe version
wipeVersion = newData["Wipe Version"];
#Update all the values in the new save with the values of the old one
newData.update(oldData);
#But keep the new save wipeversion so the game accepts it
newData["Wipe Version"] = wipeVersion;

#Write out the save file
with open('GameSlot1.sav','w') as outFile:
    json.dump(newData,outFile);
