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
Answer Sheet

Q1) The default sender profile and delivery profile name and external key cannot be updated or deleted.

@ Incorrect

@ @ Correct

Q2) You must choose Account Default for the footer, or Marketing Cloud cannot include the required elements, such as unsubscribe
link and physical mailing address, in the email.

@ @ incorrect
@ Correct

Q3) Recommended setting for Send Password Change Confirmation Email?

@ Disable
@ @ Enable

Q4) Recommended setting for Enforce Export Email Whitelist?

@ Disable
@ @ Enable

Q5) Recommended setting for Enable Audit Logging Data Collection?

@ Disable

@ @ Enable

Q6) An explicitly denied permission always overrides all other permissions.

@ Incorrect

@ @ Correct

Q7) When a permission is not explicitly granted or denied, Marketing Cloud defaults to grant permission unless another role denies that
permission.

@ @ incorrect

@ Correct

Q8)
Single Sign-On best practice is to test your SAML enablement on one business unit before enabling others on your account.

You can better resolve any configuration issues or errors when dealing with a business unit.

@ @ incorrect

@ Correct

Q9) Business units are available in Enterprise 2.0 and 1.0 tenants.

@ @ incorrect

@ Correct

Q10) Available unsubscribe settings for Business Units are unsubscribe a person from only the business unit or from all business units
within the enterprise account.

@ @ Correct

Explanation:-https://help.salesforce.com/articleView?id=mc_es_unsubscribe_settings.htm&type=5
@ Incorrect
Answer Sheet

Q1) You can customize the time zone and date format for individual business units.

@ Incorrect

@ @ Correct

Q2) Messages Marketing Cloud Supports from within the platform are: (choose five)

@ @ In-app inboxes

@ @ Push

@@sms

@ Twitter

@ @ Email

@ @ Line Group Messages

Q3) Preview and Test provides the ability to: (choose 3)

@ @ Validate AMPscript or other programmatic languages

@ @ See how personalization displays for subscribers.

@ Send a sample email to a subset of your audience to test performance.
@ Test different content versions with your audience.

@ @ View how the email appears in your own email client.

Q4)A lives in the individual studios.
@ @ Subscriber
@ Contact

Q5) A contact appears in the section.

@ All Subscribers

@ @ Al Contacts

Q6)A is a person you send messages to through any marketing channel.

@ Subscriber
@ @ Contact

Q7) Which statement is Correct?

@ Allsubscribers are contacts, and all contacts are subscribers.
@ @ Al subscribers are contacts, but not all contacts are subscribers.

Q8) You can have contacts whom you've never sent to who don't appear in All Contacts.

@ Incorrect

@ @ Correct

Q9) Data in Email Studio shows up in Contact Builder, but data in Contact Builder does not show up in Email Studio.

@ Incorrect

@ @ Correct

Q10) A subscriber in Email Studio will appear in Contact Builder under the All Contacts section, and a contact in Contact Builder will
automatically appear in Email Studio.

@ @ Incorrect
@ Correct
Answer Sheet

Q1) identifies a contact within an account and ties together the contact, channels, and the relationship.

@ Subscriber Key
@ Contact ID
@ @ Contact Key

Q2) The is the same no matter what channel is used to send messages.

@ Subscriber Key
@ Contact ID
@ @ Contact Key

Q3) The is what allows you to connect contacts in multiple channels.

@ Subscriber Key
@ Contact ID

@ @ Contact Key

Q4) In Mobile Studio, contacts are identified on , which becomes the Contact Key in Contact Builder.

@ Contact Key
Explanation:-https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-
relationships

@ Contact ID

@ @ Subscriber Key

Q5) allows you to maintain multiple sets of subscriber attributes for a single email address.
@ @ Subscriber Key

@ Contact ID
@ Contact Key

Q6) Link attribute groups and populations using the value.
@ Subscriber Key

@ Contact ID
@ @ Contact Key

Q7) allows you to include a single email address multiple times on a list.
@ @ Subscriber Key

@ Contact ID
@ Contact Key

Q8) must be present in every sendable data extension.
@ @ Subscriber Key

@ Contact ID
@ Contact Key

Q9) It's best to save populations for specific use cases where you need to create complex queries, such as if your account uses field-
level encryption or when you're using API Entry Sources in Journey Builder.

@ Incorrect

@ @ Correct

Q10) You configure the retention policy settings when creating the data extension.

@ Incorrect

@ @ Correct
Answer Sheet

Q1) Data that passes the retention limits will be permanently deleted.

@ Incorrect

@ @ Correct

Q2) Which is NOT a Data Retention delete option:

@ All Records and Data Extensions
@ All Records

@ Individual Records

@ @ Data Extensions

Q3) Member Identification Code (MID) is a ID:

@ @ Numeric

@ Alphanumeric
@ Text

@Q4) How can you find your Member Identification Code within your Marketing Cloud account? (choose 2)

@ Under your username, navigate to Setup. The MID is displayed on the Setup Home screen in Metrics.

@ @ Hover over your account name in the top corner of the Marketing Cloud interface, immediately to the left of your username.
Explanation:-Link - https://trailhead.salesforce.com/en/content/learn/modules/marketing-cloud-developer-basics/learn-administration-basics
@ Under your username, navigate to Setup. Use Quick Find to navigate to Company Settings. The MID is the Account ID.

@ @ Under your username, navigate to Setup. Use Quick Find to navigate to Account Settings. The MID is the Account ID.
Explanation:-Link - https://trallhead.salesforce.com/en/content/learn/modules/marketing-cloud-developer-basics/learn-administration-basics

Q5) Which of the following are true about All Contacts in Contact Builder? (choose 3)

@ @ All Contacts functions at the Enterprise/Parent level.

lv} fs) All Contacts functions across all Channels in Marketing Cloud.

@ All Contacts are Subscribers.

@ @ All Contacts contains All Subscribers plus anything marked as a Population.
@ All Contacts automatically links records across Studios/Channels.

Q6) Which statements are correct about Marketing Cloud and Marketing Cloud Connect when using Non-Scope by User configuration?
(choose 3)

@ Users are always prevented from sending to report or campaign members who are not visible to them without notice.
@ @ Password policies are not in effect, making this configuration easy to maintain because passwords do not expire.
Qo e An administrator can set up a user without entering a password.

@ @ Within the Marketing Cloud, returned subscribers are not limited to what is visible to the user initiating the send.

Q7) Before you can enable marketers to include the Distributed Marketing content blocks in emails, you need to do two things.

@ Create a new Business Unit to house Distributed Marketing.

@ @ Add the custom content blocks that you want to use as components.

@ @ Aad the Distributed Marketing installed package to your Marketing Cloud account.
@ Limit roles in Sales Cloud to only provide access to the Marketing functionality.

Q8) Northern Trail Outfitters purchased a Sender Authentication Package (SAP) and is provisioned within the account. The Marketing
Cloud admin wants to ensure the private domain being used as the From Address for email sends has been verified. How could the
admin meet this requirement?

@ Register each From Address with this domain individually by sending a verification email to each email address.

@ Register the private domain using Domain Registration.

@ @ The administrator does not need to verify the private domain.

@ Register each From Address with this domain by importing a data extension and sending a verification email to each email address.

Q9) Distributed Marketing channels supported: (choose two)

@@sms

@ @ Email
@ Social
@ Push

Q10) Which send process can use Sender Profiles? Choose 3 Answers.

@ @E User-initiated Sends
@ @ Triggered Sends

@ Simple Automated Sends
@ @ Guided Sends
Answer Sheet

Q1) What Salesforce Editions work with Marketing Cloud Connect? (choose 4)

@ Basic

@ @ Developer
@ @ Uniimitea
@ @ Enterprise
@ @ Performance
@ Professional

Q2) How do you find information on your MC instance?

@ Click on "Status" at any time in the top navigation menu of the Marketing Cloud interface.

@ Under your username, navigate to Setup. Use Quick Find to navigate to Account Settings. The Instance information is displayed in Account Settings.
@ Hover over your account name in the top corner of the Marketing Cloud interface, immediately to the left of your username. Click the hyperlinked
Instance # to view detailed information.

@ @ Ontrust.salesforce.com, click "Status" and enter your MID to display information.

Q3) Which IPs should be whitelisted when first configuring MC?

@ @ Whitelist the entire set of IP ranges for your region.

@ None - all users should use the standard verification process as a best practice.

@ Whitelist the IP ranges of your frequent Marketing Cloud users and administrators and Marketing Cloud Support.
@ Whitelist the IP addresses of the administrative users.

Q4) Which of the following are correct about All Contacts in Contact Builder? (choose 3)

@ @ All Contacts contains All Subscribers plus anything marked as a Population.
@ All Contacts automatically links records across Studios/Channels.

@ @ All Contacts functions across all Channels in Marketing Cloud.

lv] e All Contacts functions at the Enterprise/Parent level.

Q5) Northern Trail Outfitters plans to integrate their Sales Cloud Contacts. How should their Marketing Cloud admin configure the Sync
of the contact object so that only marketable contacts are synced over?

@ Select all marketable records.

@ Select all new records.

@ @ Select all records with an email address.
�@ Select all records.

Q6) Northern Trail Outfitters wants to switch on the out-of-the-box audit trail functionality in the Marketing Cloud account, however they
cannot see the option to enable it. What could be the likely cause?

@ User is missing the marketing cloud api user rights.

@ @ User is missing the marketing cloud security administrator rights.
@ User is missing the marketing cloud administrator rights.

@ User is missing the marketing cloud viewer rights.

Q7) Recommended setting for Login Expires After Inactivity:

@ 60 days or less

@ 45 days or less

@ @ 90 days or less
@ 180 days or less

Q8) How do you setup Company Info?

@ @ In Marketing Cloud Setup, click Company Settings, Account Settings, Edit.

@ In Marketing Cloud Setup, go to Account Settings, Company Information, Edit.

@ Marketing Cloud Support will set this up on your behalf.

@ In the dropdown to the left of your username, click on the Business Unit, then Setup.

Q9) The Northern Trail Outfitters (NTO) marketing team is launching a new email campaign. NTO's Email Specialist wants to perform
quality assurance checks on the email prior to send and has asked about using the Validate functionality for this effort. Which three
items will Validate check in an email message? Choose 3 answers

@ @ Correct syntax is used on any AMPScript in the email's code.
@ @ Each content area specified in a dynamic content rule exists.
@ @ Personalization strings map to attributes or data extension fields
@ Grammar and spelling in the email text is correct

Q10) As a Marketing Cloud Administrator you have been told about how heavy scripting in the email leads to severe delays in sending
emails out the door. The Marketing department has asked you whether there is a possibility to speed things up. Which of the below
functionality will be best suited for the need?

@ Sending through journey builder.
@ @ Enabling burst sending.

@ Do not use scripting in emails.

@ Sending through automation studio.
Answer Sheet

Q1) Global Conveyors has a new business unit. What should Admin do before creating business units?

lv} rs) Map your Organizational Structure for business unit
@ Delete your users

@ Send a test email from Marketing Cloud

@ Rename your folders

Q2)

Northern Trail Outfitters (NTO) an outdoor gear store, manages customer relationships in Sales Cloud and sends emails in Marketing
Cloud.

NTO offers a 30 day free trail program and sends three emails about the program each day:

- A follow up email to contacts who signed up for the program 14 days ago.

-A follow up email with a reminder about the trail expiration to contacts who signed up for the program 27 days ago.

NTO sends emails automatically from Marketing Cloud, using Sales Cloud reports that filter contacts by corresponding dates.

What type of campaign should be created to meet this requirement?

@ @ Drip campaign
Explanation:-
Refer:

https://help.salesforce.com/articleView?
id=mc_co_30_day_drip_campaign_salesforce_reports_salesforce_data_extensions_and_automation_studio.htm&type=5

@ Trail campaign
@ Continuous campaign
@ Nurture campaign

Q3) As an administrator you have received the following request from the Marketing Team: We want to be able to act on real-time
interaction data and pick the next best action depending on user behavior? Which Marketing Cloud add-on would best serve the
purpose?

@ @ Interaction Studio
@ Automation Studio
@ Journey Builder

@ None of these

Q4) Why is whitelisting the entire set of IP ranges for your region a best practice? Choose two.

@ It allows users to access Marketing Cloud regardless of their work location without extra authentication.

@ @ It ensures Salesforce login pools can process end users� login authentication when accessing Salesforce.
@ It minimizes the use of verification codes required for logins, saving time for users and administrators.

@ @ It avoids unintended service disruptions due to movement between primary and secondary instances.

Q5) A marketing team wants to export specific send data from their account on a weekly basis. This data needs to be encrypted and
generated with specific column names which allow for import directly into a third-party analytics system. Which method should be
used to pull the data from Marketing Cloud?

@ Query Activity

@ Tracking Data Extract

@ Data Extension Export

@ @ Data Extension Extract

Q6) Global Conveyors is determining the marketing cloud instance (MID). What can the admin do with this information? Choose two
answers.

@ @ Configure a Web Collect URL

@ Configure Marketing Connect URL

@ Obtain appropriate URL endpoint for use with REST Service API

@ @ Obtain appropriate URL endpoint for use with SOAP Service API

Q7) Which account type merges an account with a contact in a single view?

@ Commercial Account
@ User Account

@ @ Person Account

@ Consumer Account

Q8) Global Conveyors requested the Admin configure a spam filter to exempt certain email messages from being filtered or rejected.
Which process should the Admin apply?

@ Data filter

@ @ allowiisting

Explanation:-

Allowlisting is the correct answer - https://help.salesforce.com/articleView?id=sf.mc_overview_glossary.htm

@ AmPscript
@ Workflow

Q9) A Marketing Cloud admin has created some profile attributes, but doesn�t want the customer to see them in the profile center. How
should the attributes be configured?

@ Mark the attribute as read-only.

@ Mark the attribute as a preference center attribute.
@ Mark the attribute as a profile attribute.

@ @ Mark the attribute as hidden.

Q10) Which deliverability best practice helps the Marketing Admin build a positive sending reputation with ISPs?

@ @ IP Warming

@ Subscriber Preview
@ Text Versions

@ Content Detective
Answer Sheet

Q1) Global Conveyors wants to create, send, and measure SMS campaigns across the globe. Which application should be used to
accomplish this requirement?

@ Audience Builder
@ Email Studio

@ @ MobileConnect
@ Automation Studio

Q2) Which two metrics will a Marketing Cloud admin be able to view under Setup Home, given the apps are provisioned in the account?

@ @ The total number of users in your account.

@ Agraph displaying the number and states of automations from the last 14 days.

@ The total number of emails sent from your account within the last 7 days.

@ @ The total number of content pieces in your account, including a subtotal of shared assets.

Q3) Which one of these data sources does not contain the contact information?

@ Queries

@ Filters

@ Data Extensions

@ @ Email Header and Footer Rules

@Q4) Recommended setting for User Passwords Expire In:

@ 180 days
@ 45 days

@ 60 days
@ @ 90 days

Q5) Global Conveyors wants to track impression by job report. Which two considerations Admin should keep in mind? Choose 2.

@ @ only emails that use AMPscript can be tracked using these reports.

@ @ only emails that use dynamic content can be tracked using these reports.
@ Only listed ISPs are tracked.

@ Only Return Path-maintained email addresses are tracked.

Q6) Choose the correct steps needed to apply administrative permissions for Marketing Cloud Connect: (choose two)

@ Enable Marketing Cloud permissions for Marketing Cloud Connect Sends, Marketing Cloud Connect Data Sync, and Marketing Cloud Connect
Journeys

@ @ Edit the CRM User Page Layout to add the Marketing Cloud for AppExchange User and Marketing Cloud for AppExchange Admin Fields
@ @ Enable Marketing Cloud for AppExchange User and Marketing Cloud for AppExchange Admin for the Salesforce CRM Administrator User
@ Add the Marketing Cloud Connect CRM Administrative User and Save Changes in Setup

