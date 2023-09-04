import os
import openai
import json
import argparse
from data import content_json

#openai.organization = "org-jOS3rcSS5l2406Nw1OF6NZXw"
#openai.api_key =  "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"

#response = openai.Completion.create(
#    engine="davinci", 
#    prompt= "This is a test",
#    max_token = 31)
#response = "worked fine keep working"



def generate_branding_snipet(prompt: str):

    # Convert the JSON object to a formatted string
    json_string = json.dumps(content_json, indent=4)
    print(prompt)
    #print(json_string)


def main():
    print("Running our app")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print("\n")
    print("*"*25)
    generate_branding_snipet(user_input)
    print("*"*25)
    pass

if __name__== "__main__":
    main()