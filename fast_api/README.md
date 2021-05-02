## Fast API Reference

To start server run following command

```
uvicorn routes.api:app
```

### Sample API calls

```
http POST http://localhost:8000/multilingual_news_detect text="Weird things are happening in your city"
```

### Setup Instructions

```
pip -m venv ~/fakenews_env
source ~/fakenews_env/bin/activate
cd ~/Desktop/dspd/fakenews/fastapi/
pip install -r requirements
```

After installing packages, make sure the pytorch model is present in models/default with name `pytorch_model.bin`