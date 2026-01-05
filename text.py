import requests

cookies = {
    'VISITOR_INFO1_LIVE': 'cx8Ubf7KT8M',
    'VISITOR_PRIVACY_METADATA': 'CgJWThIEGgAgIA%3D%3D',
    'PREF': 'f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000',
    'SID': 'g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXclrU5XHOdglYRTr9QgoRLQACgYKAYUSARQSFQHGX2MiKGEIH-i-v9hVVvdI_w4xHxoVAUF8yKqyDSo8Ozltq9x1DMe6OLVl0076',
    '__Secure-1PSID': 'g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXX5yZYJbZJYVZg7BE6-KCzWQACgYKAY4SARQSFQHGX2MiIS_6DeGoCHrmFbK9C5lrtBoVAUF8yKrQ5GspsH8xEuF1m3T5onDp0076',
    '__Secure-3PSID': 'g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXMX7ZHi16eRCLxZqYuzA-fwACgYKAYQSARQSFQHGX2Mir9jm3nk0W3UDQHZ6tTe3YhoVAUF8yKo5aw286aYRDPk8Dr6OehOX0076',
    'HSID': 'A5ZWP_OXtm1tXt5Ra',
    'SSID': 'AAdvwo5XLkRYvN2sq',
    'APISID': 'IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6',
    'SAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    '__Secure-1PAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    '__Secure-3PAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    '__Secure-ROLLOUT_TOKEN': 'CIPG-vjppfrrFBC3h8nR0c6OAxiwsri5xPSRAw%3D%3D',
    'YSC': '-92uWbgmoxc',
    '__Secure-1PSIDTS': 'sidts-CjQBflaCdRsb-7XDjJD2-j3Ro_dTMBel4dH2bpTqP8v2UC1sdy32c-hcrWaD6rVNwZongK0xEAA',
    '__Secure-3PSIDTS': 'sidts-CjQBflaCdRsb-7XDjJD2-j3Ro_dTMBel4dH2bpTqP8v2UC1sdy32c-hcrWaD6rVNwZongK0xEAA',
    'LOGIN_INFO': 'AFmmF2swRQIhAKb1eSxUHlTVIqhFaOY_rgjy5XuUA6qjPbcuWnHj6nckAiB7Dh-qAQ3cS-mFX5d2SFMa9h0aqb6RFHQpRmbqOsw1EQ:QUQ3MjNmeUpKSW5yS3BuVnFWZC1UXzc2aG5VeXFkWVZyRm42WGI3MGZ3UFdUaVVsNkk1NktMLTdwUnNRVTFGTnB5NjJlYzdtY2RDWG9oeWxITWlwaEpORUhLYzIxcGpyU3hBQUloY2VxUkQtdjloYnBiQkxHQURuV3d3dlNwOWd4NTVKWHFBTlczRkgzWEJEVVV6d05EUm5XZmg2UkF3eGk0UjJPOGtwY09ybGtTSFFuYXNsZkh2S1VZQUFNeVBhdDlTeS1kQnEyeTFELVpRZXpseE94UV9ONUhId0V0U3VCdw==',
    'SIDCC': 'AKEyXzWpgkzEkS_yeb-Pr40kkST__b7cjHpfgMjJtDd8LV4OdGjpl7OB9UU41rySBVwQ9x4ZAWQ',
    '__Secure-1PSIDCC': 'AKEyXzXgubu2cJaIu6XdrxSJgameX0MY8MVaOfplBKzO6vV8ohKSuxaGWXRmH3H19d9Y3KRg5QI',
    '__Secure-3PSIDCC': 'AKEyXzUZDPUt94xQmuePEftxf8MuIYlJz3Ddk_pt0fjLZ8W7sgscA1q8Vm8GuXtwzl03myhtKQ',
    'ST-4n4ru8': 'session_logininfo=AFmmF2swRQIhAKb1eSxUHlTVIqhFaOY_rgjy5XuUA6qjPbcuWnHj6nckAiB7Dh-qAQ3cS-mFX5d2SFMa9h0aqb6RFHQpRmbqOsw1EQ%3AQUQ3MjNmeUpKSW5yS3BuVnFWZC1UXzc2aG5VeXFkWVZyRm42WGI3MGZ3UFdUaVVsNkk1NktMLTdwUnNRVTFGTnB5NjJlYzdtY2RDWG9oeWxITWlwaEpORUhLYzIxcGpyU3hBQUloY2VxUkQtdjloYnBiQkxHQURuV3d3dlNwOWd4NTVKWHFBTlczRkgzWEJEVVV6d05EUm5XZmg2UkF3eGk0UjJPOGtwY09ybGtTSFFuYXNsZkh2S1VZQUFNeVBhdDlTeS1kQnEyeTFELVpRZXpseE94UV9ONUhId0V0U3VCdw%3D%3D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'SAPISIDHASH 1767637089_aa167271b1037a537037e43a2ee224b9bf055766_u SAPISID1PHASH 1767637089_aa167271b1037a537037e43a2ee224b9bf055766_u SAPISID3PHASH 1767637089_aa167271b1037a537037e43a2ee224b9bf055766_u',
    'content-type': 'application/json',
    'device-memory': '8',
    'origin': 'https://www.youtube.com',
    'priority': 'u=1, i',
    'referer': 'https://www.youtube.com/@amnhacchualanh.',
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
    'sec-ch-viewport-width': '397',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-browser-channel': 'stable',
    'x-browser-copyright': 'Copyright 2025 Google LLC. All Rights reserved.',
    'x-browser-validation': 'UujAs0GAwdnCJ9nvrswZ+O+oco0=',
    'x-browser-year': '2025',
    'x-client-data': 'CI22yQEIprbJAQipncoBCOfnygEIlqHLAQiFoM0BCJaMzwEIyZHPAQjUo88BCJKkzwEImaXPAQimpc8BGOyFzwEYsobPAQ==',
    'x-goog-authuser': '0',
    'x-goog-pageid': '101132415648947005236',
    'x-goog-visitor-id': 'CgtjeDhVYmY3S1Q4TSjOgPDKBjIKCgJWThIEGgAgIA%3D%3D',
    'x-origin': 'https://www.youtube.com',
    'x-youtube-bootstrap-logged-in': 'true',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20260105.01.00',
    # 'cookie': 'VISITOR_INFO1_LIVE=cx8Ubf7KT8M; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgIA%3D%3D; PREF=f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000; SID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXclrU5XHOdglYRTr9QgoRLQACgYKAYUSARQSFQHGX2MiKGEIH-i-v9hVVvdI_w4xHxoVAUF8yKqyDSo8Ozltq9x1DMe6OLVl0076; __Secure-1PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXX5yZYJbZJYVZg7BE6-KCzWQACgYKAY4SARQSFQHGX2MiIS_6DeGoCHrmFbK9C5lrtBoVAUF8yKrQ5GspsH8xEuF1m3T5onDp0076; __Secure-3PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXMX7ZHi16eRCLxZqYuzA-fwACgYKAYQSARQSFQHGX2Mir9jm3nk0W3UDQHZ6tTe3YhoVAUF8yKo5aw286aYRDPk8Dr6OehOX0076; HSID=A5ZWP_OXtm1tXt5Ra; SSID=AAdvwo5XLkRYvN2sq; APISID=IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6; SAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-3PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-ROLLOUT_TOKEN=CIPG-vjppfrrFBC3h8nR0c6OAxiwsri5xPSRAw%3D%3D; YSC=-92uWbgmoxc; __Secure-1PSIDTS=sidts-CjQBflaCdRsb-7XDjJD2-j3Ro_dTMBel4dH2bpTqP8v2UC1sdy32c-hcrWaD6rVNwZongK0xEAA; __Secure-3PSIDTS=sidts-CjQBflaCdRsb-7XDjJD2-j3Ro_dTMBel4dH2bpTqP8v2UC1sdy32c-hcrWaD6rVNwZongK0xEAA; LOGIN_INFO=AFmmF2swRQIhAKb1eSxUHlTVIqhFaOY_rgjy5XuUA6qjPbcuWnHj6nckAiB7Dh-qAQ3cS-mFX5d2SFMa9h0aqb6RFHQpRmbqOsw1EQ:QUQ3MjNmeUpKSW5yS3BuVnFWZC1UXzc2aG5VeXFkWVZyRm42WGI3MGZ3UFdUaVVsNkk1NktMLTdwUnNRVTFGTnB5NjJlYzdtY2RDWG9oeWxITWlwaEpORUhLYzIxcGpyU3hBQUloY2VxUkQtdjloYnBiQkxHQURuV3d3dlNwOWd4NTVKWHFBTlczRkgzWEJEVVV6d05EUm5XZmg2UkF3eGk0UjJPOGtwY09ybGtTSFFuYXNsZkh2S1VZQUFNeVBhdDlTeS1kQnEyeTFELVpRZXpseE94UV9ONUhId0V0U3VCdw==; SIDCC=AKEyXzWpgkzEkS_yeb-Pr40kkST__b7cjHpfgMjJtDd8LV4OdGjpl7OB9UU41rySBVwQ9x4ZAWQ; __Secure-1PSIDCC=AKEyXzXgubu2cJaIu6XdrxSJgameX0MY8MVaOfplBKzO6vV8ohKSuxaGWXRmH3H19d9Y3KRg5QI; __Secure-3PSIDCC=AKEyXzUZDPUt94xQmuePEftxf8MuIYlJz3Ddk_pt0fjLZ8W7sgscA1q8Vm8GuXtwzl03myhtKQ; ST-4n4ru8=session_logininfo=AFmmF2swRQIhAKb1eSxUHlTVIqhFaOY_rgjy5XuUA6qjPbcuWnHj6nckAiB7Dh-qAQ3cS-mFX5d2SFMa9h0aqb6RFHQpRmbqOsw1EQ%3AQUQ3MjNmeUpKSW5yS3BuVnFWZC1UXzc2aG5VeXFkWVZyRm42WGI3MGZ3UFdUaVVsNkk1NktMLTdwUnNRVTFGTnB5NjJlYzdtY2RDWG9oeWxITWlwaEpORUhLYzIxcGpyU3hBQUloY2VxUkQtdjloYnBiQkxHQURuV3d3dlNwOWd4NTVKWHFBTlczRkgzWEJEVVV6d05EUm5XZmg2UkF3eGk0UjJPOGtwY09ybGtTSFFuYXNsZkh2S1VZQUFNeVBhdDlTeS1kQnEyeTFELVpRZXpseE94UV9ONUhId0V0U3VCdw%3D%3D',
}

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
        'UCMPY2wfkbsJJHEjP_nwtKtw',
    ],
    'params': 'EgIIAhgA',
}

