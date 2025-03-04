import requests
import json

# version for TASK 7 - by Mariano Batista
# function emotion_detector
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    dict_emotions = {}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        json_emotions = json.loads(response.text)
        dict_emotions = parse_emotions(json_emotions)
    elif response.status_code == 400:
        dict_emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else: dict_emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, \
                                'dominant_emotion': 'error - status code= ' + str(response.status_code)}

    return dict_emotions

# function parse_emotions
'''   
it takes a json response from Watson and returns a dict with the following format
with the emotions, its scores and the dominant emotion
    {
       'anger': anger_score,
       'disgust': disgust_score,
       'fear': fear_score,
       'joy': joy_score,
       'dominant_emotion': '<name of the dominant emotion>'
       'sadness': sadness_score,
      }
'''
def parse_emotions(json_emo):
    dominant_emo = ""
    dict_emo = {}
    max_value = 0
    for emo_key in json_emo['emotionPredictions'][0]['emotion']:
        emo_value = json_emo['emotionPredictions'][0]['emotion'][emo_key]
        dict_emo.update({emo_key: emo_value})
        if (emo_value > max_value):
            max_value = emo_value
            dominant_emo = emo_key
    dict_emo.update({'dominant_emotion': dominant_emo})
    return(dict_emo)

''' version for TASK 2
# function emotion_detector
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    return response.text
'''

