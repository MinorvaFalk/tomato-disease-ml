# ๐ Tomato Disease Detection

## ๐ Overview
This repository containing notebook and endpoint for tomato disease detection using Android App.

This model is trained with `700 random image` from Cifar 100 Resized for unknown class.

For model accuracy you can check each model version inside `notebooks/models`

Model Used: `EfficientNetB0`

### Dataset :
- [Tomato Disease](https://www.kaggle.com/datasets/charuchaudhry/plantvillage-tomato-leaf-dataset)
- [Plant Disease](https://www.kaggle.com/datasets/emmarex/plantdisease)
- [Cifar100 Resized 256](https://www.kaggle.com/datasets/ibraheemmoosa/cifar100-256x256)

## ๐ Requirements

```
Docker
Make (*optional)
Notebook
Python / Anaconda
```

## ๐ Project Structure
```bash
โโโโapi
โโโโnotebooks
โโโโtf-model
```

## ๐ Getting Started

### `๐ Requirements`
**Require Python or Anaconda**
```cmd
pip install -r requirements.txt
```

### `๐ TF Serving`
1. Make sure to create `tf-model` directory first (you can choose the models inside `notebooks/models`)\
2. Then copy the model inside `tf-model`\
   **Model naming format is number*
3. **optional* Reconfigure `models.config`
4. Run command this
**โ ๏ธRequire Make and Docker Installedโ ๏ธ**
    ```bash
    make deploy-tf-serving
    ```
5. Access the endpoints
    ```
    # Endpoint format is 
    # http://localhost:8051/v1/models/${MODEL_NAME}[/versions/${VERSION}|/labels/${LABEL}]:predict

    # For example:
    # http://localhost:8051/v1/models/tomato_disease/versions/2:predict
    # **version is your model directory name**
    ```

### `๐ Endpoint`
You can run manually using `cmd` or `Docker`\
- **CMD** 
  ```bash
  cd api
  hypercorn main:app --bind localhost:8080
  # or you can use uvicorn
  # uvicorn main:app --port 8080
  ```

- **๐งDocker๐ง**
  ```bash
  # Coming Soon
  ```

### `๐ Hosting for Mobile App`
Check the mobile app [here](https://github.com/MinorvaFalk/tomato_disease_android)\
To expose the API to the Internet you can use `Ngrok` or `Localtunnel`

- `Ngrok`\
  For installation you might need to check [here](https://ngrok.com/download)
  ```cmd 
  ngrok http 8080
  ```
- `Localtunnel`\
  For installation you might need to check [here](https://localtunnel.github.io/www/)
  ```cmd
  lt --port 8080
  ```
