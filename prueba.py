import json

''' con comillas dobles
str_sentiment = "{'documentSentiment':{'score':0.996954, 'label':'SENT_POSITIVE', 'mixed':false, 'sentimentMentions':[{'span':{'begin':0, 'end':26, 'text':'I love this new technology'}, 'sentimentprob':{'positive':0.9941229, 'neutral':0.0028645627, 'negative':0.0030124863}}]}, 'targetedSentiments':{'targetedSentiments':{}, 'producerId':{'name':'Aggregated Sentiment Workflow', 'version':'0.0.1'}}, 'producerId':{'name':'Aggregated Sentiment Workflow', 'version':'0.0.1'}}"
str_emotions = "{'emotionPredictions': [{'emotion': {'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167}, 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 26, 'text': 'I love this new technology'}, 'emotion': {'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}"
'''

# con comillas simples
str_sentiment = '{"documentSentiment":{"score":0.996954, "label":"SENT_POSITIVE", "mixed":false, "sentimentMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "sentimentprob":{"positive":0.9941229, "neutral":0.0028645627, "negative":0.0030124863}}]}, "targetedSentiments":{"targetedSentiments":{}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
str_emotions = '{"emotionPredictions": [{"emotion": {"anger": 0.0132405795, "disgust": 0.0020517302, "fear": 0.009090992, "joy": 0.9699522, "sadness": 0.054984167}, "target": "", "emotionMentions": [{"span": {"begin": 0, "end": 26, "text": "I love this new technology"}, "emotion": {"anger": 0.0132405795, "disgust": 0.0020517302, "fear": 0.009090992, "joy": 0.9699522, "sadness": 0.054984167}}]}], "producerId": {"name": "Ensemble Aggregated Emotion Workflow", "version": "0.0.1"}}'

json_sentiment = json.loads(str_sentiment)
json_emotions = json.loads(str_emotions)

pretty_emotions = json.dumps(json_emotions, indent=2)
pretty_sentiment = json.dumps(json_sentiment, indent=2)

print("----------------------------------------")
print("Pretty sentiment:")
print(pretty_sentiment)
print("----------------------------------------")
print("Pretty emotions:")
print(pretty_emotions)
print("----------------------------------------")
print("----------------------------------------")
print()
print("Detailed sentiment")
print(json_sentiment['documentSentiment']['label'])
print("----------------------------------------")
print("List of detailed emotions")
print(json_emotions['emotionPredictions'][0])
print("----------------------------------------")
print("Emotions in detail, anger")
print(json_emotions['emotionPredictions'][0]['emotion']['anger'])
print("----------------------------------------")
print("All emotions in detail")
for emo_key in json_emotions['emotionPredictions'][0]['emotion']:
    emo_value = json_emotions['emotionPredictions'][0]['emotion'][emo_key]
    print("Emotion: {0:8} - score: {1}".format(emo_key, emo_value))
print("----------------------------------------")
print()
