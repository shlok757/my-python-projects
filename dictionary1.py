student_data = {"id1"
{'name':["David"]}
"class": ["V"],
"subject_intergration":['english ,math,science']
{"id2"
{'name':["SARA"]}
"class": ["V"],
"subject_intergration":['english ,math,science']
"id3":
{'name':{["SARA"]
"class": ["V"],
"subject_intergration":['english ,math,science']
"id4"
{'name':{["SARA"]
"class": ["V"],
"subject_intergration":['english ,math,science']}
rsult = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)



