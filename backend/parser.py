import re
import json

class Parser():
    def __init__(self, submissions, item):
        self.submissions = submissions
        self.item = item.lower()
        self.exp = r"\[(.*?)\]"
    
    def return_links(self, item):
        ret = ""
        for s in self.submissions:
            match_obj = re.match(self.exp, s.title)
            if match_obj.group(1).lower() == self.item:
                ret += "<p><a href={}>{}</a></p>\n".format(s.shortlink, s.title)
        return ret
    
    def return_json(self):
        info = {'data':[]}
        for s in self.submissions:
            match_obj = re.match(self.exp, s.title)
            if match_obj.group(1).lower() == self.item:
                submission_info = {}
                submission_info['title'] = s.title
                submission_info['link'] = s.shortlink
                info['data'].append(submission_info)
        return json.dumps(info)