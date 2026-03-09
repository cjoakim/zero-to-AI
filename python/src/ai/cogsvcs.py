import json
import sys
import time
import traceback
import uuid

import requests

from src.env import Env


# This class is used to invoke Azure Cognitive Services via HTTP.
# TODO - refactor to use httpx and test.  This original code was
# written in ~2022.
# Chris Joakim, 3Cloud/Cognizant, 2026


class CogSvcsClient:
    """
    This class is used to access an Azure Cognitive Services account
    via REST API endpoints.
    """

    def __init__(self, opts):
        self.opts = opts

    # TextAnalytics methods:
    # See https://learn.microsoft.com/en-us/rest/api/language/

    def text_analytics_sentiment(self, text_lines, language):
        url = self.get_cogsvcs_target_url("text/analytics/v3.0/sentiment")
        headers = self.get_cogsvcs_headers()
        body = {"documents": []}
        for line in text_lines:
            body["documents"].append(
                {
                    "id": str(uuid.uuid4()),
                    "language": language,
                    "text": str(line).strip(),
                }
            )
        return requests.post(url, headers=headers, data=json.dumps(body))

    def text_analytics_key_phrases(self, text_lines, language):
        url = self.get_cogsvcs_target_url("text/analytics/v3.0/keyPhrases")
        headers = self.get_cogsvcs_headers()
        text = " ".join(text_lines)
        body = {"documents": []}
        body["documents"].append(
            {"id": str(uuid.uuid4()), "language": language, "text": str(text).strip()}
        )
        return requests.post(url, headers=headers, data=json.dumps(body))

    def text_analytics_entities(self, text_lines, language):
        url = self.get_cogsvcs_target_url("text/analytics/v3.0/entities/recognition/general")
        headers = self.get_cogsvcs_headers()
        text = " ".join(text_lines)
        body = {"documents": []}
        body["documents"].append(
            {"id": str(uuid.uuid4()), "language": language, "text": str(text).strip()}
        )
        return requests.post(url, headers=headers, data=json.dumps(body))

    # TextTranslation methods:

    def text_translate_formats(self):
        url = self.get_cogsvcs_target_url("translator/text/batch/v1.0/documents/formats")
        headers = self.get_cogsvcs_headers()
        return requests.get(url, headers=headers)

    def text_translate_languages(self):
        # https://learn.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-languages
        url = "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0"
        return requests.get(url, headers={})

    def text_translate(self, text_lines, to_lang):
        # https://learn.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate
        url = (
            f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={to_lang}"
        )
        headers, body = self.get_texttranslator_headers(), []
        for line in text_lines:
            body.append({"Text": str(line).strip()})
        return requests.post(url, headers=headers, data=json.dumps(body))

    # ComputerVision methods:

    def image_analyze(self, image_url):
        # See https://learn.microsoft.com/en-us/rest/api/computervision/3.1/analyze-image/analyze-image?tabs=HTTP
        url = self.get_cogsvcs_target_url(
            "vision/v3.1/analyze?visualFeatures=Categories,Adult,Tags,Description,Faces,Color,ImageType,Objects,Brands&details=Landmarks&language=en"
        )
        headers = self.get_cogsvcs_headers()
        body = {"url": image_url}
        return requests.post(url, headers=headers, data=json.dumps(body))

    def image_describe(self, image_url):
        # See https://learn.microsoft.com/en-us/rest/api/computervision/3.1/describe-image/describe-image?tabs=HTTP
        url = self.get_cogsvcs_target_url("vision/v3.1/describe?maxCandidates=2&language=en")
        headers = self.get_cogsvcs_headers()
        body = {"url": image_url}
        return requests.post(url, headers=headers, data=json.dumps(body))

    def image_tag(self, image_url):
        # See https://learn.microsoft.com/en-us/rest/api/computervision/3.1/tag-image/tag-image?tabs=HTTP
        url = self.get_cogsvcs_target_url("vision/v3.1/tag?language=en")
        headers = self.get_cogsvcs_headers()
        body = {"url": image_url}
        return requests.post(url, headers=headers, data=json.dumps(body))

    def image_read(self, image_url, callback_sleep_secs=3):
        try:
            # See https://learn.microsoft.com/en-us/rest/api/computervision/3.1/read/read?tabs=HTTP
            # This is a two-step process - first submit the image for analysis, then retrieve the results.
            url = self.get_cogsvcs_target_url("vision/v3.1/read/analyze?language=en")
            headers = self.get_cogsvcs_headers()
            body = {"url": image_url}
            # print(json.dumps(body))
            resp = requests.post(url, headers=headers, data=json.dumps(body))
            # print(resp)
            # print(resp.headers)
            callback_url = resp.headers["Operation-Location"]
            print(f"callback_url: {callback_url}")
            time.sleep(callback_sleep_secs)
            return requests.get(callback_url, headers=headers)
        except Exception as excp:
            print(str(excp))
            print(traceback.format_exc())
        return None

    # Face methods:

    def face_detect(self, image_url):
        # See https://learn.microsoft.com/en-us/rest/api/faceapi/face/detect-with-url?tabs=HTTP
        url = self.get_cogsvcs_target_url(
            "face/v1.0/detect?returnFaceId=false&returnFaceLandmarks=true"
        )
        headers = self.get_face_headers()
        body = {"url": image_url}
        return requests.post(url, headers=headers, data=json.dumps(body))

    # "private" methods below

    def get_cogsvcs_rest_endpoint(self, alt_env_var_name=None):
        if alt_env_var_name is None:
            return Env.var("AZURE_COGSVCS_ALLIN1_URL")
        else:
            return Env.var(alt_env_var_name)

    def get_cogsvcs_target_url(self, path):
        if self.get_cogsvcs_rest_endpoint().endswith("/"):
            return "{}{}".format(self.get_cogsvcs_rest_endpoint(), path)
        else:
            return "{}/{}".format(self.get_cogsvcs_rest_endpoint(), path)

    def get_face_rest_endpoint(self, alt_env_var_name=None):
        if alt_env_var_name is None:
            return Env.var("AZURE_COGSVCS_FACE_URL")
        else:
            return Env.var(alt_env_var_name)

    def get_face_target_url(self, path):
        if self.get_cogsvcs_rest_endpoint().endswith("/"):
            return "{}{}".format(self.get_face_rest_endpoint(), path)
        else:
            return "{}/{}".format(self.get_face_rest_endpoint(), path)

    def get_cogsvcs_headers(self, alt_env_var_name=None):
        key = None
        if alt_env_var_name is None:
            key = Env.var("AZURE_COGSVCS_ALLIN1_KEY")
        else:
            key = Env.var(alt_env_var_name)
        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Content-Type": "application/json",
        }
        return headers

    def get_texttranslator_headers(self, alt_env_var_name=None):
        key = None
        if alt_env_var_name is None:
            key = Env.var("AZURE_COGSVCS_TEXTTRAN_KEY")
        else:
            key = Env.var(alt_env_var_name)
        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Ocp-Apim-Subscription-Region": "eastus",
            "Content-Type": "application/json",
        }
        return headers

    def get_face_headers(self, alt_env_var_name=None):
        key = None
        if alt_env_var_name is None:
            key = Env.var("AZURE_COGSVCS_FACE_KEY")
        else:
            key = Env.var(alt_env_var_name)
        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Ocp-Apim-Subscription-Region": "eastus",
            "Content-Type": "application/json",
        }
        return headers

    def verbose(self):
        for arg in sys.argv:
            if arg == "--verbose":
                return True
        return False
