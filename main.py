from Course import Course
from Spider import Spider
import sys

if __name__ == '__main__':
    course = Course(term=sys.argv[1], CRN=sys.argv[2])
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0'}
    cookie = "JSESSIONID=3AC5E57A46288ADDCFC379DD705B8DFB; _ga=GA1.2.1751626557.1561253718; rollup=GA1.2.2143599923.1561254105; subdirectory=GA1.2.1907215284.1561254106; subdomain=GA1.2.1953509159.1561254106; _mkto_trk=id:558-EBH-425&token:_mch-neu.edu-1561254106843-66694; _hjid=f7bd8518-0e00-4b57-b491-5115c949e1f6; _sp_id.cb6f=219c05ce-514e-4010-a0eb-21cba0580c12.1561254106.4.1565081306.1564370721.6ac23e35-e12c-4820-8032-deff60463f54; _gid=GA1.2.1060020417.1574032199; nubanner-cookie=3676250523.36895.0000; IDMSESSID=B450B8320592C4EDD35CCFAB19035112A99279B3FAB0DB15988A4C35356A1ED4E3F335459F9D7568EC15FB5E07D48BF085D6D41FB53655C6A844236EC2477175"
    spider = Spider(course, cookie, header)
    spider.setTimeGap(5)
    spider.start()
