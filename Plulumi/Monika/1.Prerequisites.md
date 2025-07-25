# Prerequisites for Installation

This file outlines the system requirements and tools needed to successfully install Pulumi and set up Claude AI with Cursor IDE.

## Table of Contents
1. [System Requirements](#system-requirements)
    - [Windows Computer](#windows-computer)
    - [AWS Free Tier Account](#aws-free-tier-account)
    - [Node.js Installation](#nodejs-installation)
    - [Cursor IDE Installation](#cursor-ide-installation)
2. [Download Links and Commands](#download-links-and-commands)
    - [Node.js](#nodejs)
    - [Cursor IDE](#cursor-ide)
    - [Chocolatey](#chocolatey)
    - [AWS CLI](#aws-cli)
    - [Pulumi](#pulumi)
3. [Steps to Create AWS IAM User](#steps-to-create-aws-iam-user)
    - [Create IAM User](#create-iam-user)
    - [Assign Permissions](#assign-permissions)
    - [Generate Access Key ID and Secret Access Key](#generate-access-key-id-and-secret-access-key)

## System Requirements

### Windows Computer
- A Windows computer with administrative privileges is required to install tools and configure settings.

### AWS Free Tier Account
- An AWS Free Tier account is necessary for Pulumi configurations.
- Ensure you have your **AWS Access Key ID** and **Secret Access Key** ready.
- Follow the steps below to create a new IAM user and generate credentials.

### Node.js Installation
- Node.js is required for some Pulumi setups.
- Ensure you install the latest stable version of Node.js.

### Cursor IDE Installation
- Cursor IDE is used to integrate Claude AI for coding assistance.
- Download and install Cursor IDE on your system.

## Download Links and Commands

### Node.js
- **Official Link**: [https://nodejs.org/](https://nodejs.org/)
- **Chocolatey Command**:
  ```bash
  choco install nodejs
  ```

### Cursor IDE
- **Official Link**: [https://cursor.so/](https://cursor.so/)
- No Chocolatey package available for Cursor IDE. Download manually from the official website.

### Chocolatey
- Chocolatey is a package manager for Windows, used to install tools like AWS CLI and Node.js.
- **Installation Instructions**:
  - Open PowerShell as Administrator and run:
    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

### AWS CLI
- **Official Link**: [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **Chocolatey Command**:
  ```bash
  choco install awscli
  ```

### Pulumi
- **Official Link**: [Pulumi Installation](https://www.pulumi.com/docs/get-started/install/)
- **Chocolatey Command**:
  ```bash
  choco install pulumi
  ```

## Steps to Create AWS IAM User

### Create IAM User
1. Log in to the **AWS Management Console**.
2. Navigate to the **IAM (Identity and Access Management)** service.
3. In the left menu, click **Users**, then click **Add User**.
4. Enter a **User Name** (e.g., `pulumi-user`).
5. Select **Access Type**:
   - Check the box for **Programmatic Access** to generate an Access Key ID and Secret Access Key.

### Assign Permissions
1. On the **Permissions** page:
   - Select **Attach Existing Policies Directly**.
   - Search for and attach the policy: `AdministratorAccess`.
   - Alternatively, you can create a custom policy for specific permissions.
2. Click **Next** and review the permissions.

### Generate Access Key ID and Secret Access Key
1. After creating the user, you’ll see the **Success** page.
2. Click **Download .csv** to save the Access Key ID and Secret Access Key securely.
3. Alternatively:
   - Go to **IAM > Users**.
   - Select the user you created.
   - Navigate to the **Security Credentials** tab.
   - Click **Create Access Key** and note down the credentials.

## Notes
- **Important**: Keep the Access Key ID and Secret Access Key secure. Do not share them publicly.
- Ensure the IAM user has the necessary permissions for Pulumi and AWS CLI operations.
