from setuptools import setup, find_packages

setup(
    name="deep_learning_recommender",
    version="1.0.0",
    author="James Schmidt",
    description="Neural Collaborative Filtering recommender system using PyTorch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jimster397/deep-learning-recommender",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "torch>=2.0.0",
        "scipy>=1.11.0",
        "mlflow>=2.7.0",
        "fastapi>=0.100.0",
        "streamlit>=1.28.0",
        "requests>=2.31.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)