Q7) Northern Trail Outfitters� Marketing Cloud admin wants to ensure certain subscribers� opens and clicks are NOT tracked at their
request, in accordance with the EU�s General Data Protection Regulation. In which two ways should the administrator configure these
settings?

@ @ Enable the DoNotTrack Attribute on each Subscriber.

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_do_not_track_email_opens_and_clicks.htm&type=5
@ @ Create a Preference Attribute called DoNotTrack.

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_do_not_track_email_opens_and_clicks.htm&type=5
@ In Setup, change DoNottTrack to On.

@ Mark the default DoNotTrack Profile Attribute to correct.

Q8) Which field CANNOT be updated in Company Information?

@ Company Name

@ Country

@ @ Account Name

@ Company Address (Street, City, State, ZIP/Postal Code)

Q9) What are potential risks of using Non-Scope by User Data Access configuration for Marketing Cloud Connect? (choose two)

@ Users may be able to view more records than they should have access to in CRM, creating a security risk.

@ @ AuUser may run a report displaying only records visible to them but containing additional records they don't see, causing a send to deploy to more
contacts than intended.

@ Contacts may not be able to unsubscribe due to incorrect Account mapping.

@ @ AUser may run a report containing records visible to them but not the Salesforce System User, causing zero emails to be sent.

Q10) Which statement best describe a contact and a subscriber?

@ Acontact is always a subscriber. A subscriber is always a contact.

@ Acontact is a person who opts to receive communications through a specified channel. A subscriber is anyone you send messages to.

@ @ Acontact is a person you are going to send messages to. A subscriber opted to receive communications or belongs to a particular channel.
@ Acontact is a person who opts in to text messages. A subscriber is a person who opts in to email messages.
Answer Sheet

Q1) A marketing team accidentally sends SMS campaigns intended for 4 p.m. at 4 a.m. They would like to use a Blackout Window to
prevent this from happening again. Which two actions would a Blackout Window prevent?

@ @ Sends manually initiated during the Blackout Window.
@ Large sends started before the blackout window begins.
@ @ Scheduling sends during the Blackout Window.

@ Sends conducted using Mobile Connect API calls.

Q2) What are the Benefits to Distributed Marketing? (pick 3)

@ Allow for nightly reporting on tracking and ROI.

@ @ Maintain brand consistency and compliance.

g e Let business users focus on customer relationships.
@ @ Customize messages quickly and intuitively.

Q3) Which type of data source connects two different contact data tables to each other based on particular field?

@ Data Designer

@ Contact Key

@ Synchronised Data Extension
@ @ Attribute Group

Q4) For most Marketing Cloud Connect functionality, users need: (choose 2)

@ Transparent Data Encryption
@ @ Marketing Cloud License
@ Single Sign-On Functionality
@ @ Sales or Service Cloud License

Q5) A Marketing Cloud admin wants to maximize login security to ensure that data is protected. Which two settings are recommended?

@ The session timeout set to 8 hours.

@ @ The login expires after inactivity set to 90 Days.
@ @ The invalid logins before lockout set to 3 attempts.
@ The minimum username length set to 6 characters.

Q6) Northern Trail Outfitters enabled enhanced sender profile feature. The NTO admin wants to create personalized email sends to their
customers using the names of specific customer service representatives. While the content of the send remains same across the email
send, the marketer wants the From Name to appear different for each subscriber. What are next steps for email personalization?
Choose 2.

@ @ Create a sender profile that uses AMPscript to dynamically pull information from the subscriber attributes populated by Salesforce information.
@ Create subscription preference to track user's behavior.

[v} e Create From Name and From Email attributes for their subscribers to hold the From information to include in the send.

@ Create a workflow to update member status.

Q7) How are publication lists used in the Marketing Cloud?

@ To manage subscribers in guided and triggered email sends.

@ @ To allow subscribers to opt-down/out instead of unsubscribing from all.
@ To build dynamic content rules by subscriber type.

@ To send communication to all subscribers, regardless of opt-in status.

Q8) Northern Trail Outfitters (NTO) is adding Mobile Studio to its marketing tools. Currently, NTO uses Email Studio and Journey
Builder to send email messages. They are using a unique alphanumeric as the Subscriber Key in Email Studio. What should the
administrator do to prevent duplicates across all Marketing Cloud channels?

@ Use Merge functionality for new Mobile contacts.
@ @ Use a single Contact Key value.

@ Use channel-specific unique identifiers.

@ Turn on Contact Matching in Setup.

Q9) Which statement is INCORRECT about Tenant Types?

[v) e On Business unit, a tenant is the single account.

@ On agency, each top-level account and each associate client account is a separate tenant.

@ On Enterprise 2.0, tenant is the top-level account and all associated business units.

@ On Enterprise, a tenant is the top-level account and all associated ON-Your-Behalf or Lock & Publish business units.

Q10) Which standard Marketing Cloud role creates and delivers messages through applicable channel apps?

@ Marketing Cloud Channel Manager

@ @ Marketing Cloud Content Editor/Publisher
@ Marketing Cloud Administrator

@ Marketing Cloud Viewer
Answer Sheet

Q1) What should the Admin create to synchronize objects from Service Cloud Mobile, pull the information into Marketing Cloud, and
share contact data with business units?

@ Create a synchronized attribute group.

@ Create a synchronized data source with the sharing window set to outside the business unit.

@ Create a synchronized population group in Mobile Service Cloud and link the object to Marketing Cloud.
@ @ Create a synchronized data extension.

Q2) Which type of data extension has a send relationship and adds contacts to all subscribers when you send to them?

@ Attribute Data Extension

@ Transferable Data Extension
@ Transmittal Data Extension
@ @ Sendable Data Extension

Q3) Which of the following statements is correct about deleting contacts?

@ Itis best to delete unengaged subscribers in order to reduce cost.

@ Itis best to move unengaged subscribers to a separate data extension.

@ It is best to move unengaged subscribers to a synchronized data extension.

[v) e It is best to unsubscribe unengaged contacts from individual channels rather than delete them.

@4) Options for level of data access in Marketing Cloud Connect?

@ @ Non-scope by User / Scope by User
@ Admin User / Basic User

@ Limited User / Unlimited User

@ Full Access / Limited Access

Q5) Which application serves as your real-time, direct line to understanding customer data?

@ BrandBuilder
@ Content Box
@ @ Audience Builder
@ Application Switcher

Q6) A Marketing Cloud administrator is asked by the Legal Team to automatically process certain keywords (such as �Unsubscribe�)
when received as a reply to an email send, and to remove the Out of Office replies to help the team better interact with customer
responses. Which functionality should they use?

@ Tracking extracts.

@ Preference management center.
@ @ Reply mail management.

@ Sql query in automation studio.

Q7) A Marketing Cloud admin is configuring the Marketing Cloud data model for the first time. Journey Builder with of messages being
sent to customers, based on if there has been an order or not. There are two existing data model Orders:

- Customers contains information about subscribers including Email Address, First Name, Last name.

- Orders contains information about the Orders and includes the unique identifier of the customer

In which two ways should the admin configure Data Designer to allow this data to be used within a Journey?

Choose 2 answers

@ Link the Customers data extension to the data model using Email Address

@ @ Link the Customers data extension to the data model using Customer ID

@ Link the Orders data extension to the Customers data extension using a Many-to-Many relationship
Lv) e Link the Orders data extension to the Customers data extension using a One-to-Many relationship

Q8) What elements of CAN-SPAM should the Marketing Cloud admin ensure are present for each Commercial send?

@ Business name and physical mailing address

@ Business name and a link to the business website

@ Preference Center link and a link to the business website
@ @ Preference Center link and physical mailing address

Q9) Setup Assistant provides information and resources for configuring a new Marketing Cloud account. Which two topics does Setup
Assistant cover? Choose 2 answers

@ @ Setting up the Data Structure
@ @ Managing the Enhanced SFTP
@ Enabling Mobile Connect

@ Configuring Journey Builder

Q10) Which three considerations should be made when setting up Distributed Marketing? Choose 3 answers

@ @ Messages can be sent to Contacts, Leads, and Person Accounts.

@ Business users can select any email at time of send.

@ @ The DM administrator Profile is required to access Distributed Marketing.
@ @ Default options can be set up for the greeting in the email.
Answer Sheet

Q1) NTO wants to format links for consumption by Google Analytics 360. NTO wants to make sure they do not have any data which
could be considered Personally Identifiable information (PII) within their links. Which three values could be used as personalization
strings in query string parameters? Choose 3 answers.

@ @ Subscriber ID
@ @ Product Code

@ @ Application ID
@ Email Address

Q2) Which three statements should be considered before using Goals in Journey Builder? Choose 3 answers

@ @ Goals can act as exit criteria.

@ Goal target statistics are stored in a data extension.

@ @ Goals are created to evaluate journey performance.

@ @ Contacts are evaluated against the goal after a wait activity.

Q3) An email marketing manager is planning to send a promotional email to one million subscribers. Which data structure should be
used?

@ List

@ @ Data Extension
@ Publication List

@ Group

Q4) A Contact Delete request has been processed for subscribers who have been sent an email. to previously in a northern action did
NOT target all contacts in their account and a significant number of contacts which are still remaining. Which two data would still exist
in the account? Choose 2 answers.

@ Contact-specific data at the job level

@ @ Contact data in non-sendable data extensions

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_tracking_overview.htm&type=5
@ @ General tracking data at the job level

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_tracking_overview.htm&type=5
@ Contact data in sendable data extensions

Q5) Northern Trail Outfitters wants to bring subscriber data from its data warehouse into Marketing Cloud. Which 2 fields would need
minimal consideration, for size/scalability related reasons, when creating a data extension to house the data? Choose 2 answers

@ Number
@ @ Decimal
@ @ Text

@ Boolean

Q6) Northern Trail Outfitters (NTO) has expanded its marketing efforts globally and wants to implement a dedicated Sender
Authentication Package. They plan to share it across each of their Marketing Cloud accounts. Which two considerations would help
NTO determine if a Dedicated IP is the right choice? Choose 2 answers.

@ length of time needed to pause sending is greater than one month

@ @ Send volume is large enough to maintain a positive or neutral reputation
@ @ Allof NTO's accounts should be on the same stack

@ Pre-warmed IP address can be purchased from Salesforce

Q7) A Marketing Cloud admin at Northern Trail Outfitters (NTO) is exploring whether they need to separate their brands into separate
business units. When should the admin create separate business units for each of NTO's brands?

@ Anew sender profile needs to be leveraged for sending transactional emails

@ NTO requires SSL certificate configurations for Content Builder and Portfolio images

@ Multiple brand logos must be accommodated in an email header

@ @ Brand-specific private domains need to be leveraged when wrapping images and links in email campaigns

Q8) A marketing Cloud admin wants to ensure sensitive information needed for email sends is NOT imported and stored in Marketing
cloud. What solution should they implement?

@ Transparent Data Encryption
@ Key Management

@ Field level Encryption

@ @ Tokenized Sending

Q9) Northern Trail Outfitters' employees are NOT receiving emails because the messages are being blocked by Spam filters. How could
the Marketing Cloud admin address this issue?

@ @ Provide the IT team a list of relevant IP Addresses to whitelist in their spam filter
@ Ask employees to use personal email addresses instead of corporate email addresses
@ Import employee email addresses into All Subscribers with an "Active status

@ Ensure employees have opted in to the test email list or data extension

Q10) An email manager was anticipating a test email to arrive in their inbox. Where in Email Studio should the Marketing Cloud admin
look to determine if the test deployed?

@ My Reports > Administrator Reports > Email Sends By User

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_re_email_studio_reports.htm&type=5
@ @ My Tracking > Test Send Emails

@ My Tracking > A/B Testing
Answer Sheet

Q1) NTO has been noting reduced deliverability when they do large sends. Which part of deliverability is tied to hitting Spam Traps
during a send?

@ Content

@ @ List Hygiene
@ Engagement
@ Authentication

Q2) Northern Trail Outfitters (NTO) only has enough licenses for their staff. A campaign manager is out on parental leave. How should
NTO create a new user to fill in?

@ @ Disable the campaign manager's user and create a new user

@ Delete the campaign manager's user and create a new user

@ Transfer the campaign manager's permissions to a new user

@ Deactivate the campaign manager's license and assign it to the new user

Q3) Northern Trail Outfitters (NTO) hired a new Marketing Cloud admin, who was told all emails come from info@email.nto.com. the
previous admin did not leave any documentation. Which aspects would confirm a Sender Authentication Package (SAP) has been set
up on the account? 2 answers.

@ users receive Marketing Cloud password reset emails from help@email nto.com

@ The login page for Marketing Cloud Users is login.email.nto.com and is branded with NTO colors
ee Upon receiving an email, all tracked links start with click.email.nto.com

g [3] Cloudpages personalized URLs are served from cloud.email.nto.com

@4) A Marketing Cloud admin wants to configure a new keyword for an upcoming SMS campaign. After entering the desired keyword
CELEBRATION, the admin notices the keyword is unavailable. What issue could the admin be facing?

@ Keyword has too many characters

@ @ Keyword is used within another business unit
@ Keyword is a reserved word

@ Keyword fails to meet content standards

Q5) Marketing Cloud admin is asked to determine the total number of emails sent across all of their business units in the last calendar
year. Where would the admin retrieve this information?

[v) e Analytics Builder > Reports > Email Send Report
@ Email Studio > Email > Tracking > Sends

@ Contact Builder > All Contacts > Email

@ Studio > Email > Subscribers > All Subscribers

Q6) Northern Trail Outfitters is migrating from a small, in-house email solution to Marketing Cloud. What should the Marketing Cloud
admin consider when sending from the new IP Address?

@ the new IP Address is now in use.

@ Migration of larger marketing campaigns is necessary prior to bringing on smaller, triggered campaigns.
@ @ Sending in large volumes will alert ISPs

@ Building desirable sending history and data will be variable based on list size and engagement.

@ The IP address is on reserve, is already in use, and has an email sending history.

Q7) Security and legal teams determine subscriber data available to EMEA teams should NOT be available to AMER teams.
How could the Marketing Cloud admin ensure distinct data integrity across the regions?

@ Deploy separate Publication Lists for each region within one account
@ @ Separate regions into business units and apply Subscriber Filters
@ Deploy Multi-Org with a single Marketing Cloud Account

@ Filter data view permissions at the subscriber level

Q8) Northern Trail Outfitters (NTO) keeps their subscribers in sync with their external database via the import of a CSV file which is
dropped to the of Marketing Cloud SFTP each day. However, NTO has realized the number of subscribers being sent emails is
considerably lower than the number they were expecting based on records in their database. Which feature would allow NTO to monitor
whether all records were added to the target data structure each day?

@ External Key within the Import File Activity

@ RuntimeError within the File Drop Automation

@ Run Completion within the File Drop Automation

@ @ Notification Settings within the Import File Activity

Q9) Northern Trail Outfitters placed an encrypted file on their Marketing Cloud SFTP for import into a data extension. They are using a
file transfer Activity to decrypt the file. What would the decrypted data be after the File Transfer Activity completes?

@ Target Data Extension
@ Selected SFTP folder
@ @ Safehouse

@ Original SFTP folder

Q10) What is Setup Assistant?

@ Support service allowing the outsourcing of repetitive admin tasks
@ A dashboard containing key metrics for the business unit

@ Asearch within Help and Training limited to configuration documents
@@EBaA prioritized account configuration checklist
Answer Sheet

Q1) A user asks a Marketing Cloud admin to review their permissions since they are unable to send an email. The admin reviews the
user profile and notices the user has three roles assigned: Content Creator, Data Manager, and Marketing Cloud Viewer.
What should the admin do to resolve the issue so the user can send an email?

@ @ Remove the Marketing Cloud Viewer Role

@ Edit permissions and Grant permissions to Send

@ Add the Role Marketing Cloud Channel Manager

@ Edit permissions and deselect Deny for Email Sending!

Q2) Which three options determine when a contact could enter a journey? Choose 3 answers.

@ @ Re-entry at any time

@ Re-entry by date

