from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json
import asyncio

app = FastAPI()


# response 생성 함수
def make_mba_response(
        status: str,
        total_count: int,
        name: str,
        phone: str,
        customer_idx: int,
        country_code: str = "82",
        product_name: str = None,
        nft_count: int = None,
):
    return {
        "status": status,
        "totalCount": total_count,
        "targetMessageInfo": {
            "name": name,
            "phone": phone,
            "customerIdx": customer_idx,
            "countryCode": country_code,
            "productName": product_name,
            "nftCount": nft_count,
        }
    }


# NDJSON generator
async def ndjson_generator():
    total = 201
    for i in range(total):
        response = make_mba_response(
            status="PROCESSING",
            total_count=total,
            name=f"User{i}",
            phone=f"010000000{i}",
            customer_idx=i,
            product_name="Sample Product",
            nft_count=i + 1,
        )
        yield json.dumps(response) + "\n"

    # 마지막 완료 메시지
    done_response = make_mba_response(
        status="DONE",
        total_count=total,
        name="Final",
        phone="01099999999",
        customer_idx=999,
    )
    yield json.dumps(done_response) + "\n"


@app.get("/mba/stream")
async def stream():
    return StreamingResponse(ndjson_generator(), media_type="application/x-ndjson")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ndjson_fastapi:app", host="127.0.0.1", port=8000, reload=True)
