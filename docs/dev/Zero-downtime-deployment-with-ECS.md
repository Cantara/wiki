# Zero downtime deployment with ECS

## What is zero downtime deployment aka. rolling upgrade?

"At a basic level, a zero downtime deploy involves swapping out servers running new code for servers running the old code on a load balancer. Here is the general scripted process:

1. Create a new Virtual Machine (VM) image with the new code.
2. Start a number of VMs using that image, equal to the number currently running.
3. Verify each of these instances are running correctly and responding to checks.
4. Add the new instances to the ELB while removing the old (with connection draining).
5. Verify that everything is working properly. If not swap old back in for the new and diagnose the problem. If so, delete the old instances."

Src: <https://blog.codeship.com/zero-downtime-deployment-with-aws-ecs-and-elb/>

- See also <https://blog.codeship.com/easy-blue-green-deployments-on-amazon-ec2-container-service/>

## How to perform rolling upgrade (zero downtime)

1. Task Definition -> "create new revision" based on the newest revision running
2. Press the container name, and edit the tag of the "image" section to the desired release. Update and create.
3. Cluster -> Service -> Update: change to the revision you just created.
4. Click Update Service, and see the magic happen as ECS spins up the new service, it tries to spin up the new image before removing the old version.
5. In the Deployments tab you should be able to see the pending count and running counts change after a few seconds. Feel free to keep refreshing your browser tab that was pointed at the app to watch the transition.

- See also <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html>

## How to perform upgrade for services with FIFO requirements (downtime)

**Text below is not always true. With the introduction of services such as SQS FIFO Queues rolling upgrades with multiple nodes may still work if your setup is correct.**  
Due to FIFO-requirements, some applications must be stopped prior to updating. Set desired count to 0, and wait until it has shut down. Then reset the desired count to 1.   
This will ensure strict FIFO, at the cost of downtime.
