import os
import openai
import json

#openai.organization = "org-jOS3rcSS5l2406Nw1OF6NZXw"
#openai.api_key =  "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"

#response = openai.Completion.create(
#    engine="davinci", 
#    prompt= "This is a test",
#    max_token = 31)
#response = "worked fine keep working"
content_json = {
    'choices': [
        {
            'finish_reason': 'length',
            'index': 0,
            'logprobs': None,
            'text': '.\n\nLook fab in this beautiful range of artefacts.'
        }
    ],
    'created': 1640760222,
    'id': 'testid',
    'model': 'davinci',
    'object': 'text_completion'
}

# Convert the JSON object to a formatted string
json_string = json.dumps(content_json, indent=4)

print(json_string)


