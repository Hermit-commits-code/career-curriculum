import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "SLOP-SCANNER ONLINE", "version": "0.1.0"}


@app.get("/audit/{package_name}")
async def audit_packages(package_name: str):
    url = f"https://registry.npmjs.org/{package_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Package not found in the Net")
    data = response.json()
    name = data.get("name")
    latest_version = data.get("dist-tags", {}).get("latest")

    # Async bridge
    vulnerabilities = await check_vulnerabilities(name, latest_version)
    return {
        "name": data.get("name"),
        "latest_version": latest_version,
        "description": data.get("description"),
        "license": data.get("license"),
        "vulnerabilities": vulnerabilities,
    }


async def check_vulnerabilities(package_name: str, version: str):
    osv_url = "https://api.osv.dev/v1/query"
    payload = {
        "version": version,
        "package": {"name": package_name, "ecosystem": "npm"},
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(osv_url, json=payload)

    return response.json().get("vulns", [])
