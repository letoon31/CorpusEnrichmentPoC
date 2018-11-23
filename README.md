# Enrichment_Project
The code of the PoC of the cognitive corpus enrichment project, by Laurent Goujon and Elie Azeraf.

## Presentation
 
The corpus enrichment project is a project to enrich automatically cognitive corpus from an external corpus, depending on questions asked by a user to a chatbot. 

As an example, we have the following cognitive corpus (a JSON dataset in our example): <br />
<img align="middle" src="images/dataset_init.png" width="35%"> <br />
This dataset is linked with a chatbot. <br />
We also have an external corpus where the algorith will fetch the answer if the answer is not in our dataset (for the example we have all the Wikipedia articles).

A user comes and asks: <br />
<img src="images/image_user_city_superman.png" width="40%"> <br />
Here, the answer is in our dataset, so the chatbot will simply answer: <br />
<img src="images/image_assistant_metropolis.png" width="40%"> <br />
This is the very classical case.

But now, a user comes and asks: <br />
<img src="images/image_user_archenemy_batman.png" width="40%"> <br />
As you can see, the answer is not in our dataset. <br />
Instead of answering "Sorry, I can't help you.", with our enricher algorithm, the user will have the answer in only 3s: <br />
<img src="images/image_assistant_joker.png" width="40%"> <br />
On the other hand, our dataset is enriched: <br />
<img align="middle" src="images/dataset_after_archenemy.png" width="35%"> <br />

Indeed, thanks to an Open Domain Question Answering algorithm, we have the ability to find the answer in our external corpus. <br />
Moreover, for people who knows these chatbot concepts, the assistant parameters (intent, entity, dialog tree) are also enriched. <br />
METTRE TABLEAU AVANT APRES INTENTS ENTITIES

## Installation

### Cloning the project

First of all, clone or download the git project.
```
git clone https://github.com/toto222/Enrichment_Project.git
cd Enrichment_Project
```

### Python and node.js requirements

To use the algorithm and test our PoC, you have some installation to do. <br />
You must have Linux or OSX and 16Go of RAM.

If you want to insure your local packages in python, it is recommended to create a new environment on Anaconda (optionnal):
```
conda create -n Enrichment_Project python=3.6
activate Enrichment_Project (for Windows users)
source activate Enrichment_Project (for Linux/OSX users)
```

First of all, you have to install PyTorch. <br />
If your computer have a compatible GPU with CUDA X.X:
```
conda install pytorch=0.4.0 cudaXX -c pytorch
```
Otherwise, if you don't have a GPU or if you don't want to use it:
```
conda install pytorch=0.4.0 -c pytorch
```

Then, run the following code on your command prompt: 
```
pip install -r requirements.txt ; python setup.py develop
npm install watson-developer-cloud@3.9.0
```

### Downloading files

To download all the file needed for the project, you have to dowload the data file: 
https://ibm.box.com/s/igyavfyg98kgfar3pm045jtu3q16oh0u
Then, unzip it and place it in the Code_Enrichment_Project folder.

### Verification

Now, your folder must be like this:
```
Code_Enrichement_Project
|
-- data (folder)
-- drqa (folder)
-- Objects (folder)
-- scripts (folder)
-- main.py (python file)
-- setup.py (python file)
-- requirements.txt (text file)
```

## Demo

Now you can launch your algorithm on your command prompt (you much have your environment activated):
```
(Enrichment_Project) path/to/code/folder> python main.py
```

You are asked of you want to see the logs, we send y for yes. <br />
Then, you have about 7 minutes of initialisation, after that you have the interactive mode: <br />
<img src="images/interactive_mode.PNG">

You can ask a question, see you dataset or your intents and entities. <br />
This is our dataset: <br />
<img src="images/dataset_init_demo.png">

We asked the question <br /> 
<img src="images/demo_question_batman.PNG"> <br />
This information is not in our dataset, but in only 3s the user have the answer. <br />
<img src="images/demo_answer_joker.PNG"> <br />
Then, the dataset is being enriched, with the new information about the archennemy (we add this information for Batman, but also for Superman), then new intents and entities are created and adding. <br />
This is our enriched dataset: <br />
<img src="images/demo_dataset_after.PNG"> 

You can watch a video of this demo here: <br />
 <video width="320" height="240" controls>
  <source src="video/Enrichment_Project_Video.mp4" type="video/mp4"> 
Your browser does not support the video tag, the video is available in the video folder.
</video>

You can test the algorithm with many questions:
- What is the secret identity of Superman ?
- What is the city of Batman ? 

Sometimes, it is not working well, you can try:
- What is the city of Spider Man ?
