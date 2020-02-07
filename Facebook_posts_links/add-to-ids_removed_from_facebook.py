#!/usr/bin/ipython3
import pickle
with open("/home/amir/github/working/Facebook_posts_links/ids_removed_from_facebook.pkl", "rb") as file:
    ids_removed_from_facebook = pickle.load(file)
while True:
	print("Enter q for exit at any stage")
	fb_identifier = input("Enter facebook identifier. eg: muhammad.imra.100: ")
	fb_name       = input("Enter facebook name                             : ")
	if (fb_identifier == "q") or (fb_name == "q"):
		break
	else:
		ids_removed_from_facebook[fb_identifier] = fb_name

with open("/home/amir/github/working/Facebook_posts_links/ids_removed_from_facebook.pkl", "wb") as file:
    pickle.dump(ids_removed_from_facebook, file)