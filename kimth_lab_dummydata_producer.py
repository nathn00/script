import uuid
import json
import requests as req

BASE_URL = "http://ec2-13-209-216-177.ap-northeast-2.compute.amazonaws.com:8080"
header = {'Content-Type': 'application/json; charset=utf-8'}
def sign_up(companyId):
  # classification_list = ["발주처", "감리사", "건설사", "설계사", "관리자", "게스트"]
  classification_list = ["발주처", "감리사", "건설사", "설계사", "게스트"]
  for classification in classification_list:
    UUID = f"{uuid.uuid1()}".split("-")[0]
    data = {
      "companyId": f"{companyId}",
      "email": f"{UUID}_{companyId}@gmail.com",
      "password": "1234",
      "name": f"{UUID}::{companyId}",
      "number": "01012345678",
      "classification": classification
    }
    try:
      req.post(f"{BASE_URL}/auth/sign-up", data=json.dumps(data), headers=header)
      print("회원가입 완료!")
    except Exception as e:
      print(e)



def project_producer(companyId):
  construction_class_list = ["건축공사", "토목공사", "플랜트공사", "조경공사"]
  detail_construction_class_list = ["주거용 건축물", "사무용 건축물", "상업용 건축물", "공업용 건축물", "병원", "학교", "기타"]
  constructionClass = ""
  detailConstructionClass = ""
  manager_id = 0
  res = req.get(f"{BASE_URL}/crew/all/authorized?companyId={companyId}").json()
  print(res)
  for user in res:
    if user["authorized"] and user["role"] == "MEMBER":
      manager_id = user["id"]
      for construction_class in construction_class_list:
        constructionClass = construction_class
        for detail_construction_class in detail_construction_class_list:
          detailConstructionClass = detail_construction_class
          UUID = f"{uuid.uuid1()}".split("-")[0]
          data = {
            "companyId": f"{companyId}",
            "constructionClass": constructionClass,
            "detailConstructionClass": detailConstructionClass,
            "endDate": "2012-10-12",
            "floorPlanId": "-1",
            "managerId": f"{manager_id}",
            "name": f"{UUID}-companyId::{companyId}",
            "startDate": "2022-10-12",
            "thumbnailId": "-1"
          }
          req.post(f"{BASE_URL}/project/new", data=json.dumps(data), headers=header)

for companyId in range(1, 8):
  sign_up(companyId)
# for companyId in range(1, 8):
#   project_producer(companyId)

