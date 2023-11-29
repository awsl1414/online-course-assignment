from uvicorn import run


from api import app


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
    # run("main:app", host="127.0.0.1", port=5000, reload=True)
