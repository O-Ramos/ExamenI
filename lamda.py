import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    
    fileObj = s3.get_object(Bucket = "oramos-rekognition", Key = "belga.jpg")
    file_content = fileObj["Body"].read()
    
    getLabels = client.detect_labels(
       Image ={"Bytes": file_content}, MaxLabels=3, MinConfidence=75
    )
    
    getText = client.detect_text(
       Image ={"Bytes": file_content}, 
       Filters = {"WordFilter":{"MinConfidence":75}}
    )
    
    fileName = "muralistas.jpg"
    tags_array = []
    text_array = []
    
    for key, tag in getLabels.items():
        if(key == 'Labels'):
            print(key, '->', tag)
            print(type(tag))
            for key in tag:
                print(type(key))
                tag = key['Name']
                confidence = key['Confidence']
                conf_format = round(confidence, 2)
                print("tag: " + tag)
                print("confidence: " , conf_format)
                
                tags = {}
                tags['tag'] = tag
                tags['confidence'] = conf_format
                json_data = json.dumps(tags)
                tags_json = json.loads(json_data)
                
                tags_array.append(tags_json)
                
    for key, text in getText.items():
        if(key == 'TextDetections'):
            print(key, '-->', text)
            print(type(text))
            for key in text:
                text = key['DetectedText']
                confidence = key['Confidence']
                conf_format = round(confidence, 2)
                print("text: " + text)
                print("confidence: " , conf_format)
                
                text_dict = {}
                text_dict['text'] = text
                text_dict['confidence'] = conf_format
                json_data = json.dumps(text_dict)
                text_json = json.loads(json_data)
                
                text_array.append(text_json)
                
    res = {
        'fileName': fileName,
        'tags': tags_array,
        'text': text_array
    }
   # print(response2)
    print(type(res))
    print(res)

    return res