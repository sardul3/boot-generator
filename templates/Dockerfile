# Use an official OpenJDK base image
FROM openjdk:{{ java_version }}

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/{{ project_name }}.jar /app/{{ project_name }}.jar

# Run the Spring Boot application
CMD ["java", "-Dlog4j2.formatMsgNoLookups=true", "-jar", "{{ project_name }}.jar"]

# Expose the port that the Spring Boot app will listen on
EXPOSE 8080:8080