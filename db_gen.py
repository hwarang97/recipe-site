from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.jungle

db.recipe.insert_one(
    {
        "id": 1,
        "user_id": 2,
        "title": "백종원 스타일 김치볶음밥",
        "content": "잘 익은 김치를 잘게 썰어 참기름에 볶고 밥을 넣어 함께 볶는다. 간장과 고추장을 약간 넣어 간을 맞추고 마지막에 계란 프라이를 올리면 완성.",
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b",
        "class": "한식",
    }
)
db.recipe.insert_one(
    {
        "id": 2,
        "user_id": 3,
        "title": "집에서 만드는 일본식 오므라이스",
        "content": "버터에 양파와 햄을 볶고 케첩과 밥을 넣어 볶는다. 얇게 만든 계란 지단 위에 볶음밥을 올리고 감싸서 접시에 담는다.",
        "image": "https://images.unsplash.com/photo-1604908176997-4311d3b3f4c6",
        "class": "일식",
    }
)
db.recipe.insert_one(
    {
        "id": 3,
        "user_id": 1,
        "title": "크림치즈 까르보나라 파스타",
        "content": "팬에 베이컨을 볶고 생크림과 크림치즈를 넣어 소스를 만든다. 삶은 스파게티 면을 넣고 파마산 치즈와 후추로 마무리.",
        "image": "https://images.unsplash.com/photo-1608759266063-dc3c9d3b6c9c",
        "class": "양식",
    }
)
db.recipe.insert_one(
    {
        "id": 4,
        "user_id": 4,
        "title": "매콤달콤 떡볶이",
        "content": "고추장, 고춧가루, 설탕, 간장을 섞어 양념을 만든다. 물에 떡과 어묵을 넣고 끓이다가 양념을 넣어 걸쭉하게 졸인다.",
        "image": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f",
        "class": "분식",
    }
)
db.recipe.insert_one(
    {
        "id": 5,
        "user_id": 2,
        "title": "닭가슴살 아보카도 샐러드",
        "content": "구운 닭가슴살을 먹기 좋게 찢고 아보카도와 토마토를 썬다. 올리브오일과 레몬즙을 뿌려 가볍게 섞는다.",
        "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",
        "class": "다이어트",
    }
)
db.recipe.insert_one(
    {
        "id": 6,
        "user_id": 5,
        "title": "집밥 된장찌개",
        "content": "멸치와 다시마로 육수를 만든 후 된장을 풀어 끓인다. 두부, 애호박, 양파를 넣고 마지막에 고추와 마늘을 넣는다.",
        "image": "https://images.unsplash.com/photo-1590301157890-4810ed352733",
        "class": "한식",
    }
)
db.recipe.insert_one(
    {
        "id": 7,
        "user_id": 3,
        "title": "참치마요 덮밥",
        "content": "참치에 마요네즈와 약간의 간장을 넣어 섞는다. 따뜻한 밥 위에 올리고 김가루와 계란 노른자를 곁들인다.",
        "image": "https://images.unsplash.com/photo-1604909052743-94e838986d24",
        "class": "간편식",
    }
)
db.recipe.insert_one(
    {
        "id": 8,
        "user_id": 6,
        "title": "진한 초콜릿 브라우니",
        "content": "녹인 초콜릿과 버터에 설탕과 계란을 섞는다. 밀가루와 코코아파우더를 넣어 반죽한 뒤 오븐에서 180도로 20분간 굽는다.",
        "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c",
        "class": "디저트",
    }
)
db.recipe.insert_one(
    {
        "id": 9,
        "user_id": 1,
        "title": "바나나 딸기 스무디",
        "content": "바나나와 딸기, 우유를 믹서에 넣고 꿀을 약간 추가해 곱게 갈아준다.",
        "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888",
        "class": "음료",
    }
)
db.recipe.insert_one(
    {
        "id": 10,
        "user_id": 4,
        "title": "마늘버터 새우볶음",
        "content": "팬에 버터를 녹이고 다진 마늘을 볶는다. 새우를 넣고 소금과 후추로 간한 뒤 파슬리를 뿌려 완성.",
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c",
        "class": "양식",
    }
)
