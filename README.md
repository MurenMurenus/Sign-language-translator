# Sign language translator model
This model is designed to translate sign language into letters according to the American system.
In addition, a telegram bot has been written to recognize, oddly enough, sign language.
The bot is ready to use, the weights of the model in the file: bot/saved.pt

# Bot functionality:
* Recognition of letters in the photo
* Recognition of a text on video
* Recognition of a text in circles


# Model training
Training datasets are not stored in the repository, so read data/README.md and create a dataset.
The training can be started with the command:
```bash
python3 train.py
```
If you want to put the completed model in its place saved.pt , then in evaluate.py there is a commented-out line for 
saving the model in .pt format, then the new weights are moved to bot/ and that's it!

# Initializing telegram bot

If you want to use telegram bot with the model you've trained, do the following:
* Create a bot using BotFather
* Go to bot/main.py
* Change YOUR_NGROK_TOKEN and YOUR_TELEGRAM_BOT_TOKEN to the corresponding tokens
* Run bot/main.py
* Enjoy!
