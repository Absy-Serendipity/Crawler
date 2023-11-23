import json
import os
from selenium import webdriver

class Crawler:
    def createFolder(self):
        try:
            currentDirectory = os.path.dirname(os.path.abspath(__file__))
            folderPath = os.path.join(currentDirectory, self.platformName)
        except:
            folderPath = self.platformName

        try:
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
                print(f"Folder '{folderPath}' created successfully")
            else:
                print(f"Folder '{folderPath}' already exists")
        except OSError:
            print("Error: Failed to create the directory.")

        folderPath = os.path.join(self.platformName, "webtoons")
        try:
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
                print(f"Folder '{folderPath}' created successfully")
            else:
                print(f"Folder '{folderPath}' already exists")
        except OSError:
            print("Error: Failed to create the directory.")
        
    def saveToJson(self, fileName, data):
        with open(fileName + ".json", "w", encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile, indent=4, ensure_ascii=False, default=self.serialize)
    
    def serialize(self, obj):
        return obj.__dict__