### 🧩 **User Story 1: EC2 Deployment Mini Project**

**Goal**: Deploy EC2 instances using Pulumi (TypeScript) to learn company DevOps/infrastructure standards.

#### 📘 **Learn Pulumi Basics**

* [ ] Read about:

  * Projects & Stacks Overview

    * 📄 [Organizing Projects & Stacks](https://www.pulumi.com/docs/intro/concepts/project/)
    * 📄 [Stacks | Pulumi Docs](https://www.pulumi.com/docs/intro/concepts/stack/)
  * Pulumi.yaml & Configuration

    * 📄 [Pulumi YAML Reference](https://www.pulumi.com/docs/intro/languages/yaml/)
    * 📄 [Project File Reference](https://www.pulumi.com/docs/intro/concepts/project/)
  * Secrets & Configs

    * 📄 [Managing Configuration and Secrets](https://www.pulumi.com/docs/intro/concepts/config/)
    * 📄 [Secrets | Pulumi Concepts](https://www.pulumi.com/docs/intro/concepts/secrets/)
    * 📄 [How to Manage Secrets with Pulumi (Blog)](https://www.pulumi.com/blog/managing-secrets-with-pulumi/)
  * Managing Stacks

    * 📄 [Stacks Overview](https://www.pulumi.com/docs/intro/concepts/stack/)
    * 📄 [`pulumi stack change-secrets-provider`](https://www.pulumi.com/docs/cli/commands/pulumi_stack_change-secrets-provider/)
  * Using Commands

    * 📄 [Pulumi CLI Commands](https://www.pulumi.com/docs/cli/)
    * 📄 [`pulumi up`](https://www.pulumi.com/docs/cli/commands/pulumi_up/)

#### 🛠️ **Hands-on Tasks**

* [ ] Deploy **2 EC2 instances** using **Pulumi (TypeScript)** in **2 AWS regions**
* [ ] Create & attach **IAM Roles + Instance Profiles**
* [ ] Use **init scripts** to install **Wiz Sensor**
* [ ] Apply standardized **AWS tags + environment names**: `"dev"`, `"test"`

---