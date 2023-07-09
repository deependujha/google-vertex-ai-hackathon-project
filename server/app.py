from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import random
import string
import json
import os
from utilsHtml.htmlParts import (
    productDescription,
    navbarColor,
    navbarToCarousel,
    headingTitle,
    leftHeading,
    contactAndCopyRight,
)
from palmAPI import get_response_from_palmAPI, prompt, prompt_output
import shutil


app = Flask(__name__)
CORS(app)

# get current working directory
parent_dir = os.getcwd()
source = os.path.join(parent_dir, "BASEHTML")
destination = os.path.join(parent_dir, "generatedWebsite")


colors = ["blue", "purple", "pink", "orange", "green"]


# recursively copy entire directory tree
def copyTheWholeDirectory(source, destination):
    for file_name in os.listdir(source):
        # check if it is a file
        if os.path.isfile(f"{source}/{file_name}"):
            sourceFileName = f"{source}/{file_name}"
            destinationFileName = f"{destination}/{file_name}"
            # copy only files
            shutil.copy(sourceFileName, destinationFileName)
            print("copied", file_name)

        else:
            # create new directory in destination folder
            newDestination = f"{destination}/{file_name}"
            os.mkdir(newDestination)

            # recursively call the function to copy all the files inside the directory
            sourceDirectory = f"{source}/{file_name}"
            copyTheWholeDirectory(sourceDirectory, newDestination)


# function that takes businessName and description and returns a json object with 8 points
def getPoints(businessName, description):
    myPrompt = (
        prompt.format(
            busName=businessName,
            desc=description,
        )
        + prompt_output
    )
    print(myPrompt)
    print("-------------------")
    response = get_response_from_palmAPI(myPrompt)

    # sanatising the response
    myResponse = ""
    isStarted = False
    for myChar in response:
        if myChar == "{":
            isStarted = True
            myResponse += myChar
        elif myChar == "}":
            isStarted = False
            myResponse += myChar
            break
        elif isStarted:
            myResponse += myChar

    print(myResponse)
    jsonResponse = json.loads(myResponse)

    print(jsonResponse)

    bulletPoints = {
        f"desc{i + 1}": point for i, point in enumerate(jsonResponse["points"])
    }
    print(bulletPoints)
    return bulletPoints


# function to copy all the files from one directory to another
def copyFiles(name):
    path = os.path.join(destination, name)
    os.mkdir(path)

    # recursively copy entire directory tree
    copyTheWholeDirectory(source, path)


# function to write html to file
def writeHtmlToFile(file_path, data):
    i = random.randint(0, len(colors) - 1)
    # first empty the file
    with open(file_path, "w") as file:
        file.write("")
    with open(file_path, "a") as file:
        _extracted_from_writeHtmlToFile_8(file, data, i)


# TODO Rename this here and in `writeHtmlToFile`
def _extracted_from_writeHtmlToFile_8(file, data, i):
    # Append content to the file
    file.write(headingTitle.format(businessName=data["name"]))
    file.write(leftHeading)
    file.write(navbarColor.format(color=colors[i]))
    file.write(navbarToCarousel)
    file.write(
        productDescription.format(
            desc1=data["desc1"],
            desc2=data["desc2"],
            desc3=data["desc3"],
            desc4=data["desc4"],
            desc5=data["desc5"],
            desc6=data["desc6"],
            desc7=data["desc7"],
            desc8=data["desc8"],
            color=colors[i],
        )
    )
    file.write(contactAndCopyRight.format(color=colors[i]))


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/create-website", methods=["POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        bulletPoints = getPoints(data["name"], data["desc"])
        bulletPoints["name"] = data["name"]

        randomDirectoryName = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        )
        print(randomDirectoryName)
        copyFiles(randomDirectoryName)
        writeHtmlToFile(
            f"./generatedWebsite/{randomDirectoryName}/index.html", bulletPoints
        )

        # Zip the folder
        dir_name = os.path.join(parent_dir, f"generatedWebsite/{randomDirectoryName}")
        output_filename = f"generatedZIP/{randomDirectoryName}"
        shutil.make_archive(output_filename, "zip", dir_name)

        # return jsonify(bulletPoints)
        file_path = f"./generatedZIP/{randomDirectoryName}.zip"

        # Send the file to the frontend
        return send_file(file_path, as_attachment=True)
        # return "This is a POST request"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
