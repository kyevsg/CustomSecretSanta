def send_assignments(assignments):
  """
  Sends an email to each person in the list of assignments.

  Need to edit mapped_user_info name once variable names are decided in secret_santa.py file.
  Also need to add more details to the email (such as budget, wishlist link, etc if those features get added).
  """
  successful_notification_counter = 0
  for gift_sender, gift_recipient in assignments.items():
    body = "{}, you are {}'s Secret Santa this year. Remember to get them a gift!".format(
        mapped_user_info[gift_sender],
        mapped_user_info[gift_recipient]
    )

    try:
        message = # need to add email function here
        print("Secret Santa assignment sent to {} via email".format(mapped_user_info[gift_sender]))
        successful_notification_counter += 1

    except Exception as e:
        print(e)
        print("There may have been a problem sending the notification to {}".format(mapped_user_info[gift_sender]))
        continue

  print("Notifications were sent to {} people".format(successful_notification_counter))
  return