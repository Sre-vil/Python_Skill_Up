import requests, json, time

pid = "6EEBC9536F1F4501918C25A814B0FEFB" # ID 넣으삼

url1 = "https://coupon.netmarble.com/api/coupon/reward?gameCode=tskgb&couponCode=%s&langCd=KO_KR&pid="+pid
url2 = "https://coupon.netmarble.com/api/coupon"

coupon = \
"""
세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 1

[RINKARMA]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 2

[GOODLUCK]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 3

[LOVELYRUBY]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 4

[BONVOYAGE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 5

[THANKYOU]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 6

[YONGSANIM]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 7

[REBIRTHBACK]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 8

[WELCOMEBACK]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 9

[CMMAY]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 10

[EVANKARIN]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 11

[THEMONTHOFSENA]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 12

[DARKKNIGHTS]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 13

[GUILDWAR]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 14

[SENAHAJASENA]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 15

[INFINITETOWER]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 16

[7777777]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 17

[LOVESENA]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 18

[TREASURE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 19

[7SENASENA7]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 20

[UPDATES]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 21

[SENARAID]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 22

[SENAEVENTS]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 23

[SECRETCODE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 24

[MAILBOX]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 25

[YUISSONG]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 26

[RELEASEPET]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 27

[MOREKEYS]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 28

[WELCOMESENA]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 29

[HEROSOMMON]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 30

[SENAREGOGO]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 31

[SHOWMETHEMONEY]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 32

[PDKIMJUNGKI]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 33

[INFOCODEX]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 34

[THEHOLYCROSS]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 35

[FUSEGETSPECIAL]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 36

[ADVENTURER]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 37

[NOHOSCHRONICLE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 38

[VALKYRIE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 39

[LEGENDSRAID]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 40

[STORYEVENT]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 41

[SURPRISE]

세븐나이츠리버스 세나의달 이벤트 기념 쿠폰코드 42

[INTOTHESENA]
""".split("\n")

def removeBrackets(s):
    return s[1:-1]

s = requests.Session()

for line in coupon:
    if not line.startswith("["): continue
    line = removeBrackets(line)
    try:
        result1 = json.JSONDecoder().decode(s.get(url1%line).text)
        data = json.dumps({"gameCode":"tskgb", "couponCode":line, "langCd":"KO_KR", "pid":pid})
        result2 = json.JSONDecoder().decode(s.post(url2, data=data).text)
        print(line, result1["resultData"][0]["productName"], result2["errorMessage"])
    except Exception as e:
        print(line, result1["errorMessage"])
    time.sleep(0.5)