# DomExtract
## Function
DomExtract is a CLI program to accesses your Gmail account and retrieve the username and the domain name of the sender's email for a particular email. 
**This particular app is only meant for Gmail clients. 
This app requires python3 to be installed on the client system and some prerequisite libraries.**

## Installation
The below step-by-step guide to the installation of the program assumes that the client system already has Python 3.x installed and added to path. If your system does not meet these requirements, please follow the steps provided is this video: 
- Windows --> https://www.youtube.com/watch?v=VkdkwxGka3M
- MacOS or OSX --> Preinstalled in the system
- Linux --> Preinstalled in the system
#### External libraries
Open the terminal and run the following command:
- Windows --> ```python -m pip install python-imap```
- MacOS or OSX --> ```python -m pip install python-imap```
- Linux --> ```pip3 install python-imap```
#### Installation Of Script
The script does not require any installation process. Just download the script according to **your particular operating system** and fire it up!

## Configurations
Before using the script for the first time, you will have to configure your Gmail account to be compatible with the script's functioning. 
**This will not affect the regular functioning of your Gmail account.**
Since its recent updates, Gmail does not allow third party apps to access your Gmail account with your Gmail password directly. However, you may allow third party apps to use your Gmail account by setting up an app password. To set up an app password, follow the steps in the below video:
```https://www.youtube.com/watch?v=rqPmaDxigNY```

Once you have setup your app password, save it in a secure location as you would need it to sign in to your Gmail account through the program. 

## Usage
Open up your terminal and navigate to the directory where the script is stored. While in this directory, you can run the script using the command:
- Windows --> ```python <name by which you have saved the sript>.py```
- MacOS/OSX --> ```python <name by which you have saved the sript>.py```
- Linux --> ```python3 <name by which you have saved the sript>.py```

In the prompt to enter your gmail account, enter your **complete gmail address** along with domain name.
In the prompt for password, enter the **app password** that you created in the **Configurations** step.
Select the **Filters** you wish to apply and sit back and relax as the program does the rest!

**You may terminate the functioning of the program at any instant by pressing control+C**

## Filters
The program uses gmail filters in order to pin point the message for which you wish to get the domain name and user ID. Be careful with the filters you use as applying a filter that's too broad would lead to a huge amount of data and hence longer wait times, whereas applying too narrow a filter might make you miss your mark.
Below is an explanation of each of the filters:

#### Labels
Labels correspond to the labels of your gmail account that are assigned to emails. Eg: Inbox, Important or Spam.
Below is an explanation to all:
- All: Searches the entire mail box for the required message.
- Inbox: Searches only the inbox folder for the required message.
- Important: Searches only the important folder for the required message.
- Spam: Searches only the spam folder for the required message.

#### Basis To Filter Message
These define further sub categories which can help you to pinpoint the message you are looking for. Eg: Subject, Date or Sender's email.
Below is an explanation to all:
- Subject: Enter a fragment of the subject of the email you wish to search for. This would return the user ID and domain name of the senders of all mails that have that fragment in their subject.
- Sender's email: If you wish to filter only the mails recieved by a particular email, then enter the complete email address or a fragment of the email adress here. This would return the user ID and domain name of the senders of all mails that have that fragment in their sender's email.
- Date: This is a particularly powerful filter that allows you to search for emails of the basis of the date you recieved them. All dates are enteres in this format: DD-First three letters of the month-YYYY. Eg: ```11-Jan-2023```
The date filter has further three subdivisions:
    * Before: This filter filters all emails recieved before a particular date. Be very careful with this filter as it can return as massive data set and hence take a very long time to process. It is not the most ideal filter unless you are looking for an email that dates back to when you just created your account.
    * Since: This filter filters all emails recieved after a particular date. Be very careful with this filter as it can return as massive data set and hence take a very long time to process. It is not the most ideal filter unless you are looking for an email that has been recieved recently.
    * Before And Since: This filter filters all emails recieved after a particular date and before a particular date. It is the most powerful filter and is a combination of the above two filters.


