FROM eclipse-temurin:17-jdk

WORKDIR /app

# Copy all files
COPY . /app/

# Compile the Java project
RUN mkdir -p /app/bin && \
    javac -d /app/bin -sourcepath /app/src/main/java \
    /app/src/main/java/com/customframework/apps/legacy/Main.java \
    /app/src/main/java/com/customframework/apps/buganizer/Main.java \
    /app/src/main/java/com/customframework/apps/docsportal/Main.java

# Expose the ports
EXPOSE 8080
EXPOSE 8081
EXPOSE 8082

# Default command runs the Legacy Enterprise Portal
CMD ["java", "-cp", "/app/bin", "com.customframework.apps.legacy.Main"]
