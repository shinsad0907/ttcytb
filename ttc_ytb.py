import requests

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
            'x-client-data': 'CI22yQEIprbJAQipncoBCOfnygEIlKHLAQiFoM0BCJaMzwEIyZHPAQi1os8BCL2izwEI1KPPAQiSpM8BCJmlzwEIpqXPARjshc8BGLKGzwE=',
            # 'x-goog-authuser': '1',
            'x-goog-visitor-id': 'CgtjeDhVYmY3S1Q4TSjByurKBjIKCgJWThIEGgAgIA%3D%3D',
            'x-origin': 'https://www.youtube.com',
            'x-youtube-bootstrap-logged-in': 'true',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20260101.00.00',
            # 'cookie': 'VISITOR_INFO1_LIVE=cx8Ubf7KT8M; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgIA%3D%3D; __Secure-ROLLOUT_TOKEN=CIPG-vjppfrrFBC3h8nR0c6OAxi7lOmp_u-RAw%3D%3D; YSC=h9IQ4D7ENrM; PREF=f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000; SID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXclrU5XHOdglYRTr9QgoRLQACgYKAYUSARQSFQHGX2MiKGEIH-i-v9hVVvdI_w4xHxoVAUF8yKqyDSo8Ozltq9x1DMe6OLVl0076; __Secure-1PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXX5yZYJbZJYVZg7BE6-KCzWQACgYKAY4SARQSFQHGX2MiIS_6DeGoCHrmFbK9C5lrtBoVAUF8yKrQ5GspsH8xEuF1m3T5onDp0076; __Secure-3PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXMX7ZHi16eRCLxZqYuzA-fwACgYKAYQSARQSFQHGX2Mir9jm3nk0W3UDQHZ6tTe3YhoVAUF8yKo5aw286aYRDPk8Dr6OehOX0076; HSID=A5ZWP_OXtm1tXt5Ra; SSID=AAdvwo5XLkRYvN2sq; APISID=IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6; SAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-3PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; __Secure-3PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; CONSISTENCY=APeVyi-gntr9YHcYRsCd6p7ZSmbT1cvVYJ6CyyT01sEfKNxyo0nuVgBt5Qop61Cp9KT639KmbRcdIVGK-eEQoIWfjnv06z7UNlInd4QQ5MegLzfgJojUsDIUmi-SB-mjQPour3bYr-Jut9xfpjl0nxZDAawDgPMpyCji4bjuLlZuuJEGrrHfa5iDvcqSNQ; LOGIN_INFO=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI:QUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; ST-xuwub9=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; SIDCC=AKEyXzUX_VbFZDmKRzeoI_1XRy33oRJhJN0djffmdGqinEkUopqz-gJB66uhueQiG_y28BeNT_w; __Secure-1PSIDCC=AKEyXzX2O-nY78GwG5jw4IEwVBI5Ibx9Osth1_uLy7R9o0oURRXRaBjESSU9vy3m3mwDGIzG9uQ; __Secure-3PSIDCC=AKEyXzUBalvNXBqsuihqCihEtF5zHff1va8j51wP8ps-sH-nH-vVXYQoUgitZcJHB8CPig1Crw; ST-4n4ru8=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3',
        }

        self.base_url = "https://www.youtube.com/youtubei/v1/subscription/subscribe"

    def getdata(self):
        

class TTC:
    def __init__(self, api_key = "bc2a075708b3eec4929da5f613c5dfdf"):
        self.api_key = api_key
        self.base_url = "https://tuongtaccheo.com/logintoken.php"
        self.cookies = {
            '_fbp': 'fb.1.1761508765559.516195470818743635',
            'PHPSESSID': 'cjp45dr87nu8gqv9a96hcl7sk3',
            '_gid': 'GA1.2.242056569.1767635360',
            '_gat_gtag_UA_88794877_6': '1',
            '_ga': 'GA1.2.1652707960.1761508764',
            '_ga_6RNPVXD039': 'GS2.1.s1767635359$o85$g1$t1767635524$j51$l0$h0',
        }

        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
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
            # 'cookie': '_fbp=fb.1.1761508765559.516195470818743635; PHPSESSID=cjp45dr87nu8gqv9a96hcl7sk3; _gid=GA1.2.242056569.1767635360; _gat_gtag_UA_88794877_6=1; _ga=GA1.2.1652707960.1761508764; _ga_6RNPVXD039=GS2.1.s1767635359$o85$g1$t1767635524$j51$l0$h0',
        }

    def get_cookie(self):
        re = requests.post(self.base_url, headers=self.headers, data={'access_token': self.api_key})
        return re.cookies.get_dict()['PHPSESSID']
    
    def getpost(self):
        cookies = self.cookies.copy()
        cookies['PHPSESSID'] = self.get_cookie()
        response = requests.get('https://tuongtaccheo.com/youtube/kiemtien/subcheo/getpost.php', cookies=cookies, headers=self.headers)
        return response.json()
    
if __name__ == "__main__":
    ttc = TTC()
    print(ttc.getpost())