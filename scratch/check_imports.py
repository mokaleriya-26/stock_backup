import sys
import os

packages = [
    'django',
    'tensorflow',
    'joblib',
    'yfinance',
    'numpy',
    'pandas',
    'requests',
    'transformers',
    'torch',
    'deep_translator',
    'textblob',
    'sklearn'
]

print("Checking packages...")
for p in packages:
    try:
        __import__(p.replace('-', '_'))
        print(f"✅ {p} is installed")
    except ImportError:
        print(f"❌ {p} is MISSING")
