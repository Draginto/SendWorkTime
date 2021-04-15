# SendWorkTime
A lightweight Timecamp plugin designed to email your hours worked to your boss through a simple python script.

The plugin utilizes an smtp server through gmail, so if you want to continue using this plugin you should create a dummy gmail account specifically used for sending emails. 

Upon initializing this plugin, you'll need your api key, gmail account, password to that gmail account and to SET your pay period (Either weekly, bi-weekly, or monthly).

## Get Your API Key from Timecamp
Visit this link to get your API key: https://app.timecamp.com/app#/settings/users/me

## Setup your Dummy Gmail Account for SMTP
Visit this link and sign into your dummy gmail account: https://myaccount.google.com/lesssecureapps make sure that when you created this account you did not enable 2-step verification. If it's not enabled, when you visit the aforementioned link, you should see a toggle. Click it to enable less secure apps access.

## Add your API key and SET Pay Period
When you receieved your api key, if for private use, replace the "os.environ.get()" to the api string. If for public use, please set an the api key to an environment variable and keep the os.environ.get() statement, replacing the string to your variable name.
