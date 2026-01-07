import requests

cookies = {
    'VISITOR_INFO1_LIVE': 'cx8Ubf7KT8M',
    'VISITOR_PRIVACY_METADATA': 'CgJWThIEGgAgIA%3D%3D',
    'PREF': 'f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000',
    'HSID': 'A5ZWP_OXtm1tXt5Ra',
    'SSID': 'AAdvwo5XLkRYvN2sq',
    'APISID': 'IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6',
    'SAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    '__Secure-1PAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    '__Secure-3PAPISID': '0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz',
    'YSC': '73fkziYJT74',
    '__Secure-ROLLOUT_TOKEN': 'CIPG-vjppfrrFBC3h8nR0c6OAxiQqOGpnveRAw%3D%3D',
    'SID': 'g.a0005Qi7fX9BvQQK_1ZuU5TxO6DQQi1tIOhtkjQPwSt0SmGTAoMclLCyJ6ULTZBu1evCwURYLAACgYKAfASARQSFQHGX2Miv9j2mwdZ98IcHiWAqAIQZhoVAUF8yKrIjqD9HAqVucExtjhuO9_x0076',
    '__Secure-1PSID': 'g.a0005Qi7fX9BvQQK_1ZuU5TxO6DQQi1tIOhtkjQPwSt0SmGTAoMc9Ga3NEWghllxu-QNYoCXUQACgYKAZgSARQSFQHGX2Miia1yC4khWnaW72Ols6Ua1hoVAUF8yKo-M2BcIfHxz_7acnc4Vedd0076',
    '__Secure-3PSID': 'g.a0005Qi7fX9BvQQK_1ZuU5TxO6DQQi1tIOhtkjQPwSt0SmGTAoMcx4xgOsTjmpP8WwZkzbcAfAACgYKAXgSARQSFQHGX2MiBosGK6GtgvwCldf2XhnXeBoVAUF8yKo69okCagv68d8hRHdbUfLB0076',
    '__Secure-1PSIDTS': 'sidts-CjQBflaCdYj03C2y2Z_0W7yp3-n74Vwv5I6MA7VlxEEIkDArhnWf9LxG2nYborv-AOasupIxEAA',
    '__Secure-3PSIDTS': 'sidts-CjQBflaCdYj03C2y2Z_0W7yp3-n74Vwv5I6MA7VlxEEIkDArhnWf9LxG2nYborv-AOasupIxEAA',
    'LOGIN_INFO': 'AFmmF2swRAIgeK-0TEVhb7HobGTCt831Q2aqRmTz6KEKhfX16Y0kDkICIGhxch0PnmUCwy1b4r-PDZuPZ75LmYgUEjDogTXA4K7D:QUQ3MjNmd1BFVnIyRmNSLWs2MUt6UXpubUxra0gwWVl5T1prQTJsMUxtb3NOV2VpOFdqY0xnT3Q0eDNMazNfNlhOSTVRdl9pZ3B0U3dma2ZVUzFPaTJIRl9wOFFmbGxuclBVZ19ZMFI2dGVMM3JtdFF5dnJxc3BOcGI5ZVJYcTd3cndLTU5RYmxPUDJ2emxHb0Z1WUZ3Q2NzQ3QxWWMzVGc3bDBXeWJoVmd1WTBqQ1lBUGE5ZDgzZ0JFR29xb1VQSWU4MFZ3MjE1Qm9NRklEQTVwcU9BTzAzVEZFQzJZcXFuQQ==',
    'SIDCC': 'AKEyXzWMO9bpcIS5PmuotuF4Q6QqKlx3pEmfo1qSMBqmnsaz9qZaBIXv5MfEYrtXuWoXVqxfJvs',
    '__Secure-1PSIDCC': 'AKEyXzWkKl6K4hwHIrP2GDrPjajMiXLQstCW_N1gWlN8ffTtkQnSClT5nVt5nN7yBbuGfbUTjD0',
    '__Secure-3PSIDCC': 'AKEyXzWVaphR0gb11ruRDSQC0YqJ7vgv5NlwJo1GjlOUjFSCbXlh14-zsPSqDIZu3a17tXrn7A',
    'ST-4n4ru8': 'session_logininfo=AFmmF2swRAIgeK-0TEVhb7HobGTCt831Q2aqRmTz6KEKhfX16Y0kDkICIGhxch0PnmUCwy1b4r-PDZuPZ75LmYgUEjDogTXA4K7D%3AQUQ3MjNmd1BFVnIyRmNSLWs2MUt6UXpubUxra0gwWVl5T1prQTJsMUxtb3NOV2VpOFdqY0xnT3Q0eDNMazNfNlhOSTVRdl9pZ3B0U3dma2ZVUzFPaTJIRl9wOFFmbGxuclBVZ19ZMFI2dGVMM3JtdFF5dnJxc3BOcGI5ZVJYcTd3cndLTU5RYmxPUDJ2emxHb0Z1WUZ3Q2NzQ3QxWWMzVGc3bDBXeWJoVmd1WTBqQ1lBUGE5ZDgzZ0JFR29xb1VQSWU4MFZ3MjE1Qm9NRklEQTVwcU9BTzAzVEZFQzJZcXFuQQ%3D%3D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'SAPISIDHASH 1767727505_bcf9f55efb71ab6d57f104b16e29f2b6c4cff09d_u SAPISID1PHASH 1767727505_bcf9f55efb71ab6d57f104b16e29f2b6c4cff09d_u SAPISID3PHASH 1767727505_bcf9f55efb71ab6d57f104b16e29f2b6c4cff09d_u',
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
    'x-client-data': 'CI22yQEIprbJAQipncoBCOfnygEIlKHLAQiFoM0BCJaMzwEIyZHPAQi9os8BCNSjzwEIkqTPAQiZpc8BCKalzwEY7IXPARiyhs8B',
    'x-goog-authuser': '2',
    'x-goog-visitor-id': 'CgtjeDhVYmY3S1Q4TSj_wvXKBjIKCgJWThIEGgAgIA%3D%3D',
    'x-goog-pageid': '111871817318464101779',
    # 'x-goog-pageid': '101132415648947005236',
    'x-origin': 'https://www.youtube.com',
    'x-youtube-bootstrap-logged-in': 'true',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20260101.00.00',
    # 'cookie': 'VISITOR_INFO1_LIVE=cx8Ubf7KT8M; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgIA%3D%3D; __Secure-ROLLOUT_TOKEN=CIPG-vjppfrrFBC3h8nR0c6OAxi7lOmp_u-RAw%3D%3D; YSC=h9IQ4D7ENrM; PREF=f6=40000000&tz=Etc.GMT-7&f5=20000&f4=10000; SID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXclrU5XHOdglYRTr9QgoRLQACgYKAYUSARQSFQHGX2MiKGEIH-i-v9hVVvdI_w4xHxoVAUF8yKqyDSo8Ozltq9x1DMe6OLVl0076; __Secure-1PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXX5yZYJbZJYVZg7BE6-KCzWQACgYKAY4SARQSFQHGX2MiIS_6DeGoCHrmFbK9C5lrtBoVAUF8yKrQ5GspsH8xEuF1m3T5onDp0076; __Secure-3PSID=g.a0005Qi7fZVpKG4km_uacFqWXYQrFkJuPQjerasb0h03E201aGXXMX7ZHi16eRCLxZqYuzA-fwACgYKAYQSARQSFQHGX2Mir9jm3nk0W3UDQHZ6tTe3YhoVAUF8yKo5aw286aYRDPk8Dr6OehOX0076; HSID=A5ZWP_OXtm1tXt5Ra; SSID=AAdvwo5XLkRYvN2sq; APISID=IJz7TmK8UgtRgkEF/AznTi6P9b-JF452i6; SAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-3PAPISID=0n9NojMQuwyzVQAX/AuhNAVIwY0dYK9iRz; __Secure-1PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; __Secure-3PSIDTS=sidts-CjQBflaCdRvTnDHSN7tANscsgu-6OgRbm9T2KrwmQAD1s5aQR_lSy1wluSWOxt4nqPRMx_VXEAA; CONSISTENCY=APeVyi-gntr9YHcYRsCd6p7ZSmbT1cvVYJ6CyyT01sEfKNxyo0nuVgBt5Qop61Cp9KT639KmbRcdIVGK-eEQoIWfjnv06z7UNlInd4QQ5MegLzfgJojUsDIUmi-SB-mjQPour3bYr-Jut9xfpjl0nxZDAawDgPMpyCji4bjuLlZuuJEGrrHfa5iDvcqSNQ; LOGIN_INFO=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI:QUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; ST-xuwub9=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3; SIDCC=AKEyXzUX_VbFZDmKRzeoI_1XRy33oRJhJN0djffmdGqinEkUopqz-gJB66uhueQiG_y28BeNT_w; __Secure-1PSIDCC=AKEyXzX2O-nY78GwG5jw4IEwVBI5Ibx9Osth1_uLy7R9o0oURRXRaBjESSU9vy3m3mwDGIzG9uQ; __Secure-3PSIDCC=AKEyXzUBalvNXBqsuihqCihEtF5zHff1va8j51wP8ps-sH-nH-vVXYQoUgitZcJHB8CPig1Crw; ST-4n4ru8=session_logininfo=AFmmF2swRgIhAIe5rkTUekhZAMKg563E_QdD8KHdhuM-C6isrIWMTCgoAiEAsVNNuVJss4EVrNYz-uJSEqublf3ibVMm3rNaMRAIjxI%3AQUQ3MjNmd3NLclMzYV9xTlZWcUJuV3h4MXduWmNTMGM0YUo3d0NBNTRQSHVXMUNiWS1KdU5JVHlLQmRkaS1STEd3N1lSMzJDUFd6ZHk4WVN4ZTk5M1JBZS1rSDY0NVg3Q1ZmNHpYZWV6X0ZNWUpNVVdaaFppUTVFNjM4aFJLZEdJSWY5Ny13c1JyYWdnRzBDNUZyYzlBRkV1eWtCQkE5XzZ3',
}

