Answer Sheet

Q1) Requirements for Distributed Marketing: (choose 3)

@ Salesforce Pardot with Engage License

@ @ Salesforce Connect with the ability to connect to one external data source

@ @ Salesforce Sales Cloud, Service Cloud, Financial Services Cloud (FSC), or Community Cloud (Partner Community License or Login, only)
@ @ Salesforce Marketing Cloud with Journey Builder

@ Available Marketing Cloud licenses for every Sales user of Distributed Marketing

Q2) A Marketing Cloud license is required for every Distributed Marketing user.

@ @ Incorrect

@ Correct

Q3) Distributed Marketing can be used with Enterprise 1.0 and 2.0 editions of Marketing Cloud.

@ @ incorrect
@ Correct

Q4) To use Distributed Marketing, each business unit requires a unique Marketing Cloud user (a system user), where the business unit
you want to connect is the default business unit of the system user.

@ Incorrect

@ @ Correct

Q5) Distributed Marketing requires Lightning.

@ Incorrect

@ @ Correct

Q6) Distributed Marketing supports sending from both - journeys and individual channels, like selecting and sending a single Content
Builder email.

@ @ incorrect

Explanation:-All messages in Distributed Marketing are sent using Marketing Cloud�s Journey Builder. Link - https://help.salesforce.com/article View?
id=mc_dm_create_marketing_cloud_journey.htm&type=5
@ Correct

Q7) It is recommended that you install the Distributed Marketing Package for admins only or for specific profiles so that you are
installing for licensed users only.

@ @ Correct

Explanation:-Access to Distributed Marketing is controlled through custom permissions and permission set licenses. You can assign the custom
permissions in your Salesforce org using installed permission sets or using your own custom permission sets or profiles. The permission set licenses are
provisioned in your account and can be assigned using installed permission sets. refer - https://trailhead.salesforce.com/content/learn/modules/distributed-
marketing-administration/install-configure-distributed-marketing

@ Incorrect

Q8) The DMAdministrator Permission Set contains everything included in DMStandard plus Visualforce pages for Distributed Marketing
administration.

@ Incorrect

@ @ Correct

Q9) Distributed Marketing Approvers need a license.

@ @ Incorrect
@ Correct

Q10) If you don't log out of active Marketing Cloud sessions when configuring Distributed Marketing, Salesforce automatically
authenticates against an active session.

@ Incorrect

@ @ Correct
Answer Sheet

Q1) After a Business User sends a message using Distributed Marketing, Distributed Marketing adds the contact or lead to the
appropriate data extension along with data from the contact or lead, such as unique identifier (ContactID or LeadID), email address, and
the user ID of the user who pressed Send.

@ Incorrect

@ @ Correct

Q2) Campaign Marketplace in Distributed Marketing allows you to create and share collections�or marketplaces�of campaigns based
on common categories, themes, and intentions.

@ Incorrect

@ @ Correct

Q3) Whitelist the following domains, if you have policies to whitelist only MC domains: (choose 3)

@ @ *.marketingcloudapps.com
@ Code.marketingcloud.com

@ @ Bounce.exacttarget.com
@ @ Exacttarget.com

@ Help.marketingcloud.com

Q4) IP Addresses for the following use cases are not instance-specific and should be whitelisted for any tenant: (choose 5)

@ @ SOAP API Calls

@ @ Device Integrations

@ @ REST API Calls

@ Authenticated Sending

@ @ Authentication API Calls
@ @ FTP Integrations

Q5) All Marketing Cloud accounts use a pool of IP Addresses that vary depending upon send volume by default. All administrators
should therefore whitelist the ranges of IPs for the stack their instance resides in.

@ @ Correct

Explanation:-Assign a unique IP address to your account and manage your own sending reputation in Marketing Cloud Email Studio. When your send
volume is high enough that your sending reputation is hard to control in a shared IP pool, investigate using a dedicated IP address. Link -
https://help.salesforce.com/articleView?id=mc_es_dedicated_ip.htm&type=5.

@ Incorrect

Q6) Developers creating Android apps for use with MobilePush must whitelist regional IP addresses in their Google API Key
Configuration IP Whitelist.

@ Incorrect

@ @ Correct

Q7) Domain Verification protects your brand reputation by making sure From addresses used in send emails are approved and
provides assurance that you send messages from confirmed addresses.

@ Incorrect

@ @ Correct

Q8) You can import and verify (Bulk Upload) multiple From address in From Address Management in individual accounts.

@ Incorrect

@ @ Correct

Q9) Places to verify From addresses in MC: (choose 4)

@ @ From Address Management
@ Delivery Profiles
@ @ Sender Profiles

@ @ My Users
@ @ Account Settings
@ Company Information

Q10) You can choose to honor an Opt-Out List in all types of Marketing Cloud Transactional email sends.

@ @ incorrect
@ Correct