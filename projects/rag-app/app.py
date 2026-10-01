import os
import sys

# Ensure projects/rag-app directory is in python module path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import subprocess
    streamlit_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "streamlit_app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_script])
