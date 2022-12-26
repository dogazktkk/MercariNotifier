from db_functions import *
from config import *
from methods import *


#CreateorConnectDB(dbname, "Create Table If not exists Iphones (ID INTEGER NOT NULL, IphoneModel TEXT, url TEXT, PRIMARY KEY (ID))")
#CreateorConnectDB(dbname, "Create Table If not exists Macbooks (ID INTEGER NOT NULL, MacbookModel TEXT, url TEXT, PRIMARY KEY (ID))")
#CreateorConnectDB(dbname, "Create Table If not exists Ipads (ID INTEGER NOT NULL, IPadModel TEXT, url TEXT, PRIMARY KEY (ID))")
#CreateorConnectDB(dbname, "Create Table If not exists IphoneOffers (ID INTEGER NOT NULL, url TEXT, Info TEXT, Notified INT, PRIMARY KEY (ID))")
#CreateorConnectDB(dbname, "Create Table If not exists IpadOffers (ID INTEGER NOT NULL, url TEXT, Info TEXT, Notified INT, PRIMARY KEY (ID))")
#CreateorConnectDB(dbname, "Create Table If not exists MacbookOffers (ID INTEGER NOT NULL, url TEXT, Info TEXT, Notified INT, PRIMARY KEY (ID))")

Iphones_list = AssignDBContenttoList(dbname, "Iphones", "url")
Ipads_list = AssignDBContenttoList(dbname, "Ipads", "url")
Macbooks_list = AssignDBContenttoList(dbname, "Macbooks", "url")

ScrapeItemsMercari(Iphones_list, "IphoneOffers")
message1 = NotificationMessageBuilder("IphoneOffers")
TelegramNotification(message1, tgtoken, group_chat_ID)
QueryToDB(dbname,'UPDATE IphoneOffers set Notified=1')

ScrapeItemsMercari(Ipads_list, "IpadOffers")
message2 = NotificationMessageBuilder("IpadOffers")
TelegramNotification(message2, tgtoken, group_chat_ID)
QueryToDB(dbname,'UPDATE IpadOffers set Notified=1')

ScrapeItemsMercari(Macbooks_list, "MacbookOffers")
message3 = NotificationMessageBuilder("IpadOffers")
TelegramNotification(message3, tgtoken, group_chat_ID)
QueryToDB(dbname,'UPDATE IpadOffers set Notified=1')

