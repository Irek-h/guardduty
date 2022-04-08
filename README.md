# guardduty

# Member account  

How to Use:

1. Open CloudShell
2. git clone https://github.com/Irek-h/guardduty.git
3. cd guardduty
4. python3 enable_gd.py
5. python3 accept_invite.py

It will enable guardduty in all regions on your AWS account and accept an inivite  
Docs:  
https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html#master_member_relationships  
https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html

<!-- 
1. Open CloudShell
2. git clone https://github.com/Irek-h/guardduty.git
3. cd guardduty
4. chmod +x gd_setup.sh
5. ./gd_setup.sh
 -->

# Master account

How to send invites:

1. Open CloudShell
2. git clone https://github.com/Irek-h/guardduty.git
3. cd guardduty
4. edit "ACCID", "EMAIL" in file **send_invite.py** and save  
![obraz](https://user-images.githubusercontent.com/82705344/162448697-c2773c89-f4eb-4372-b666-7f281bd32672.png)  
![obraz](https://user-images.githubusercontent.com/82705344/162448741-daddea50-36d7-46db-a9b3-817c7d76adec.png)  
Where ACCID is AWS account Id number, EMAIL is email address the account has been created with  
5. python3 send_invite.py









