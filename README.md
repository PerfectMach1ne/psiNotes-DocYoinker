# psiNotes-DocYoinker

## omega Notes/psi Notes link

#### [Table of Contents](https://docs.google.com/spreadsheets/d/15nSuKrllBI4PdawNSxqVGMqnc-CjYMN8A3c6kASYd9Y/edit#gid=0)
#### [Notebook Zero](https://docs.google.com/document/u/0/d/1fz6j5w-gRXjCB6A2YbGQ8nM6YWFTutaRBLvcFss0ZpI/edit)
#### [Notebook M1 - Mathematics I](https://docs.google.com/document/u/0/d/1fz6j5w-gRXjCB6A2YbGQ8nM6YWFTutaRBLvcFss0ZpI/edit)
#### [Notebook M2 - Mathematics II](https://docs.google.com/document/d/1atUiihcPNvC6ZJ6zaNojDx4xlyAYLdFpMfhGF_0AS8A/edit)
#### [Notebook M3 - Mathematics III](https://docs.google.com/document/d/1B3wYPnc0o-pXTQ9-VUc_LiJ6paK7evIwy9SeTKGXFDc/edit)
#### [Notebook P1 - Physics I](https://docs.google.com/document/d/1Rd4AC_L55x6gUJv-PJml873m1Dfjos9FKvycyKInA8U/edit)
#### [Notebook P2 - Physics II](https://docs.google.com/document/d/1RSSwYydFolNc4p4JK-naT1SZMQHPtWL2R5GO0KgQIp0/edit)
#### [Notebook C1 - Chemistry I](https://docs.google.com/document/d/1X2yIsOxmf8Ic6RYuAG5ZV9Ru9OOH3aloRcAKSjDRkGM/edit)
#### [Notebook C2 - Chemistry II](https://docs.google.com/document/d/1fLyzY6NaSRK1DbRcdNZOQK3fufGBCBDGdtRs6qczpfw/edit)
#### [Notebook EE1 - Electrical Engineering I](https://docs.google.com/document/d/1ystzIw9OHbofu2B4iGF6gWu2fW9T4bQYbCz05yY1KxY/edit)
#### [Notebook A&M - Astronomy & Meteorology](https://docs.google.com/document/d/1xvy_JRqsYY-qSEcwylL_5nBubLNtkDJb5otq_C_03hY/edit)
#### [Notebook B1 - Biology I](https://docs.google.com/document/d/1zWZL0GyYb_uM2vJaP384nmyajioygD1viWTZuCSl5sU/edit)
#### [Notebook CS](https://docs.google.com/document/d/1bJfCXJYjRITR9V7hJwZ2iaY7Leld8PIdRR4h51N8nCU/edit)

## How to use

### Prerequisites

- Access to my Google Account (good luck).
- Up to date Google API credentials and token (credentials.json in ./app/ or a safer place).
- A virtual environment /w requirements installed:
#### `python -m venv .venv`
#### `pip install -r requirements.txt`

## The "master plan pipeline"
- [x] ~~Put the GDoc Document object's JSON in a `.json`.~~ 
- [ ] Option to check what docs are downloaded to not waste bandwith. (and also compare revisionId to see if there were any changes.)
- [ ] Save doc metadata somewhere.
- [ ] Make a stash of functions to handle different parts of it.
- [x] ~~First, the hard part - search for all images and their positions (so, `PositionedObject`'s).~~ "hard part" lol
- [ ] Download all of the images to `../yoinkstash/pos_objs/` and put their ID's into `../yoinkstash/pos_objs/rawposobjs.json`
- [ ] Then grab all the text and tables.
- - [ ] Find and put tables in a `../yoinkstash/tables/tables.json`
- [ ] The rest goes to `../yoinkstash/text/rawtext.json`
- - [ ] Develop some system to identify your headers and etc (initially only for Notebook Zero).
- - [ ] Implement an separate general header segmenting system for non-Notebook-Zero notebooks.
- - - [ ] Split `rawtext.json` into `segtext.json` (segmented text). 09/11/24 NOTE: maybe that's stupid.
- [ ] Make the app into a CLI to control what it is supposed to do any given time.
- **<❗>** Everything stores its position!
- [ ] The first hellish attempt at trying to convert everything to XML ~~or even HTML~~...
- - **<❗>** ....but maybe converting the JSON data into a very decent XML format i can engineer is a better idea?
### 1-image project explanation
![A meme](me_irl.png)
