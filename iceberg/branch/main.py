from pynessie import init

client = init(config_dict={
    "endpoint": "http://nessie.datalake.svc.cluster.local:19120/api/v1"
})

# 브랜치 목록
branches = client.list_references()
for ref in branches.references:
    print(f"{ref.name} ({type(ref).__name__}): {ref.hash_}")

# 커밋 히스토리
for entry in client.get_log("main"):
    print(f"{entry.commit_meta.hash_}: {entry.commit_meta.message}")

# main 브랜치 해시 가져오기
main_ref = client.get_reference("main")
main_hash = main_ref.hash_

# 브랜치 생성 (현재 main 기준)
client.create_branch("analysis-20241209", ref="main", hash_on_ref=main_hash)

# 특정 커밋에서 브랜치 생성
# client.create_branch("analysis-20241209", ref="main", hash_on_ref="<commit_hash>")

# 태그 생성
client.create_tag("daily-20241209", ref="main", hash_on_ref=main_hash)