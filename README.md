# boot-generator

## Description

This project is a Spring Boot application generator providing a customizable template to kickstart development of an enterprise level Java Application

## Features

- **Language**: Java
- **Packaging**: Jar
- **Java Version**: 11
- **Build Tool**: Maven

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- [Java JDK 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [Maven](https://maven.apache.org/download.cgi)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/[your-username]/boot-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd boot-generator
    ```

### Usage

Follow these steps to run the project:

1. Build the project:

    ```bash
    mvn clean install
    ```

2. Run the application:

    ```bash
    java -jar target/boot-generator.jar
    ```

### Usage

#### Using the Command Line Interface (CLI)

This project provides a CLI for generating Spring Boot projects. Here are the available commands:

- **Generating a Project:**

    ```bash
    python main.py --company "Your Company" --team-name "Your Team" --project-name "New Project" --language java --packaging jar --java-version 11 --build-tool maven --generate-resources
    ```

    Replace `"Your Company"`, `"Your Team"`, `"New Project"`, and other options with your desired values.

- **Options:**

    - `--company`: The name of the company.
    - `--team-name`: The name of the team.
    - `--project-name`: The name of the Spring Boot project.
    - `--language`: Programming language for the project (java/groovy/kotlin).
    - `--packaging`: Packaging type for the `pom.xml` file (jar/war).
    - `--java-version`: Java version for the project.
    - `--build-tool`: Build management tool for the project (maven/gradle).
    - `--generate-resources`: Generate resources and YAML files for all Spring Boot profiles.
