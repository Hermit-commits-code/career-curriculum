import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/audit/{package_name}")
async def audit_packages(package_name: str):
    url = f"https://registry.npmjs.org/{package_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Package not found in the Net")
    data = response.json()
    # I only want high-level metadata for now.
    return {
        "name": data.get("name"),
        "latest_version": data.get("dist-tags", {}).get("latest"),
        "description": data.get("description"),
        "license": data.get("license"),
    }


@app.get("/")
def read_root():
    return {"status": "SLOP-SCANNER ONLINE", "version": "0.1.0"}
