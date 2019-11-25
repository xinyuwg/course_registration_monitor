import requests


class Course(object):
    def __init__(self, term, CRN) -> None:
        self.term = term
        self.CRN = CRN
        self.waitlist = 0
        self.enrollment = 0

    def __str__(self) -> str:
        return "term:" + str(self.term) + " CRN:" + str(self.CRN)

    def setEnrollmentWaitList(self, enrollment, waitlist):
        self.enrollment = enrollment
        self.waitlist = waitlist

    def getEnrollmentWaitList(self):
        return {"enrollment": self.enrollment, "waitlist": self.waitlist}

    def getCourseRequestInfo(self):
        return "term=" + self.term + "&courseReferenceNumber=" + self.CRN

    def checkChange(self, courseInfoDict, courseInfoDetail=""):
        if courseInfoDict["Enrollment Seats Available"] != self.enrollment or courseInfoDict[
            "Waitlist Actual"] != self.waitlist:
            if courseInfoDetail == "":
                push = "https://api.day.app/HJPVr6RN3LR26q5pVgPmGb/%s/%s" % (str(self.CRN) + " notification", self.CRN +
                                                                             " available seat change from " + str(
                    self.enrollment) + " to " + str(
                    courseInfoDict["Enrollment Seats Available"]))
            else:
                push = "https://api.day.app/HJPVr6RN3LR26q5pVgPmGb/%s/%s" % (
                str(self.CRN) + " notification", courseInfoDetail)
            requests.get(push)
            self.setEnrollmentWaitList(courseInfoDict["Enrollment Seats Available"], courseInfoDict[
                "Waitlist Actual"])