@ @ No re-entry

@ @ Re-entry only after exiting

Q3) A Marketing Cloud admin is using the Import Wizard to import data into a non-sendable data extension, but receives an error
indicating the import type being used requires a primary key. Which import type could the admin use instead?

@ Add and Update
@ @ Overmrite
@ Update Only

@ Add Only

@Q4) Northern Trail Outfitters (NTO) has a franchise model which allows locally-owned stores to operate under the corporate umbrella.
They are required by corporate policy to email each franchisee a monthly statement, but the statement cannot be publicly accessible.
Which Marketing Cloud product should NTO purchase as a solution?

@ Email Rachments

@ @ Distributed Sending
@ Content Syndication
@ Analytics Builder

Q5) A Marketing Cloud admin has scheduled a query on a daily basis. They notice the query sometimes fails to execute. How would the
admin ensure a notification is received when the query fails?

@ @ Add their Email Address in the automation "Runtime Error or Skipped Run Notification Settings
@ Install the Marketing Cloud App on phone to receive Push Messages

@ Configure the "Event Notification Service" in Setup with their Email Address

@ Add their Email Address in the Query Activity Notifications Field

Q6) Northern Trail Outfitters installed Query Studio for Marketing Cloud, however, users are reporting they do NOT have access. How
should the Marketing Cloud admin ensure users have access?

@ @ License all appropriate users within the installed package
@ Install App-appropriate business units for expanded access
@ Configure the API Integration to allow all users access

@ Choose Public App Integration during the installation

Q7) A Marketing Cloud admin wants to create a suppression list for hard-bounced email addresses. Where could the details be found?

@ Runa Bounce Email Report

@ @ Query the Bounce Data View

@ Run an Account Send Summary Report
@ Query the Send Log

Q8) Northern Trail Outfitters (NTO) wants to limit who can receive Marketing Cloud tracking data via email from their Account to any
email associated with their domain (ntoretail.com). Which steps should be taken to implement this? Choose 2 answers

@ @ Add a Domain to the Export Email Whitelist
@ Edit the entity Verification Settings

@ @ Enforce Export Email Whitelist

@ Enable IP Whitelisting

Q9) Northern Trail Outfitters (NTO) is building a journey which randomly sends five different versions of an initial welcome email to new
subscriber however, subscribers receive the same follow-up email two weeks later. To improve maintainability of their email content,
NTO want to use 3 completely different emails, rather than having one email with dynamic content.

Which activity would allow NTO to build the journey with the fewest activities possible?

@ Einstein STO
@ Wait Until Date

@ @ Engagement Split
@ Join

Q10) NTO wants to copy journeys across business units. What could be used to replicate journey structure so it can be easily recreated
in another account?

@ Journey Extracts

@ Copy activities

@ Journey Templates

@ @ Deployment Manager
Answer Sheet

Q1) A user asks a Marketing Cloud admin to update and increase their session timeout setting. Which three considerations should the
admin review before making this update? Choose 3 answers.

@ @ Change impacts all users

@ @ Security risk of unauthorized users for longer timeout settings
@ @ Best practice suggests a 20-minute timeout setting

@ Typical length of time users spend in Marketing Cloud

Q2) Northern Trail Outfitters does NOT want to store email addresses or phone numbers within Marketing Cloud. Which feature should
they use?

@ Lookup reference to Contact Object
@ Field Level Encryption

@ @ Tokenized Sending

@ Master-detail relationship to Contacts

Q3) Northern Trail Outfitters is preparing to send a promotional email. The audience file was loaded into a data extension but does not
display for Marketing Cloud admin scheduling the send. What should the admin confirm to resolve the issue?

@ @ The data extension is marked as Sendable

@ The data extension is linked using the Contact Key

@ The Data extension is marked as Sendable and Testable
@ The data extension contains a Salesforce ID

Q4) A Marketing Cloud admin is tasked with overhauling the data model for Enterprise. While the current data model is isolated to the
email channel and there are plans to expand to both SMS and Push channels in the near future. Which three data preparations should
be made to retain high data quality in the new mode? Choose 3 answers.

@ @ Normalize data and fields to prevent redundancy.

@ @ Identify and assign appropriate keys to tie records together.
@ Ensure every data source has a sendable field.

@ @ Remove nonessential data for marketing purposes.

Q5) Northern Trail Outfitters wants to set up their Send Log data extension. Which three considerations should be made for long term
success? Choose 3 answers

ee Log attribute data necessary for auditing communications
@ @ Apply an appropriately-scoped Data Retention period
@ Set the period to a fixed date in the Data Retention Policy
@ @ Add custom fields not included in the Send Log Template

Q6) A Marketing Cloud admin discovers large sends are not meeting send speed goals set by the organization. What functionality
would get messages out the door faster?

@ @ Burst Sending

@ Marketing Cloud Connect

@ Send Throttling

@ Journey Builder Triggered Sends

Q7) Northern Trail Outfitters wants to segment audiences based on Sales Cloud data. Where would their Marketing Cloud admin
configure Sales Cloud Objects to be synced and leveraged in Marketing Co.

@ @ Contact Builder > Data Sources

@ Contact Builder > Data Extensions > Synchronized Data Extensions
@ Setup >Data Management > Synchronized Data Extensions

@ Setup > Apps > Salesforce Integration

Q8) A Marketing Cloud admin is configuring Social Studio to manage Northern Trail Outfitters social media accounts. Which 2
prerequisites for configuring Social Studio should the admin consider? Choose 2 answers

@ @ Bitly URL Shortener

@ @ Login detail for each social media account
@ Google URL shortner

@ Facebook ad manager

Q9) What does Marketing Cloud authenticate when a user logs in through the user interface?

@ If the user is assigned a role in the parent business unit
@ @ Ifthe user is logging in from a whitelisted IP address
@ If the user has login hours enabled on their profile

@ If the user is an API User on their record

Q10) Northern Trail Outfitters (NTO) is concerned about unauthorized API access to their Marketing Cloud account. Which feature
would NTO enable to assist in reducing threats from malicious API attacks?

@ Field Level Encryption
@ Advanced Audit Trail

@ @ IP Whitelisting
@ Single Sign on Authentication
Answer Sheet

Q1) Northern Trail Outfitters has five business units in their Marketing Cloud account. All business units should be configured to use
the same SFTP directory. How should this setup be achieved?

@ Each business unit should have multiple SFTP users

@ child business unit SFTP user should be created

@ @ Alichild business units should have an individual SFTP user
@ Copy the parent SFTP user into each child business unit

Q2) Northern Trail Outfitters (NTO) uses data extensions for all of their email audiences. A customer reports they unsubscribed several
week-end ago, but continue to receive NTO's daily digest at their old address. NTO's Marketing cloud Admin has confidently deleted
them from present in the appropriate data extension.
What consideration could account for this behavior?

@ The data extension was not configured as sendable.

@ Contact Builder was not configured properly.

@ @ Data retention settings were incorrect in the data extension.
@ The email address in All Subscribers is prioritized.

Q3) Northern Trail Outfitters has noticed an issue with their sends today. Which two links in Setup Home could be used to troubleshoot
the issue? Choose 2 answers

@ Failed Sends

@ @ Help and Training
@ @ system Status

@ Create Support Case

@4) Northern Trail Outfitters wants to drive additional online sales. They are interested in using Einstein to recommend similar items to
customers during the checkout process.
Which two terms would they add to their website to accomplish this? Choose 2 answers.

@ Email Conversion Code
@ @ Collect Code

@ @ Recommendation Code
@ Conversion/Cart Code

Q5) A Marketing Cloud admin notices Individual Email Results are NOT being pushed back into Sales Cloud for a particular end. The
admin of Marketing Cloud Connect is functioning properly. What should the admin confirm about the data extension?

@ The triggeredSendDataExtension data extension template was used.

@ The data extension is located in the Synchronized Data Extensions folder.
@ The wind relationship links Subscriber Key to Subscribers on Email Address
@ @ The data extension is located in the Salesforce Data Extensions folder.

Q6) A Marketing Cloud admin is asked to append an Urchin Tracking Module (UTM) variable string to links in emails. What functionality
would allow this?

@ @ Web Analytics Connector
@ Web and Mobile Analytics

@ Advertising Studio

@ Personalization Builder

Q7) A Marketing Cloud Administrator noticed a File Drop Automation has been falling on the Import File activity. The automation is
configured with a filename pattern, so the filename is expected to begin with customer import_. The import is configured to look for a
file named Customer import %%Year%%%% Month%%%%Day%%.csv, however, the admin notices the filenames Include seconds and
milliseconds

what should the admin do to fix the issue?

@ @ Use %%FILENAME_FROM_TRIGGER%% in the Import File Activity.
@ Use the exact file name used for the trigger in the Import File Activity.

@ Make sure the team has a date stamp to avoid duplication.

@ Make sure the files placed on the correct sub-folder within the SFTP.

Q8) While setting up Marketing Cloud Connect, a Marketing Cloud admin navigates to the Marketing Cloud tab in Sales Cloud to
complete the integration. The admin then receives the following error message:

- Insufficient User Permissions. You have not been designated as an integrated Marketing Cloud user. Contact your system
administrator.

The admin notices the Marketing Cloud for AppExchange Admin option is selected when looking at the user settings. What action
should correct the issue?

@ @ Apply the administrator and Marketing Cloud Administrator permission sets to user
@ Apply the appropriate user mappings in the CRM configuration

@ Reset al passwords to force new tokens

@ Apply the Marketing Cloud for AppExchange User option as well

Q9) Northern Trail Outfitters (NTO) wants a business analyst to import contact lists. The analyst has the follow Cloud Channel Manager
and Marketing Cloud Viewer. The Analyst logged in but is unable to import contacts. How should NTO update the user to allow the
analyst the appropriate access?

@ Add Distributed Sending User

@ Add Marketing Cloud Security Administrator
@ @ Remove Marketing Cloud Viewer

@ Remove Marketing Cloud Channel Manager

Q10) A Marketing Cloud admin is tasked with requesting Marketing Cloud Connect Multi-Org enablement. What consideration should be
given to the preference profile centers for this integration?

@ Profile/Preference centers are automatically created for each business unit connected through Multi-org
@ @ Multi org does not support the standard profile preference center for the business units.

@ Branding for each business units� profile centers will be inherited from the default business unit setup.
@ Profile/Preference centers for Multi-Org accounts are configured in the Salesforce CRM settings.
Answer Sheet

Q1) Where would a Marketing Cloud admin view all verified email addresses?

@ Reply Mail Management

@ Identity Verification Log

@ Sender Profiles

@ @ From Address Management

Q2) A Marketing Cloud admin is asked to add a set of four tracking parameters automatically to all the links in an email sent via email
studio. Which solution should the admin suggest?

@ AMPscript for Marketing Cloud
@ Google Analytics 360

@ Marketing Cloud Connect

@ @ Web Analytics Connector

Q3) A MC admin wants to sync Contacts from Sales Cloud, but is concerned about the number of Contacts since not all the contacts
will be sent an email.
What should the admin do to ensure only specific Contacts are synced?

@ Filter existing records in All Subscribers

@ Filter records on a formula field

@ @ Filter records on a Boolean field

@ Filter records created after a specified date

@Q4) Northern Trail Outfitters uses Marketing Cloud Connect to leverage Sales Cloud data in their journeys. a user recently reported the
data coming from Sales Cloud is NOT up to date. Where should the Marketing Cloud admin begin troubleshooting?

@ @ Contact Builder > Data Sources

@ Email Studio > Synchronized Data Extensions

@ Contact Builder > Synchronized Data Extensions
@ Automation Studio > File Transfers

Q5) Northern Trail Outfitters (NTO) has the Discover Reporting Tool. Which two report types could help NTO drive their mobile adoption
strategy? Choose 2 answers.

@ @ Email Sending Performance Report
@ Deliverability Complaint Rate

@ @ Email Performance by Device

@ Time Between Send and Engagement
Answer Sheet

Q1) Which statements are correct about Marketing Cloud and Marketing Cloud Connect when using Non-Scope by User configuration?
(choose 3)

@ Users are always prevented from sending to report or campaign members who are not visible to them without notice.
@ @ Password policies are not in effect, making this configuration easy to maintain because passwords do not expire.
@ @ An administrator can set up a user without entering a password.

@ @ Within the Marketing Cloud, returned subscribers are not limited to what is visible to the user initiating the send.

Q2) Before you can enable marketers to include the Distributed Marketing content blocks in emails, you need to do two things.

@ Create a new Business Unit to house Distributed Marketing

[v] [3] Add the custom content blocks that you want to use as components.

@ @ Aad the Distributed Marketing installed package to your Marketing Cloud account.
@ Limit roles in Sales Cloud to only provide access to the Marketing functionality.

Q3) Northern Trail Outfitters purchased a Sender Authentication Package (SAP) and is provisioned within the account. The Marketing
Cloud admin wants to ensure the private domain being used as the From Address for email sends has been verified. How could the
admin meet this requirement?

@ Register each From Address with this domain individually by sending a verification email to each email address.

@ Register the private domain using Domain Registration.

@ @ The administrator does not need to verify the private domain.

@ Register each From Address with this domain by importing a data extension and sending a verification email to each email address.

Q4) Distributed Marketing channels supported: (choose two)

@ @sms
@ @ Email
@ Social
@ Push

Q5) Which send process can use Sender Profiles? Choose 3 Answers.

@ @ User-initiated Sends
@ @ Triggered Sends

@ Simple Automated Sends
@ @ Guided Sends

Q6) What Salesforce Editions work with Marketing Cloud Connect? (choose 4)

@ Basic

@ @ Developer
@ @ Unlimited
@ @ Enterprise
@ @ Performance
@ Professional

Q7) How do you find information on your MC instance?

@ Click on "Status" at any time in the top navigation menu of the Marketing Cloud interface.

@ Under your username, navigate to Setup. Use Quick Find to navigate to Account Settings. The Instance information is displayed in Account Settings.
@ Hover over your account name in the top corner of the Marketing Cloud interface, immediately to the left of your username. Click the hyperlinked
Instance # to view detailed information.

@ @ On trust.salesforce.com, click "Status" and enter your MID to display information.

Q8) Which IPs should be whitelisted when first configuring MC?

@ @ Whitelist the entire set of IP ranges for your region.

@ None - all users should use the standard verification process as a best practice.

@ Whitelist the IP ranges of your frequent Marketing Cloud users and administrators and Marketing Cloud Support.
@ Whitelist the IP addresses of the administrative users.

Q9) Which of the following are correct about All Contacts in Contact Builder? (choose 3)

@ @ Al Contacts contains All Subscribers plus anything marked as a Population.
@ All Contacts automatically links records across Studios/Channels.

@ @ Al Contacts functions across all Channels in Marketing Cloud.

@ @ All Contacts functions at the Enterprise/Parent level.

Q10) Northern Trail Outfitters plans to integrate their Sales Cloud Contacts. How should their Marketing Cloud admin configure the
Sync of the contact object so that only marketable contacts are synced over?

@ Select all marketable records.

@ Select all new records.

@ @ Select all records with an email address.
@ Select all records.

Q11) Northern Trail Outfitters wants to switch on the out-of-the-box audit trail functionality in the Marketing Cloud account, however
they cannot see the option to enable it. What could be the likely cause?

@ User is missing the marketing cloud api user rights.

@ @ User is missing the marketing cloud security administrator rights.
@ User is missing the marketing cloud administrator rights.

@ User is missing the marketing cloud viewer rights.

Q12) Recommended setting for Login Expires After Inactivity:

@ 60 days or less

@ 45 days or less

@ @ 290 days or less
@ 180 days or less

Q13) How do you setup Company Info?

@ @ In Marketing Cloud Setup, click Company Settings, Account Settings, Edit.

@ In Marketing Cloud Setup, go to Account Settings, Company Information, Edit.

@ Marketing Cloud Support will set this up on your behalf.

@ In the dropdown to the left of your username, click on the Business Unit, then Setup.

