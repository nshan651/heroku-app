#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

def sparkbadge_base64():
    return '<!DOCTYPE html><html lang="en"><head><title> sparkbadge</title><meta charset="UTF-8" /><meta name="viewport" content="width=device-width,initial-scale=1" /><meta name="description" content="" /></head><body><div><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPwAAAA6CAYAAACUGjTOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAC0ElEQVR4nO3cr24UYRSG8eds+FOJqADEpqhWl5tAV9dxGQRFeg0oHLU4BBeALJYQREkNiE1AkLBA0g+xC7h2N5yvO8N5fskmKzZvZyf7diZnvplorSGphsmmN0DS1bHwUiEWXirEwkuFWHipEAsvFWLhpUIsvFSIhZcKubbpDdBmRMQU2E6OnbXWzpIzlcjCFxQRU4J3NLZyg5lHxK6lHy4LX9M2jS0OyDvGz4AXbC0TLfxAWfjKtoG7m94IXSULr2x7EZGd6WwgiYVXjq9AAI3j9GxnA2ksvHLMgQapcwFwNpDMwiuXc4FBs/Aai+zZQMm5gIXXsPWaDRSdC5QuvKvNRqDHbKDwXKBs4butNoPvEXEAfErM9J+Is4EUZQtPj9VmZ8ArbtJ4mZS4UPT0U/kqF34h88gxw9NPDZqF78HTTw2U98NLhXiEl5KM4aqPhZcSjOUZAxZeyjGKZwxYeCnTwAe2Du2kQiy8VIiFlwqx8FIhKw/tImJ/jdzbwK21t+Zi14GfiXk7ALxnMQ3N8HuOmpn5+c+7BxGxl5S6Awz/u/fKHcs+/budKz0LoLX25rLPRGttpb8dEat9UNJGtNYu/a+wzmW5+yt+bg84fgLcWyP8Iq+Bp0Bm5inwePH2EfAhKRb6nIkcPQTuJAV+BJ4t3g79u/fK3QGORvJ7+kLmrdattdQXsA+0E2gt6fV8cQ9aaubJMhPYz94HyftzOoFv/N3elNcyc7rp77ehfZr+Gx3L78mFNwPXWjuLiF2S12if+1CNkiz8CCyLaTn1z7wsJxXS7Qj/NjHrtENmZpY0Fj0KP5vA/JDc2wQnwGFm4CJzfp571VgatPTCdxwy3QB+JGc6uFIpXU7pHTJJw+SUXmVVnAlZeFXUa840+JnQymvppf/JGB442YOFlwpx4Y1UiIWXCrHwUiEWXirEwkuFWHipEAsvFWLhpUIsvFTIL223PR3hiK3OAAAAAElFTkSuQmCC"/></div></body></html>'
