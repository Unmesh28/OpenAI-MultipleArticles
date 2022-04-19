import os
import openai
import settings
from flask import Flask, request, jsonify
#import requests, jsonify
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

openai.api_key = settings.OPENAI_API_KEY

def getArticle(prompt_suffix):
    try :
        prompt = settings.PROMPT_PREFIX + prompt_suffix
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.5
        )
        return response.choices[0]["text"]

    except :
        return("Error From OPENAI API") 

@app.route('/getArtciles', methods=['GET'])
def getArtciles():
    list = request.json
    print(list["promptList"])
    articles = {}
    for prompt in list["promptList"] :
        text = getArticle(prompt)
        print(text)
        articles[prompt] = text
    return(articles)

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host= '0.0.0.0',debug=True)