params = {
    'prettyPrint': 'false',
}
json_data = {
    'context': {
        'client': {
            'hl': 'vi',
            'gl': 'VN',
            'remoteHost': '2405:4802:6f82:34c0:5582:95a3:4b1d:a210',
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': 'CgtucVl3WWhDTEI2USi7v_XKBjIKCgJWThIEGgAgFmLfAgrcAjE0LllUPWtYMEtfcmhkMFRERVFWcXd2SC0tSG9zTl92eFpDdU5Pb25NaWZZUFdUVkZyMnBjUldPTUNIcmxfQmZQVldNVjB4V0RDNHRlWG9uczluQ1FlOVlMRXN5cjcxR0VGVEtWRm5xM0NDZkxKX2hZcm5qMllmRFE5a09BbGtqM2xWVVg3Z1dYckxwSkNycktXNVFqMTI1UjdwYnRRU1RDcXhzNVlRbm13OEx2Vk4wajY1ZVFZN1hSZ3dNYWc0Y3NVUTFsR09hQ0pKV1ozQjlmT2p5b2FYQ3B3Uy0tSjhoQURuYTZ4LU9XNzBPU2laVkdOR3BHNzhzcmZibmU5TVRfYnZEWnQyZWtYNnVzNjNwUDlRQUc0YmZ4YldVSWZZZEFFNXN3eU1Bb2VHZVZwNUZTLTl0RTZLSU5SblRjNzl0SVVOVzZwY01ZT2dHN2FqT3g4dTFIZExTN1A1Zw%3D%3D',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20260105.05.00',
            'osName': 'Windows',
            'osVersion': '10.0',
            'originalUrl': 'https://www.youtube.com/watch?v=u25xbCQjnm0',
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'windowWidthPoints': 1365,
            'configInfo': {
                'appInstallData': 'CLu_9coGEMzfrgUQt8nPHBC9irAFEPG00BwQgo_PHBCln6kXEJX3zxwQrKzQHBDatNAcEM3RsQUQjbDQHBCIh7AFEJS20BwQ167QHBDKu9AcEIeD0BwQkYz_EhC8v9AcENqu0BwQndCwBRD8ss4cEIHNzhwQu9nOHBDGvYATEL22rgUQ8p3QHBDGxs8cEObgzxwQtMHQHBCU_rAFEMOR0BwQ8czPHBDhwYATENvB0BwQyfevBRC8s4ATELyk0BwQs5DPHBCcuNAcENK90BwQt4bPHBCM6c8cEImwzhwQvZmwBRCmmrAFEPXVzhwQh6zOHBCW288cEMj3zxwQ9quwBRCihbgiEK7WzxwQqJ-pFxDmh9AcELfq_hIQ5aTQHBDevM4cEMzrzxwQudnOHBC45M4cENPhrwUQ8cTQHBCTg9AcEIOe0BwQm8LQHBC_288cENr3zhwQx7bQHBDi1K4FELnA0BwQieiuBRCmttAcEODNsQUQmrnQHBDE9M8cEIv3zxwQwY_QHBDys9AcEJ3XzxwQmY2xBRCU8s8cEI-50BwQy9GxBRC7woATEK230BwQsZ3_EhC-wdAcEKHB0BwQyrHQHBCw9s8cKmhDQU1TU1JWQy1acS1ETWVVRW9jT3FnTE1CYl9CNWd2d3NSS0hUREtnckFRRHk3NEYtam41Z2dhZ0JxSXVrMmpPRC0xYzlTXzJENFVVNGlQdW5RWGpGc1VxZ3k3cEU1NUxnaWdHSFFjPTAA',
                'coldConfigData': 'CLu_9coGEOy6rQUQvbauBRDi1K4FEL2KsAUQjcywBRCd0LAFEM_SsAUQ4_iwBRCvp84cEPyyzhwQ9dXOHBDGxs8cEPjGzxwQ29PPHBCd188cEJ7XzxwQx9rPHBC_288cEM_gzxwQ5efPHBDn588cELD2zxwQk4PQHBCbhdAcEP2T0BwQhZ7QHBDOrNAcEKyy0BwQ8bTQHBCgtdAcENC10BwQ67jQHBCaudAcEJW70BwQucDQHBChwdAcEL7B0BwQ28HQHBCyw9AcEKjF0BwQ6srQHBCihbgiGjJBQ0RTUjJUQXQ2OEZRNEYySTcyNGxHMUdpdkhCM1JVS2hPNzQ5eGRsdVRDd3pfSDVqUSIyQUNEU1IyVHN1QWlmZzB6X19TUElKdnhROXhDMVJUWllETjBtWEVlQXlvT3R6YzFpa3cqsAFDQU1TZncwMnVOMjNBcVFabHgtZlQ1bVNtaEQ3Rm8wMl9pT25EY2dBckF4cU5QWVlxQUxaRjdZTkFpNlhBT2dGMFFLWEJReWpCQlZObWJHM0g0V2tCWkdjQmVIYkFjX0NBSS1uQnYzVUJqTFBnQVhacEFZRG9ySUZ5a3NHc0ctSEE4WUo4d09JNUFYTFNnU1N2Z2FaUGVveGxRVmJnd1RaV3BBaWowNndITE1Hd2k4PQ%3D%3D',
                'coldHashData': 'CLu_9coGEhMyMjkxMTkxMDc1OTU0MjA5MDcyGLu_9coGMjJBQ0RTUjJUQXQ2OEZRNEYySTcyNGxHMUdpdkhCM1JVS2hPNzQ5eGRsdVRDd3pfSDVqUToyQUNEU1IyVHN1QWlmZzB6X19TUElKdnhROXhDMVJUWllETjBtWEVlQXlvT3R6YzFpa3dCsAFDQU1TZncwMnVOMjNBcVFabHgtZlQ1bVNtaEQ3Rm8wMl9pT25EY2dBckF4cU5QWVlxQUxaRjdZTkFpNlhBT2dGMFFLWEJReWpCQlZObWJHM0g0V2tCWkdjQmVIYkFjX0NBSS1uQnYzVUJqTFBnQVhacEFZRG9ySUZ5a3NHc0ctSEE4WUo4d09JNUFYTFNnU1N2Z2FaUGVveGxRVmJnd1RaV3BBaWowNndITE1Hd2k4PQ%3D%3D',
                'hotHashData': 'CLu_9coGEhQxMTk0MDU3NDMwMzkwOTU2NzY0NRi7v_XKBiiU5PwSKKXQ_RIonpH-Eii36v4SKOft_hIokYz_Eiixnf8SKNKu_xIoy5GAEyi1m4ATKNiwgBMok7SAEyiwt4ATKKW4gBMouMGAEyiywoATKLvCgBMopZ-pFyion6kXMjJBQ0RTUjJUQXQ2OEZRNEYySTcyNGxHMUdpdkhCM1JVS2hPNzQ5eGRsdVRDd3pfSDVqUToyQUNEU1IyVHN1QWlmZzB6X19TUElKdnhROXhDMVJUWllETjBtWEVlQXlvT3R6YzFpa3dCNENBTVNJdzBKb3RmNkZhN0JCdXViQnRVTW5BTVZGdDNQd2d6aTlnX2NxZVlMbDlja204b0c%3D',
            },
            'screenDensityFloat': 1,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Etc/GMT-7',
            'browserName': 'Chrome',
            'browserVersion': '143.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': 'ChxOelU1TWpNeU9UZ3dOVFl3TWprek5qQTJNQT09ELu_9coGGLu_9coG',
            'rolloutToken': 'CJL-0sznxOmuyAEQiNSa3aPykQMYh_XWpc32kQM%3D',
            'screenWidthPoints': 1365,
            'screenHeightPoints': 953,
            'screenPixelDensity': 1,
            'utcOffsetMinutes': 420,
            'connectionType': 'CONN_CELLULAR_4G',
            'memoryTotalKbytes': '8000000',
            'mainAppWebInfo': {
                'graftUrl': 'https://www.youtube.com/watch?v=u25xbCQjnm0',
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
            'consistencyTokenJars': [
                {
                    'encryptedTokenJarContents': 'APeVyi_Kw55r3K_i98RNGpYxS4gx4SrSwPCpfkVuDx9a2-TmtPtU5RZ9dvzL1cvFM8mRbTbMdo0w-K9gSrD0Q7Pb14LJN_3nCUbZBnN8i8BFaqkK8jF34hB-D069mP6_q0fsafzQLqggoue1Npk',
                },
            ],
            'internalExperimentFlags': [],
        },
        'clientScreenNonce': 'SkuSgH5lKVJO04UH',
        'clickTracking': {
            'clickTrackingParams': 'CJwDEJsrIhMIlt6isND3kQMV23k4BR2IkDDqKPgdMgV3YXRjaMoBBFBP-xk=',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1767727036963',
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
                    'value': '16',
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
                    'value': '953',
                },
                {
                    'key': 'biw',
                    'value': '1350',
                },
                {
                    'key': 'brdim',
                    'value': '1920,92,1920,92,1920,92,1920,1040,1365,953',
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
            'bid': 'ANyPxKpNHj7WXH3FQMh-yZZ73-fuitRChhyGtVuUtvnvd9jwxREeKlfWdsJoS7x3B87tdCffYT7c-juqVVcIyL5YiQ4pEBn1PQ',
        },
    },
    'channelIds': [
        'UCjcetjIFa1Sbp7pJOqjiRHA',
    ],
    'params': 'EgIIAxgAIgt1MjV4YkNRam5tMA%3D%3D',
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
#data = '{"context":{"client":{"hl":"vi","gl":"VN","remoteHost":"2405:4802:9620:2460:6435:cdd8:4c34:1ffd","deviceMake":"","deviceModel":"","visitorData":"CgtjeDhVYmY3S1Q4TSiKuOrKBjIKCgJWThIEGgAgIA%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20260101.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/watch?v=fsuiTRwgmZE","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","windowWidthPoints":552,"configInfo":{"appInstallData":"CIq46soGEJX3zxwQieiuBRCBzc4cELvZzhwQt4bPHBDE9M8cEKKFuCIQyPfPHBDT4a8FEKys0BwQmY2xBRCHg9AcEJbbzxwQlPLPHBC8s4ATEPG00BwQwY_QHBC5wNAcEJ7QsAUQiIewBRCi-88cEM3RsQUQ2q7QHBCwhs8cEI2w0BwQtMHQHBDxxNAcEParsAUQ167QHBC-irAFEJq50BwQ4cGAExDys9AcEJGM_xIQyrvQHBDyndAcELOQzxwQm8LQHBDM688cELjkzhwQ5ofQHBCUttAcENvB0BwQg57QHBC9mbAFEMa9gBMQi_fPHBDFxs8cELfJzxwQx7bQHBCmmrAFEObgzxwQ2vfOHBC8pNAcEODNsQUQlIPQHBCPudAcEMn3rwUQnLjQHBDM364FEN68zhwQh6zOHBCJsM4cEJzXzxwQ0r3QHBDlpNAcEMvRsQUQ_LLOHBCM6c8cELy_0BwQlP6wBRCrnc8cEL22rgUQ4tSuBRCCj88cEK7WzxwQqJ-pFxDxzM8cELfq_hIQudnOHBDatNAcEKa20BwQw5HQHBCynf8SEMWM0BwQvsHQHBDJutAcEKuK0BwQ4L_QHBDLsdAcEMfDgBMqdENBTVNVeFZJLVpxLURNZVVFdlVBaWdhcUFzd0Z1UWItdy1ZTDhMRVNoMHd5b0t3RUE4dS1CZm81LVlJR29BYWlMcG9oOFVfT0QtMWM5U18yRDRVVTRpUHVuUVhqRnNVcWd5NzBEXzBNbmdyNE9ZSW9CaDBIMAA%3D","coldConfigData":"CIq46soGEO66rQUQxYWuBRC9tq4FEOLUrgUQvoqwBRCNzLAFEJ7QsAUQz9KwBRDj-LAFEK-nzhwQ_LLOHBCA_M4cELCGzxwQrpTPHBCrnc8cELTGzxwQxcbPHBD4xs8cENvTzxwQnNfPHBCf188cEMjazxwQz-DPHBDl588cEOfnzxwQlIPQHBCritAcEMWM0BwQ_pPQHBDOrNAcEPG00BwQoLXQHBDPtdAcEOy40BwQmrnQHBDJutAcEJW70BwQ4L_QHBC5wNAcEL7B0BwQ28HQHBCxw9AcEJvF0BwQp8XQHBCihbgiGjJBQ0RTUjJUUTh1RHV3SWpZM1RJVkRWdzR6YlpYOVFsY3Y5NXk3RE1oYWxPMUwxV3BSZyIyQUNEU1IyU2pSbmxKS0VrTkhVc0hJdG8wOUZCMVh3SmcwdVpRS091cnluNUVlM1huc3cqvAFDQU1TaGdFTk03amR0d0trR1pjZm4wLVprcG9RMUFxdkE0MDJfaU9uRGNnQXJBeHFOTG9TdEEyb0F0a1h0ZzBDTDVZQTZBWE9BZ3lXQlF3VlNiVy15UXpzLS1ZTGhhUUZrWndGNGRzQno4SUFyM3pZSV8zVUJqTFBnQVhacEFZRG9ySUZ5a3NHc0ctSEE4WUo4d09JNUFYTFNnU1N2Z2FaUGVveGxRVmJnZ1RhV3BBaXAwOXZzUnl6Qmc9PQ%3D%3D","coldHashData":"CIq46soGEhQxNDc2MDc1NDk4MTQ1MjU4MjUyORiKuOrKBjIyQUNEU1IyVFE4dUR1d0lqWTNUSVZEVnc0emJaWDlRbGN2OTV5N0RNaGFsTzFMMVdwUmc6MkFDRFNSMlNqUm5sSktFa05IVXNISXRvMDlGQjFYd0pnMHVaUUtPdXJ5bjVFZTNYbnN3QrwBQ0FNU2hnRU5NN2pkdHdLa0daY2ZuMC1aa3BvUTFBcXZBNDAyX2lPbkRjZ0FyQXhxTkxvU3RBMm9BdGtYdGcwQ0w1WUE2QVhPQWd5V0JRd1ZTYlcteVF6cy0tWUxoYVFGa1p3RjRkc0J6OElBcjN6WUlfM1VCakxQZ0FYWnBBWURvcklGeWtzR3NHLUhBOFlKOHdPSTVBWExTZ1NTdmdhWlBlb3hsUVZiZ2dUYVdwQWlwMDl2c1J5ekJnPT0%3D","hotHashData":"CIq46soGEhMyOTA1NDU5ODM0MzYyODkxMzg1GIq46soGKJTk_BIopdD9Eiiekf4SKMjK_hIot-r-EiiRjP8SKLKd_xIoy5GAEyi1m4ATKLSwgBMo2LCAEyiTtIATKLC3gBMopbiAEyi5wYATKLLCgBMox8OAEyion6kXMjJBQ0RTUjJUUTh1RHV3SWpZM1RJVkRWdzR6YlpYOVFsY3Y5NXk3RE1oYWxPMUwxV3BSZzoyQUNEU1IyU2pSbmxKS0VrTkhVc0hJdG8wOUZCMVh3SmcwdVpRS091cnluNUVlM1huc3dCNENBTVNJdzBKb3RmNkZhN0JCdXViQnRVTW5BTVZGdDNQd2d6aTlnX2NxZVlMbDlja204b0c%3D"},"screenDensityFloat":1,"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"Etc/GMT-7","browserName":"Chrome","browserVersion":"143.0.0.0","memoryTotalKbytes":"8000000","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOelU1TVRVMU1UWTROVE15T1RZeU56VTVOdz09EIq46soGGIm46soG","rolloutToken":"CIPG-vjppfrrFBC3h8nR0c6OAxi7lOmp_u-RAw%3D%3D","screenWidthPoints":552,"screenHeightPoints":952,"screenPixelDensity":1,"utcOffsetMinutes":420,"connectionType":"CONN_CELLULAR_4G","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/watch?v=fsuiTRwgmZE","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clientScreenNonce":"kmCoZXJZM3z7Y3ST","clickTracking":{"clickTrackingParams":"CJwGEJsrIhMIr73hu63ykQMVY5lWAR2TIgsmKPgdMgV3YXRjaMoBBHLJBbE="},"adSignalsInfo":{"params":[{"key":"dt","value":"1767545866704"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"420"},{"key":"u_his","value":"12"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"952"},{"key":"biw","value":"537"},{"key":"brdim","value":"2937,92,2937,92,1920,92,910,1047,552,952"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKo_PH-BUL6N_iqxbcAowVLV_xyMs0Pg0XHHuMB9kSTJmOK5YblAG_0nQ7qveUopsQd2tTq7fpR4Mm0RMNZPNz0ofnQ73A"}},"channelIds":["UC8gai-XGPEQuseaTHeNoSKQ"],"params":"EgIIAxgAIgtmc3VpVFJ3Z21aRQ%3D%3D"}'
#response = requests.post(
#    'https://www.youtube.com/youtubei/v1/subscription/subscribe',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)