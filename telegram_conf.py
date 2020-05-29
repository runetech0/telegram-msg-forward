
# To get API_ID value follow these steps
# Go to https://my.telegram.org/auth
# Login with your normal telegram user account number.
# Go to API development tools
# A Create new application window will appear. Fill in your application details.
# There is no need to enter any URL. Just enter the App title and short name of your choice.
# Click on Create application at the end.
# Copy the API_ID and API_HASH values and paste here.
API_ID = 12425
# NOTE: The API_HASH must be in single quotes. Below is a sample.
API_HASH = 'd15e36f9526a8384b2d0c547d'



# OWN_CHANNEL_ID is the unique id of your channel/group where you want to receive the updates.
# To get this id run the get_id.py file using 'python get_id.py'.
#  After login, if you have'nt already. It would instruct to you to got to the channel you want the id for and send any message there.
# After you send the message check your terminal. Find your message and copy the channel id to OWN_CHANNEL_ID.
# Be careful with the minus(-) sign. If it is in the id then place it as well.
OWN_CHANNEL_ID = -1043423531

# Get the ids for all the channel you want to receive updates from and paste them here.
CHANNELS_TO_GET_UPDATES_FROM = [-1032347421, -10234410845, 9344540]



# Use socks5 proxy if telegram web is not working in your region.
PROXY = True
SOCKS5_SERVER = '81.19.223.180'
SOCKS5_PORT = 1080

# You are done!
# Run the telegram_forwarder script using python telegram_forwarder.py using 'python telegram_forwarder.py'.
