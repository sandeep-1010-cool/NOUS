1. What is a Pulumi Project?  
- A Pulumi project is a folder with a Pulumi.yaml file.  
- The Pulumi.yaml file defines important info about the project, like the programming runtime and metadata.

2. Creating a Project:  
- Use the command `pulumi new` to create a new project folder with the Pulumi.yaml file inside.

3. Pulumi.yaml File:  
- This file must begin with a capital "P" and can have .yml or .yaml extension.  
- It specifies the runtime (such as Node.js, Python, Go, etc.) and other project settings.  
- Examples of configuring runtimes are given for Node.js, Go, .NET, Java, and YAML.

4. Project Runtime:  
- The runtime tells Pulumi what language and environment to use when running the deployment program.  
- For JavaScript/TypeScript, you usually need a package.json to point to the entry file (like index.js).  
- For Python, an entry file like __main__.py or setup.py is used.

5. Project-relative paths:  
- Any file paths referenced by the project are relative to the project folder. For example, Dockerfile context in subfolder.

6. Getting Project Info Programmatically:  
- You can use `pulumi.getProject()` in your code to get the project name during deployment.

7. Stack Settings:  
- Each stack has its own settings file named Pulumi.<stackname>.yaml in the project root.  
- These files store stack-specific configs and can be safely checked into version control since secrets are encrypted.  
- You can change where these files are stored by setting `stackConfigDir` in the project metadata.

---

### Q1: What is a Pulumi project?  
**A1:**  
A Pulumi project is a folder that contains a `Pulumi.yaml` file. This file defines metadata about the project, including the runtime environment used to run the Pulumi program during deployments. At runtime, Pulumi determines the current project by looking for the nearest parent folder with a `Pulumi.yaml` file.

---

### Q2: How do I create a new Pulumi project?  
**A2:**  
You create a new Pulumi project using the command:  
```bash
pulumi new
```  
This command initializes a directory with a `Pulumi.yaml` file and other necessary files for the project.

---

### Q3: What does the `Pulumi.yaml` project file contain?  
**A3:**  
The `Pulumi.yaml` file specifies:  
- The runtime environment (e.g., nodejs, python, go, dotnet, java, yaml)  
- Metadata like the project name and description  
- Optional runtime options, such as entrypoints or binary locations for precompiled programs.  

Example `Pulumi.yaml` for a Node.js project:  
```yaml
name: webserver
runtime: nodejs
description: A minimal JavaScript Pulumi program.
```

---

### Q4: Can you show examples of `Pulumi.yaml` configurations for different runtimes?  
**A4:**  
Yes, here are some examples:  

- Node.js using JavaScript (not TypeScript):  
```yaml
name: my-project
runtime:
  name: nodejs
  options:
    typescript: false
```

- Go program using a pre-built executable named `mybinary`:  
```yaml
name: my-project
description: A precompiled Go Pulumi program.
runtime:
  name: go
  options:
    binary: mybinary
```

- .NET program with a pre-built assembly `MyInfra.dll`:  
```yaml
name: my-project
description: A precompiled .NET Pulumi program.
runtime:
  name: dotnet
  options:
    binary: bin/MyInfra.dll
```

- Java program with a pre-built JAR file:  
```yaml
name: my-project
description: A precompiled Java Pulumi program.
runtime:
  name: java
  options:
    binary: target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar
```

- YAML program with inline resources:  
```yaml
name: my-project
runtime: yaml
resources:
  bucket:
    type: aws:s3:BucketV2
```

---

### Q5: How does Pulumi determine the program entrypoint?  
**A5:**  
- In JavaScript/TypeScript projects, the working directory should contain a `package.json` file pointing to an entry file like `index.js`.  
- In Python projects, having a `__main__.py` or `setup.py` file defines the entrypoint.  
- For precompiled binaries, the location is specified in the `Pulumi.yaml` file under runtime options as shown in examples above.

---

### Q6: How are relative file paths handled in a Pulumi project?  
**A6:**  
File paths referenced by the Pulumi program are always relative to the working directory (which is usually the project folder).  

Example in TypeScript using AWS ECR image build context from a subfolder:  
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("repository", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    context: "./app",  // relative path to Docker build context
    platform: "linux/amd64",
});

export const url = repository.url;
```

---

### Q7: How can I get the current project name programmatically in my Pulumi code?  
**A7:**  
Use the `pulumi.getProject()` function. For example:  
```typescript
const project = pulumi.getProject();
console.log(`Deploying project: ${project}`);
```

---

### Q8: What are Pulumi stack settings files?  
**A8:**  
Each stack you create in a project has a settings file called `Pulumi.<stackname>.yaml`. This file contains configuration settings specific to that stack, such as configuration values and secrets. They usually live in the root project directory unless configured otherwise.

---

### Q9: How can I change the location of stack configuration files?  
**A9:**  
Set the `stackConfigDir` metadata attribute in your `Pulumi.yaml` file to a relative directory where you want to store stack config files.

---

### Q10: Can I commit stack settings files to version control?  
**A10:**  
Yes! Stack settings files encrypt secret values, so they are safe to check into source control, which helps with team collaboration and development. For ephemeral stacks, these files are usually not committed.
