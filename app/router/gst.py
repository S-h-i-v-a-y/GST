# app/routers/gst.py

from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

def fetch_gst_details(gstin: str):
    url = f"https://apisetu.gov.in/gstn/v2/taxpayers/{gstin}"
    headers = {
        "X-APISETU-APIKEY": "464878dad551152c087d3787b803495db3078773119da052ab9bd6c49069c4cb",
        "X-APISETU-CLIENTID": "com.denadatecnologia",
        "Accept": "application/json"
    }
    cookies = {
        "Path": "/"
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch GST details: {e}")

@router.get("/gst/{gstin}")
def get_gst_details(gstin: str):
    return fetch_gst_details(gstin)
