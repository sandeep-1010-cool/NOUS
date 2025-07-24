# Pulumi Projects: A Beginner's Guide

## What is a Pulumi Project?
- A Pulumi project is a **folder** that contains a `Pulumi.yaml` file.
- This `Pulumi.yaml` file is the core of the project and specifies:
  - The **runtime** to use (e.g., Node.js, Python, Go).
  - The **program** to execute during deployments.

- **How Pulumi Determines the Project**:
  - At runtime, Pulumi looks for the **nearest parent folder** containing a `Pulumi.yaml` file to identify the current project.

## How to Create a Pulumi Project
- Use the following command to create a new project:
  ```bash
  pulumi new
  ```

## The `Pulumi.yaml` Project File

### Purpose
- Specifies the runtime and metadata for the project.
- Determines where Pulumi should look for the deployment program.

### Supported Runtimes
- **Node.js**
- **Python**
- **.NET**
- **Go**
- **Java**
- **YAML**

### Naming Rules
- The file must start with a capital **P** (`Pulumi.yaml` or `Pulumi.yml`).

### Typical Structure
Example of a basic `Pulumi.yaml` file:
```yaml
name: webserver
runtime: nodejs
description: A minimal JavaScript Pulumi program.
```

### Additional Examples
- **Node.js with JavaScript**:
  ```yaml
  name: my-project
  runtime:
    name: nodejs
    options:
      typescript: false
  ```

- **Go with Pre-built Executable**:
  ```yaml
  name: my-project
  description: A precompiled Go Pulumi program.
  runtime:
    name: go
    options:
      binary: mybinary
  ```

- **.NET with Pre-built Assembly**:
  ```yaml
  name: my-project
  description: A precompiled .NET Pulumi program.
  runtime:
    name: dotnet
    options:
      binary: bin/MyInfra.dll
  ```

- **Java with Pre-built JAR**:
  ```yaml
  name: my-project
  description: A precompiled Java Pulumi program.
  runtime:
      name: java
      options:
          binary: target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar
  ```

- **YAML with Inline Resources**:
  ```yaml
  name: my-project
  runtime: yaml
  resources:
    bucket:
      type: aws:s3:BucketV2
  ```

## Working Directory and Entrypoints
- **JavaScript/TypeScript**:
  - The working directory should contain a `package.json` file pointing to the entrypoint (e.g., `index.js`).
- **Python**:
  - The directory should include a `__main__.py` or `setup.py` file.
- **Other Languages**:
  - The entrypoint is defined based on the runtime (e.g., binary files for Go or .NET).

## Project-Relative Paths
- Paths in Pulumi programs are always **relative to the working directory**.
- Example:
  ```javascript
  const repository = new awsx.ecr.Repository("repository", {
      forceDelete: true,
  });

  const image = new awsx.ecr.Image("image", {
      repositoryUrl: repository.url,
      context: "./app", // Relative path to Dockerfile
      platform: "linux/amd64",
  });

  export const url = repository.url;
  ```

## Getting the Current Project Programmatically
- Use the `getProject` function to retrieve the name of the current project:
  ```javascript
  const project = pulumi.getProject();
  ```

## Stack Settings Files

### What are Stack Settings Files?
- Each stack in a project has a file named `Pulumi.<stackname>.yaml` that contains stack-specific configuration.
- These files are typically located in the root of the project directory.

### Customizing Stack Configuration Location
- Use the `stackConfigDir` metadata attribute to specify a custom directory for stack settings.

### Collaboration and Source Control
- For team projects:
  - Check stack settings into source control for collaboration.
  - Secret values in the settings are encrypted, so it is safe to store them in repositories.

- For ephemeral stacks:
  - Stack settings are usually **not** checked into source control.

### More Details
- For detailed information on stack settings, refer to the [Stack Settings File Reference](https://www.pulumi.com/docs/).

## Summary
- A Pulumi project is defined by a `Pulumi.yaml` file.
- The `Pulumi.yaml` file specifies the runtime, entrypoint, and metadata for the project.
- Stack settings files provide configuration for individual stacks.
- Pulumi makes it easy to organize, manage, and collaborate on infrastructure projects using familiar programming languages and tools.

Let me know if you need further clarification or additional examples!
