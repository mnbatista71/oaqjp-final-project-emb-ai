""" TASK 8 - by Mariano Batista """
# Import Flask, render_template, request from the flask pramework package:
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

# main page for Emotion Detector
@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and runs emotion detection over it 
    using emotion_detector() function. The output returned shows a string with 
    all the emotions, their scores and the dominant emotion, with the followging format:
    -----
    "For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 
    'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy. "
    ------
    This content, for instance, could be placed in the "system_response" div of the HTML '''

     # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    dict_response = emotion_detector(text_to_analyze)
    str_response = ""
    if dict_response['dominant_emotion'] is None:
        str_response = "Invalid text! Please try again!"
    else:
        # convert the response in a sting with the required format
        str_response = "For the given statement, the system response is " \
        + "'anger': " + str(dict_response['anger']) + ", " \
        + "'disgust': " + str(dict_response['disgust']) + ", " \
        + "'fear': " + str(dict_response['fear']) + ", " \
        + "'joy': " + str(dict_response['joy']) + ", " \
        + "and 'sadness': " + str(dict_response['sadness']) + ". " \
        + "The dominant emotion is " + str(dict_response['dominant_emotion']) + "."

    return str_response

# default route to "/"
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    