Q14) The Northern Trail Outfitters (NTO) marketing team is launching a new email campaign. NTO's Email Specialist wants to perform
quality assurance checks on the email prior to send and has asked about using the Validate functionality for this effort. Which three
items will Validate check in an email message? Choose 3 answers

@ @ Correct syntax is used on any AMPScript in the email's code.
@ @ Each content area specified in a dynamic content rule exists.
@ @ Personalization strings map to attributes or data extension fields
@ Grammar and spelling in the email text is correct.

Q15) As a Marketing Cloud Administrator you have been told about how heavy scripting in the email leads to severe delays in sending
emails out the door. The Marketing department has asked you whether there is a possibility to speed things up. Which of the below
functionality will be best suited for the need?

@ Sending through journey builder.
@ @ Enabling burst sending.

@ Do not use scripting in emails.

@ Sending through automation studio.

Q16) Global Conveyors has a new business unit. What should Admin do before creating business units?

@ @ Map your Organizational Structure for business unit
@ Delete your users

@ Send a test email from Marketing Cloud

@ Rename your folders

17)

Northern Trail Outfitters (NTO) an outdoor gear store, manages customer relationships in Sales Cloud and sends emails in Marketing
Cloud.

NTO offers a 30 day free trail program and sends three emails about the program each day:

- A follow up email to contacts who signed up for the program 14 days ago.

-A follow up email with a reminder about the trail expiration to contacts who signed up for the program 27 days ago.

NTO sends emails automatically from Marketing Cloud, using Sales Cloud reports that filter contacts by corresponding dates.

What type of campaign should be created to meet this requirement?

@ @ Drip campaign
Explanation:-
Refer:

https://help.salesforce.com/articleView?
id=mc_co_30_day_drip_campaign_salesforce_reports_salesforce_data_extensions_and_automation_studio.htm&type=5

@ Trail campaign
@ Continuous campaign
@ Nurture campaign

Q18) As an administrator you have received the following request from the Marketing Team: We want to be able to act on real-time
interaction data and pick the next best action depending on user behavior? Which Marketing Cloud add-on would best serve the
purpose?

@ @ interaction Studio
@ Automation Studio
@ Journey Builder

@ None of these

Q19) Why is whitelisting the entire set of IP ranges for your region a best practice? Choose two.

@ It allows users to access Marketing Cloud regardless of their work location without extra authentication.

lv} @ It ensures Salesforce login pools can process end users� login authentication when accessing Salesforce.
@ It minimizes the use of verification codes required for logins, saving time for users and administrators.

@ @ It avoids unintended service disruptions due to movement between primary and secondary instances.

Q20) A marketing team wants to export specific send data from their account on a weekly basis. This data needs to be encrypted and
generated with specific column names which allow for import directly into a third-party analytics system. Which method should be
used to pull the data from Marketing Cloud?

@ Query Activity

@ Tracking Data Extract

@ Data Extension Export

@ @ Data Extension Extract

Q21) Global Conveyors is determining the marketing cloud instance (MID). What can the admin do with this information? Choose two
answers.

@ @ Configure a Web Collect URL

@ Configure Marketing Connect URL

@ Obtain appropriate URL endpoint for use with REST Service API
iv) e Obtain appropriate URL endpoint for use with SOAP Service API

Q22) Which account type merges an account with a contact in a single view?

@ Commercial Account
@ User Account

@ @ Person Account

@ Consumer Account

Q23) Global Conveyors requested the Admin configure a spam filter to exempt certain email messages from being filtered or rejected.
Which process should the Admin apply?

@ Data filter

@ @ allowiisting

Explanation:-

Allowlisting is the correct answer - https://help.salesforce.com/articleView?id=sf.mc_overview_glossary.htm

@ AmPscript
@ Workflow

Q24) A Marketing Cloud admin has created some profile attributes, but doesn�t want the customer to see them in the profile center. How
should the attributes be configured?

@ Mark the attribute as read-only.

@ Mark the attribute as a preference center attribute.
@ Mark the attribute as a profile attribute.

@ @ Mark the attribute as hidden.

Q25) Which deliverability best practice helps the Marketing Admin build a positive sending reputation with ISPs?

@ @ IP Warming

@ Subscriber Preview
@ Text Versions

@ Content Detective

Q26) Global Conveyors wants to create, send, and measure SMS campaigns across the globe. Which application should be used to
accomplish this requirement?

@ Audience Builder
@ Email Studio

@ @ MobileConnect
@ Automation Studio

Q27) Which two metrics will a Marketing Cloud admin be able to view under Setup Home, given the apps are provisioned in the
account?

@ @ The total number of users in your account.

@ Agraph displaying the number and states of automations from the last 14 days.

@ The total number of emails sent from your account within the last 7 days.

@ @ The total number of content pieces in your account, including a subtotal of shared assets.

Q28) Which one of these data sources does not contain the contact information?

@ Queries

@ Filters

@ Data Extensions

@ @ Email Header and Footer Rules

Q29) Recommended setting for User Passwords Expire In:

@ 180 days
@ 45 days

@ 60 days
@ @ 90 days

Q30) Global Conveyors wants to track impression by job report. Which two considerations Admin should keep in mind? Choose 2.

ee Only emails that use AMPscript can be tracked using these reports.

@ @ Only emails that use dynamic content can be tracked using these reports
@ Only listed ISPs are tracked.

@ Only Return Path-maintained email addresses are tracked.

Q31) Choose the correct steps needed to apply administrative permissions for Marketing Cloud Connect: (choose two)

@ Enable Marketing Cloud permissions for Marketing Cloud Connect Sends, Marketing Cloud Connect Data Sync, and Marketing Cloud Connect
Journeys

@ @ Edit the CRM User Page Layout to add the Marketing Cloud for AppExchange User and Marketing Cloud for AppExchange Admin Fields
@ @ Enable Marketing Cloud for AppExchange User and Marketing Cloud for AppExchange Admin for the Salesforce CRM Administrator User
@ Add the Marketing Cloud Connect CRM Administrative User and Save Changes in Setup

Q32) Northern Trail Outfitters� Marketing Cloud admin wants to ensure certain subscribers� opens and clicks are NOT tracked at their
request, in accordance with the EU�s General Data Protection Regulation. In which two ways should the administrator configure these
settings?

@ @ Enable the DoNotTrack Attribute on each Subscriber.

Explanation:-Link - https://help.salesforce.com/article View?id=mc_es_do_not_track_email_opens_and_clicks.htm&type=5
@ @ Create a Preference Attribute called DoNotTrack.

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_do_not_track_email_opens_and_clicks.htm&type=5
@ In Setup, change DoNotTrack to On.

@ Mark the default DoNotTrack Profile Attribute to correct.

Q33) Which field CANNOT be updated in Company Information?

@ Company Name

@ Country

@ @ Account Name

@ Company Address (Street, City, State, ZIP/Postal Code)

Q34) What are potential risks of using Non-Scope by User Data Access configuration for Marketing Cloud Connect? (choose two)

@ Users may be able to view more records than they should have access to in CRM, creating a security risk.

@ @Auser may run a report displaying only records visible to them but containing additional records they don't see, causing a send to deploy to more
contacts than intended.

@ Contacts may not be able to unsubscribe due to incorrect Account mapping.

@ @ AUser may run a report containing records visible to them but not the Salesforce System User, causing zero emails to be sent.

Q35) Which statement best describe a contact and a subscriber?

@ Acontact is always a subscriber. A subscriber is always a contact.

@ Acontact is a person who opts to receive communications through a specified channel. A subscriber is anyone you send messages to.

@ @ Acontact is a person you are going to send messages to. A subscriber opted to receive communications or belongs to a particular channel.
@ Acontact is a person who opts in to text messages. A subscriber is a person who opts in to email messages.

Q36) A marketing team accidentally sends SMS campaigns intended for 4 p.m. at 4 a.m. They would like to use a Blackout Window to
prevent this from happening again. Which two actions would a Blackout Window prevent?

@ @ Sends manually initiated during the Blackout Window.
@ Large sends started before the blackout window begins.
@ @ Scheduling sends during the Blackout Window.

@ Sends conducted using Mobile Connect API calls.

Q37) What are the Benefits to Distributed Marketing? (pick 3)

@ Allow for nightly reporting on tracking and ROI.

@ @ Maintain brand consistency and compliance.

@ @ Let business users focus on customer relationships.
@ @ Customize messages quickly and intuitively.

Q38) Which type of data source connects two different contact data tables to each other based on particular field?

@ Data Designer

@ Contact Key

@ Synchronised Data Extension
@ @ Attribute Group

Q39) For most Marketing Cloud Connect functionality, users need: (choose 2)

@ Transparent Data Encryption
@ @ Marketing Cloud License
@ Single Sign-On Functionality
@ @ Sales or Service Cloud License

@Q40) A Marketing Cloud admin wants to maximize login security to ensure that data is protected. Which two settings are
recommended?

@ The session timeout set to 8 hours.

@ @ The login expires after inactivity set to 90 Days.
@ @ The invalid logins before lockout set to 3 attempts.
@ The minimum username length set to 6 characters.

Q41) Northern Trail Outfitters enabled enhanced sender profile feature. The NTO admin wants to create personalized email sends to
their customers using the names of specific customer service representatives. While the content of the send remains same across the
email send, the marketer wants the From Name to appear different for each subscriber. What are next steps for email personalization?
Choose 2.

@ @ Create a sender profile that uses AMPscript to dynamically pull information from the subscriber attributes populated by Salesforce information.
@ Create subscription preference to track user's behavior.

@ @ Create From Name and From Email attributes for their subscribers to hold the From information to include in the send.

@ Create a workflow to update member status.

Q42) How are publication lists used in the Marketing Cloud?

@ To manage subscribers in guided and triggered email sends.

@ @ To allow subscribers to opt-down/out instead of unsubscribing from all.
@ To build dynamic content rules by subscriber type.

@ To send communication to all subscribers, regardless of opt-in status.

Q43) Northern Trail Outfitters (NTO) is adding Mobile Studio to its marketing tools. Currently, NTO uses Email Studio and Journey
Builder to send email messages. They are using a unique alphanumeric as the Subscriber Key in Email Studio. What should the
administrator do to prevent duplicates across all Marketing Cloud channels?

@ Use Merge functionality for new Mobile contacts.
@ @ Use a single Contact Key value.

@ Use channel-specific unique identifiers.

@ Tum on Contact Matching in Setup.

@Q44) Which statement is INCORRECT about Tenant Types?

@ @ On Business unit, a tenant is the single account.

@ On agency, each top-level account and each associate client account is a separate tenant.

@ On Enterprise 2.0, tenant is the top-level account and all associated business units.

@ On Enterprise, a tenant is the top-level account and all associated ON-Your-Behalf or Lock & Publish business units.

@45) Which standard Marketing Cloud role creates and delivers messages through applicable channel apps?

@ Marketing Cloud Channel Manager

@ @ Marketing Cloud Content Editor/Publisher
@ Marketing Cloud Administrator

@ Marketing Cloud Viewer

Q46) What should the Admin create to synchronize objects from Service Cloud Mobile, pull the information into Marketing Cloud, and
share contact data with business units?

@ Create a synchronized attribute group.

@ Create a synchronized data source with the sharing window set to outside the business unit.

@ Create a synchronized population group in Mobile Service Cloud and link the object to Marketing Cloud.
@ @ Create a synchronized data extension.

Q47) Which type of data extension has a send relationship and adds contacts to all subscribers when you send to them?

@ Attribute Data Extension

@ Transferable Data Extension
@ Transmittal Data Extension
@ @ Sendable Data Extension

Q48) Which of the following statements is correct about deleting contacts?

@ Itis best to delete unengaged subscribers in order to reduce cost.

@ Itis best to move unengaged subscribers to a separate data extension.

@ Itis best to move unengaged subscribers to a synchronized data extension.

@ @ Itis best to unsubscribe unengaged contacts from individual channels rather than delete them.

Q49) Options for level of data access in Marketing Cloud Connect?

@ @ Non-scope by User / Scope by User
@ Admin User / Basic User

@ Limited User / Unlimited User

@ Full Access / Limited Access
Answer Sheet

Q1) Which application serves as your real-time, direct line to understanding customer data?

@ BrandBuilder
@ Content Box
@ @ Audience Builder
@ Application Switcher

Q2) A Marketing Cloud administrator is asked by the Legal Team to automatically process certain keywords (such as �Unsubscribe�)
when received as a reply to an email send, and to remove the Out of Office replies to help the team better interact with customer
responses. Which functionality should they use?

@ Tracking extracts.

@ Preference management center.
@ @ Reply mail management.

@ Sql query in automation studio.

Q3) A Marketing Cloud admin is configuring the Marketing Cloud data model for the first time. Journey Builder with of messages being
sent to customers, based on if there has been an order or not. There are two existing data model Orders:

- Customers contains information about subscribers including Email Address, First Name, Last name.

- Orders contains information about the Orders and includes the unique identifier of the customer

In which two ways should the admin configure Data Designer to allow this data to be used within a Journey?

Choose 2 answers

@ Link the Customers data extension to the data model using Email Address

@ @ Link the Customers data extension to the data model using Customer ID

@ Link the Orders data extension to the Customers data extension using a Many-to-Many relationship
lv) e Link the Orders data extension to the Customers data extension using a One-to-Many relationship

@Q4) What elements of CAN-SPAM should the Marketing Cloud admin ensure are present for each Commercial send?

@ Business name and physical mailing address

@ Business name and a link to the business website

@ Preference Center link and a link to the business website
@ @ Preference Center link and physical mailing address

Q5) Setup Assistant provides information and resources for configuring a new Marketing Cloud account. Which two topics does Setup
Assistant cover? Choose 2 answers

@ @ Setting up the Data Structure
@ @ Managing the Enhanced SFTP
@ Enabling Mobile Connect

@ Configuring Journey Builder

Q6) Which three considerations should be made when setting up Distributed Marketing? Choose 3 answers

@ @ Messages can be sent to Contacts, Leads, and Person Accounts.

@ Business users can select any email at time of send.

@ @ The DM administrator Profile is required to access Distributed Marketing.
@ @ Default options can be set up for the greeting in the email.

Q7) NTO wants to format links for consumption by Google Analytics 360. NTO wants to make sure they do not have any data which
could be considered Personally Identifiable information (PII) within their links. Which three values could be used as personalization
strings in query string parameters? Choose 3 answers.

@ @ Subscriber ID
@ @ Product Code
@ @ Application ID
@ Email Address

Q8) Which three statements should be considered before using Goals in Journey Builder? Choose 3 answers

@ @ Goals can act as exit criteria.

@ Goal target statistics are stored in a data extension.

@ @ Goals are created to evaluate journey performance.

@ @ Contacts are evaluated against the goal after a wait activity.

Q9) An email marketing manager is planning to send a promotional email to one million subscribers. Which data structure should be
used?

@ List

@ @ Data Extension
@ Publication List

@ Group

Q10) A Contact Delete request has been processed for subscribers who have been sent an email. to previously in a northern action did
NOT target all contacts in their account and a significant number of contacts which are still remaining. Which two data would still exist
in the account? Choose 2 answers.

@ Contact-specific data at the job level

@ @ Contact data in non-sendable data extensions

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_tracking_overview.htm&type=5
@ @ General tracking data at the job level

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_es_tracking_overview.htm&type=5
@ Contact data in sendable data extensions

Q11) Northern Trail Outfitters wants to bring subscriber data from its data warehouse into Marketing Cloud. Which 2 fields would need
minimal consideration, for size/scalability related reasons, when creating a data extension to house the data? Choose 2 answers

@ Number
@ @ Decimal
@ @ Text

@ Boolean

Q12) Northern Trail Outfitters (NTO) has expanded its marketing efforts globally and wants to implement a dedicated Sender
Authentication Package. They plan to share it across each of their Marketing Cloud accounts. Which two considerations would help
NTO determine if a Dedicated IP is the right choice? Choose 2 answers.

