# Assignment 2.

Members: Colin Hansen, Bryan Steitz, Pan Wang


To create servers: Please keep in mind that you need to enter your own username and password. You also need your own security key for VM creation to comply with Horizon requirements.

NOTE: Since the ansible playbooks are using bash commands to start other ansible playbooks, the feedback will not be seen as each task is completed. Rather one would see all of the feedback once the ansible play has finished.


## End of Assignment Survey: Evaluating the Deployment Approach
Scale: 1 to 10; increasing in difficulty  

##### Ease of deployment: Scale [1-10]  
 8: Ansible was difficult and unreasonable to use for deploying a single webserver and a single database server.

##### How much time and effort you required to deploy the application (in minutes), including internet searches you have to do to find the steps?  
*   To deploy OpenStack servers: *4 hours*
*  	To install Apache: *15 minutes*
*   To install and configure PHP: *15 minutes*
*   To install and configure MySQL: *6 hours*
*   Overall time to deploy application: *10 hours 30 minutes*


##### Challenges you faced for this simple 3-tier application deployment 
There is a bit of a learning curve with Ansible, and some things still aren’t clear. We had to do a few hacks to get the deployment to work. One issue was having the playbook wait for the servers on Openstack to be up before attempting to access them. Another issue was getting the webserver to communicate with database server. 
