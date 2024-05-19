import requests
import pandas
import difflib


# CONSTANTS
THRESHOLD = 0.6
WEB_PAGES = 13


# TODO 1 // fetch data from the pages API


def fetch_api(num):
    pages = {
        "page": num
    }
    # getting a request from an API
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    response = requests.get(api_url, params=pages)

    # checking if there was a response // 3 ways
    # 1. show_status_c = response.status_code // returns 200 to show a successful request
    # print(show_status_c)

    # 2. print(response.ok) // returns True if request was successful

    # 3. Best option as it handles errors for us if there was any
    response.raise_for_status()  # returns None if no error

    # storing data into JSON to work with it // visual through Chrome and pretty print extension
    arr_of_objects = response.json()
    return arr_of_objects


citations = []
for _ in range(WEB_PAGES):

    new_arr_of_objects = fetch_api(_).copy()

    # TODO 2 indentify if response is in sources and returning the source context and link
    objects_data = new_arr_of_objects["data"]["data"]
    index_id = []
    for _ in range(len(objects_data)):
        index_id.append(objects_data[_]["id"])

    data = pandas.DataFrame(objects_data, index=index_id, columns=["response", "source"])
    # print(data)


    def check_similarity(sentence_1, sentence_2):
        # Create a SequenceMatcher object
        matcher = difflib.SequenceMatcher(None, sentence_1, sentence_2)

        # Get the similarity ratio
        similarity_ratio = matcher.ratio()

        # If similarity ratio is greater than a threshold, return True// you can change the THRESHOLD PER REQUIREMENT
        if similarity_ratio > THRESHOLD:
            return True
        else:
            return False


    int_ids_list = data.index.to_list()

    for each_id in int_ids_list:

        def citations_array(new_index_id):
            citations_list = []
            sentence1 = data.loc[new_index_id]["response"]

            sent2_len = len(data.loc[new_index_id]["source"])
            for _ in range(sent2_len):

                sentence2 = data.loc[new_index_id]["source"][_]["context"]
                cit_obj = {
                    "i_d": data.loc[new_index_id]["source"][_]["id"],
                    "link": data.loc[new_index_id]["source"][_]["link"]
                }

                if check_similarity(sentence1, sentence2):
                    citations_list.append(cit_obj)
                else:
                    citations_list += []
            return citations_list
        citations += citations_array(new_index_id=each_id)

print(citations)