@ length of time needed to pause sending is greater than one month

@ @ Send volume is large enough to maintain a positive or neutral reputation
@ @ Allof NTO's accounts should be on the same stack

@ Pre-warmed IP address can be purchased from Salesforce

Q13) A Marketing Cloud admin at Northern Trail Outfitters (NTO) is exploring whether they need to separate their brands into separate
business units. When should the admin create separate business units for each of NTO's brands?

@ Anew sender profile needs to be leveraged for sending transactional emails

@ NTO requires SSL certificate configurations for Content Builder and Portfolio images

@ Multiple brand logos must be accommodated in an email header

@ @ Brand-specific private domains need to be leveraged when wrapping images and links in email campaigns

Q14) A marketing Cloud admin wants to ensure sensitive information needed for email sends is NOT imported and stored in Marketing
cloud. What solution should they implement?

@ Transparent Data Encryption
@ Key Management

@ Field level Encryption

@ @ Tokenized Sending

Q15) Northern Trail Outfitters' employees are NOT receiving emails because the messages are being blocked by Spam filters. How
could the Marketing Cloud admin address this issue?

@ @ Provide the IT team a list of relevant IP Addresses to whitelist in their spam filter
@ Ask employees to use personal email addresses instead of corporate email addresses
@ Import employee email addresses into All Subscribers with an "Active status

@ Ensure employees have opted in to the test email list or data extension

Q16) An email manager was anticipating a test email to arrive in their inbox. Where in Email Studio should the Marketing Cloud admin
look to determine if the test deployed?

@ My Reports > Administrator Reports > Email Sends By User

Explanation:-Link - https://help.salesforce.com/articleView?id=mc_re_email_studio_reports.htm&type=5
@ @ My Tracking > Test Send Emails

@ My Tracking > A/B Testing

Q17) NTO has been noting reduced deliverability when they do large sends. Which part of deliverability is tied to hitting Spam Traps
during a send?

@ Content

@ @ List Hygiene
@ Engagement
@ Authentication

Q18) Northern Trail Outfitters (NTO) only has enough licenses for their staff. A campaign manager is out on parental leave. How should
NTO create a new user to fill in?

@ @ Disable the campaign manager's user and create a new user

@ Delete the campaign manager's user and create a new user

@ Transfer the campaign manager's permissions to a new user

@ Deactivate the campaign manager's license and assign it to the new user

Q19) Northern Trail Outfitters (NTO) hired a new Marketing Cloud admin, who was told all emails come from info@email.nto.com. the
previous admin did not leave any documentation. Which aspects would confirm a Sender Authentication Package (SAP) has been set
up on the account? 2 answers.

@ users receive Marketing Cloud password reset emails from help@email nto.com

@ The login page for Marketing Cloud Users is login.email.nto.com and is branded with NTO colors
g ea Upon receiving an email, all tracked links start with click.email.nto.com

@ @ Cloudpages personalized URLs are served from cloud.email.nto.com

Q20) A Marketing Cloud admin wants to configure a new keyword for an upcoming SMS campaign. After entering the desired keyword
CELEBRATION, the admin notices the keyword is unavailable. What issue could the admin be facing?

@ Keyword has too many characters

@ @ Keyword is used within another business unit
@ Keyword is a reserved word

@ Keyword fails to meet content standards

Q21) Marketing Cloud admin is asked to determine the total number of emails sent across all of their business units in the last calendar
year. Where would the admin retrieve this information?

@ @ Analytics Builder > Reports > Email Send Report
@ Email Studio > Email > Tracking > Sends

@ Contact Builder > All Contacts > Email

@ Studio > Email > Subscribers > All Subscribers

Q22) Northern Trail Outfitters is migrating from a small, in-house email solution to Marketing Cloud. What should the Marketing Cloud
admin consider when sending from the new IP Address?

@ the new IP Address is now in use.

@ Migration of larger marketing campaigns is necessary prior to bringing on smaller, triggered campaigns.
@ @ Sending in large volumes will alert ISPs

@ Building desirable sending history and data will be variable based on list size and engagement.

@ The IP address is on reserve, is already in use, and has an email sending history.

Q23) Security and legal teams determine subscriber data available to EMEA teams should NOT be available to AMER teams.
How could the Marketing Cloud admin ensure distinct data integrity across the regions?

@ Deploy separate Publication Lists for each region within one account
@ @ Separate regions into business units and apply Subscriber Filters
@ Deploy Multi-Org with a single Marketing Cloud Account

@ Filter data view permissions at the subscriber level

Q24) Northern Trail Outfitters (NTO) keeps their subscribers in sync with their external database via the import of a CSV file which is
dropped to the of Marketing Cloud SFTP each day. However, NTO has realized the number of subscribers being sent emails is
considerably lower than the number they were expecting based on records in their database. Which feature would allow NTO to monitor
whether all records were added to the target data structure each day?

@ External Key within the Import File Activity

@ RuntimeError within the File Drop Automation

@ Run Completion within the File Drop Automation

@ @ Notification Settings within the Import File Activity

Q25) Northern Trail Outfitters placed an encrypted file on their Marketing Cloud SFTP for import into a data extension. They are using a
file transfer Activity to decrypt the file. What would the decrypted data be after the File Transfer Activity completes?

@ Target Data Extension
@ Selected SFTP folder
@ @ Safehouse

@ Original SFTP folder

Q26) What is Setup Assistant?

@ Support service allowing the outsourcing of repetitive admin tasks
@ A dashboard containing key metrics for the business unit

@ Asearch within Help and Training limited to configuration documents
@@BA prioritized account configuration checklist

Q27) A user asks a Marketing Cloud admin to review their permissions since they are unable to send an email. The admin reviews the
user profile and notices the user has three roles assigned: Content Creator, Data Manager, and Marketing Cloud Viewer.
What should the admin do to resolve the issue so the user can send an email?

@ @ Remove the Marketing Cloud Viewer Role

@ Edit permissions and Grant permissions to Send

@ Add the Role Marketing Cloud Channel Manager

@ Edit permissions and deselect Deny for Email Sending!

Q28) Which three options determine when a contact could enter a journey? Choose 3 answers.

@ @ Re-entry at any time

@ Re-entry by date

@ @ No re-entry

@ @ Re-entry only after exiting

Q29) A Marketing Cloud admin is using the Import Wizard to import data into a non-sendable data extension, but receives an error
indicating the import type being used requires a primary key. Which import type could the admin use instead?

@ Add and Update
@ @ Ovemrite
@ Update Only

@ Add Only

Q30) Northern Trail Outfitters (NTO) has a franchise model which allows locally-owned stores to operate under the corporate umbrella.
They are required by corporate policy to email each franchisee a monthly statement, but the statement cannot be publicly accessible.
Which Marketing Cloud product should NTO purchase as a solution?

@ Email Rachments

@ @ Distributed Sending
@ Content Syndication

@ Analytics Builder

Q31) A Marketing Cloud admin has scheduled a query on a daily basis. They notice the query sometimes fails to execute. How would
the admin ensure a notification is received when the query fails?

@ @ Add their Email Address in the automation "Runtime Error or Skipped Run Notification Settings
@ Install the Marketing Cloud App on phone to receive Push Messages

@ Configure the "Event Notification Service" in Setup with their Email Address

@ Add their Email Address in the Query Activity Notifications Field

Q32) Northern Trail Outfitters installed Query Studio for Marketing Cloud, however, users are reporting they do NOT have access. How
should the Marketing Cloud admin ensure users have access?

@ @ License all appropriate users within the installed package
@ Install App-appropriate business units for expanded access
@ Configure the API Integration to allow all users access

@ Choose Public App Integration during the installation

Q33) A Marketing Cloud admin wants to create a suppression list for hard-bounced email addresses. Where could the details be found?

@ Runa Bounce Email Report

@ @ Query the Bounce Data View

@ Run an Account Send Summary Report
@ Query the Send Log

Q34) Northern Trail Outfitters (NTO) wants to limit who can receive Marketing Cloud tracking data via email from their Account to any
email associated with their domain (ntoretail.com). Which steps should be taken to implement this? Choose 2 answers

@ @ Add a Domain to the Export Email Whitelist
@ Edit the entity Verification Settings

@ @ Enforce Export Email Whitelist

@ Enable IP Whitelisting

Q35) Northern Trail Outfitters (NTO) is building a journey which randomly sends five different versions of an initial welcome email to
new subscriber however, subscribers receive the same follow-up email two weeks later. To improve maintainability of their email
content, NTO want to use 3 completely different emails, rather than having one email with dynamic content.

Which activity would allow NTO to build the journey with the fewest activities possible?

@ Einstein STO

@ Wait Until Date

@ @ Engagement Spiit
@ Join

Q36) NTO wants to copy journeys across business units. What could be used to replicate journey structure so it can be easily recreated
in another account?

@ Journey Extracts

@ Copy activities

@ Journey Templates

@ @ Deployment Manager

Q37) A user asks a Marketing Cloud admin to update and increase their session timeout setting. Which three considerations should the
admin review before making this update? Choose 3 answers.

@ @ Change impacts all users

@ @ Security risk of unauthorized users for longer timeout settings
@ @ Best practice suggests a 20-minute timeout setting

@ Typical length of time users spend in Marketing Cloud

Q38) Northern Trail Outfitters does NOT want to store email addresses or phone numbers within Marketing Cloud. Which feature should
they use?

@ Lookup reference to Contact Object
@ Field Level Encryption

@ @ Tokenized Sending

@ Master-detail relationship to Contacts

Q39) Northern Trail Outfitters is preparing to send a promotional email. The audience file was loaded into a data extension but does not
display for Marketing Cloud admin scheduling the send. What should the admin confirm to resolve the issue?

@ @ The data extension is marked as Sendable

@ The data extension is linked using the Contact Key

@ The Data extension is marked as Sendable and Testable
@ The data extension contains a Salesforce ID

Q40) A Marketing Cloud admin is tasked with overhauling the data model for Enterprise. While the current data model is isolated to the
email channel and there are plans to expand to both SMS and Push channels in the near future. Which three data preparations should
be made to retain high data quality in the new mode? Choose 3 answers.

@ @ Normalize data and fields to prevent redundancy.

@ @ Identify and assign appropriate keys to tie records together.
@ Ensure every data source has a sendable field

@ @ Remove nonessential data for marketing purposes.

Q41) Northern Trail Outfitters wants to set up their Send Log data extension. Which three considerations should be made for long term
success? Choose 3 answers

@ @ Log attribute data necessary for auditing communications
@ @ Apply an appropriately-scoped Data Retention period
@ Set the period to a fixed date in the Data Retention Policy
@ @ Add custom fields not included in the Send Log Template

Q42) A Marketing Cloud admin discovers large sends are not meeting send speed goals set by the organization. What functionality
would get messages out the door faster?

@ @ Burst Sending

@ Marketing Cloud Connect

@ Send Throttling

@ Journey Builder Triggered Sends

Q43) Northern Trail Outfitters wants to segment audiences based on Sales Cloud data. Where would their Marketing Cloud admin
configure Sales Cloud Objects to be synced and leveraged in Marketing Co.

@ @ Contact Builder > Data Sources

@ Contact Builder > Data Extensions > Synchronized Data Extensions
@ Setup >Data Management > Synchronized Data Extensions

@ Setup > Apps > Salesforce Integration

Q44) A Marketing Cloud admin is configuring Social Studio to manage Northern Trail Outfitters social media accounts. Which 2
prerequisites for configuring Social Studio should the admin consider? Choose 2 answers

@ @ Bitly URL Shortener

@ @ Login detail for each social media account
@ Google URL shortner

@ Facebook ad manager

Q45) What does Marketing Cloud authenticate when a user logs in through the user interface?

@ [If the user is assigned a role in the parent business unit
@ @ Ifthe user is logging in from a whitelisted IP address
@ If the user has login hours enabled on their profile

@ If the user is an API User on their record

Q46) Northern Trail Outfitters (NTO) is concerned about unauthorized API access to their Marketing Cloud account. Which feature
would NTO enable to assist in reducing threats from malicious API attacks?

@ Field Level Encryption

@ Advanced Audit Trail

@ @ IP Whitelisting

@ Single Sign on Authentication

Q47) Northern Trail Outfitters has five business units in their Marketing Cloud account. All business units should be configured to use
the same SFTP directory. How should this setup be achieved?

@ Each business unit should have multiple SFTP users

@ child business unit SFTP user should be created

@ @ Alichild business units should have an individual SFTP user
@ Copy the parent SFTP user into each child business unit

Q48) Northern Trail Outfitters (NTO) uses data extensions for all of their email audiences. A customer reports they unsubscribed
several week-end ago, but continue to receive NTO's daily digest at their old address. NTO's Marketing cloud Admin has confidently
deleted them from present in the appropriate data extension.

What consideration could account for this behavior?

@ The data extension was not configured as sendable.

@ Contact Builder was not configured properly.

@ @ Data retention settings were incorrect in the data extension.
@ The email address in All Subscribers is prioritized.

Q49) Northern Trail Outfitters has noticed an issue with their sends today. Which two links in Setup Home could be used to
troubleshoot the issue? Choose 2 answers

@ Failed Sends

@ @ Help and Training
@ @ system Status

@ Create Support Case

Q50) Northern Trail Outfitters wants to drive additional online sales. They are interested in using Einstein to recommend similar items
to customers during the checkout process.
Which two terms would they add to their website to accomplish this? Choose 2 answers.

@ Email Conversion Code
@ @ Collect Code

@ @ Recommendation Code
@ Conversion/Cart Code

Q51) A Marketing Cloud admin notices Individual Email Results are NOT being pushed back into Sales Cloud for a particular end. The
admin of Marketing Cloud Connect is functioning properly. What should the admin confirm about the data extension?

@ The triggeredSendDataExtension data extension template was used.

@ The data extension is located in the Synchronized Data Extensions folder.
@ The wind relationship links Subscriber Key to Subscribers on Email Address
g ea The data extension is located in the Salesforce Data Extensions folder.

@52) A Marketing Cloud admin is asked to append an Urchin Tracking Module (UTM) variable string to links in emails. What
functionality would allow this?

@ @ Web Analytics Connector
@ Web and Mobile Analytics

@ Advertising Studio

@ Personalization Builder

Q53) A Marketing Cloud Administrator noticed a File Drop Automation has been falling on the Import File activity. The automation is
configured with a filename pattern, so the filename is expected to begin with customer import_. The import is configured to look for a
file named Customer import %%Year%%%% Month%%%%Day%%.csv, however, the admin notices the filenames Include seconds and
milliseconds

what should the admin do to fix the issue?

@ @ Use %%FILENAME_FROM_TRIGGER%% in the Import File Activity.
@ Use the exact file name used for the trigger in the Import File Activity.

@ Make sure the team has a date stamp to avoid duplication.

@ Make sure the files placed on the correct sub-folder within the SFTP.

Q54) While setting up Marketing Cloud Connect, a Marketing Cloud admin navigates to the Marketing Cloud tab in Sales Cloud to
complete the integration. The admin then receives the following error message:

- Insufficient User Permissions. You have not been designated as an integrated Marketing Cloud user. Contact your system
administrator.

The admin notices the Marketing Cloud for AppExchange Admin option is selected when looking at the user settings. What action
should correct the issue?

ee Apply the administrator and Marketing Cloud Administrator permission sets to user
@ Apply the appropriate user mappings in the CRM configuration

@ Reset al passwords to force new tokens

@ Apply the Marketing Cloud for AppExchange User option as well

Q55) Northern Trail Outfitters (NTO) wants a business analyst to import contact lists. The analyst has the follow Cloud Channel
Manager and Marketing Cloud Viewer. The Analyst logged in but is unable to import contacts. How should NTO update the user to allow
the analyst the appropriate access?

@ Add Distributed Sending User

@ Add Marketing Cloud Security Administrator
@ @ Remove Marketing Cloud Viewer

@ Remove Marketing Cloud Channel Manager

