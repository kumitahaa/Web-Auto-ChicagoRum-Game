                                        ChicagoRum Web Automation Bot
Configuration Instructions:

    - Open the config.yaml file to customize your login credentials.
    - Update the username and password fields with your ChicagoRum account credentials.
    - Ensure that you only modify the credential strings and refrain from making any other changes to maintain the bot's functionality.


Configure the crime_check_box parameter:

    - The crime_check_box parameter accepts an integer value ranging from 1 to 9.
    - By default, it is set to 9, which selects the last checkbox from the crime list.
    - To choose a different checkbox, set the value accordingly:
    - 8 for the second-to-last checkbox,
    - 7 for the third-to-last checkbox,
    and so on.

    - Adjust this value based on the checkboxes that appear as you progress in the game.



Installation
    Follow these steps to install the ChicagoRum Web Automation Bot:

    - Paste the code on your desktop.
    - Open Anaconda. (Already install it)
    - Change the directory to your desktop by using the following command:
                ```
                cd Desktop
                ```
    - Change the directory to your bot folder:
                ```
                cd YourBotFolderName
                ```
    - Run the following command to install the necessary packages:
                    ```
                    pip install -r requirements.txt
                    ```
    - This will ensure that the required dependencies are installed for the ChicagoRum Web Automation Bot to function correctly.


Execution
    Open Anaconda in the desired folder containing the bot code.

    - Run the bot using the following command:
                ```
                python run.py
                ```

    After running the code, press the UP navigation arrow, then press Enter. Repeat this process around 10 times. This precaution helps in case the bot encounters an issue; it will resume automatically without requiring manual intervention.




Credits
        GitHub: [KumiTahaA](https://github.com/KumiTahaA)
