### Pulumi Stack Q&A Guide

---

### **1. What is a Pulumi stack?**
A Pulumi stack is an isolated, independently configurable instance of a Pulumi program. Stacks are commonly used to represent different phases of development (e.g., `development`, `staging`, `production`) or feature branches (e.g., `feature-x-dev`).

---

### **2. How do you create a new stack?**
To create a new stack, use the `pulumi stack init <stackName>` command. This creates an empty stack and sets it as the active stack.

#### **Command:**
```bash
pulumi stack init staging
```

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";

// Get the current stack name programmatically
const stack = pulumi.getStack();
console.log(`Current stack: ${stack}`);
```

---

### **3. What are the formats for specifying stack names?**
Stack names can be specified in the following formats:
1. **`stackName`**: Identifies the stack in the current user account or default organization.
2. **`orgName/stackName`**: Identifies the stack in the organization.
3. **`orgName/projectName/stackName`**: Identifies the stack in the organization and project.

#### **Example:**
For the stack `my-org/my-project/dev`, the following are equivalent:
- `my-org/my-project/dev`
- `my-org/dev`
- `dev`

---

### **4. How do you list all stacks in a project?**
Use the `pulumi stack ls` command to list stacks associated with the current project.

#### **Command:**
```bash
pulumi stack ls
```

#### **Output Example:**
```
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev                                  4 hours ago              97
staging*                                  n/a                      n/a
broomellc/test                            2 weeks ago              121
```

---

### **5. How do you select an active stack?**
Use the `pulumi stack select <stackName>` command to change the active stack.

#### **Command:**
```bash
pulumi stack select jane-dev
```

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";

// Programmatically get the active stack
const activeStack = pulumi.getStack();
console.log(`Active stack: ${activeStack}`);
```

---

### **6. How do you preview and save an update plan for a stack?**
To preview an update and save the plan, use the `pulumi preview --save-plan=<filename>` command.

#### **Command:**
```bash
pulumi preview --save-plan=plan.json
```

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";

if (pulumi.runtime.isDryRun()) {
    console.log("This is a preview operation.");
}
```

---

### **7. How do you update a stack?**
To update the active stack, use the `pulumi up` command. You can also constrain updates using a saved plan.

#### **Command:**
```bash
pulumi up --plan=plan.json
```

---

### **8. How do you view stack resources?**
Run the `pulumi stack` command without arguments to see metadata, resources, and outputs for the active stack.

#### **Command:**
```bash
pulumi stack
```

#### **Output Example:**
```
Current stack is jane-dev:
    Last updated 1 week ago
    Pulumi version v0.11.0
    Plugin aws [resource] version 0.11.0

Current stack resources:
    TYPE                                             NAME
    pulumi:pulumi:Stack                              webserver-jane-dev
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www

Current stack outputs:
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197
```

---

### **9. What are stack tags and how do you manage them?**
Stack tags are metadata in the form of key-value pairs. Built-in tags are automatically assigned during updates, while custom tags can be added for grouping.

#### **Commands:**
- View tags:
  ```bash
  pulumi stack tag ls
  ```
- Add a custom tag:
  ```bash
  pulumi stack tag set environment production
  ```
- Remove a tag:
  ```bash
  pulumi stack tag rm environment
  ```

---

### **10. How do you export and import stack deployments?**
- **Export**: Use `pulumi stack export --file <filename>` to export the stack's raw data.
- **Import**: Use `pulumi stack import --file <filename>` to import the modified stack.

#### **Commands:**
```bash
pulumi stack export --file stack.json
pulumi stack import --file stack.json
```

---

### **11. How do you destroy a stack's resources?**
Use the `pulumi destroy` command to delete all resources in the stack.

#### **Command:**
```bash
pulumi destroy
```

---

### **12. How do you delete a stack?**
Use `pulumi stack rm` to delete a stack. Use `--force` to delete a stack with resources.

#### **Commands:**
```bash
pulumi stack rm
pulumi stack rm --force
```

---

### **13. How do you export values as stack outputs?**
Stack outputs are values exported by your program. Use `pulumi.stack.output` to retrieve them.

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";

// Export a URL as a stack output
export const url = "https://example.com";

// Retrieve the output via CLI
// Command: pulumi stack output url
```

---

### **14. How do you reference outputs from another stack?**
Use `StackReference` to access outputs of another stack.

#### **Code Example (Inter-stack dependency):**
```typescript
import * as pulumi from "@pulumi/pulumi";

const otherStack = new pulumi.StackReference("my-org/my-project/other");
const otherOutput = otherStack.getOutput("x");

console.log(`Other stack output: ${otherOutput}`);
```

---

### **15. How do you process outputs programmatically?**
Use `getOutput` for gated access or `getOutputDetails` for direct access.

#### **Code Examples:**
- **Using `getOutput`:**
  ```typescript
  const infra = new pulumi.StackReference("my-org/my-project/dev");
  const ip = infra.getOutput("privateIp");
  const logKey = ip.apply(ip => `logs/${ip}.log`);
  ```

- **Using `getOutputDetails`:**
  ```typescript
  const infra = new pulumi.StackReference("my-org/my-project/dev");
  const subnetsJSON = await infra.getOutputDetails("subnets");
  const subnets = JSON.parse(subnetsJSON.value);

  subnets.forEach((subnet, i) => {
      const host = new aws.ec2.Instance(`bastion-${i}`, { subnetId: subnet.id });
  });
  ```

---

### **16. How do you get the current stack programmatically?**
Use `pulumi.getStack()` to retrieve the current stack name.

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";

const currentStack = pulumi.getStack();
console.log(`Current stack: ${currentStack}`);
```

---

### **17. How do you define inter-stack dependencies for environments?**
Use `StackReference` to link stacks across environments.

#### **Code Example:**
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const env = pulumi.getStack();
const infra = new pulumi.StackReference(`mycompany/infra/${env}`);
const provider = new k8s.Provider("k8s", { kubeconfig: infra.getOutput("kubeConfig") });

const service = new k8s.core.v1.Service("my-service", { spec: { /* ... */ } }, { provider });
```

---

### **18. How do you handle secrets in stack outputs?**
Secrets in stack outputs are encrypted. To view plaintext values, use the `--show-secrets` flag.

#### **Command:**
```bash
pulumi stack output --show-secrets
```