Q56) A Marketing Cloud admin is tasked with requesting Marketing Cloud Connect Multi-Org enablement. What consideration should be
given to the preference profile centers for this integration?

@ Profile/Preference centers are automatically created for each business unit connected through Multi-org
@ @ Multi org does not support the standard profile preference center for the business units.

@ Branding for each business units� profile centers will be inherited from the default business unit setup.
@ Profile/Preference centers for Multi-Org accounts are configured in the Salesforce CRM settings.

Q57) Where would a Marketing Cloud admin view all verified email addresses?

@ Reply Mail Management

@ Identity Verification Log

@ Sender Profiles

@ @ From Address Management

Q58) A Marketing Cloud admin is asked to add a set of four tracking parameters automatically to all the links in an email sent via email
studio. Which solution should the admin suggest?

@ AMPscript for Marketing Cloud
@ Google Analytics 360

@ Marketing Cloud Connect

@ @ Web Analytics Connector

Q59) A MC admin wants to sync Contacts from Sales Cloud, but is concerned about the number of Contacts since not all the contacts
will be sent an email.
What should the admin do to ensure only specific Contacts are synced?

@ Filter existing records in All Subscribers

@ Filter records on a formula field

@ @ Filter records on a Boolean field

@ Filter records created after a specified date

Q60) Northern Trail Outfitters uses Marketing Cloud Connect to leverage Sales Cloud data in their journeys. a user recently reported the
data coming from Sales Cloud is NOT up to date. Where should the Marketing Cloud admin begin troubleshooting?

@ @ Contact Builder > Data Sources

@ Email Studio > Synchronized Data Extensions
@ Contact Builder > Synchronized Data Extensions
@ Automation Studio > File Transfers

Q61) Northern Trail Outfitters (NTO) has the Discover Reporting Tool. Which two report types could help NTO drive their mobile
adoption strategy? Choose 2 answers.

@ @ Email Sending Performance Report
@ Deliverability Complaint Rate

@ @ Email Performance by Device

@ Time Between Send and Engagement
Answer Sheet

Q1) Which statements are true about Marketing Cloud and Marketing Cloud Connect when using Non-Scope by User configuration?
(choose 3)

@ @ Within the Marketing Cloud, returned subscribers are not limited to what is visible to the user initiating the send.
@ Within the Marketing Cloud, report or campaign lists are limited to only what is visible to the user initiating the send.
@ @ Password policies are not in effect, making this configuration easy to maintain because passwords do not expire.
@ @ Anaadministrator can set up a user without entering a password.

@ Users are always prevented from sending to report or campaign members who are not visible to them without notice.

Q2)

With non-scope by user accounts, imports return results based on the Salesforce system user's data access. With scope by user
accounts, all automated import activities are executed as the Marketing Cloud API user, and the number of records reflect the
Salesforce system user's level of access to data.

Manual import activities respect scoping, so the number of records that appear in the report are specific to the user who is running the
import.

@ Incorrect

@ @ Correct

Q3) All Contacts functions across Studios/Channels at a Business Unit level.

@ Correct

Explanation:-Sometimes accounts with business units can't access all contacts. Some contact records can overlap in business units, but other contacts
can remain available only to a particular business unit. Link - https://help.salesforce.com/article View?
id=mc_cab_contact_definition_and_count_determination.htm&type=5

@ @ incorrect

@Q4) Which of the following are all reasons to know your Marketing Cloud instance? (choose 3)

@ @ The instance helps you use the release schedule to predict when new features are released to your account.
@ The instance identifies the top-level parent in your Enterprise account.

@ @ The instance helps you monitor any performance concerns on the Salesforce Trust site.

@ @ The instance is needed to configure the Web Collect URL, SOAP Web Services API, and more.

@ The instance determines priority in sending on each Marketing Cloud server.

Q5) Why is whitelisting the entire set of IP ranges for your region a best practice?

@ It minimizes the use of verification codes required for logins, saving time for users and administrators.

@ @ It avoids unintended service disruptions due to movement between primary and secondary instances.
Explanation:-

Refer: https://help.salesforce.com/articleView?id=000321501 &language=en_US&type=1&mode=1

@ It allows users to access Marketing Cloud regardless of their work location without extra authentication.

@ @ It ensures Salesforce login pools can process end users� login authentication when accessing Salesforce.

Q6) Individual users can change the Time Zone and Date Format for their own accounts in their Settings.

@ Incorrect

@ @ Correct

Q7) The default Email Display Name and Email Reply To Address for email sends in your Marketing Cloud account should be selected
carefully, as they may be used for sending.

@ Incorrect

@ @ Correct

Q8) The default Email Display Name and Email Reply To Address are configured by the administrator in:

@ Marketing Cloud Settings
@ Default Sender Profile
@ @ Account Settings

@ General Settings

Q9) Contact configuration is tied to an individual Business Unit.

@ Incorrect

@ @ Correct

Q10) All Subscribers are Contacts but not all Contacts are Subscribers

@ Incorrect

@ @ Correct

Q11) Lightning Experience is supported for Marketing Cloud Connect features.

@ @ incorrect
@ Correct

Q12) Marketing Cloud Connect requires a relationship between a single Marketing Cloud account and only one Salesforce org.

@ @ Incorrect
@ Correct

Q13) It is recommended that you use a dedicated system user as the Salesforce System User, which does consume a user license.

@ Incorrect

@ @ Correct

Q14) The Marketing Cloud Connect API user is typically a shared user.

@ @ incorrect
@ Correct

Q15) If a Sales or Service Cloud org is connected to a Marketing Cloud Enterprise 2.0 account, the Marketing Cloud Connect API user's
Business Unit access in the Marketing Cloud determines which Business Units are available for use within the Sales or Service Cloud.

@ Incorrect

@ @ Correct

Q16) You must manually manage the linking of disparate IDs for Contact Visualizer to function across Studios/Builders; Marketing
Cloud does not do this automatically.

@ Incorrect

@ @ Correct

Q17) Developers creating Android apps for use with MobilePush must whitelist regional IP addresses in their Google API Key
Configuration IP Whitelist.

@ Incorrect

@ @ Correct

Q18) When modifying the Lead/Contact Page Layouts in CRM for Marketing Cloud connect, add: (choose 3)

@ @ Email Sends

@ @ Lead/ContactActions
@ @ Individual Email Results
@ Email Tracking

@ Marketing Cloud Sends

Q19) The choices you make for Tracking setup in Marketing Cloud Connect can affect the overall storage of your CRM org.

@ Incorrect

@ @ Correct

Q20) Benefits to Distributed Marketing? (pick 3)

@ Allow for nightly reporting on tracking and ROI.

g e Let business users focus on customer relationships.
@ @ Customize messages quickly and intuitively.

@ Allow Sales to manually import customers into journeys.
@ @ Maintain brand consistency and compliance.

Q21) If you don't log out of active Marketing Cloud sessions when configuring Distributed Marketing, Salesforce automatically
authenticates against an active session.

@ Incorrect

@ @ Correct

Q22) After a Business User sends a message using Distributed Marketing, Distributed Marketing adds the contact or lead to the
appropriate data extension along with data from the contact or lead, such as unique identifier (ContactID or LeadID), email address, and
the user ID of the user who pressed Send.

@ Incorrect

@ @ Correct

Q23) Campaign Marketplace in Distributed Marketing allows you to create and share collections�or marketplaces�of campaigns
based on common categories, themes, and intentions.

@ Incorrect

@ @ Correct

Q24) Whitelist the following domains, if you have policies to whitelist only MC domains: (choose 3)

@ @ *.marketingcloudapps.com
@ Code.marketingcloud.com
@ @ Bounce.exacttarget.com
@ @ Exacttarget.com

@ Help.marketingcloud.com

Q25) IP Addresses for the following use cases are not instance-specific and should be whitelisted for any tenant: (choose 5)

@ @ sone APi Calis

@ @ Device Integrations

@ @ RESTAPI Calls

@ Authenticated Sending

@ @ Authentication API Calls
@ @ FIP integrations

Q26) Domain Verification protects your brand reputation by making sure From addresses used in send emails are approved and
provides assurance that you send messages from confirmed addresses.

@ Incorrect

@ @ Correct

Q27) You can import and verify (Bulk Upload) multiple From address in From Address Management in individual accounts.

@ Incorrect

@ @ Correct

Q28) You can use Distributed Marketing if you use custom objects to track individual records.

@ @ Incorrect
@ Correct

Q29) Requirements for Distributed Marketing: (choose 3)

@ Salesforce Pardot with Engage License

@ @ Salesforce Connect with the ability to connect to one external data source

@ @ Salesforce Sales Cloud, Service Cloud, Financial Services Cloud (FSC), or Community Cloud (Partner Community License or Login, only)
@ @ Salesforce Marketing Cloud with Journey Builder

@ Available Marketing Cloud licenses for every Sales user of Distributed Marketing

Q30) A Marketing Cloud license is required for every Distributed Marketing user.

@ @ Incorrect
@ Correct

Q31) Distributed Marketing can be used with Enterprise 1.0 and 2.0 editions of Marketing Cloud.

@ @ incorrect
@ Correct

Q32) To use Distributed Marketing, each business unit requires a unique Marketing Cloud user (a system user), where the business unit
you want to connect is the default business unit of the system user.

@ Incorrect

@ @ Correct

Q33) Distributed Marketing requires Lightning.

@ Incorrect

@ @ Correct

Q34) All Marketing Cloud accounts use a pool of IP Addresses that vary depending upon send volume by default. All administrators
should therefore whitelist the ranges of IPs for the stack their instance resides in.

@ @ Correct

Explanation:-Assign a unique IP address to your account and manage your own sending reputation in Marketing Cloud Email Studio. When your send
volume is high enough that your sending reputation is hard to control in a shared IP pool, investigate using a dedicated IP address. Link -
https://help.salesforce.com/articleView?id=mc_es_dedicated_ip.htm&type=5

@ Incorrect

Q35) Where do you navigate in Setup to create users?

@ @ Users
@ Role Setup
@ Role

@ User Setup

Q36) Business units are used to:

@ @ Control access to information and sharing of information throughout Marketing Cloud.
@ Ensure that content can be modified by all Marketing Cloud users.

@ Track the total number of businesses you send emails to.

@ None of these

Q37) What should you do before creating business units?

@ Delete your users.

@ Rename your folders.

@ @ Map your organizational structure for business units.
@ Send a test email from Marketing Cloud.

Q38) Correct or Incorrect: A triggered send is when you choose a specific time and recipient for a message.

@ @ incorrect
@ Correct

Q39) Which statement best describes a contact and a subscriber?

@ Acontact is always a subscriber. A subscriber is always a contact.

@ Acontact is a person who opts in to receive communications through a specified channel. A subscriber is anyone you send messages to.

@ @ Acontactis a person you are going to send messages to. A subscriber opted to receive communications or belongs to a particular channel.
@ Acontact is a person who opts in to text messages. A subscriber is a person who opts in to email messages.

Q40) What is used by Salesforce to uniquely identify a contact throughout Marketing Cloud?

@ Contact Account Number

@ Contact Key

@ @ Contact ID

Explanation:-Contact ID is a unique number for your contacts in Salesforce Marketing Cloud. This number helps uniquely identifying the contact on the
back-end system. This is an application level number thru the entire Marketing Cloud system.

@ Subscriber ID

@ Subscriber Key

Q41) Which Contact Builder tool is used to define, organize, and relate information about a contact within an account?

@ Journey Builder
@ @ Data Designer
@ Email Studio

@ Data Extension
@ Population

42) Which type of data source connects two different contact data tables to each other based on a particular field?

@ Population

@ Synchronized Data Extension
@ @ Attribute Group

@ Data Designer

@ Contact Key

@Q43) Correct or Incorrect: Contact Delete requests remove contact information from sendable data extensions only and does not affect
data in other data extensions.

@ Incorrect

@ @ Correct

Q44) Which of these data sources does not contain contact information?

@ @ Email Header and Footer Rules
@ Filters

@ Queries

@ Data extensions

Answer Sheet

Q1) Distributed Marketing supports sending from both - journeys and individual channels, like selecting and sending a single Content
Builder email.

@ @ incorrect

Explanation:-All messages in Distributed Marketing are sent using Marketing Cloud�s Journey Builder. Link - https://help.salesforce.com/articleView?
id=mc_dm_create_marketing_cloud_journey.htm&type=5

@ Correct

Q2) It is recommended that you install the Distributed Marketing Package for admins only or for specific profiles so that you are
installing for licensed users only.

@ @ Correct

Explanation:-Access to Distributed Marketing is controlled through custom permissions and permission set licenses. You can assign the custom
permissions in your Salesforce org using installed permission sets or using your own custom permission sets or profiles. The permission set licenses are
provisioned in your account and can be assigned using installed permission sets. refer - https://trailhead.salesforce.com/content/learn/modules/distributed-
marketing-administration/install-configure-distributed-marketing

@ Incorrect

Q3) The DMAdministrator Permission Set contains everything included in DMStandard plus Visualforce pages for Distributed Marketing
administration.

@ Incorrect

@ @ Correct

Q4) Distributed Marketing Approvers need a license.

@ @ incorrect

@ Correct

Q5) Places to verify From addresses in MC: (choose 4)

@ @ From Address Management
@ Delivery Profiles
@ @ Sender Profiles

@ @ My Users
@ @ Account Settings
@ Company Information

Q6) You can choose to honor an Opt-Out List in all types of Marketing Cloud Transactional email sends.

@ @ incorrect

@ Correct

Q7) The default sender profile and delivery profile name and external key cannot be updated or deleted.

@ Incorrect

@ @ Correct

Q8) You must choose Account Default for the footer, or Marketing Cloud cannot include the required elements, such as unsubscribe
link and physical mailing address, in the email.

@ @ incorrect

@ Correct

Q9) You can customize the time zone and date format for individual business units.

@ Incorrect

@ @ Correct

Q10) Messages Marketing Cloud Supports from within the platform are: (choose five)

@ @ In-app inboxes
@ @ Push
@@sms

@ Twitter

@ @ Email
@ @ Line Group Messages

Q11) Recommended setting for Send Password Change Confirmation Email?

@ Disable
@ @ Enable

Q12) Recommended setting for Enforce Export Email Whitelist?

@ Disable
@ @ Enable

Q13) Recommended setting for Enable Audit Logging Data Collection?

@ Disable
@ @ Enable

Q14) An explicitly denied permission always overrides all other permissions.

@ Incorrect

@ @ Correct

Q15) When a permission is not explicitly granted or denied, Marketing Cloud defaults to grant permission unless another role denies
that permission.

@ @ incorrect
@ Correct

Q16)
Single Sign-On best practice is to test your SAML enablement on one business unit before enabling others on your account.

You can better resolve any configuration issues or errors when dealing with a business unit.

@ @ Incorrect
@ Correct

Q17) Business units are available in Enterprise 2.0 and 1.0 tenants.

@ @ Incorrect

@ Correct

Q18) Available unsubscribe settings for Business Units are unsubscribe a person from only the business unit or from all business units
within the enterprise account.

@ @ Correct
Explanation:-https://help.salesforce.com/article View?id=mc_es_unsubscribe_settings.htm&type=5
@ Incorrect

Q19) identifies a contact within an account and ties together the contact, channels, and the relationship.

@ Subscriber Key
@ Contact ID
@ @ Contact Key

Q20) The is the same no matter what channel is used to send messages.

@ Subscriber Key
@ Contact ID
@ @ Contact Key

Q21) Preview and Test provides the ability to: (choose 3)

@ @ Validate AMPscript or other programmatic languages

@ @ See how personalization displays for subscribers

@ Send a sample email to a subset of your audience to test performance.
@ Test different content versions with your audience.

@ @ View how the email appears in your own email client.

Q22)A lives in the individual studios.
@ @ Subscriber
@ Contact

Q23) A contact appears in the section.

@ All Subscribers
@ @ AI Contacts

Q24)A is a person you send messages to through any marketing channel.

@ Subscriber
@ @ Contact

