import requests
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
import time
import re

class YTB:
    def __init__(self, cookie: str, authorization: str):
        self.cookies = {}
        for item in cookie.split(";"):
            key, value = item.strip().split("=", 1)
            self.cookies[key] = value

        self.headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'authorization': authorization,
            'content-type': 'application/json',
            'origin': 'https://www.youtube.com',
            'priority': 'u=1, i',
            'referer': 'https://www.youtube.com/@AlexWarren',
            'sec-ch-dpr': '1',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-form-factors': '"Desktop"',
            'sec-ch-ua-full-version': '"143.0.7499.170"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="143.0.7499.170", "Chromium";v="143.0.7499.170", "Not A(Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-ch-viewport-width': '1008',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'x-browser-channel': 'stable',
            'x-browser-copyright': 'Copyright 2025 Google LLC. All Rights reserved.',
            'x-browser-validation': 'UujAs0GAwdnCJ9nvrswZ+O+oco0=',
            'x-browser-year': '2025',
            'x-client-data': 'CI22yQEIprbJAQipncoBCOfnygEIkqHLAQiFoM0BCJaMzwEIyZHPAQjUo88BCJKkzwEImaXPAQimpc8BGOyFzwEYsobPAQ==',
            'x-goog-authuser': '0',
            # 'x-goog-visitor-id': 'CgtjeDhVYmY3S1Q4TSjByurKBjIKCgJWThIEGgAgIA%3D%3D',
            'x-goog-pageid': '101132415648947005236',
            'x-origin': 'https://www.youtube.com',
            'x-youtube-bootstrap-logged-in': 'true',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20260101.00.00',
            # 'cookie': 'VISITOR_INFO1_LIVE=cx8Ubf7KT8M; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgIA%3D%3D; __Secure-ROLLOUT_TOKEN=CIPG-vjppfrrFBC3h8nR0c6OAxi7lOmp_u-RAw%3D%3D; YSC=h9IQ4D7ENrM; PREF=f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000; SID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXclrU5XHOdglYRTr9QgoRLQACgYKAYUSARQSFQHGX2MiKGEIH-i-v9hVVvdI_w4xHxoVAUF8yKqyDSo8Ozltq9x1DMe6OLVl0076; __Secure-1PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXX5yZYJbZJYVZg7BE6-KCzWQACgYKAY4SARQSFQHGX2MiIS_6DeGoCHrmFbK9C5lrtBoVAUF8yKrQ5GspsH8xEuF1m3T5onDp0076; __Secure-3PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXMX7ZHi16eRCLxZqYuzA-fwACgYKAYQSARQSFQHGX2Mir9jm3nk0W3UDQHZ6tTe3YhoVAUF8yKo5aw286aYRDPk8Dr6OehOX0076; HSID=A5ZWP_OXtm1tXt5Ra; SSID=AAdvwo5XLkRYvN2sq; APISID=IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6; SAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-3PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; __Secure-3PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; CONSISTENCY=APeVyi-gntr9YHcYRsCd6p7ZSmbT1cvVYJ6CyyT01sEfKNxyo0nuVgBt5Qop61Cp9KT639KmbRcdIVGK-eEQoIWfjnv06z7UNlInd4QQ5MegLzfgJojUsDIUmi-SB-mjQPour3bYr-Jut9xfpjl0nxZDAawDgPMpyCji4bjuLlZuuJEGrrHfa5iDvcqSNQ; LOGIN_INFO=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI:QUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; ST-xuwub9=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; SIDCC=AKEyXzUX_VbFZDmKRzeoI_1XRy33oRJhJN0djffmdGqinEkUopqz-gJB66uhueQiG_y28BeNT_w; __Secure-1PSIDCC=AKEyXzX2O-nY78GwG5jw4IEwVBI5Ibx9Osth1_uLy7R9o0oURRXRaBjESSU9vy3m3mwDGIzG9uQ; __Secure-3PSIDCC=AKEyXzUBalvNXBqsuihqCihEtF5zHff1va8j51wP8ps-sH-nH-vVXYQoUgitZcJHB8CPig1Crw; ST-4n4ru8=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3',
        }

    def getdata(self, url: str):
        re = requests.get(url, cookies=self.cookies, headers=self.headers).text
        try:
            self.authuser = re.split('"SESSION_INDEX":"')[1].split('"')[0]
        except:
            self.authuser = False
        try:
            self.pageid = re.split('"DELEGATED_SESSION_ID":"')[1].split('"')[0]
        except:
            self.pageid = False
        
        self.visitorid = re.split('"VISITOR_DATA":"')[1].split('"')[0]
        # self.idytb = re.split('"https://www.youtube.com/@')[1].split('"')[0]
        try:
            self.chanelid = re.split('"channelId":"')[1].split('"')[0]
        except:
            self.chanelid = ''
        # print(self.pageid, self.visitorid, self.chanelid)
        return self.pageid, self.visitorid, self.chanelid, self.authuser


    def follow(self, url: str):
        headers = self.headers.copy()
        pageid, visitorid, chanelid, authuser = self.getdata(url)
        if not pageid:
            headers['x-goog-visitor-id'] = visitorid
        else:
            headers['x-goog-visitor-id'] = visitorid
            headers['x-goog-pageid'] = pageid
        
        if not authuser:
            pass
        else:
            headers['x-goog-authuser'] = authuser

        params = {
            'prettyPrint': 'false',
        }

        json_data = {
            'context': {
                'client': {
                    'hl': 'vi',
                    'gl': 'VN',
                    'remoteHost': '2405:4802:6f82:34c0:5540:fc20:2e7:14ad',
                    'deviceMake': '',
                    'deviceModel': '',
                    'visitorData': 'CgtjeDhVYmY3S1Q4TSjOgPDKBjIKCgJWThIEGgAgIA%3D%3D',
                    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36,gzip(gfe)',
                    'clientName': 'WEB',
                    'clientVersion': '2.20260105.01.00',
                    'osName': 'Windows',
                    'osVersion': '10.0',
                    'originalUrl': 'https://www.youtube.com/',
                    'platform': 'DESKTOP',
                    'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                    'windowWidthPoints': 615,
                    'configInfo': {
                        'appInstallData': 'CM6A8MoGEJTyzxwQ8rPQHBDhwYATEOaH0BwQxcbPHBC52c4cEL22rgUQ9quwBRDM688cELyk0BwQ0-GvBRDJ968FEOWk0BwQt4bPHBDDkdAcEIeszhwQo4W4IhDL0bEFEJX3zxwQvL_QHBCmmrAFEIiHsAUQ4tSuBRDgzbEFEN68zhwQxPTPHBDa984cEIKPzxwQjbDQHBCi-88cEJy40BwQnNfPHBCM6c8cEPG00BwQi_fPHBCRjP8SELCGzxwQ_LLOHBC36v4SEPHE0BwQ167QHBCHg9AcEKifqRcQvoqwBRC45M4cENvB0BwQ8p3QHBCPudAcEJq50BwQmY2xBRDartAcEMGP0BwQ5uDPHBDKu9AcEJSD0BwQlP6wBRCUttAcEKa20BwQntCwBRCBzc4cENq00BwQibDOHBCsrNAcELOQzxwQu9nOHBDSvdAcEMa9gBMQvZmwBRCW288cEMj3zxwQm8LQHBC8s4ATEK7WzxwQq53PHBDHttAcEM3RsQUQzN-uBRCDntAcELnA0BwQieiuBRC0wdAcEMWM0BwQy7HQHBDgv9AcEMfDgBMQvsHQHBDJutAcKnRDQU1TVWhWSi1acS1ETWVVRW9jT3FnTE1CYmtHX3NQbUNfQ3hFb2RNTXFDc0JBUEx2Z1g2T2ZtQ0JxQUdvaTZhSWZGUHpnX3RYUFV2OWctRkZPSWo3cDBGNHhiRktsUzNMX1FQX1F5ZUN2ZzVnaWdHSFFjPTAA',
                        'coldConfigData': 'CM6A8MoGEO66rQUQxYWuBRC9tq4FEOLUrgUQvoqwBRCNzLAFEJ7QsAUQz9KwBRDj-LAFEK-nzhwQ_LLOHBCA_M4cELCGzxwQrpTPHBCrnc8cELTGzxwQxcbPHBD4xs8cENvTzxwQnNfPHBCf188cEMjazxwQz-DPHBDl588cEOfnzxwQlIPQHBDFjNAcEP6T0BwQzqzQHBDxtNAcEKC10BwQz7XQHBDsuNAcEJq50BwQybrQHBCVu9AcEOC_0BwQucDQHBC-wdAcENvB0BwQscPQHBCbxdAcEKfF0BwQo4W4IhoyQUNEU1IyVFE4dUR1d0lqWTNUSVZEVnc0emJaWDlRbGN2OTV5N0RNaGFsTzFMMVdwUmciMkFDRFNSMlNqUm5sSktFa05IVXNISXRvMDlGQjFYd0pnMHVaUUtPdXJ5bjVFZTNYbnN3KrQBQ0FNU2dBRU5OYmpkdHdLa0daY2ZuMC1aa3BvUTFBcXZBNDAyX2lPbkRjZ0FyQXhxTlBZWXFBTFpGN1lOQWktV0FPZ0Z6Z0lNbGdVTUZVMlpzYmNmaGFRRmtad0Y0ZHNCejhJQXIzellJXzNVQmpMUGdBWFpwQVlEb3JJRnlrc0dzRy1IQThZSjh3T0k1QVhMU2dTU3ZnYVpQZW94bFFWYmdnVGFXcEFpcDA5dnNSeXpCZz09',
                        'coldHashData': 'CM6A8MoGEhMxODgxMDYwNDgxNDc3OTQ0ODQwGM6A8MoGMjJBQ0RTUjJUUTh1RHV3SWpZM1RJVkRWdzR6YlpYOVFsY3Y5NXk3RE1oYWxPMUwxV3BSZzoyQUNEU1IyU2pSbmxKS0VrTkhVc0hJdG8wOUZCMVh3SmcwdVpRS091cnluNUVlM1huc3dCtAFDQU1TZ0FFTk5iamR0d0trR1pjZm4wLVprcG9RMUFxdkE0MDJfaU9uRGNnQXJBeHFOUFlZcUFMWkY3WU5BaS1XQU9nRnpnSU1sZ1VNRlUyWnNiY2ZoYVFGa1p3RjRkc0J6OElBcjN6WUlfM1VCakxQZ0FYWnBBWURvcklGeWtzR3NHLUhBOFlKOHdPSTVBWExTZ1NTdmdhWlBlb3hsUVZiZ2dUYVdwQWlwMDl2c1J5ekJnPT0%3D',
                        'hotHashData': 'CM6A8MoGEhMyOTA1NDU5ODM0MzYyODkxMzg1GM6A8MoGKJTk_BIopdD9Eiiekf4SKMjK_hIot-r-EiiRjP8SKMuRgBMotZuAEyi0sIATKNiwgBMok7SAEyiwt4ATKKW4gBMoucGAEyiywoATKMfDgBMoqJ-pFzIyQUNEU1IyVFE4dUR1d0lqWTNUSVZEVnc0emJaWDlRbGN2OTV5N0RNaGFsTzFMMVdwUmc6MkFDRFNSMlNqUm5sSktFa05IVXNISXRvMDlGQjFYd0pnMHVaUUtPdXJ5bjVFZTNYbnN3QjRDQU1TSXcwSm90ZjZGYTdCQnV1YkJ0VU1uQU1WRnQzUHdnemk5Z19jcWVZTGw5Y2ttOG9H',
                    },
                    'screenDensityFloat': 1,
                    'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                    'timeZone': 'Etc/GMT-7',
                    'browserName': 'Chrome',
                    'browserVersion': '143.0.0.0',
                    'memoryTotalKbytes': '8000000',
                    'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'deviceExperimentId': 'ChxOelU1TVRrME16UXdOek16TmpFd01USXdOdz09EM6A8MoGGM6A8MoG',
                    'rolloutToken': 'CIPG-vjppfrrFBC3h8nR0c6OAxiwsri5xPSRAw%3D%3D',
                    'screenWidthPoints': 397,
                    'screenHeightPoints': 952,
                    'screenPixelDensity': 1,
                    'utcOffsetMinutes': 420,
                    'connectionType': 'CONN_CELLULAR_4G',
                    'mainAppWebInfo': {
                        'graftUrl': 'https://www.youtube.com/@amnhacchualanh.',
                        'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                        'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                        'isWebNativeShareAvailable': True,
                    },
                },
                'user': {
                    'lockedSafetyMode': False,
                },
                'request': {
                    'useSsl': True,
                    'internalExperimentFlags': [],
                    'consistencyTokenJars': [],
                },
                'clientScreenNonce': 'wkjLpRlUEBiyQF_T',
                'clickTracking': {
                    'clickTrackingParams': 'CCMQmysYASITCNTznaKB9ZEDFe1BDwIdlxImgSjyODIJY2hhbm5lbHM0ygEEcskFsQ==',
                },
                'adSignalsInfo': {
                    'params': [
                        {
                            'key': 'dt',
                            'value': '1767637071559',
                        },
                        {
                            'key': 'flash',
                            'value': '0',
                        },
                        {
                            'key': 'frm',
                            'value': '0',
                        },
                        {
                            'key': 'u_tz',
                            'value': '420',
                        },
                        {
                            'key': 'u_his',
                            'value': '4',
                        },
                        {
                            'key': 'u_h',
                            'value': '1080',
                        },
                        {
                            'key': 'u_w',
                            'value': '1920',
                        },
                        {
                            'key': 'u_ah',
                            'value': '1040',
                        },
                        {
                            'key': 'u_aw',
                            'value': '1920',
                        },
                        {
                            'key': 'u_cd',
                            'value': '24',
                        },
                        {
                            'key': 'bc',
                            'value': '31',
                        },
                        {
                            'key': 'bih',
                            'value': '952',
                        },
                        {
                            'key': 'biw',
                            'value': '382',
                        },
                        {
                            'key': 'brdim',
                            'value': '931,0,931,0,1920,0,996,1047,397,952',
                        },
                        {
                            'key': 'vis',
                            'value': '1',
                        },
                        {
                            'key': 'wgl',
                            'value': 'true',
                        },
                        {
                            'key': 'ca_type',
                            'value': 'image',
                        },
                    ],
                    'bid': 'ANyPxKotoTKZSSvB3Jj_2rog8gqJ3T4F6X-Z2mZnJ8tDux9RlB-jLEOaKThedT5tUf_ro7qcMWqRecQv6U2hPQZYLdfwSJP_yw',
                },
            },
            'channelIds': [
                chanelid,
            ],
            'params': 'EgIIAhgA',
        }

        response = requests.post(
            'https://www.youtube.com/youtubei/v1/subscription/subscribe',
            params=params,
            cookies=self.cookies,
            headers=headers,
            json=json_data,
        ).json()
        # print(response)
            


