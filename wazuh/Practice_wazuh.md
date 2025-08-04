Absolutely! Here’s a **simple, step-by-step guide** to set up Wazuh on AWS using Pulumi and automate it with GitHub Actions.  
This will get you started quickly, with clear next steps for each part.

---

# 🚀 Step-by-Step: Deploy Wazuh on AWS with Pulumi & GitHub Actions

---

## 1️⃣ **Project Setup**

**a.** Create a new directory for your project:
```bash
mkdir wazuh-aws-pulumi && cd wazuh-aws-pulumi
```

**b.** Initialize a new Pulumi project (choose TypeScript for example):
```bash
pulumi new aws-typescript
```

---

## 2️⃣ **Define Your AWS Infrastructure**

For a basic Wazuh deployment, let’s launch an EC2 instance (or more, as needed) running Wazuh Manager + Docker.

**a.** Install Docker on your EC2 instance using a User Data script.

**b.** In `index.ts`, add a simple EC2 resource:

````typescript
import * as aws from "@pulumi/aws";

// 1. Get the latest Amazon Linux 2 AMI
const ami = aws.ec2.getAmi({
    mostRecent: true,
    owners: ["amazon"],
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*-x86_64-ebs"] }],
});

// 2. Create a security group allowing SSH, HTTP, HTTPS, and Wazuh ports
const sg = new aws.ec2.SecurityGroup("wazuh-sg", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },   // SSH
        { protocol: "tcp", fromPort: 5601, toPort: 5601, cidrBlocks: ["0.0.0.0/0"] }, // Kibana
        { protocol: "tcp", fromPort: 1514, toPort: 1515, cidrBlocks: ["0.0.0.0/0"] }, // Wazuh
        { protocol: "tcp", fromPort: 443, toPort: 443, cidrBlocks: ["0.0.0.0/0"] },   // HTTPS
    ],
    egress: [{ protocol: "-1", fromPort: 0, toPort: 0, cidrBlocks: ["0.0.0.0/0"] }],
});

// 3. Create a key pair (or use an existing one)
const keyName = "wazuh-keypair"; // Replace with your key pair name

// 4. EC2 instance with Docker + Wazuh Docker Compose in user data
const userData = `#!/bin/bash
yum update -y
amazon-linux-extras install docker -y
service docker start
usermod -a -G docker ec2-user
curl -fsSL https://get.docker.com -o get-docker.sh
bash get-docker.sh
yum install git -y
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker
docker-compose up -d
`;

const server = new aws.ec2.Instance("wazuh-server", {
    ami: ami.then(a => a.id),
    instanceType: "t3.medium",
    vpcSecurityGroupIds: [sg.id],
    keyName: keyName,
    userData: userData,
    tags: { Name: "Wazuh-Server" },
});

// 5. Export the public IP
export const publicIp = server.publicIp;
export const publicDns = server.publicDns;
````

---

## 3️⃣ **Pulumi Configuration**

- Set your AWS credentials as environment variables or configure with `aws configure`.
- In `Pulumi.<stack>.yaml`, you can set region and other configs.

---

## 4️⃣ **Deploy with Pulumi**

```bash
pulumi up
```
- Approve the deployment.  
- After a few minutes, your EC2 instance will be running Wazuh via Docker Compose.

---

## 5️⃣ **Access Wazuh Dashboard**

- Once the instance is up, visit `http://<public-ip>:5601` in your browser.
- Default credentials (for the Docker setup) are typically:
  - **Username:** admin
  - **Password:** admin

---

## 6️⃣ **Automate with GitHub Actions**

**a.** Add your AWS credentials as GitHub repository secrets:  
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`

**b.** Add a workflow file `.github/workflows/pulumi.yml`:

````yaml
name: Pulumi Deploy

on:
  push:
    branches: [ main ]

jobs:
  up:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - uses: pulumi/actions@v4
        with:
          command: up
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
````

- Add your Pulumi access token as a secret: `PULUMI_ACCESS_TOKEN`.

---

## 7️⃣ **Next Steps**

- **Add Agents:** Install Wazuh agents on other servers or endpoints and connect them to your Wazuh Manager.
- **Secure your deployment:** Restrict security group rules, use HTTPS, and set strong passwords.
- **Explore Dashboards:** Use Kibana (at port 5601) to view alerts and reports.

---

# 🎉 That’s it! You now have a simple, automated Wazuh deployment on AWS using Pulumi and GitHub Actions.

Let me know if you want to:
- Deploy a more advanced (multi-node) Wazuh cluster
- Use managed services (like RDS for Elasticsearch/OpenSearch)
- Add monitoring, secrets management, or other features

Just ask for the next steps!