Q25) Which statement is Correct?

@ All subscribers are contacts, and all contacts are subscribers.
@ @ Alisubscribers are contacts, but not all contacts are subscribers.

Q26) You can have contacts whom you've never sent to who don't appear in All Contacts.

@ Incorrect

@ @ Correct

Q27) Data in Email Studio shows up in Contact Builder, but data in Contact Builder does not show up in Email Studio.

@ Incorrect

@ @ Correct

Q28) A subscriber in Email Studio will appear in Contact Builder under the All Contacts section, and a contact in Contact Builder will
automatically appear in Email Studio.

@ @ incorrect

@ Correct

Q29) Data that passes the retention limits will be permanently deleted.

@ Incorrect

@ @ Correct

Q30) Which is NOT a Data Retention delete option:

@ All Records and Data Extensions
@ All Records

@ Individual Records

@ @ Data Extensions

Q31) The is what allows you to connect contacts in multiple channels.

@ Subscriber Key
@ Contact ID
@ @ Contact Key

Q32) In Mobile Studio, contacts are identified on , which becomes the Contact Key in Contact Builder.

@ Contact Key
Explanation:-https://trailhead.salesforce.com/content/learn/modules/marketing-cloud-contact-management/understand-contacts-and-contact-model-
relationships

@ Contact ID

@ @ Subscriber Key

Q33) allows you to maintain multiple sets of subscriber attributes for a single email address.

@ @ Subscriber Key
@ Contact ID
@ Contact Key

Q34) Link attribute groups and populations using the value.

@ Subscriber Key
@ Contact ID

@ @ Contact Key

Q35) allows you to include a single email address multiple times on a list.

@ @ Subscriber Key
@ Contact ID
@ Contact Key

Q36) must be present in every sendable data extension.

@ @ Subscriber Key
@ Contact ID
@ Contact Key

Q37) Which Social Studio component do you use to start conversations in social accounts?

@ Analyze
@ Engage
@ @ Publish

@ Einstein

Q38) What can you do in with workplace calendars?

@ @ Schedule and design content
@ Create user roles

@ Add social accounts

@ Add workspace members

Q39) Correct or Incorrect: User roles control permissions at the workspace level.

@ @ incorrect
@ Correct

Q40) It's best to save populations for specific use cases where you need to create complex queries, such as if your account uses field-
level encryption or when you're using API Entry Sources in Journey Builder.

@ Incorrect

@ @ Correct

Q41) You configure the retention policy settings when creating the data extension.

@ Incorrect

@ @ Correct

Q42) Which deliverability best practice helps you build a positive sending reputation with ISPs?

@ Content Detective
@ Text Versions

@ @ IP Warming
@ Subscriber Preview

Q43) What Marketing Cloud feature can you use to view data from an individual send?

@ Reports
@ Email Trends
@ Data Trends

@ @ Tracking

Q44) What are some options for exporting reports? (Choose 2)

@ None of these
@ sms

@ @FiP

@ @ Email

Q45) When you build an email send in Salesforce CRM, which field is required before you can click Send?

@ The Dedupe subscribers checkbox
@ Disable Individual Level Tracking

@ The exclusions list

@ @ The opt-in certification checkbox

Q46) What does Marketing Cloud Connect do?

@ Itis a set of tools for designing email templates.

@ It connects Marketing Cloud Email Studio and Journey Builder.

@ It allows your Marketing Cloud users to connect with your customers' social media accounts.
@ @itisan integration that connects Salesforce Marketing Cloud and CRM environments.

Q47) Where are shared data extensions stored?

@ Ina shared extension folder in the Data Sources tab.

@ Ina shared extension folder in the Imports tab.

@ @ Ina shared extension folder in the Data Extensions tab.
@ Ina shared folder in the Poll Schedule tab.

Q48) Which of the following statements applies to retention settings?

@ @ You cannot remove the configured data retention settings once you configure them.
@ You cannot modify the deletion period for existing data extension.

@ You cannot select a specific date to delete the data in the extension.

@ You cannot set the sharing window.

@ You cannot delete all records and the entire data extension.

Q49) Correct or Incorrect: You don't need to enable Contact Delete for use in Marketing Cloud.

@ @ incorrect
@ Correct

Q50) What is the Marketing Cloud Connected App Permission Set used for?

@ To relax IP address restrictions for the Salesforce System User

@ @ To grant Salesforce CRM access to users connecting from Marketing Cloud
@ To grant permission to the Managed Package

@ To authorize users connecting to Marketing Cloud from Salesforce CRM

Q51) When you configure the connected app settings in Salesforce CRM, which settings do you update?

@ IP Relaxation, Start URL, High-assurance session required
@ Start URL, Enable Single Logout, Refresh Token Policy

@ Permitted Users, Start URL, Timeout Value

@ @ Permitted Users, IP Relaxation, Refresh Token Policy

Q52) When testing Marketing Cloud Connect, why is it important to build a report that sends email only to a single test recipient?

@ @ The test send generates real emails, and it's important not to send unexpected messages to users or customers.
@ Marketing Cloud Connect can only use reports for the recipient list.

@ With just a single result, the test completes quickly.

@ Marketing Cloud Connect allows for sending only to a single recipient from within the CRM org.

Q53) What status indicates the number of delete requests that successfully processed?

@ @ Complete

@ Processing
@ Total
@ Invalid

Q54) Correct or Incorrect: You can delete a contact using only a ContactTypelD value.

@ @ incorrect
@ Correct

Q55) How do journeys help business users connect with customers? (Choose 2)

@ None of these

@ They keep messages generic, because messages don't need to be personalized.

ee They let business users focus on customer relationships.

@ @ They maintain brand consistency by creating on-brand, marketing-approved journeys in Marketing Cloud.

Q56) Which clouds are required for using Distributed Marketing?

[v) e Marketing Cloud plus: Sales Cloud or Service Cloud or Financial Services Cloud (FSC) or Community Cloud (with the Partner Community license)
@ Marketing Cloud plus: Service Cloud or Commerce Cloud or Sales Cloud or Community Cloud (with the Partner Community license)

@ Service Cloud plus: Marketing Cloud or Sales Cloud or Commerce Cloud or Financial Services Cloud (FSC)

@ Sales Cloud plus: Marketing Cloud or Service Cloud or Government Cloud or Financial Service Cloud (FSC)

Q57) How can you find the installation link for the Distributed Marketing managed package?

@ Log a support case with Salesforce.

@ @ Navigate to the Install Managed Package page on Salesforce Help.
@ Look for the link in an email from Salesforce.

@ You don't need to install a managed package for Distributed Marketing.
Answer Sheet

Q1) What is the recommended security setting for session timeout?

@ 2days
@ 1 hour

@ @ 20 minutes
@ Never

Q2) How can you locate your MID? (Choose 2)

@ @ In Account Settings under Setup
@ @ Next to your username

@ In Setup under MID

@ None of these

Q3) Which of the following statements is true about deleting contacts?

@ Itis best to move unengaged subscribers to a separate synchronized population group.

@ Itis best to delete unengaged subscribers in order to reduce cost.

@ @ Itis best to unsubscribe unengaged contacts from individual channels rather than delete them.
@ It is best to move unengaged subscribers to a synchronized data extension.

@Q4) What should you create to synchronize objects from Service Cloud, pull the information into Marketing Cloud, and share contact
data with business units?

@ Create a synchronized attribute group in Marketing Cloud and link the objects to Service Cloud.
@ Create a synchronized population group in Service Cloud and link the objects to Marketing Cloud.
@ @ Create a synchronized data extension.

@ Create a synchronized data source with the sharing window set to outside the business unit.

@ Create a synchronized attribute group.

Q5) What do you use to synchronize Sales Cloud and Service Cloud data with Marketing Cloud?

@ Journey Builder

@ Data Designer

@ Contact Builder

@ @ Marketing Cloud Connect
@ Email Studio

Q6) What value do you need to review the status of a Contact Delete request?

@ Status

@ @ OperationID
@ ContactKey
@ Partnerkey

Q7) Where do contact deletions take place in Enterprise 2.0 accounts?

@ @ Top-level accounts and all business units in the specified Enterprise 2.0 account.
@ Aspecified group of business units

@ Just the top-level business unit

@ All Enterprise 2.0 accounts and business units you manage

Q8) Correct or Incorrect: Delete requests take precedence over all other account activities.

@ @ incorrect
@ Correct

Q9) Which page has links to help you check the health of your Marketing Cloud instance?

@ Database page
@ Compliance page
@ @ Status page
@ Security page

Q10) Which page contains best practices for keeping your Marketing Cloud instance secure?

@ Trust page

@ @ Security page
@ Compliance page
@ Status page

Q11) Which of the following can you use to locate your Marketing Cloud database?

@ Node ID

@ @ Marketing Cloud ID (MID)
@ OrgID

@ Database ID

Q12) Correct or Incorrect: You can receive notifications about the status of your Marketing Cloud instance via email.

@ Incorrect

@ @ Correct

Q13) Which of the following are features of Marketing Cloud Connect?

ee Marketing Cloud users can use data and events from Salesforce CRM in Journey Builder.
@ Service Cloud users can send push notifications directly to contacts from a case detail screen.
@ @ CRM users can see email tracking data on the contact record.

@ None of these

Q14) Which Salesforce CRM Edition supports Marketing Cloud Connect?

@ @ Enterprise Edition
@ Professional Edition
@ Essentials Edition

@ None of these

Q15) Before installing the managed package, what CRM feature needs to be verified?

@ Record types on the contact and lead objects
@ Person accounts

@ Default workflow user

@ @ Platform events

@ Multicurrency

Q16) Why is it important to set up a Salesforce System User?

@ The system user is the only one who can customize Marketing Cloud Connect.
@ The CRM org can't function without a system user.

@ @ This user record connects Marketing Cloud to the CRM org.

@ The Salesforce admin doesn't have privileges that the system user does.

Q17) Before you create the Marketing Cloud API user, what do you do?

@ @ Configure the connected app settings in Salesforce CRM.
@ Create field mapping.

@ Connect to Marketing Cloud within Salesforce CRM.

@ Set up your CRM Sales Cloud end user.

Q18) Who can add social accounts to a workspace?

@ @ Super User

@ Workspace contributor
@ @ Workspace admin
@ None of these

Q19) A workspace consists of what blocks?

@ Keywords
@ @ Topic profiles
@ @ Users

@ None of these

Q20) Correct or Incorrect: You need to be a workspace admin to add workspace users.

@ Incorrect

@ @ Correct

Q21) What is a topic profile?

@ Agroup of related words.

@ A dashboard of social media posts.

@ Company information shared on social medi

[v] [3] Asocial media search composed of keywords and filters.

Q22) Correct or Incorrect: You can customize keyword groups using logic operators.

@ Incorrect

@ @ Correct

Q23) Which statement best describes sentiment tuning?

@ Targeting a specific social audience

@ @The process of listening to your audience to understand how they feel about your brand, competitors, or industry
@ Using emojis in social posts

@ Singing about your feelings

Q24) Correct or Incorrect: Transparent Data Encryption prevents unauthorized data access, even if somebody has physical possession
of the encrypted drive.

@ Incorrect

@ @ Correct

Q25) What does Identity Verification use to verify your browser or app?

@ Carrier pigeon
@ SMS message
@ Phone call

@ @ Email

Q26) Which keys require you to upload a certificate?

@@ssH

@ Symmetric

@ @ Asymmetric
@ None of these

Q27) What activity uses salt keys?

@ @ WT use with Journey Builder
@ Text encryption

@ File transfer

@ SSO authentication

Q28) How can you obtain SSL certificates for use with Marketing Cloud?

@ @ Have Marketing Cloud purchase them for you

@ @ Buy them yourself
@ Upload from your library
@ None of these

Q29) Correct or Incorrect: You should pass SubscriberKey values in the clear.

@ @ Incorrect
@ Correct

Q30) Correct or Incorrect: You should store credit card numbers in Marketing Cloud.

@ @ Incorrect
@ Correct

Q31) Where should you store refresh token values?

@ Thumb drive

@ @ Your own server
@ Marketing Cloud

@ Triplicate forms

Q32) What percentage is a good goal for sentiment agreement?

@ 0.95
@ C079
@ 0.46
@ 0.25

Q33) What app do you use to authenticate a Marketing Cloud business unit with your Salesforce org?

@ Distributed Marketing Settings

@ Distributed Marketing Authentication
@ @ Distributed Marketing Administration
@ Distributed Marketing Security

Q34) Which step is part of setting up Distributed Marketing?

@ Add the Distributed Marketing component.
@ Create a recipient profile.

@ Map system attributes.

@ @ Create an entry event data extension.

Q35) What can you do with Quick Send?

@ Review and send a series of messages to individuals or groups of individuals.
@ @ Send a single message to an individual.

@ Create new campaign messages.

@ Display a list of messages you receive from Distributed Marketing users.

Q36) Where do you click Connect Campaign to associate a campaign with a journey?

@ In the Campaign Messages component on the lead or contact record
@ @ In the Campaign Messages component on the campaign record
@ In Journey Builder

@ In Email Studio

Q37) What do you create in Marketing Cloud to test the Distributed Marketing setup in Sales Cloud?

@ @ Anemail and a journey
@ Acampaign and a journey
@ Sender and recipient profiles
@ A journey and a contact

Q38) What's the passing score for the Marketing Cloud Administrator Certification exam?

@ 0.62
@ 0.65

@ 80.67
@07

Q39) The setup section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 0.14
@ 0.15
@ 0.19
@ CB 0.38

istrator Certification exam?

@40) Which objective is the most heavily weighted for the Marketing Cloud Admi

@ Channel management
@ Subscriber data management

@ @ Setup

@ Maintenance

Q41) The subscriber data management section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@01

@ 0.18
@ 02
@ 0.05

Q42) The subscriber data management section of the exam covers which key topics?

@ Integrations and data quality

@ @ Data quality and mail management
@ Business units and security

@ Marketing Cloud extension products

Q43) The maintenance section of the exam covers which key topics?

� Configuring integrations
@ Data quality and mail management

@ @ Data cleanup
@ Digital marketing compliance

Q44) The digital marketing section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 60.13
@ 0.15
@ 0.18
@ 0.35

Q45) The digital marketing section of the exam covers which key topic?

@ Data quality and mail management
@ Contact model

@ @ Product offerings

@ Advertising Studio configurations

Q46) The channel management section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 0.15

9 C016
@ 0.35
@ 0.38

Q47) The channel management section of the exam covers which key topics?

@ Product offerings

@ Data compliance

@ @ Configuration of Email Studio

@ Data filters, filter activities, and data extensions

Q48) The maintenance section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 01

@ C015
@ 02

@ 0.05
Answer Sheet

Q1) Where do you navigate in Setup to create users?

@ @ Users
@ Role Setup
@ Role

@ User Setup

Q2) Business units are used to:

@ @ Control access to information and sharing of information throughout Marketing Cloud.
@ Ensure that content can be modified by all Marketing Cloud users.

@ Track the total number of businesses you send emails to.

@ None of these

Q3) What should you do before creating business units?

@ Delete your users.

@ Rename your folders.

@ @ Map your organizational structure for business units.
@ Send a test email from Marketing Cloud.

Q4) Correct or Incorrect: A triggered send is when you choose a specific time and recipient for a message.

@ @ Incorrect
@ Correct

Q5) Which deliverability best practice helps you build a positive sending reputation with ISPs?

@ Content Detective
@ Text Versions

@ @ IP warming
@ Subscriber Preview

Q6) What Marketing Cloud feature can you use to view data from an individual send?

@ Reports

@ Email Trends
@ Data Trends
@ @ Tracking

Q7) What are some options for exporting reports? (Choose 2)

@ None of these
@ sms

@ @FiP

@ @ Email

Q8) What is the recommended security setting for session timeout?

@ 2days
@ 1 hour
@ @ 20 minutes

@ Never

Q9) How can you locate your MID? (Choose 2)

@ @ InAccount Settings under Setup
@ @ Next to your username

