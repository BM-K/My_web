import pymongo

m = {
    "이름": "홍길동",
    "나이": 30,
    "거주지": "서울",
    "몸무게": 80,
    "프로필사진":[
        "a.jpg",
        "b.jpg"
    ]
}

m2 = {
    "이름": "최길동",
    "나이": 60,
    "몸무게": 100,
    "거주기": "충청",
    "프로필사진":[
        "a.jpg",
        "b.jpg"
    ]
}

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test
col = db.members

#col.insert(m2)

# r = col.find({"나이":{"$gt":50}}, {"_id": False, "이름": True}  ).sort(-1)
# for i in r:
#     print(i)

rs = col.find( {"이름": "최길동"} )
for r in rs:
    print(r)
#col.update( {"이름":"최길동"}, {"$set": {"이름": "남박사"}} )
col.remove( {"이름": "남박사"} )