import requests
import time
import random
from bs4 import BeautifulSoup
from requests.cookies import cookiejar_from_dict


class Spider(object):
    def __init__(self, course, cookie, header, timegap=5) -> None:
        self.course = course
        self.cookie = cookie
        self.header = header
        self.timegap = timegap

    @staticmethod
    def cookie_to_dict(cookie):
        cookie_dict = {}
        items = cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            cookie_dict[key] = value
        return cookie_dict

    def setTimeGap(self, timegap):
        self.timegap = timegap

    @staticmethod
    def courseInfo(courseInfo):
        infoList = courseInfo.strip().split("\n")
        infoDict = {}
        for i in infoList:
            if i == "":
                continue
            key = i.split(":")[0]
            value = i.split(":")[1].strip()
            infoDict[key] = int(value)
        return infoDict

    def start(self):
        cookie_dict = self.cookie_to_dict(self.cookie)
        url = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/searchResults/getEnrollmentInfo?" + self.course.getCourseRequestInfo()
        session = requests.session()
        session.cookies = cookiejar_from_dict(cookie_dict)
        while True:
            res = session.get(url, headers=self.header)
            soup = BeautifulSoup(res.content, "html.parser")
            courseInfoDict = self.courseInfo(soup.text)
            print("-------- %s ---------\n" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print(self.course)
            print(soup.text)
            self.course.checkChange(courseInfoDict, soup.text)
            time.sleep(self.timegap * 60 * random.random() * 10)
