plugins {
    java
}
java.sourceCompatibility = JavaVersion.VERSION_13
java.targetCompatibility = JavaVersion.VERSION_13

allprojects {
    apply(plugin = "java")

    repositories {
        mavenCentral()
    }
    dependencies {
        extra["jupiterVersion"] = "5.6.2"
        testImplementation("org.junit.jupiter:junit-jupiter-api:${extra["jupiterVersion"]}")
        testImplementation("org.junit.jupiter:junit-jupiter-engine:${extra["jupiterVersion"]}")
    }
    tasks.withType<Test> {
        useJUnitPlatform()
    }
}