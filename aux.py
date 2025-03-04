
'''
    # TASK 7: Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
'''


'''
str_response is the variable to return the well formed string with the following format
-----
For the given statement, the system response is 
'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. 
The dominant emotion is joy.
------
This content, for instance, could be placed in the "system_response" div of the HTML
# dynamic
str_response = "For the given statement, the system response is "
cc = 0 # used to count items and decide if a comma behind the item is needed or not 
for emo_key in dict_response.keys():
    str_aux = emo_key + "': " + str(dict_response[emo_key]) 
    if cc==0: # check initial connector with comma or not
        str_aux = "'" + str_aux
    else:
        str_aux = "', " + str_aux
    str_response = str_response + str_aux
    cc+=1
str_response = str_response + ". The dominant emotion is " + dict_response['dominant_emotion'] + "."

# hardcoded
str_response = "For the given statement, the system response is " \
    + "'anger': " + str(dict_response['anger']) + ", " \
    + "'disgust': " + str(dict_response['disgust']) + ", " \
    + "'fear': " + str(dict_response['fear']) + ", " \
    + "'joy': " + str(dict_response['joy']) + ", " \
    + "'sadness': " + str(dict_response['sadness']) + ". " \
    + "The dominant emotion is " + str(dict_response['dominant_emotion']) + "."
'''

