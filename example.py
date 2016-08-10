from instabot import InstaBot

bot = InstaBot(login="xxxxxx", password="xxxxxx",
               like_per_day=1000,
               max_like_for_one_tag=5,
               follow_per_day=150,
               follow_time=5*60*60,
               unfollow_per_day=150,
               comments_per_day=0,
               tag_list=['tunisian', 'tunisia', 'tunisie','tunisianboy','tunisiangirl'],
               log_mod=0)

bot.new_auto_mod()
