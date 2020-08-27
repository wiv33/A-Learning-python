plugins {
    java
}
java.sourceCompatibility = JavaVersion.VERSION_13
java.targetCompatibility = JavaVersion.VERSION_13

group = "org.psawesome"
version = "1.0-SNAPSHOT"

allprojects {
    apply(plugin = "java")

    repositories {
        mavenCentral()
    }
    dependencies {
        extra["jupiterVersion"] = "5.6.2"
        testImplementation("org.junit.jupiter:junit-jupiter-api:${extra["jupiterVersion"]}")
        testImplementation("org.junit.jupiter:junit-jupiter-engine:${extra["jupiterVersion"]}")
        testImplementation("org.junit.jupiter:junit-jupiter-params:${extra["jupiterVersion"]}")
    }
    tasks.withType<Test> {
        useJUnitPlatform()
    }
}