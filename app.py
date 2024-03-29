from twitter import Twitter
import time


tw = Twitter()
#tojssds
def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                # I take sender_id just in case you want to know who's sent the message
                # ID of the user
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) is not 0 and len(message) < 280:
                    # !conk is the keyword
                    # if you want to turn off the case sensitive like: !conk, !coNk, !CoNk
                    # just use lower(message) and check it, but please remove the replace function line
                    if "!conk" in message:
                        message = message.replace("!conk", "!conk")
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                              
                                tw.api.send_direct_message(sender_id,"Pesan kamu sudah terkirim :)")
                                tw.delete_dm(id)
                                
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                            
                                tw.api.send_direct_message(sender_id,"Pesan kamu sudah terkirim :)")
                                tw.delete_dm(id)
                          
                        else:
                            print("DM deleted because its empty..")
                            tw.delete_dm(id)
                           
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        
                        # tw.api.send_direct_message(sender_id,"Pesan kamu tidak mengandung keyword/trigger :(")
                        tw.delete_dm(id)
                   
                        

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0 or dms is None:
                time.sleep(60)

if __name__ == "__main__":
    start()