import os
import sys
import subprocess
import importlib.util
import platform

def check_module(module_name):
    """Check if a Python module is installed"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            return False
        return True
    except ModuleNotFoundError:
        return False

def check_command(command):
    """Check if a command is available in the system"""
    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        return True
    except FileNotFoundError:
        return False

def is_venv():
    """Check if running in a virtual environment"""
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def main():
    """Main function to check environment"""
    print("=" * 50)
    print("Medical Data Extraction - Environment Check")
    print("=" * 50)
    print()

    # System information
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Running in Virtual Environment: {'Yes' if is_venv() else 'No'}")
    print()

    # Check required Python packages
    required_packages = [
        "PyPDF2", "pytesseract", "opencv-python", "numpy", "pillow",
        "pytest", "fastapi", "uvicorn", "python-multipart", "streamlit"
    ]
    
    print("Checking Python packages:")
    all_packages_installed = True
    for package in required_packages:
        installed = check_module(package.replace("-", "_"))
        status = "✓" if installed else "✗"
        print(f"  {package}: {status}")
        if not installed:
            all_packages_installed = False
    
    if not all_packages_installed:
        print("\nSome packages are missing. Please install them using:")
        print("  pip install -r requirements.txt")
    else:
        print("\nAll required Python packages are installed.")
    
    print()

    # Check external dependencies
    print("Checking external dependencies:")
    
    # Check Tesseract
    tesseract_path = os.environ.get("TESSERACT_PATH", "")
    if tesseract_path:
        tesseract_exists = os.path.exists(tesseract_path)
        print(f"  Tesseract: {'✓' if tesseract_exists else '✗'}")
        print(f"    Path: {tesseract_path} {'(exists)' if tesseract_exists else '(not found)'}")
    else:
        print("  Tesseract: ✗ (TESSERACT_PATH environment variable not set)")
        
        # Try to find tesseract in common locations
        if platform.system() == "Windows":
            common_paths = [
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
            ]
        else:
            common_paths = ["/usr/bin/tesseract", "/usr/local/bin/tesseract"]
        
        for path in common_paths:
            if os.path.exists(path):
                print(f"    Tesseract found at: {path}")
                print(f"    Set TESSERACT_PATH environment variable to this path.")
                break
    
    print()
    
    # Check if backend and frontend directories exist
    print("Checking project structure:")
    backend_exists = os.path.exists("backend")
    frontend_exists = os.path.exists("frontend")
    print(f"  Backend directory: {'✓' if backend_exists else '✗'}")
    print(f"  Frontend directory: {'✓' if frontend_exists else '✗'}")
    
    print()
    print("=" * 50)
    print("Environment check completed.")
    print()
    
    # Provide recommendations
    if not is_venv():
        print("RECOMMENDATION: Run this project in a virtual environment.")
        print("  Create: python -m venv venv")
        print("  Activate (Windows): venv\\Scripts\\activate")
        print("  Activate (macOS/Linux): source venv/bin/activate")
        print()
    
    if not all_packages_installed or not tesseract_exists:
        print("RECOMMENDATION: Follow the setup instructions in SETUP.md")
        print()

if __name__ == "__main__":
    main()