response = requests.post(
    'https://www.youtube.com/youtubei/v1/subscription/subscribe',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"context":{"client":{"hl":"vi","gl":"VN","remoteHost":"2405:4802:6f82:34c0:5540:fc20:2e7:14ad","deviceMake":"","deviceModel":"","visitorData":"CgtjeDhVYmY3S1Q4TSjOgPDKBjIKCgJWThIEGgAgIA%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20260105.01.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","windowWidthPoints":615,"configInfo":{"appInstallData":"CM6A8MoGEJTyzxwQ8rPQHBDhwYATEOaH0BwQxcbPHBC52c4cEL22rgUQ9quwBRDM688cELyk0BwQ0-GvBRDJ968FEOWk0BwQt4bPHBDDkdAcEIeszhwQo4W4IhDL0bEFEJX3zxwQvL_QHBCmmrAFEIiHsAUQ4tSuBRDgzbEFEN68zhwQxPTPHBDa984cEIKPzxwQjbDQHBCi-88cEJy40BwQnNfPHBCM6c8cEPG00BwQi_fPHBCRjP8SELCGzxwQ_LLOHBC36v4SEPHE0BwQ167QHBCHg9AcEKifqRcQvoqwBRC45M4cENvB0BwQ8p3QHBCPudAcEJq50BwQmY2xBRDartAcEMGP0BwQ5uDPHBDKu9AcEJSD0BwQlP6wBRCUttAcEKa20BwQntCwBRCBzc4cENq00BwQibDOHBCsrNAcELOQzxwQu9nOHBDSvdAcEMa9gBMQvZmwBRCW288cEMj3zxwQm8LQHBC8s4ATEK7WzxwQq53PHBDHttAcEM3RsQUQzN-uBRCDntAcELnA0BwQieiuBRC0wdAcEMWM0BwQy7HQHBDgv9AcEMfDgBMQvsHQHBDJutAcKnRDQU1TVWhWSi1acS1ETWVVRW9jT3FnTE1CYmtHX3NQbUNfQ3hFb2RNTXFDc0JBUEx2Z1g2T2ZtQ0JxQUdvaTZhSWZGUHpnX3RYUFV2OWctRkZPSWo3cDBGNHhiRktsUzNMX1FQX1F5ZUN2ZzVnaWdHSFFjPTAA","coldConfigData":"CM6A8MoGEO66rQUQxYWuBRC9tq4FEOLUrgUQvoqwBRCNzLAFEJ7QsAUQz9KwBRDj-LAFEK-nzhwQ_LLOHBCA_M4cELCGzxwQrpTPHBCrnc8cELTGzxwQxcbPHBD4xs8cENvTzxwQnNfPHBCf188cEMjazxwQz-DPHBDl588cEOfnzxwQlIPQHBDFjNAcEP6T0BwQzqzQHBDxtNAcEKC10BwQz7XQHBDsuNAcEJq50BwQybrQHBCVu9AcEOC_0BwQucDQHBC-wdAcENvB0BwQscPQHBCbxdAcEKfF0BwQo4W4IhoyQUNEU1IyVFE4dUR1d0lqWTNUSVZEVnc0emJaWDlRbGN2OTV5N0RNaGFsTzFMMVdwUmciMkFDRFNSMlNqUm5sSktFa05IVXNISXRvMDlGQjFYd0pnMHVaUUtPdXJ5bjVFZTNYbnN3KrQBQ0FNU2dBRU5OYmpkdHdLa0daY2ZuMC1aa3BvUTFBcXZBNDAyX2lPbkRjZ0FyQXhxTlBZWXFBTFpGN1lOQWktV0FPZ0Z6Z0lNbGdVTUZVMlpzYmNmaGFRRmtad0Y0ZHNCejhJQXIzellJXzNVQmpMUGdBWFpwQVlEb3JJRnlrc0dzRy1IQThZSjh3T0k1QVhMU2dTU3ZnYVpQZW94bFFWYmdnVGFXcEFpcDA5dnNSeXpCZz09","coldHashData":"CM6A8MoGEhMxODgxMDYwNDgxNDc3OTQ0ODQwGM6A8MoGMjJBQ0RTUjJUUTh1RHV3SWpZM1RJVkRWdzR6YlpYOVFsY3Y5NXk3RE1oYWxPMUwxV3BSZzoyQUNEU1IyU2pSbmxKS0VrTkhVc0hJdG8wOUZCMVh3SmcwdVpRS091cnluNUVlM1huc3dCtAFDQU1TZ0FFTk5iamR0d0trR1pjZm4wLVprcG9RMUFxdkE0MDJfaU9uRGNnQXJBeHFOUFlZcUFMWkY3WU5BaS1XQU9nRnpnSU1sZ1VNRlUyWnNiY2ZoYVFGa1p3RjRkc0J6OElBcjN6WUlfM1VCakxQZ0FYWnBBWURvcklGeWtzR3NHLUhBOFlKOHdPSTVBWExTZ1NTdmdhWlBlb3hsUVZiZ2dUYVdwQWlwMDl2c1J5ekJnPT0%3D","hotHashData":"CM6A8MoGEhMyOTA1NDU5ODM0MzYyODkxMzg1GM6A8MoGKJTk_BIopdD9Eiiekf4SKMjK_hIot-r-EiiRjP8SKMuRgBMotZuAEyi0sIATKNiwgBMok7SAEyiwt4ATKKW4gBMoucGAEyiywoATKMfDgBMoqJ-pFzIyQUNEU1IyVFE4dUR1d0lqWTNUSVZEVnc0emJaWDlRbGN2OTV5N0RNaGFsTzFMMVdwUmc6MkFDRFNSMlNqUm5sSktFa05IVXNISXRvMDlGQjFYd0pnMHVaUUtPdXJ5bjVFZTNYbnN3QjRDQU1TSXcwSm90ZjZGYTdCQnV1YkJ0VU1uQU1WRnQzUHdnemk5Z19jcWVZTGw5Y2ttOG9H"},"screenDensityFloat":1,"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Etc/GMT-7","browserName":"Chrome","browserVersion":"143.0.0.0","memoryTotalKbytes":"8000000","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOelU1TVRrME16UXdOek16TmpFd01USXdOdz09EM6A8MoGGM6A8MoG","rolloutToken":"CIPG-vjppfrrFBC3h8nR0c6OAxiwsri5xPSRAw%3D%3D","screenWidthPoints":397,"screenHeightPoints":952,"screenPixelDensity":1,"utcOffsetMinutes":420,"connectionType":"CONN_CELLULAR_4G","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/@amnhacchualanh.","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clientScreenNonce":"wkjLpRlUEBiyQF_T","clickTracking":{"clickTrackingParams":"CCMQmysYASITCNTznaKB9ZEDFe1BDwIdlxImgSjyODIJY2hhbm5lbHM0ygEEcskFsQ=="},"adSignalsInfo":{"params":[{"key":"dt","value":"1767637071559"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"420"},{"key":"u_his","value":"4"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"952"},{"key":"biw","value":"382"},{"key":"brdim","value":"931,0,931,0,1920,0,996,1047,397,952"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKotoTKZSSvB3Jj_2rog8gqJ3T4F6X-Z2mZnJ8tDux9RlB-jLEOaKThedT5tUf_ro7qcMWqRecQv6U2hPQZYLdfwSJP_yw"}},"channelIds":["UCMPY2wfkbsJJHEjP_nwtKtw"],"params":"EgIIAhgA"}'
#response = requests.post(
#    'https://www.youtube.com/youtubei/v1/subscription/subscribe',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)