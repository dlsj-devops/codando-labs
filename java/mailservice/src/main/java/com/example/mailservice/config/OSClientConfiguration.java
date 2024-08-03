package com.example.mailservice.config;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.springframework.context.annotation.Configuration;

import com.oracle.bmc.ConfigFileReader;
import com.oracle.bmc.Region;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.objectstorage.ObjectStorage;
import com.oracle.bmc.objectstorage.ObjectStorageClient;

@Configuration
public class OSClientConfiguration {
    String configurationFilePath = "/.oci/config";
    String profile = "DEFAULT";

    public ObjectStorage getObjectStorage() throws IOException {
        System.out.println("Configuração do OCI");
        
        Path currentRelativePathe = Paths.get("");

        final ConfigFileReader.ConfigFile configFile = ConfigFileReader.parse(currentRelativePathe.toAbsolutePath() + configurationFilePath, profile); 
        final ConfigFileAuthenticationDetailsProvider provider = new ConfigFileAuthenticationDetailsProvider(configFile);

        return ObjectStorageClient.builder().region(Region.SA_SAOPAULO_1).build(provider);
    }
}
