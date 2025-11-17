import sys
import os

# 添加父目錄到路徑，以便導入 main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Vercel 需要這個文件來作為 serverless 函數的入口點
# 直接導出 FastAPI app
__all__ = ["app"]