class TTC:
    def __init__(self, api_key="bc2a075708b3eec4929da5f613c5dfdf"):
        self.index_job = 0
        self.index_button = 1
        self.idpost = ''
        self.api_key = api_key
        self.base_url = "https://tuongtaccheo.com/logintoken.php"
        self.headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://tuongtaccheo.com',
            'priority': 'u=1, i',
            'referer': 'https://tuongtaccheo.com/youtube/kiemtien/subcheo/',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            # 'cookie': '_fbp=fb.1.1761508765559.516195470818743635; _gid=GA1.2.242056569.1767635360; _gcl_au=1.1.387163357.1767677503; PHPSESSID=07qvlfrfl578le7cc2a8hlrml5; _ga=GA1.1.1652707960.1761508764; _ga_6RNPVXD039=GS2.1.s1767693400$o87$g1$t1767694388$j11$l0$h0',
        }
        # cookie gốc
        self.cookies = {
            '_fbp': 'fb.1.1761508765559.516195470818743635',
            'PHPSESSID': 'dlr4jh5pvm9s4tkb9h39a7m4s0',
            '_gid': 'GA1.2.242056569.1767635360',
            '_gat_gtag_UA_88794877_6': '1',
            '_ga': 'GA1.2.1652707960.1761508764',
            '_ga_6RNPVXD039': 'GS2.1.s1767635359$o85$g1$t1767635524$j51$l0$h0',
        }

        self.driver = None

    # ================== INIT SELENIUM + ADD FULL COOKIE ==================
    def __init_driver__(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)

        # mở domain trước khi add cookie
        self.driver.get("https://tuongtaccheo.com/")
        time.sleep(2)

    def wait_and_click(self, locator, locator_type="xpath", timeout=60, driver=None):
        driver = driver or self.driver
        if locator_type.lower() == "xpath":
            by = By.XPATH
        elif locator_type.lower() == "id":
            by = By.ID 
        elif locator_type.lower() == "name":
            by = By.NAME
        else:
            raise ValueError("Unsupported locator type")

        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()
        sleep(random.uniform(1, 2))  # 🔴 Random delay

    def wait_and_send_keys(self, locator, keys, locator_type="xpath", timeout=60, driver=None):
        driver = driver or self.driver

        def human_typing(element, text, delay_range=(0.1, 0.3)):
            for char in text:
                element.send_keys(char)
                sleep(random.uniform(*delay_range))

        if locator_type.lower() == "xpath":
            by = By.XPATH
        elif locator_type.lower() == "id":
            by = By.ID 
        elif locator_type.lower() == "name":
            by = By.NAME
        else:
            raise ValueError("Unsupported locator type")

        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.clear()
        human_typing(element, keys)
        sleep(random.uniform(1, 2))  # 🔴 Random delay

    def login_ttc(self):
        self.wait_and_send_keys('/html/body/div[1]/div/div[4]/div/div[2]/form/input[1]', 'Shinsad1')
        self.wait_and_send_keys('/html/body/div[1]/div/div[4]/div/div[2]/form/input[2]', 'shinsad0907')
        self.wait_and_click('/html/body/div[1]/div/div[4]/div/div[2]/form/input[4]')

    # ================== GETPOST BẰNG SELENIUM ==================

    def getcoin(self, idpost):
        data = {
            'id': idpost,
        }

        response = requests.post(
            'https://tuongtaccheo.com/youtube/kiemtien/subcheo/nhantien.php',
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        ).json()
        return response
        # print(response.json())
    def selenium_getpost(self,cookie, authorization):
        wait = WebDriverWait(self.driver, 15)
        main_tab = self.driver.current_window_handle
        old_tabs = self.driver.window_handles
        self.driver.get(f"https://tuongtaccheo.com/youtube/kiemtien/subcheo/")
        input("Đăng nhập TTC xong nhấn Enter để tiếp tục...")
        try:
            while True:
                button = self.driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div/div/div/div[{self.index_button}]/div/div/button')
                # button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div/div/div[2]/div/div/button')
                onclick_value = button.get_attribute('onclick')
                print(onclick_value)
                match = re.search(r"like\('([^']+)','([^']+)'\)", onclick_value)
                job_id = match.group(1)
                youtube_url = match.group(2)
                # đợi tab mới mở
                self.wait_and_click(f'/html/body/div/div/div[3]/div/div/div/div[{self.index_button}]/div/div/button')

                wait.until(lambda d: len(d.window_handles) > len(old_tabs))

                # xác định tab mới
                new_tab = [t for t in self.driver.window_handles if t not in old_tabs][0]

                # chuyển qua tab youtube
                self.driver.switch_to.window(new_tab)
                time.sleep(2)

                self.driver.close()
                # quay lại tab TTC
                self.driver.switch_to.window(main_tab)
                time.sleep(3)
                ytb = YTB(cookie, authorization)
                ytb.follow(youtube_url)
                sleep(10)
                self.idpost += f'{job_id},'
                self.index_job += 1
                self.index_button += 1
                if self.index_job == 4:
                    idpost = self.idpost.rstrip(',')
                    print(f'Gửi idpost: {idpost}')
                    # input("Nhấn Enter để tiếp tục...")
                    getcoin = self.getcoin(idpost)
                    print(getcoin)
                    self.index_job = 0
                    # pass
                # input("Nhấn Enter để tiếp tục...")
        except Exception as e:
            pass

    # ================== MAIN ==================
    def main(self,cookie, authorization):
        self.__init_driver__()
        self.login_ttc()
        self.selenium_getpost(cookie, authorization)

    
if __name__ == "__main__":
    cookie = input("Nhap cookie YTB: ")
    authorization = input("Nhap authorization YTB: ")
    print('-------------------------------------------------')
    ttc = TTC()
    print(ttc.main(cookie, authorization))