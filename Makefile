tf-serving:
	docker run -t --rm -p 8501:8501 -v C:/Users/Minorva/notebooks/tomato-disease-detection:/tomato-disease tensorflow/serving \
	--rest_api_port=8501 \
	--model_config_file=/tomato-disease/models.config