@ In Setup under MID

@ None of these
Answer Sheet

Q1) Which statement best describes a contact and a subscriber?

@ Acontact is always a subscriber. A subscriber is always a contact.

@ Acontact is a person who opts in to receive communications through a specified channel. A subscriber is anyone you send messages to.

@ @ Acontact is a person you are going to send messages to. A subscriber opted to receive communications or belongs to a particular channel.
@ Acontact is a person who opts in to text messages. A subscriber is a person who opts in to email messages.

Q2) What is used by Salesforce to uniquely identify a contact throughout Marketing Cloud?

@ Contact Account Number

@ Contact Key

@ @ Contact ID

Explanation:-Contact ID is a unique number for your contacts in Salesforce Marketing Cloud. This number helps uniquely identifying the contact on the
back-end system. This is an application level number thru the entire Marketing Cloud system.

@ Subscriber ID

@ Subscriber Key

Q3) Which Contact Builder tool is used to define, organize, and relate information about a contact within an account?

@ Journey Builder
@ @ Data Designer
@ Email Studio

@ Data Extension
@ Population

Q4) Which type of data source connects two different contact data tables to each other based on a particular field?

@ Population

@ Synchronized Data Extension
@ @ Attribute Group

@ Data Designer

@ Contact Key

Q5) Where are shared data extensions stored?

@ Ina shared extension folder in the Data Sources tab.

@ Ina shared extension folder in the Imports tab.

@ @ Ina shared extension folder in the Data Extensions tab.
@ Ina shared folder in the Poll Schedule tab.

Q6) Which of the following statements applies to retention settings?

@ @ You cannot remove the configured data retention settings once you configure them.
@ You cannot modify the deletion period for existing data extension.

@ You cannot select a specific date to delete the data in the extension.

@ You cannot set the sharing window.

@ You cannot delete all records and the entire data extension.

Q7) Which of the following statements is true about deleting contacts?

@ It is best to move unengaged subscribers to a separate synchronized population group.

@ Itis best to delete unengaged subscribers in order to reduce cost.

@ @ Itis best to unsubscribe unengaged contacts from individual channels rather than delete them.
@ It is best to move unengaged subscribers to a synchronized data extension.

Q8) What should you create to synchronize objects from Service Cloud, pull the information into Marketing Cloud, and share contact
data with business units?

@ Create a synchronized attribute group in Marketing Cloud and link the objects to Service Cloud.
@ Create a synchronized population group in Service Cloud and link the objects to Marketing Cloud.
@ @ Create a synchronized data extension.

@ Create a synchronized data source with the sharing window set to outside the business unit.

@ Create a synchronized attribute group.

Q9) What do you use to synchronize Sales Cloud and Service Cloud data with Marketing Cloud?

@ Journey Builder

@ Data Designer

@ Contact Bullder

@ @ Marketing Cloud Connect
@ Email Studio
Answer Sheet

Q1) Correct or Incorrect: Contact Delete requests remove contact information from sendable data extensions only and does not affect
data in other data extensions.

@ Incorrect

@ @ Correct

Q2) Which of these data sources does not contain contact information?

@ @ Email Header and Footer Rules
@ Filters

@ Queries

@ Data extensions

Q3) Correct or Incorrect: You don't need to enable Contact Delete for use in Marketing Cloud.

@ @ incorrect
@ Correct

Q4) What status indicates the number of delete requests that successfully processed?

@ @ Complete

@ Processing
@ Total
@ Invalid

Q5) Correct or Incorrect: You can delete a contact using only a ContactTypelD value.

@ @ Incorrect
@ Correct

Q6) What value do you need to review the status of a Contact Delete request?

@ Status

@ @ OperationID
@ ContactKey
@ PartnerKey

Q7) Where do contact deletions take place in Enterprise 2.0 accounts?

@ @ Top-level accounts and all business units in the specified Enterprise 2.0 account.
@ Aspecified group of business units

@ Just the top-level business unit

@ All Enterprise 2.0 accounts and business units you manage

Q8) Correct or Incorrect: Delete requests take precedence over all other account activities.

@ @ incorrect
@ Correct
Answer Sheet

Q1) Which page has links to help you check the health of your Marketing Cloud instance?

@ Database page
@ Compliance page
@ @ Status page
@ Security page

Q2) Which page contains best practices for keeping your Marketing Cloud instance secure?

@ Trust page

@ @ Security page
@ Compliance page
@ Status page

Q3) Which of the following can you use to locate your Marketing Cloud database?

@ Node ID

@ @ Marketing Cloud ID (MID)
@ OrgID

@ Database ID

Q4) Correct or Incorrect: You can receive notifications about the status of your Marketing Cloud instance via email.

@ Incorrect

@ @ Correct
Answer Sheet

Q1) What is the Marketing Cloud Connected App Permission Set used for?

@ To relax IP address restrictions for the Salesforce System User

@ @ To grant Salesforce CRM access to users connecting from Marketing Cloud
@ To grant permission to the Managed Package

@ To authorize users connecting to Marketing Cloud from Salesforce CRM

Q2) When you configure the connected app settings in Salesforce CRM, which settings do you update?

@ IP Relaxation, Start URL, High-assurance session required
@ Start URL, Enable Single Logout, Refresh Token Policy

@ Permitted Users, Start URL, Timeout Value

@ @ Permitted Users, IP Relaxation, Refresh Token Policy

Q3) When testing Marketing Cloud Connect, why is it important to build a report that sends email only to a single test recipient?

@ @ The test send generates real emails, and it's important not to send unexpected messages to users or customers.
@ Marketing Cloud Connect can only use reports for the recipient list.

@ With just a single result, the test completes quickly.

@ Marketing Cloud Connect allows for sending only to a single recipient from within the CRM org.

Q4) When you build an email send in Salesforce CRM, which field is required before you can click Send?

@ The Dedupe subscribers checkbox
@ Disable Individual Level Tracking

@ The exclusions list

@ @ The opt-in certification checkbox

Q5) What does Marketing Cloud Connect do?

@ It is a set of tools for designing email templates.

@ It connects Marketing Cloud Email Studio and Journey Builder.

@ It allows your Marketing Cloud users to connect with your customers' social media accounts.
@ @itisan integration that connects Salesforce Marketing Cloud and CRM environments.

Q6) Which of the following are features of Marketing Cloud Connect?

ee Marketing Cloud users can use data and events from Salesforce CRM in Journey Builder.
@ Service Cloud users can send push notifications directly to contacts from a case detail screen.
@ @cRM users can see email tracking data on the contact record.

@ None of these

Q7) Which Salesforce CRM Edition supports Marketing Cloud Connect?

@ @ Enterprise Edition
@ Professional Edition
@ Essentials Edition

@ None of these

Q8) Before installing the managed package, what CRM feature needs to be verified?

@ Record types on the contact and lead objects
@ Person accounts

@ Default workflow user

@ @ Platform events

@ Multicurrency

Q9) Why is it important to set up a Salesforce System User?

@ The system user is the only one who can customize Marketing Cloud Connect.
@ The CRM org can't function without a system user.

@ @ This user record connects Marketing Cloud to the CRM org.

@ The Salesforce admin doesn't have privileges that the system user does.

Q10) Before you create the Marketing Cloud API user, what do you do?

@ @ Configure the connected app settings in Salesforce CRM.
@ Create field mapping.

@ Connect to Marketing Cloud within Salesforce CRM.

@ Set up your CRM Sales Cloud end user.
Answer Sheet

Q1) Which Social Studio component do you use to start conversations in social accounts?

@ Analyze
@ Engage
@ @ Publish

@ Einstein

Q2) What can you do in with workplace calendars?

@ @ Schedule and design content
@ Create user roles

@ Add social accounts

@ Add workspace members

Q3) Correct or Incorrect: User roles control permissions at the workspace level.

@ @ incorrect

@ Correct

Q4) Who can add social accounts to a workspace?

@ @ Super User

@ Workspace contributor
@ @ Workspace admin
@ None of these

Q5) A workspace consists of what blocks?

@ Keywords
@ @ Topic profiles
@ @ Users

@ None of these

Q6) Correct or Incorrect: You need to be a workspace admin to add workspace users.

@ Incorrect

@ @ Correct

Q7) What is a topic profile?

@ A group of related words.

@ A dashboard of social media posts.

@ Company information shared on social medi

lv) (3) Asocial media search composed of keywords and filters.

Q8) Correct or Incorrect: You can customize keyword groups using logic operators.

@ Incorrect

@ @ Correct

Q9) Which statement best describes sentiment tuning?

@ Targeting a specific social audience

@ @The process of listening to your audience to understand how they feel about your brand, competitors, or industry
@ Using emojis in social posts

@ Singing about your feelings

Q10) What percentage is a good goal for sentiment agreement?

@ 0.95
@ C079
@ 0.46
@ 0.25
Answer Sheet

Q1) How do journeys help business users connect with customers? (Choose 2)

@ None of these

@ They keep messages generic, because messages don't need to be personalized.

ee They let business users focus on customer relationships.

@ @ They maintain brand consistency by creating on-brand, marketing-approved journeys in Marketing Cloud.

Q2) Which clouds are required for using Distributed Marketing?

@ @ Marketing Cloud plus: Sales Cloud or Service Cloud or Financial Services Cloud (FSC) or Community Cloud (with the Partner Community license)
@ Marketing Cloud plus: Service Cloud or Commerce Cloud or Sales Cloud or Community Cloud (with the Partner Community license)

@ Service Cloud plus: Marketing Cloud or Sales Cloud or Commerce Cloud or Financial Services Cloud (FSC)

@ Sales Cloud plus: Marketing Cloud or Service Cloud or Government Cloud or Financial Service Cloud (FSC)

Q3) How can you find the installation link for the Distributed Marketing managed package?

@ Log a support case with Salesforce.

@ @ Navigate to the Install Managed Package page on Salesforce Help.
@ Look for the link in an email from Salesforce.

@ You don't need to install a managed package for Distributed Marketing.

@Q4) What app do you use to authenticate a Marketing Cloud business unit with your Salesforce org?

@ Distributed Marketing Settings

@ Distributed Marketing Authentication
@ @ Distributed Marketing Administration
@ Distributed Marketing Security

Q5) Which step is part of setting up Distributed Marketing?

@ Add the Distributed Marketing component.
@ Create a recipient profile.

@ Map system attributes.

@ @ Create an entry event data extension.

Q6) What can you do with Quick Send?

@ Review and send a series of messages to individuals or groups of individuals.
@ @ Send a single message to an individual.

@ Create new campaign messages.

@ Display a list of messages you receive from Distributed Marketing users.

Q7) Where do you click Connect Campaign to associate a campaign with a journey?

@ In the Campaign Messages component on the lead or contact record
@ @ In the Campaign Messages component on the campaign record
@ In Journey Builder

@ In Email Studio

Q8) What do you create in Marketing Cloud to test the Distributed Marketing setup in Sales Cloud?

@ @ Anemail and a journey
@ Acampaign and a journey
@ Sender and recipient profiles
@ A journey and a contact
Answer Sheet

Q1) Correct or Incorrect: Transparent Data Encryption prevents unauthorized data access, even if somebody has physical possession
of the encrypted drive.

@ Incorrect

@ @ Correct

Q2) What does Identity Verification use to verify your browser or app?

@ Carrier pigeon
@ SMS message
@ Phone call

@ @ Email

Q3) Which keys require you to upload a certificate?

@ @ssH

@ symmetric

@ @ Asymmetric
@ None of these

Q4) What activity uses salt keys?

@ @ JWT use with Journey Builder
@ Text encryption

@ File transfer

@ SSO authentication

Q5) How can you obtain SSL certificates for use with Marketing Cloud?

@ @ Have Marketing Cloud purchase them for you

@ @ Buy them yourself
@ Upload from your library
@ None of these

Q6) Correct or Incorrect: You should pass SubscriberKey values in the clear.

@ @ Incorrect

@ Correct

Q7) Correct or Incorrect: You should store credit card numbers in Marketing Cloud.

@ @ Incorrect

@ Correct

Q8) Where should you store refresh token values?

@ Thumb drive

@ @ Your own server
@ Marketing Cloud

@ Triplicate forms
Answer Sheet

Q1) What's the passing score for the Marketing Cloud Administrator Certification exam?

@ 0.62
@ 0.65

@ 80.67
@07

Q2) The setup section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 0.14
@ 0.15
@ 0.19
@ @ 0.38

Q3) Which objective is the most heavily weighted for the Marketing Cloud Administrator Certification exam?

@ Channel management
@ Subscriber data management

@ @ setup

@ Maintenance

Q4) The subscriber data management section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@0.1
9 @0.18
@ 02
@ 0.05

Q5) The subscriber data management section of the exam covers which key topics?

@ Integrations and data quality

@ @ Data quality and mail management
@ Business units and security

@ Marketing Cloud extension products
Answer Sheet

Q1) The maintenance section of the exam covers which key topics?

@ Configuring integrations
@ Data quality and mail management

@ @ Data cleanup
@ Digital marketing compliance

Q2) The digital marketing section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ B0.13
@ 0.15
@ 0.18
@ 0.35

Q3) The di

ital marketing section of the exam covers which key topic?

@ Data quality and mail management
@ Contact model

@ @ Product offerings

@ Advertising Studio configurations

Q4) The channel management section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 0.15

8 0.16
@ 0.35
@ 0.38

@Q5) The channel management section of the exam covers which key topics?

@ Product offerings

@ Data compliance

@ @ Configuration of Email Studio

@ Data filters, filter activities, and data extensions

Q6) The maintenance section makes up what percentage of the Marketing Cloud Administrator Certification exam?

@ 01

9 80.15
@ 02

@ 0.05
Answer Sheet

Q1) Which of the following are all reasons to know your Marketing Cloud instance? (choose 3)

@ @ The instance helps you use the release schedule to predict when new features are released to your account.
@ The instance identifies the top-level parent in your Enterprise account.

@ @ The instance helps you monitor any performance concerns on the Salesforce Trust site.

@ @ The instance is needed to configure the Web Collect URL, SOAP Web Services API, and more.

@ The instance determines priority in sending on each Marketing Cloud server.

Q2) Why is whitelisting the entire set of IP ranges for your region a best practice?

@ It minimizes the use of verification codes required for logins, saving time for users and administrators.
@ @ It avoids unintended service disruptions due to movement between primary and secondary instances.
Explanation:-

Refer: https://help.salesforce.com/article View?id=000321501 &language=en_US&type=1&mode=1

@ It allows users to access Marketing Cloud regardless of their work location without extra authentication.
@ @ It ensures Salesforce login pools can process end users� login authentication when accessing Salesforce.

Q3) Individual users can change the Time Zone and Date Format for their own accounts in their Settings.

@ Incorrect

@ @ Correct

Q4) The default Email Display Name and Email Reply To Address for email sends in your Marketing Cloud account should be selected
carefully, as they may be used for sending.

@ Incorrect

@ @ Correct

Q5) The default Email Display Name and Email Reply To Address are configured by the administrator in:

@ Marketing Cloud Settings
@ Default Sender Profile
@ @ Account Settings

@ General Settings

Q6) All Contacts functions across Studios/Channels at a Business Unit level.
@ Correct
Explanation:-Sometimes accounts with business units can't access all contacts. Some contact records can overlap in business units, but other contacts
can remain available only to a particular business unit. Link - https://help.salesforce.com/article View?

id=mc_cab_contact_definition_and_count_determination.htm&type=5

@ @ incorrect

Q7) You must manually manage the linking of disparate IDs for Contact Visualizer to function across Studios/Builders; Marketing Cloud
does not do this automatically.

@ Incorrect

@ @ Correct

Q8) Contact configuration is tied to an individual Business Unit.

@ Incorrect

@ @ Correct

Q9) All Subscribers are Contacts but not all Contacts are Subscribers

@ Incorrect

@ @ Correct

Q10) Lightning Experience is supported for Marketing Cloud Connect features.

@ @ Incorrect
@ Correct
