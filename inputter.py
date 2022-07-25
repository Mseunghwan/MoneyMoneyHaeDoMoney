import json
import requests
import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "MMHDM",
    user = "postgres",
    password = "min95440949@"
    )


# member = [] # 가입자 수
# number = [] # 사업자등록번호
# isjoin = [] # 사업장가입상태코드
# address = [] # 사업장도로명 상세주소
# companyname = [] # 사업장 명
# companysecotr = [] # 사업장 업종코드 명

# 총 데이터 -- 544122 --> 페이지 당 10 --> 마지막 페이지 54413

member = [] # 가입자 수
number = [] # 사업자등록번호
isjoin = [] # 사업장가입상태코드
address = [] # 사업장도로명 상세주소
companyname = [] # 사업장 명
companysector = [] # 사업장 업종코드 명

for num in range(1, 54411):
    comp = requests.get("https://api.odcloud.kr/api/15083277/v1/uddi:d7e2de87-da03-4ec4-9741-ef4208ce393c?page={}&perPage=10&serviceKey=7mNZWRMWcGvUjboFRTOFbF7lMbFLsF%2F%2Ff9wkD3vZ6DqJ8QRu4zse0OMfQDgAgbs6EZST23Ndv3j2e4gHO2we5g%3D%3D".format(num))
    js = json.loads(comp.content)
    for num2 in range(10):
        member.append(js["data"][num2]['가입자수'])
        number.append(js["data"][num2]['사업자등록번호'])
        isjoin.append(js["data"][num2]['사업장가입상태코드 1 등록 2 탈퇴'])
        address.append(js["data"][num2]['사업장도로명상세주소'])
        companyname.append(js["data"][num2]['사업장명'])
        companysector.append(js["data"][num2]['사업장업종코드명'])


cur = con.cursor()

for num3 in range(0, 544100):
    cur.execute("insert into moneytable (id, member, number, address, companyname, companysector, isjoin) values (%s, %s, %s, %s, %s, %s, %s)", (num3+544121, member[num3], number[num3], address[num3], companyname[num3], companysector[num3], isjoin[num3]))
    con.commit()   ## 입력 후 해줘야 하는 commit()

cur.close()
con.close()