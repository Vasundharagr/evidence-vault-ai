package com.internship.tool.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

import java.time.Duration;
import java.util.Map;

@Service
public class AiServiceClient {

    private static final Logger logger = LoggerFactory.getLogger(AiServiceClient.class);
    private final RestTemplate restTemplate;
    
    // Looks for a URL in application.yml, defaults to your local Python port 5000
    @Value("${ai.service.url:http://localhost:5000}")
    private String aiServiceUrl;

    public AiServiceClient(RestTemplateBuilder restTemplateBuilder) {
        // Enforce the strict 10-second timeout rule
        this.restTemplate = restTemplateBuilder
                .setConnectTimeout(Duration.ofSeconds(10))
                .setReadTimeout(Duration.ofSeconds(10))
                .build();
    }

    /**
     * Generic method to call the AI Flask service
     */
    private String callAiEndpoint(String endpoint, Map<String, Object> payload) {
        try {
            String url = aiServiceUrl + endpoint;
            
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            
            HttpEntity<Map<String, Object>> request = new HttpEntity<>(payload, headers);
            
            // Call the Python Flask endpoint
            return restTemplate.postForObject(url, request, String.class);
            
        } catch (RestClientException e) {
            // Requirement: Return null on error
            logger.error("Error communicating with AI Service at {}: {}", endpoint, e.getMessage());
            return null;
        }
    }

    // --- The 3 Endpoint Wrappers ---

    public String describe(String inputData) {
        return callAiEndpoint("/describe", Map.of("data", inputData));
    }

    public String recommend(String inputData) {
        return callAiEndpoint("/recommend", Map.of("data", inputData));
    }

    public String generateReport(String inputData) {
        return callAiEndpoint("/generate-report", Map.of("data", inputData));
    }
}
