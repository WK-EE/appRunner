This python GUI application will allow you to run some apps that you use on a daily basis.
Also, it will save your preferences, by generating a text file that contains all your settings.
Therefore, the next time you run this GUI, and click on "Run Apps" in the GUI window, it will run all your chosen apps. 

Before you run this python file, please ensure the following is taken care of:
- Give the variable textfile_path a path of your choice where the text file that holds your application preferences will be created.
- If you are using this on a windows machine, change the argument on line 45 "applications" to "executables", and "*.app" to "*.exe".
  If you are using a machine that is running macOS, then skip this step. 