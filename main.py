from fastapi import FastAPI

app = FastAPI()

BALANCE = {}


@app.get("/balance")
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return {"total balance": sum(BALANCE.values())}
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f'wallet "{wallet_name}" not found'
        )
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}


@app.post("/wallets/{name}")
def receive_money(name: str, amount: int):
    if name not in BALANCE:
        BALANCE[name] = 0
    BALANCE[name] += amount
    return {
        "message": f"Added {amount} to {name}",
        "wallet": name,
        "new balance": BALANCE[name]
    }
