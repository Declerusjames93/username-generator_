from ensurepip import version
from http.server import executable
from pydoc import describe
from tabnanny import verbose
from unicodedata import name
from cx_Freeze import setup, Executable

setup(
    name="Username Generator",
    version= "1.0",
    description="Provide any first name and last name; i will suggest you username for social media.", 
    executables = [Executable("C:/Users/Jim/Desktop/code9class-bootcamp/username_generator/username-generator_/pseudo.py")],
)

