# Mem-Base 🧠🗒️
Python script for a to-do list app that utilizes SHA3-512 and local storage via file handling

![Alt text](images/200612.jpg) 
                  
Requirements
* Ensure the latest version of python is installed in your terminal (python 3.x)

Installation
* To download simply type "git clone https://github.com/RavenTheBird789/Mem-Base" in your command line within your terminal               
         
Execution
* To run, simply type "python3 mem_base.py" in your command line within your terminal or a shortcut can be created in a terminal session using the bash alias command to run the program faster. (Ex: alias run="python3 mem_base.py")

Global Execution (Optional)
* Alternatively, you can run the program globally by simply typing "membase" from anywhere in your terminal, follow these steps (For macOS and Linux):
  1. Make the file executable by typing "chmod +x mem_base.py" in your terminal
  2. Copy the file to a new name using "cp mem_base.py membase" then make that executable too with "chmod +x membase"
  3. Create a local bin folder if you don't already have one using "mkdir -p ~/.local/bin"
  4. Move the file into it using "mv membase ~/.local/bin/"
  5. Make sure that folder is in your PATH by adding "export PATH="HOME/.local/bin:PATH"" to your ~/.bashrc (or ~/.zshrc if you use zsh)
  6. Reload your terminal config using "source ~/.bashrc" (or ~/.zshrc)
  7. Type "membase" from anywhere to run the program

* For Windows
  1. Make sure Python is added to your PATH (check by typing "python --version" in Command Prompt. If it shows a version number, you're set)
  2. Create a folder to hold your global scripts, such as "C:\Scripts" (You can make this anywhere, just don't forget the path)
  3. Copy "mem_base.py" into that folder and rename the copy "membase.py"
  4. In the same folder, create a new text file named "membase.bat"
  5. Open "membase.bat" in Notepad and add this single line "@python "%~dp0membase.py" %*"
  6. Save and close the file
  7. Add your folder to your PATH: press the Windows key, search "Environment Variables", click "Edit the system environment variables", click "Environment Variables", under "User variables" select "Path", click "Edit", click "New", then paste in your folder path (e.g. "C:\Scripts")
  8. Click OK on all the windows to save
  9. Close and reopen Command Prompt or Powershell
  10. Type "membase" from anywhere to run the program

Key Terminology:
* Memories - Reminders for yourself that you write to the "memories.txt" file
* Forgetting - The process of deleting a chosen reminder (memory) from the memories.txt file
* Altering - The process of changing an already existing reminder into something else based on its index

Notes For Usage:
* Whenever adding new memories, it is suggested to write them in proactive second person to increase personalization and accountability for yourself
* Run the "membase" command only while inside the Mem-Base installation directory. This ensures the application can access your saved username and memories

Updates (For Version 1.2.0)
* Exit animation speed increased
* Redirection to the main menu animation speed increased
* Additional option created to conveniently allow users to update their username (Option 6)
